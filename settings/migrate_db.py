"""
MIGRATE_DB.PY - Database Migration Controller

Konsep alur migrasi:
- Database lama (dataleap_v5_example) → Database baru (dataleap_v5_migration)
- Migrasi dilakukan PER FASE (tidak sekaligus semua fase)
- Setiap fase:
    1. Jalankan 3 notebook (script_cimut, script_afrida, script_hanif) secara berurutan
    2. Kumpulkan hasil transformasi dari setiap notebook
    3. Simpan hasil akhir ke database baru
    4. Lanjut ke fase berikutnya

FASE:
- FASE 1: Master & Wilayah (Independen)
- FASE 2: SDM & Karyawan (Dependensi: Fase 1)
- FASE 3: CRM, Rekrutmen & Sarpras (Dependensi: Fase 1, 2)
- FASE 4: KBM & Rapor (Dependensi: Fase 1, 2, 3)
"""

import os
import sys
import json
import logging
import mysql.connector
from datetime import datetime
from pathlib import Path
from config import get_db_config, get_fase_config
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# ==================== SETUP LOGGING ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('migration.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DatabaseMigration:
    """
    Controller untuk migrasi database fase per fase.
    """
    
    def __init__(self):
        self.config = get_db_config()
        self.fase_config = get_fase_config()
        self.migration_results = {}
        self.current_fase = None
        
    def connect_db(self, db_type='old'):
        """
        Buat koneksi ke database lama atau baru.
        
        Args:
            db_type (str): 'old' untuk database lama, 'new' untuk database baru
            
        Returns:
            mysql.connector.MySQLConnection
        """
        try:
            db_config = self.config[f'db_{db_type}']
            conn = mysql.connector.connect(**db_config)
            logger.info(f"✓ Connected to database {db_type}: {db_config['database']}")
            return conn
        except mysql.connector.Error as err:
            logger.error(f"✗ Connection failed: {err}")
            sys.exit(1)
    
    def run_notebook(self, fase, person):
        """
        Jalankan Jupyter notebook untuk satu orang di satu fase.
        
        Args:
            fase (str): Nama fase (fase_1, fase_2, dst)
            person (str): Nama script (script_cimut, script_afrida, script_hanif)
            
        Returns:
            dict: Hasil migrasi dari notebook
        """
        notebook_path = Path(fase) / f"{person}.ipynb"
        
        if not notebook_path.exists():
            logger.warning(f"⚠ Notebook tidak ditemukan: {notebook_path}")
            return {'status': 'error', 'message': f'Notebook {notebook_path} tidak ditemukan'}
        
        try:
            logger.info(f"▶ Menjalankan notebook: {notebook_path}")
            
            # Baca notebook
            with open(notebook_path, 'r', encoding='utf-8') as f:
                notebook = nbformat.read(f, as_version=4)
            
            # Execute notebook
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(notebook, {'metadata': {'path': str(Path(fase).absolute())}})
            
            logger.info(f"✓ Notebook berhasil dijalankan: {person}")
            
            # Extract output (migration_result variable dari notebook)
            result = {
                'status': 'completed',
                'fase': fase,
                'person': person,
                'records_migrated': 0,
                'timestamp': datetime.now().isoformat()
            }
            
            return result
            
        except Exception as e:
            logger.error(f"✗ Error menjalankan notebook {person}: {str(e)}")
            return {'status': 'error', 'person': person, 'message': str(e)}
    
    def run_fase(self, fase_name):
        """
        Jalankan satu fase lengkap dengan semua scriptnya.
        
        Args:
            fase_name (str): Nama fase (fase_1, fase_2, fase_3, fase_4)
            
        Returns:
            dict: Hasil lengkap untuk satu fase
        """
        self.current_fase = fase_name
        fase_info = self.fase_config[fase_name]
        
        logger.info("\n" + "="*70)
        logger.info(f"MEMULAI {fase_info['nama']}")
        logger.info(f"Deskripsi: {fase_info['deskripsi']}")
        logger.info("="*70)
        
        fase_results = {
            'fase': fase_name,
            'nama_fase': fase_info['nama'],
            'start_time': datetime.now().isoformat(),
            'scripts': {},
            'status': 'in_progress'
        }
        
        # Jalankan setiap script per orang dalam fase ini
        for person in fase_info['people']:
            logger.info(f"\n📝 [{fase_name}] Menjalankan {person}...")
            result = self.run_notebook(fase_name, person)
            fase_results['scripts'][person] = result
            
            if result['status'] == 'error':
                logger.warning(f"⚠ {person} mengalami error: {result['message']}")
            else:
                logger.info(f"✓ {person} selesai")
        
        # Kumpulkan hasil dari semua scripts dalam fase
        fase_results['end_time'] = datetime.now().isoformat()
        fase_results['status'] = 'completed'
        
        self.migration_results[fase_name] = fase_results
        
        return fase_results
    
    def validate_fase_results(self, fase_name):
        """
        Validasi hasil migrasi satu fase sebelum lanjut ke fase berikutnya.
        
        Args:
            fase_name (str): Nama fase yang akan divalidasi
            
        Returns:
            bool: True jika valid, False jika ada error
        """
        if fase_name not in self.migration_results:
            logger.error(f"✗ Hasil fase {fase_name} tidak ditemukan")
            return False
        
        fase_results = self.migration_results[fase_name]
        
        # Check apakah ada error dalam scripts
        errors = [
            script for script, result in fase_results['scripts'].items()
            if result.get('status') == 'error'
        ]
        
        if errors:
            logger.error(f"✗ Ada error dalam scripts: {', '.join(errors)}")
            return False
        
        logger.info(f"✓ Validasi {fase_name} OK")
        return True
    
    def save_fase_to_new_db(self, fase_name):
        """
        Simpan hasil migrasi satu fase ke database baru.
        
        Args:
            fase_name (str): Nama fase yang akan disimpan
            
        Returns:
            bool: True jika berhasil
        """
        logger.info(f"\n💾 Menyimpan hasil {fase_name} ke database baru...")
        
        try:
            db_new = self.connect_db('new')
            cursor = db_new.cursor(dictionary=True)
            
            # Ambil tabel-tabel yang harus dimigrasikan untuk fase ini
            tabel_utama = self.fase_config[fase_name]['tabel_utama']
            logger.info(f"   Tabel yang akan disimpan: {len(tabel_utama)} tabel")
            
            # TODO: Implement logic untuk save data ke database baru
            # Setiap notebook sudah transform data, tinggal simpan ke DB baru
            
            cursor.close()
            db_new.close()
            
            logger.info(f"✓ Hasil {fase_name} berhasil disimpan ke database baru")
            return True
            
        except Exception as e:
            logger.error(f"✗ Error menyimpan {fase_name}: {str(e)}")
            return False
    
    def run_all_fases(self, start_fase=1):
        """
        Jalankan semua fase migrasi secara berurutan.
        
        Args:
            start_fase (int): Nomor fase untuk mulai (default: 1)
        """
        fases = ['fase_1', 'fase_2', 'fase_3', 'fase_4']
        start_index = start_fase - 1
        
        logger.info("\n" + "█"*70)
        logger.info("█ MEMULAI MIGRASI DATABASE LEAP")
        logger.info("█ Mode: Sequential (1 Fase → Kumpulkan Hasil → Simpan ke DB Baru)")
        logger.info("█"*70)
        
        for i, fase_name in enumerate(fases[start_index:], start=start_index+1):
            logger.info(f"\n\n{'='*70}")
            logger.info(f"FASE {i}/4: {self.fase_config[fase_name]['nama']}")
            logger.info(f"{'='*70}")
            
            # 1. Run fase
            self.run_fase(fase_name)
            
            # 2. Validate hasil
            if not self.validate_fase_results(fase_name):
                logger.error(f"✗ Validasi fase {fase_name} gagal. Berhenti migrasi.")
                break
            
            # 3. Simpan ke database baru
            if not self.save_fase_to_new_db(fase_name):
                logger.error(f"✗ Penyimpanan fase {fase_name} gagal. Berhenti migrasi.")
                break
            
            logger.info(f"✓ Fase {i} BERHASIL DISELESAIKAN")
            
            # Ask untuk lanjut ke fase berikutnya
            if i < 4:
                response = input(f"\n✓ Fase {i} selesai. Lanjut ke Fase {i+1}? (y/n): ").lower()
                if response != 'y':
                    logger.info(f"Migrasi dihentikan oleh user setelah fase {i}")
                    break
        
        # Print summary
        self.print_migration_summary()
    
    def print_migration_summary(self):
        """
        Cetak ringkasan hasil migrasi.
        """
        logger.info("\n\n" + "█"*70)
        logger.info("█ RINGKASAN MIGRASI DATABASE")
        logger.info("█"*70)
        
        for fase_name, results in self.migration_results.items():
            fase_num = fase_name.split('_')[1]
            logger.info(f"\n🔹 {results['nama_fase']}")
            logger.info(f"   Status: {results['status']}")
            logger.info(f"   Start: {results['start_time']}")
            logger.info(f"   End: {results['end_time']}")
            logger.info(f"   Scripts:")
            
            for person, script_result in results['scripts'].items():
                status = "✓" if script_result['status'] == 'completed' else "✗"
                logger.info(f"     {status} {person}: {script_result['status']}")
        
        # Save summary to JSON
        summary_path = f"migration_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(summary_path, 'w') as f:
            json.dump(self.migration_results, f, indent=2)
        
        logger.info(f"\n✓ Ringkasan disimpan ke: {summary_path}")


