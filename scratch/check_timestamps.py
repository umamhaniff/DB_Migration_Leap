import os
import time

def main():
    csv_dir = 'extract/cek_csv'
    print(f"=== CHECKING FILE TIMESTAMPS IN {csv_dir} ===")
    
    files = sorted(os.listdir(csv_dir))
    for f in files:
        path = os.path.join(csv_dir, f)
        mtime = os.path.getmtime(path)
        size = os.path.getsize(path)
        mtime_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        print(f"File: {f:<30} | Size: {size:>8} bytes | Modified: {mtime_str}")

if __name__ == '__main__':
    main()
