import os
import glob

def main():
    print("--- Scanning for Notebooks in Fase 1 - 5 ---")
    for i in range(1, 6):
        folder = f"fase_{i}"
        if os.path.exists(folder):
            notebooks = glob.glob(os.path.join(folder, "*.ipynb"))
            print(f"\nFolder: {folder}")
            for nb in sorted(notebooks):
                print(f"  - {os.path.basename(nb)} ({os.path.getsize(nb)} bytes)")

if __name__ == '__main__':
    main()
