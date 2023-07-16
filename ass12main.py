import ass12login,ass12forgotpass,ass12changepass,ass12navtofile,ass12register;
def main():
    while True:
        print("\nLogin Page")
        print("1. Login")
        print("2. Register")
        print("3. Forgot Password")
        print("4. Change Password")
        print("5. Navigate to a Site")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ass12login.login()
        elif choice == "2":
            ass12register.register()
        elif choice == "3":
            ass12forgotpass.forgot_password()
        elif choice == "4":
            ass12changepass.change_password()
        elif choice == "5":
           ass12navtofile.navigate_to_site()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()