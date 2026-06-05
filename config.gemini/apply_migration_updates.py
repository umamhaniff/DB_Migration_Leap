import json
import os

def patch_fase_3():
    path = "fase_3/script_hanif.ipynb"
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    new_transformations = """# 3. pelamar -> pelamar
if 'pelamar' in raw_data:
    df = pd.DataFrame(raw_data['pelamar'])
    df['tempat_lahir'] = df['ttl'].apply(extract_place)
    df['tanggal_lahir'] = df['ttl'].apply(extract_date).apply(parse_date)
    
    # enum & data cleaning
    def map_nikah(x):
        val = str(x).strip().lower()
        if val in ['menikah', 'nikah', 'kawin']: return 'Menikah'
        if val in ['lajang', 'belum', 'single', 'x', 'none', 'nan', '', '0']: return 'Belum Menikah'
        return 'Belum Menikah'
    
    df['status_pernikahan'] = df['statusnikah'].apply(map_nikah)
    df['penggunaan_laptop'] = df['gunalaptop'].apply(lambda x: 'Pernah' if str(x).strip().lower() in ['pernah', 'ya, pernah', 'ya'] else 'Tidak Pernah')
    df['gaji'] = df['gaji'].apply(clean_currency)
    
    # Generate integer ID auto-increment mapping
    df = df.reset_index()
    df['id_pelamar_new'] = df['index'] + 1
    pelamar_id_map = dict(zip(df['idpelamar'], df['id_pelamar_new']))
    df['id_pelamar'] = df['id_pelamar_new']
    
    mapping = {
        'id_pelamar': 'id_pelamar', 'idpengajuan': 'id_pengajuan', 'email': 'email_pelamar',
        'nama': 'nama_lengkap', 'panggilan': 'nama_panggilan', 'jk': 'jenis_kelamin',
        'tempat_lahir': 'tempat_lahir', 'tanggal_lahir': 'tanggal_lahir',
        'alamat': 'alamat_ktp', 'domisili': 'alamat_domisili', 'wa': 'nomor_wa',
        'linkedin': 'akun_linkedin', 'ig': 'akun_instagram', 'fb': 'akun_facebook', 
        'sosmed': 'sosmed_lain', 'laptop': 'spesifikasi_laptop', 'internet': 'internet',
        'kegiatan': 'kegiatan_sekarang', 'rencana': 'rencana_karir', 'mobilitas': 'mobilitas',
        'info': 'sumber_info', 'wfo': 'siap_wfo', 'bergabung': 'tanggal_bergabung',
        'jenis': 'kategori_pelamar', 'work': 'riwayat_kerja', 'ppdk': 'riwayat_pendidikan',
        'pengalaman': 'pengalaman_bidang', 'wawasan': 'wawasan', 'sehat': 'riwayat_kesehatan',
        'status_pernikahan': 'status_pernikahan', 'ajar': 'kemampuan_ajar', 'app': 'penguasaan_aplikasi', 
        'apps': 'aplikasi_lainnya', 'penggunaan_laptop': 'penggunaan_laptop', 'toefl': 'skor_toefl',
        'gaji': 'ekspektasi_gaji', 'link': 'tautan_berkas', 'resign': 'alasan_resign',
        'hasiliq': 'skor_iq', 'piciq': 'foto_iq', 'picminat': 'foto_minat', 
        'picpribadi': 'foto_kepribadian', 'created_at': 'created_at'
    }
    transformed_dfs['pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 4. pekerjaan -> pelamar_kerja
if 'pekerjaan' in raw_data:
    df = pd.DataFrame(raw_data['pekerjaan'])
    df['id_pelamar'] = df['idusers'].map(pelamar_id_map).astype('Int64')
    mapping = {
        'idpekerjaan': 'id_pelamar_kerja', 'id_pelamar': 'id_pelamar',
        'namaperusahaan': 'nama_perusahaan', 'periode': 'periode', 'jabatan': 'jabatan',
        'jobdesk': 'deskripsi_kerja'
    }
    transformed_dfs['pelamar_kerja'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 5. pendidikan -> pelamar_sekolah
if 'pendidikan' in raw_data:
    df = pd.DataFrame(raw_data['pendidikan'])
    df['tahun'] = df['tahun'].apply(extract_latest_year)
    df['ipk'] = df['ipk'].apply(clean_ipk)
    df['id_pelamar'] = df['idusers'].map(pelamar_id_map).astype('Int64')
    mapping = {
        'idpendidikan': 'id_pelamar_sekolah', 'id_pelamar': 'id_pelamar',
        'sekolah': 'nama_sekolah', 'jenjang': 'jenjang', 'prodi': 'prodi',
        'tahun': 'tahun_lulus', 'ipk': 'ipk', 'organisasi': 'organisasi'
    }
    transformed_dfs['pelamar_sekolah'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 6. kursus -> pelamar_kursus
if 'kursus' in raw_data:
    df = pd.DataFrame(raw_data['kursus'])
    df['tanggal'] = df['tanggal'].apply(parse_date)
    df['id_pelamar'] = df['idusers'].map(pelamar_id_map).astype('Int64')
    mapping = {
        'idkursus': 'id_pelamar_kursus', 'id_pelamar': 'id_pelamar',
        'nama': 'nama_kursus', 'tanggal': 'tanggal', 'deskripsi': 'deskripsi',
        'lokasi': 'lokasi', 'nosertifikat': 'nomor_sertifikat'
    }
    transformed_dfs['pelamar_kursus'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 7. pelamar_note -> progres_pelamar
if 'pelamar_note' in raw_data:
    df = pd.DataFrame(raw_data['pelamar_note'])
    df['status'] = df['status'].replace('baru', 'Baru')
    df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
    mapping = {
        'idnote': 'id_progres_pelamar', 'id_pelamar': 'id_pelamar',
        'idusers': 'id_user', 'status': 'status_progres_pelamar',
        'note': 'catatan', 'link': 'tautan_file', 'pertanyaan': 'pertanyaan',
        'created_at': 'created_at'
    }
    transformed_dfs['progres_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 8. pelamar_users -> rekrutmen_pelamar
if 'pelamar_users' in raw_data:
    df = pd.DataFrame(raw_data['pelamar_users'])
    df['id_pelamar'] = df['idpelamar'].map(pelamar_id_map).astype('Int64')
    mapping = {
        'idassign': 'id_rekrutmen', 'id_pelamar': 'id_pelamar', 'idusers': 'id_user'
    }
    transformed_dfs['rekrutmen_pelamar'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

print(f"OK: Transformasi {len(transformed_dfs)} tabel Fase 3 selesai.")"""

    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "# 3. pelamar -> pelamar" in "".join(cell["source"]):
            source_lines = cell["source"]
            # Find the line that has "# 3. pelamar -> pelamar"
            target_idx = -1
            for idx, line in enumerate(source_lines):
                if "# 3. pelamar -> pelamar" in line:
                    target_idx = idx
                    break
            
            if target_idx != -1:
                # Keep lines before "# 3. pelamar -> pelamar"
                new_lines = source_lines[:target_idx]
                # Append the new transformations
                for line in new_transformations.split("\n"):
                    new_lines.append(line + "\n")
                if new_lines[-1] == "\n": new_lines.pop()
                cell["source"] = new_lines
                patched = True
                break

    if patched:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 3 notebook patched successfully!")
    else:
        print("Error: Target cell in Fase 3 notebook not found.")

