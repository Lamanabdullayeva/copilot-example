import shutil

active_db_file =  'app.db'
backup_db_file = 'backup.db'

def backup_db():
    shutil.copy(active_db_file, backup_db_file)
    print(f'Backup of {active_db_file} created successfully!')

def restore_db():

    shutil.copy(backup_db_file, active_db_file)
    print(f'{active_db_file} restored successfully!')

def main():
    print('1. Bakcup the database')
    print('2. Restore the database')
    print('3. Exit')

    choice = input('Enter your choice: ')
    if choice == '1':
        backup_db()
    elif choice == '2':
        restore_db()
    else:
        print('Invalid choice')

    if __name__ == '__main__':
        main()
