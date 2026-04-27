contact_file ='data/contact.txt' # Define the path to the contact file

def add_contact(): 
    name = input('Enter contact name: ') 
    phone = input('Enter contact phone number: ') 
    with open(contact_file, 'a') as f: 
        f.write(f'{name}, {phone}\n')   
    print(f'🎉 {name} added successfully!') 

def view_contacts(): 
    try:
        with open(contact_file, 'r') as f:
            contacts = f.readlines()
            if not contacts:
                print('Your Contact List is Empty! Please add a contact first.')
            else:
                print('⭐ Your Contact List ⭐:')

                for contact in contacts:
                    print(contact, end='')
                 
    except FileNotFoundError as e:
        raise 'Your Contact List is Empty! Please add a contact first.' from e
    
def main(): # Main function to run the contact list application     
    while True:
        print('\nContact List Application:')
        print('1. Add Contact')
        print('2. View Contacts')
        print('3. Quit')
        choice = input('Enter your choice: ')
    
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print('Goodbye! Exiting the application.')
            break
        else:
            print('Invalid choice. Please try again.')
                
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")