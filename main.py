from cryptography.fernet import Fernet

# need to add input validation
class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        if not path:
            raise ValueError("No path specified for the key")
        
        try:
            with open(path, 'rb') as f:
                self.key = f.read()
        except:    raise ValueError("Unable to load key")

    def create_password_file(self, path, initial_values=None):
        self.password_file = path
        with open(path, 'wb'):
            pass
    
        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        if not path:
            raise ValueError("No path specified for the password file")

        try:
            self.password_file = path

            with open(path, 'r') as f:
                for line in f:
                    site, encrypted = line.split(":")
                    self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
       
        except:   raise ValueError("Unable to load Password File")
        

    def add_password(self, site, password):
        if site not in self.password_dict:
            self.password_dict[site] = password

            if self.password_file is not None:
                with open(self.password_file, 'a+') as f:
                    encrypted = Fernet(self.key).encrypt(password.encode())
                    f.write(site + ":" + encrypted.decode() + "\n")

            if not site:    raise ValueError("Please enter a site name")


    def get_password(self, site):
        if site in self.password_dict:
            return self.password_dict[site]
        
        else:   raise ValueError("Unable to locate site in password file")
        
# TODO: FIX THIS FUNCTION
    def get_sites(self, path):
        try: 
            self.load_password_file(path)
            if self.password_dict:
                return list(self.password_dict.keys())
            else:
                raise ValueError("No sites found in password dictionary")
        except Exception as e:
            raise ValueError("Unable to load password file") from e
    


def main():

    #test case
    password = {
        "email": "1234567",
        "facebook": "myfbpassword",
        "youtube": "helloworld123",
        "x":"elonsucks"
    }

    pm = PasswordManager()

# Command Line Interface
    print("""What do you want to do?
        (1) Create a new key
        (2) Load an existing key
        (3) Create a new password file
        (4) Load existing password file
        (5) Add a new password
        (6) Get a password
        (7) View associated sites
        (q) Quit
        """)

    done = False

    while not done:
        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)

        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)

        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path)

        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)

        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
            
        elif choice == "6":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
            
        elif choice == "7":
            sites = pm.get_sites()
            print("Associated sites:")
            for site in sites:
                print(site)

        elif choice == "q":
            done = True
            print("Enjoy!")

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()