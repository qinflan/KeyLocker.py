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
root.minsize(700,500)
root.maxsize(1200,800)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# font objects
output_font = customtkinter.CTkFont("DM Sans 14pt", size=24, weight="bold")
btn = customtkinter.CTkFont("DM Sans 14pt", size=14, weight="bold")

# logo header
logo_img = customtkinter.CTkImage(dark_image=Image.open("keylocker-dir/logo+text.png"), 
light_image=Image.open("keylocker-dir/logo+text-black.png"), size=(300, 58))
logo_label = customtkinter.CTkLabel(master=root, text="", image=logo_img)
logo_label.place(rely=0.02, relx=0.1)


# frame containers
#-----------------------

# get/add password buttons
frame1 = customtkinter.CTkFrame(master=root)
frame1.place(relx = 0.08, rely = 0.15, relwidth = 0.35, relheight = 0.38)

# submission and output frame
frame2 = customtkinter.CTkFrame(master=root)
frame2.place(relx = 0.47, rely = 0.15, relwidth = 0.45, relheight = 0.38)

# grid frame for file/load buttons
frame3 = customtkinter.CTkFrame(master=root)
frame3.place(relx = 0.08, rely = 0.58, relheight = 0.38, relwidth = 0.84)
frame3.columnconfigure((0,1,2), weight = 1)
frame3.rowconfigure((0,1,2), weight = 1)

# entry handling
path_entry = customtkinter.CTkEntry(frame2, width=250, placeholder_text="Enter site for password", font=btn)
path_entry.pack(pady=40)

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

# insert logic for pulling all keys from (key, value) pair in API
def view_sites():
    pass

# Submission Handling
def submit_path():
    user_input = path.get()
    return user_input

def toggle_theme():
    val=switch.get()
    if val:
        customtkinter.set_appearance_mode("light")
    else:
        customtkinter.set_appearance_mode("dark")

# buttons
button1 = customtkinter.CTkButton(master=frame1, 
    width=210, 
    height=50, 
    corner_radius=14, 
    text="Retrieve password", 
    font=btn, 
    command=get_password_btn)
button1.pack(pady=10, padx=0)

button2 = customtkinter.CTkButton(master=frame1, 
    width=210, 
    height=50,
    corner_radius=14,
    text="Add a password", 
    font=btn, 
    command=add_password_btn)
button2.pack(pady=10, padx=10)

button3 = customtkinter.CTkButton(master=frame1, 
    width=210, 
    height=50,
    corner_radius=14,
    text="View used sites", 
    font=btn, 
    command=add_password_btn)
button3.pack(pady=10, padx=10)

button4 = customtkinter.CTkButton(master=frame3, 
    width=250, 
    height=50,
    corner_radius=14,
    text="Create new password file", 
    font=btn, 
    command=create_password_file_btn)
button4.grid(row = 0, column = 0, sticky="se")

button5 = customtkinter.CTkButton(master=frame3, 
    width=250, 
    height=50,
    corner_radius=14,
    text="Load password file", 
    font=btn, 
    command=load_password_file_btn)
button5.grid(row = 0, column = 2, sticky="sw")

button6 = customtkinter.CTkButton(master=frame3, 
    width=250, 
    height=50,
    corner_radius=14,
    text="Create a new key", 
    font=btn, 
    command=create_key_btn)
button6.grid(row = 2, column = 0, sticky="ne")

button7 = customtkinter.CTkButton(master=frame3, 
    width=250, 
    height=50,
    corner_radius=14,
    text="Load existing key",
    font=btn, 
    command=load_key_btn)
button7.grid(row = 2, column = 2, sticky="nw")

submit_button = customtkinter.CTkButton(master=frame2,
    width=100, 
    height=40,
    corner_radius=14,
    text="Submit", 
    font=btn, 
    command=submit_path)
submit_button.pack(side="top")

# light mode/dark mode switch
switch = customtkinter.CTkSwitch(root, text='Toggle Theme',
    font=btn,
    onvalue=1,
    offvalue=0,
    command=toggle_theme)
switch.place(relx = 0.72, rely = 0.06)
print(switch.get())

root.mainloop()