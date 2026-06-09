import sys
import os

# Add config.gemini folder directly to sys.path to bypass the folder dot-naming issue
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.gemini'))
import apply_migration_updates

def update_fase_3():
    apply_migration_updates.patch_fase_3()
    apply_migration_updates.patch_fase_3_insert_handler()

def update_fase_4():
    apply_migration_updates.patch_fase_4()

def update_fase_5():
    apply_migration_updates.patch_fase_5()

if __name__ == '__main__':
    update_fase_3()
    update_fase_4()
    update_fase_5()
    print("Update notebooks finished.")
