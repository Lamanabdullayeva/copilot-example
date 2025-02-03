import shutil

active_db_file = 'app.db'
backup_db_file = 'backup.db'

def backup_db():
    shutil.copy(active_db_file, backup_db_file)
    print(f'Backup of {active_db_file} created successfully!')

def restore_db():
    shutil.copy(backup_db_file, active_db_file)
    print(f'{active_db_file} restored successfully!')

def print_menu():
    print('1. Backup the database')
    print('2. Restore the database')
    print('3. Exit')

def get_user_choice():
    return input('Enter your choice: ')

def handle_choice(choice):
    if choice == '1':
        backup_db()
    elif choice == '2':
        restore_db()
    else:
        print('Invalid choice')

def main():
    print_menu()
    choice = get_user_choice()
    handle_choice(choice)

if __name__ == '__main__':
    main()
