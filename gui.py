import customtkinter
from main import PasswordManager
from PIL import Image


# Initialize PasswordManager Object
pm = PasswordManager()

# set basic theme
root = customtkinter.CTk()
root.title("KeyLocker")
root.iconbitmap("keylocker-dir/logo.ico")
root.geometry("1000x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# font objects
my_font = customtkinter.CTkFont("DM Sans 14pt", size=24, weight="bold")
btn = customtkinter.CTkFont("DM Sans 14pt", size=14, weight="bold")

# label - insert image and logo here
logo_img = customtkinter.CTkImage(dark_image=Image.open("keylocker-dir/logo+text.png"), 
light_image=Image.open("keylocker-dir/logo+text.png"), size=(400, 80))

logo_label = customtkinter.CTkLabel(master=root, text="", image=logo_img)
logo_label.place(rely=0.02, relx=0.05)

# frame containers
frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(side="left", pady=100, padx=40, fill="both", expand=True)
frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(side="right", pady=175, padx=40, fill="both", expand=True)

# entry handling
path_entry = customtkinter.CTkEntry(frame2, placeholder_text="Name key file", font=btn)
path_entry.pack(pady=20)

# output label display
output_label = customtkinter.CTkLabel(frame2, text="", font=my_font)
output_label.pack(pady=40)

# Button Callback Functions
def create_key_btn():
    path = path_entry.get()
    pm.create_key(path)
    output_label.configure(text=f"Created key at: {path}")

def load_key_btn():
    path = input("Enter path: ")
    pm.load_key(path)

def create_password_file_btn():
    path = input("Enter path: ")
    pm.create_password_file(path, password)

def load_password_file_btn():
    path = input("Enter path: ")
    pm.load_password_file(path)

def add_password_btn():
    site = input("Enter the site: ")
    password = input("Enter the password: ")
    pm.add_password(site, password)
            
def get_password_btn():
    site = input("What site do you want: ")
    print(f"Password for {site} is {pm.get_password(site)}")

# Submission Handling
def submit_path():
    user_input = path.get()
    return user_input

# buttons
button1 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Get a password", font=btn, command=get_password_btn)
button1.pack(pady=14, padx=10)

button2 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Add a password", font=btn, command=add_password_btn)
button2.pack(pady=14, padx=10)

button3 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Create a new password file", font=btn, command=create_password_file_btn)
button3.pack(pady=14, padx=10)

button4 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Load existing password file", font=btn, command=load_password_file_btn)
button4.pack(pady=14, padx=10)

button5 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Create a new key", font=btn, command=create_key_btn)
button5.pack(pady=14, padx=10)

button6 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Load an existing key", font=btn, command=load_key_btn)
button6.pack(pady=14, padx=10)

submit_button = customtkinter.CTkButton(master=frame2, width=100, height=50, text="Submit", font=btn, command=submit_path)
submit_button.pack(pady=20)

root.mainloop()