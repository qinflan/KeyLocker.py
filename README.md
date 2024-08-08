# KeyLocker: Password-Manager:
 A local python password manager that utilizes secret key encryption to store/retrieve passwords. Featuring a minimal graphical user interface, you're able to securely store passwords, and only access them with a secret generated key with Fernet Encryption.
![image alt](https://github.com/qinflan/KeyLocker.py/blob/d7b17599e6caf6e75213060f5e94426d02f74353/KeyLocker%20GUI%20Startup%20Frame.png)
# How to use:
 A user must first create a key and password file to add or update passwords from. These files must be loaded in order to be able to add/retrieve/update passwords.

 There is a file dialog prompt for creation and loading of these files, if a user does not have an existing key and password file, then they should initially create this pair. They can exist in any folder, but for improved security I'd recommend storing the key on a USB flash drive, which would provide a layer of physical security.


![image alt](https://github.com/qinflan/KeyLocker.py/blob/87ca62a2fe3a9080d177f427c9e6c13f379f2308/KeyLocker%20GUI%20Operations%20Frame.png)


# Intended Use:
 I originally created this password-manager at the command line, but wanted to implement a user friendly GUI to make it accessable to non-technical users. I'm currently thinking about developing a second version that would initiate a local database instance for a user, and store encrypted passwords through tables instead of a local file. However, I wanted to start by creating a safe local version that is not susceptible to SQL injection.

# Note:
 This is my first project involving encryption and a python graphical user-interface, so any criticism or feedback is welcome and appreciated! 

 Enjoy!

