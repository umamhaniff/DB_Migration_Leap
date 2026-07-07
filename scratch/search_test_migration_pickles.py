import os

def main():
    print("--- Searching for test_migration_pickles.py ---")
    for root, dirs, files in os.walk("."):
        for f in files:
            if "test_migration_pickles" in f:
                print(os.path.join(root, f))

if __name__ == '__main__':
    main()
