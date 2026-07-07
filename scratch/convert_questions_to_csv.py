import csv

def parse_questions_md():
    path = "questions.md"
    students = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if "|" in line and "nama_lengkap" not in line and "---" not in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                # Format: | nama_lengkap | nomor_induk | kursus | tipe_kursus |
                name = parts[1]
                no_induk = parts[2]
                kursus = parts[3]
                tipe_kursus = parts[4]
                if name and no_induk:
                    students.append({
                        'nama_lengkap': name,
                        'nomor_induk': no_induk,
                        'kursus': kursus,
                        'tipe_kursus': tipe_kursus
                    })
    return students

def main():
    students = parse_questions_md()
    
    # Save to CSV in fase_4
    csv_path = "fase_4/daftar_siswa_keluar.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['nama_lengkap', 'nomor_induk', 'kursus', 'tipe_kursus'])
        writer.writeheader()
        for s in students:
            writer.writerow(s)
            
    print(f"Successfully converted {len(students)} rows to {csv_path}")

if __name__ == '__main__':
    main()
