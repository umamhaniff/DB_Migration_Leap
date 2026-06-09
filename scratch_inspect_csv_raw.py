with open("extract/cek_csv/pelamar.csv", "r") as f:
    lines = [f.readline() for _ in range(10)]

for i, line in enumerate(lines):
    print(f"Line {i}: {line.strip()}")