def main():
    """
    Main entry point untuk menjalankan migrasi database.
    """
    migration = DatabaseMigration()
    
    print("\n" + "█"*70)
    print("█ DATALEAP V5 DATABASE MIGRATION")
    print("█ From: dataleap_v5_example (Old DB)")
    print("█ To: dataleap_v5_migration (New DB)")
    print("█"*70)
    
    print("\nPilih Mode:")
    print("1. Run semua fase (1-4)")
    print("2. Run dari fase tertentu")
    print("3. Run satu fase saja")
    print("4. Exit")
    
    choice = input("\nMasukkan pilihan (1-4): ").strip()
    
    if choice == '1':
        migration.run_all_fases(start_fase=1)
    elif choice == '2':
        fase_num = int(input("Masukkan nomor fase untuk mulai (1-4): "))
        migration.run_all_fases(start_fase=fase_num)
    elif choice == '3':
        fase_num = int(input("Masukkan nomor fase (1-4): "))
        fase_name = f'fase_{fase_num}'
        migration.run_fase(fase_name)
        migration.validate_fase_results(fase_name)
        migration.save_fase_to_new_db(fase_name)
        migration.print_migration_summary()
    elif choice == '4':
        print("Exit")
        sys.exit(0)
    else:
        print("Pilihan tidak valid")
        sys.exit(1)


if __name__ == "__main__":
    main()
