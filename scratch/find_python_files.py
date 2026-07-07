import os
import glob

def main():
    print("--- Listing Python scripts in Root and Subfolders ---")
    files = glob.glob("**/*.py", recursive=True)
    for f in sorted(files):
        if "venv" not in f and ".gemini" not in f:
            print(f)

if __name__ == '__main__':
    main()
