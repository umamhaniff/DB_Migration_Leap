with open("extract/cek_csv/pelamar.csv", "r") as f:
    header = f.readline().strip().split(',')
    id_pengajuan_idx = header.index('id_pengajuan')
    for _ in range(50):
        line = f.readline()
        if not line:
            break
        parts = line.strip().split(',')
        if len(parts) > id_pengajuan_idx and parts[id_pengajuan_idx] != '':
            print(f"Raw line: {line.strip()[:100]}... -> id_pengajuan: '{parts[id_pengajuan_idx]}'")
