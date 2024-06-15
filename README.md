# KeyLocker: Password-Manager:
 A local python password manager that utilizes secret key encryption to store/retrieve passwords. Featuring a minimal graphical user interface, you're able to securely store passwords, and only access them with a secret generated key with Fernet Encryption.

# How to use:
 A user must first create a key and password file to add or update passwords from. These files must be loaded in order to be able to add/retrieve/update passwords.

 There is a file dialog prompt for creation and loading of these files, if a user does not have an existing key and password file, the user must initially create this pair. They can exist in any folder, but for improved security I'd recommend storing the key on a USB flash drive, which would provide a layer of physical security.

# Intended Use:
 I originally created this password-manager at the command line, but wanted to implement a user friendly GUI to make it accessable to non-technical users. I'm currently thinking about developing a second version that would initiate a local database instance for a user, and store encrypted passwords through tables instead of a local file. However, I wanted to start by creating a safe local version that is not susceptible to SQL injection.

# Note:
 This is my first project involving encryption, so any criticism or feedback is welcome and appreciated! 

 Enjoy!