def patch_fase_4():
    path = "fase_4/script_hanif.ipynb"
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # Load file to find cell and replace the entire source of the target cell
    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "# 1. siswa -> siswa" in "".join(cell["source"]):
            source = "".join(cell["source"])
            
            # Replace mapping definition in siswa
            old_mapping = """        'kodepos': 'kode_pos', 'statussiswa': 'status_aktif', 'rekomen': 'rekomendasi',
        'info': 'sumber_info', 'pembayaran': 'metode_pembayaran', 'nama_ayah': 'nama_ayah',
        'pekerjaan_ayah': 'pekerjaan_ayah', 'jenjang_ayah': 'pendidikan_ayah', 
        'penghasilan_ayah': 'penghasilan_ayah', 'nama_ibu': 'nama_ibu', 'penghasilan_ibu': 'penghasilan_ibu',
        'jenjang_ibu': 'pendidikan_ibu', 'nama_wali': 'nama_wali', 'pekerjaan_wali': 'pekerjaan_wali',
        'jenjang_wali': 'pendidikan_wali', 'penghasilan_wali': 'penghasilan_wali',
        'wapeserta': 'wa_siswa', 'wawalmur': 'wa_ortu', 'waadmin': 'wa_administrasi',
        'sts_pengisian': 'status_pengisian', 'bukti': 'path_bukti_bayar', 'lulus': 'status_lulus_siswa',"""

            new_mapping = """        'kodepos': 'kode_pos', 'statussiswa': 'status_pendaftaran', 'rekomen': 'rekomendasi',
        'info': 'sumber_info', 'pembayaran': 'metode_pembayaran', 'nama_ayah': 'nama_ayah',
        'pekerjaan_ayah': 'pekerjaan_ayah', 'jenjang_ayah': 'pendidikan_ayah', 
        'penghasilan_ayah': 'penghasilan_ayah', 'nama_ibu': 'nama_ibu', 'penghasilan_ibu': 'penghasilan_ibu',
        'jenjang_ibu': 'pendidikan_ibu', 'nama_wali': 'nama_wali', 'pekerjaan_wali': 'pekerjaan_wali',
        'jenjang_wali': 'pendidikan_wali', 'penghasilan_wali': 'penghasilan_wali',
        'wapeserta': 'wa_siswa', 'wawalmur': 'wa_ortu', 'waadmin': 'wa_administrasi',
        'sts_pengisian': 'status_pengisian', 'bukti': 'path_bukti_bayar',"""

            source = source.replace(old_mapping, new_mapping)
            
            # Replace slow Kelurahan mapping loop with vectorized merge
            old_kelurahan_loop = """    kel_map = {}
    df_new_kel['key'] = df_new_kel['clean'] + "_" + df_new_kel['id_kecamatan'].astype(str)
    for _, row in df_old_kel.iterrows():
        new_kec_id = kec_map.get(row['idkecamatan'])
        if new_kec_id:
            key = row['clean'] + "_" + str(new_kec_id)
            match = df_new_kel[df_new_kel['key'] == key]
            if not match.empty:
                kel_map[row['idkelurahan']] = match.iloc[0]['id_kelurahan']"""
                
            new_kelurahan_merge = """    # Vectorized merge for Kelurahan mapping (Instant 1-second mapping for 83k rows!)
    df_old_kel['new_kec_id'] = df_old_kel['idkecamatan'].map(kec_map)
    df_old_kel_filtered = df_old_kel.dropna(subset=['new_kec_id']).copy()
    df_old_kel_filtered['new_kec_id'] = df_old_kel_filtered['new_kec_id'].astype(int)

    df_merged_kel = pd.merge(
        df_old_kel_filtered,
        df_new_kel,
        left_on=['new_kec_id', 'clean'],
        right_on=['id_kecamatan', 'clean'],
        how='inner'
    )
    kel_map = dict(zip(df_merged_kel['idkelurahan'], df_merged_kel['id_kelurahan']))"""
            
            source = source.replace(old_kelurahan_loop, new_kelurahan_merge)
            cell["source"] = [line + "\n" for line in source.split("\n")]
            if cell["source"][-1] == "\n": cell["source"].pop()
            patched = True
            break

    if patched:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 4 notebook patched successfully!")
    else:
        print("Error: Target cell in Fase 4 notebook not found.")

