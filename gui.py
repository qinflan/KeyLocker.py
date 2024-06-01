import customtkinter
from main import PasswordManager

# set basic theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")



root = customtkinter.CTk()
root.title("Password Manager")
root.geometry("1000x600")

# font objects
my_font = customtkinter.CTkFont("DM Sans 14pt", size=24, weight="bold")
btn = customtkinter.CTkFont("DM Sans 14pt", size=14, weight="bold")

# label - insert image and logo here
tempLabel = customtkinter.CTkLabel(master=root, text="Password Manager", font=my_font)
tempLabel.pack(pady=20, padx=10)

# frame container
frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(side="left", pady=20, padx=20, fill="both", expand=True)
frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(side="right", pady=20, padx=20, fill="both", expand=True)

# buttons
button1 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Get a password", font=btn)
button1.pack(pady=14, padx=10)

button2 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Add a password", font=btn)
button2.pack(pady=14, padx=10)

button3 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Create a new password file", font=btn)
button3.pack(pady=14, padx=10)

button4 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Load existing password file", font=btn)
button4.pack(pady=14, padx=10)

button5 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Create a new key", font=btn)
button5.pack(pady=14, padx=10)

button6 = customtkinter.CTkButton(master=frame1, width=210, height=50, text="Load an existing key", font=btn)
button6.pack(pady=14, padx=10)


# button output display function



root.mainloop()