def patch_fase_5():
    path = "fase_5/script_hanif.ipynb"
    if not os.path.exists(path):
        print(f"File {path} not found.")
        return
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    new_transformations = """# 7. rapor -> rapor_siswa
if 'rapor' in raw_data:
    df = pd.DataFrame(raw_data['rapor'])
    
    # Generate integer ID auto-increment mapping
    df = df.reset_index()
    df['id_rapor_siswa_new'] = df['index'] + 1
    rapor_id_map = dict(zip(df['idrapor'], df['id_rapor_siswa_new']))
    df['id_rapor_siswa'] = df['id_rapor_siswa_new']
    
    mapping = {
        'id_rapor_siswa': 'id_rapor_siswa', 'idjadwal': 'id_jadwal', 'idsiswa': 'id_siswa',
        'tanggal': 'tanggal_input', 'idp_nilai': 'id_parameter_nilai', 'nilai': 'final_result'
    }
    transformed_dfs['rapor_siswa'] = df.rename(columns=mapping)[list(mapping.values())]

# 8. file_rapor_siswa -> rapor_siswa_file
if 'file_rapor_siswa' in raw_data and 'rapor_siswa' in transformed_dfs:
    df = pd.DataFrame(raw_data['file_rapor_siswa'])
    
    # Generate integer ID auto-increment mapping for file table
    df = df.reset_index()
    df['id_rapor_siswa_file_new'] = df['index'] + 1
    file_id_map = dict(zip(df['idfile'], df['id_rapor_siswa_file_new']))
    df['id_rapor_siswa_file'] = df['id_rapor_siswa_file_new']
    
    # Fetch old idrapor string and map it to new id_rapor_siswa integer
    df_rapor_old = pd.DataFrame(raw_data['rapor'])[['idsiswa', 'idjadwal', 'idrapor']].drop_duplicates(subset=['idsiswa', 'idjadwal'])
    df = df.merge(df_rapor_old, on=['idsiswa', 'idjadwal'], how='left')
    df['id_rapor_siswa'] = df['idrapor'].map(rapor_id_map).astype('Int64')
    
    mapping = {
        'id_rapor_siswa_file': 'id_rapor_siswa_file', 'id_rapor_siswa': 'id_rapor_siswa', 'path': 'file_rapor_path'
    }
    transformed_dfs['rapor_siswa_file'] = df.rename(columns=mapping).reindex(columns=list(mapping.values()))

# 9. history_rapor -> rapor_lacak
if 'history_rapor' in raw_data and 'rapor_siswa_file' in transformed_dfs:
    df = pd.DataFrame(raw_data['history_rapor'])
    df['status'] = df['status'].replace({'Terkirim': 'Terkirim', 'Gagal': 'Gagal'})
    
    df_file_old = pd.DataFrame(raw_data['file_rapor_siswa'])[['idfile', 'idsiswa', 'idjadwal']]
    df_file_old['id_rapor_siswa_file'] = df_file_old['idfile'].map(file_id_map).astype('Int64')
    
    mapping = {
        'idhistori': 'id_rapor_lacak', 'idsiswa': 'id_siswa',
        'idjadwal': 'id_jadwal', 'tgl': 'tanggal_terkirim', 'status': 'status_pengiriman'
    }
    df_merged = df.merge(df_file_old[['idsiswa', 'idjadwal', 'id_rapor_siswa_file']], on=['idsiswa', 'idjadwal'], how='left')
    df_final = df_merged.rename(columns=mapping)
    transformed_dfs['rapor_lacak'] = df_final[list(mapping.values()) + ['id_rapor_siswa_file']]

print(f"OK: Transformasi {len(transformed_dfs)} tabel Fase 5 selesai.")"""

    patched = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code" and "# 7. rapor -> rapor_siswa" in "".join(cell["source"]):
            source_lines = cell["source"]
            target_idx = -1
            for idx, line in enumerate(source_lines):
                if "# 7. rapor -> rapor_siswa" in line:
                    target_idx = idx
                    break
            
            if target_idx != -1:
                new_lines = source_lines[:target_idx]
                for line in new_transformations.split("\n"):
                    new_lines.append(line + "\n")
                if new_lines[-1] == "\n": new_lines.pop()
                cell["source"] = new_lines
                patched = True
                break

    if patched:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print("OK: Fase 5 notebook patched successfully!")
    else:
        print("Error: Target cell in Fase 5 notebook not found.")

if __name__ == "__main__":
    patch_fase_3()
    patch_fase_4()
    patch_fase_5()
