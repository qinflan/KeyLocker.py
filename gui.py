import customtkinter
from main import PasswordManager
from PIL import Image

# Initialize PasswordManagerGUI class
class App:
    
    def __init__(self):
        self.pm = PasswordManager()
        self.current_function = None
        self.output_msg = ""

        # set basic theme
        self.root = customtkinter.CTk()
        self.root.title("KeyLocker")
        self.root.iconbitmap("keylocker-dir/logo.ico")
        self.root.geometry("900x700")
        self.root.minsize(700,600)
        self.root.maxsize(1200,700)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        # font objects
        self.output_font = customtkinter.CTkFont("DM Sans 14pt", size=18, weight="bold")
        self.btn = customtkinter.CTkFont("DM Sans 14pt", size=14, weight="bold")

        # logo header
        logo_img = customtkinter.CTkImage(dark_image=Image.open("keylocker-dir/logo+text.png"), 
        light_image=Image.open("keylocker-dir/logo+text-black.png"), size=(300, 58))
        self.logo_label = customtkinter.CTkLabel(master=self.root, text="", image=logo_img)
        self.logo_label.pack(pady=100)

        # startup hero
        startup_img = customtkinter.CTkImage(dark_image=Image.open("keylocker-dir/flat-character-graphic.png"), 
        light_image=Image.open("keylocker-dir/flat-character-graphic.png"), size=(300, 300))
        self.startup_label = customtkinter.CTkLabel(master=self.root, text="", image=startup_img)
        self.startup_label.place(rely=0.45, relx=0.48)

        self.startup_desc = customtkinter.CTkLabel(master=self.root, 
            text="A free and easy way to safely\nsecure and manage your\npasswords", 
            font=self.output_font, 
            width=200, 
            height=90,
            justify="left")
        self.startup_desc.place(relx=0.48, rely=0.3)

        # icons
        folder_icon = customtkinter.CTkImage(Image.open("keylocker-dir/folder-icon.png"), size=(22,22))
        search_icon = customtkinter.CTkImage(Image.open("keylocker-dir/search-icon.png"), size=(22,22))
        view_icon = customtkinter.CTkImage(Image.open("keylocker-dir/list-icon.png"), size=(30,30))
        add_icon = customtkinter.CTkImage(Image.open("keylocker-dir/add-icon.png"), size=(20,20))
        new_key_icon = customtkinter.CTkImage(Image.open("keylocker-dir/add-key-icon2.png"), size=(23,23))
        add_file_icon = customtkinter.CTkImage(Image.open("keylocker-dir/add-file.png"), size=(25,25))
        key_icon = customtkinter.CTkImage(Image.open("keylocker-dir/logo.png"), size=(22,22))


    # frame containers
    #-----------------------

        # get/add password buttons
        self.frame1 = customtkinter.CTkFrame(master=self.root)
        self.frame1.place(relx = 0.08, rely = 0.2, relwidth = 0.35, relheight = 0.34)
        self.frame1.columnconfigure((0), weight = 1)
        self.frame1.rowconfigure((0,1,2), weight = 1)
        self.frame1.place_forget()

        # submission and output frame
        self.frame2 = customtkinter.CTkFrame(master=self.root)
        self.frame2.place(relx = 0.47, rely = 0.2, relwidth = 0.45, relheight = 0.34)
        self.frame2.columnconfigure((0), weight = 1)
        self.frame2.rowconfigure((0,1,2,3), weight = 1)
        self.frame2.place_forget()

        # grid frame for file/load buttons
        self.startup_frame1 = customtkinter.CTkFrame(master=self.root)
        self.startup_frame1.place(relx = 0.1, rely = 0.3, relheight = 0.25, relwidth = 0.32)
        self.startup_frame1.columnconfigure((0), weight = 1)
        self.startup_frame1.rowconfigure((0,1), weight = 1)
        

        self.startup_frame2 = customtkinter.CTkFrame(master=self.root)
        self.startup_frame2.place(relx = 0.1, rely = .58, relheight = 0.25, relwidth = 0.32)
        self.startup_frame2.columnconfigure((0), weight = 1)
        self.startup_frame2.rowconfigure((0,1), weight = 1)

        

        # entry handling
        self.entry_box = customtkinter.CTkEntry(self.frame2, width=250, placeholder_text="Select an option", font=self.btn)
        self.entry_box.grid(row = 0)
        self.password_entry = customtkinter.CTkEntry(self.frame2, width=250, placeholder_text="Enter password", font=self.btn, show="●")
        self.password_entry.grid(row=1)  # Initially grid it, but set it to be invisible
        self.password_entry.grid_remove()  # Hide it initially


    # Submission Handling
        def submit_input():
            user_input = self.entry_box.get()
            user_password = self.password_entry.get()

            # validate input
            if not user_input:
                self.output_msg = "No input received"
                self.output_label.configure(text=self.output_msg)
                self.output_label.grid()

            try:
            # add_password() submission
                if user_password:
                    if self.current_function:
                        self.current_function(user_input, user_password)
                    self.current_function(user_input, user_password)
                    self.output_label.configure(text=self.output_msg)
                    self.output_label.grid()
                    self.entry_box.delete(0, 'end')
                    self.password_entry.delete(0, 'end')

                # create file on submit
                else:
                    if user_input and self.current_function:
                        self.current_function(user_input)
                    self.output_label.configure(text=self.output_msg)
                    self.output_label.grid()
                    self.entry_box.delete(0, 'end')
                    self.root.focus_set()
                    self.entry_box.configure(placeholder_text="Select an option")

                    # display password when get_password() is called
                    if self.current_function == self.pm.get_password:
                        password = self.current_function(user_input)
                        if password:
                            self.display_password.configure(state="normal")  # Enable the text box
                            self.display_password.delete("1.0", "end")  # Clear previous content
                            self.output_msg = f"Password for {user_input}"
                            self.output_label.configure(text=self.output_msg)
                            self.output_label.grid(row=2)
                            self.display_password.tag_config("center", justify='center')
                            self.display_password.insert("end", password)  # Insert password
                            self.display_password.configure(state="disabled")  # Set back to read-only
                            self.display_password.tag_add("center", "1.0", "end")
                            self.display_password.grid()

                self.entry_box.delete(0, 'end')
                self.root.focus_set()
                self.entry_box.configure(placeholder_text="Select an option")

            except ValueError as e:
                    self.output_msg = str(e)
                    self.output_label.configure(text=self.output_msg)
                    self.output_label.grid()

            self.entry_box.delete(0, 'end')
            self.root.focus_set()
            self.entry_box.configure(placeholder_text="Select an option")


    # Button Callback Functions
        def create_key_btn():
            self.display_password.grid_remove()
            self.password_entry.grid_remove()
            self.display_sites.grid_remove()
            self.output_label.grid_remove()
            submit_button.grid(row=1)
            self.entry_box.configure(placeholder_text="Specify name for key")
            self.current_function = self.pm.create_key
            self.output_msg = "Key successfully created"

        def load_key_btn():
            self.display_password.grid_remove()
            self.password_entry.grid_remove()
            self.display_sites.grid_remove()
            self.output_label.grid_remove()
            submit_button.grid(row=1)
            self.current_function = self.pm.load_key
            self.entry_box.configure(placeholder_text="Specify key filename")
            self.output_msg = "Key loaded successfully"
            open_file()

    # Create blank file if no values are given, API library requires filename
        def create_password_file_btn():
            self.display_password.grid_remove()
            self.password_entry.grid_remove()
            self.display_sites.grid_remove()
            self.output_label.grid_remove()
            submit_button.grid(row=1)
            self.current_function = self.pm.create_password_file
            self.entry_box.configure(placeholder_text="Specify name for password file")
            self.output_msg = "Password file created"

        def load_password_file_btn():
            self.display_password.grid_remove()
            self.password_entry.grid_remove()
            self.display_sites.grid_remove()
            self.output_label.grid_remove()
            submit_button.grid(row=1)
            self.current_function = self.pm.load_password_file
            self.entry_box.configure(placeholder_text="Specify password filename")
            self.output_msg = "Password file loaded successfully"
            open_file()

        def add_password_btn():
            self.display_password.grid_remove()
            self.password_entry.grid_remove()
            self.display_sites.grid_remove()
            self.output_label.grid(row=3)
            self.output_label.grid_remove()
            submit_button.grid(row=2)
            self.current_function = lambda site, password: self.pm.add_password(site, password)
            self.entry_box.configure(placeholder_text="Enter site/service name")
            self.password_entry.grid()
            self.output_msg = "Password added"
                    
        def get_password_btn():
            self.password_entry.grid_remove()
            self.display_sites.grid_remove()
            self.output_label.grid_remove()
            submit_button.grid(row=1)
            self.current_function = self.pm.get_password
            self.entry_box.configure(placeholder_text="Enter site for password") 

        def get_sites_btn():
            self.password_entry.grid_remove()
            self.display_password.grid_remove()
            submit_button.grid(row=1)
            self.entry_box.configure(placeholder_text="Select an option")
            self.current_function = self.pm.get_sites
            self.output_msg = "Associated sites"
            self.display_sites.configure(state="normal", height=60)  # Enable the text box
            self.display_sites.delete("1.0", "end")  # Clear previous content

            # Error handling - ensure password file is loaded
            try:
                for site in self.current_function():
                    self.display_sites.insert("end", f"{site}\n")  # Insert site
                self.display_sites.configure(state="disabled",)  # Set back to read-only
                self.display_sites.tag_config("center", justify='center')
                self.display_sites.tag_add("center", "1.0", "end")
                self.display_sites.grid()
                self.output_label.configure(text=self.output_msg)
                self.output_label.grid(row=2)

            # Output error message
            except:
                self.output_msg = "Please load password file"
                self.output_label.configure(text=self.output_msg)
                self.output_label.grid(row=2)


        def toggle_theme():
            val=self.switch.get()
            if val:
                customtkinter.set_appearance_mode("light")
            else:
                customtkinter.set_appearance_mode("dark")


# TODO: add error handling - key must be loaded first
        def open_file():
            path = customtkinter.filedialog.askopenfilename()
            if path:
                self.current_function(path)
                self.output_label.configure(text=self.output_msg)
                self.output_label.grid()


# TODO: fucntion for dynamically switching startup frames to operations frames 
        def switch_frames():
            if self.pm.check_loaded():
                self.startup_frame1.destroy()
                self.startup_frame2.destroy()
                self.startup_frame3.destroy()
                self.startup_label.destroy()
                self.logo_label.configure()
                self.frame1.place()
                self.frame2.place()
                self.frame3.place()

            # add error msg handling here
            else: 
                pass


    # buttons
        button1 = customtkinter.CTkButton(master=self.frame1, 
            image=search_icon,
            width=210, 
            height=50, 
            compound="right",
            corner_radius=14, 
            text="Retrieve password", 
            font=self.btn, 
            command=get_password_btn)
        button1.grid(row=0, pady=10, padx=10, sticky="s")

        button2 = customtkinter.CTkButton(master=self.frame1,
            image=add_icon,
            width=210, 
            height=50,
            compound="right",
            corner_radius=14,
            text="Add a password", 
            font=self.btn, 
            command=add_password_btn)
        button2.grid(row=1, pady=10, padx=10)

        button3 = customtkinter.CTkButton(master=self.frame1, 
            image=view_icon,
            width=210, 
            height=50,
            compound="right",
            corner_radius=14,
            text="View used sites", 
            font=self.btn, 
            command=get_sites_btn)
        button3.grid(row=2, pady=10, padx=10, sticky="n")

        # submission button
        submit_button = customtkinter.CTkButton(master=self.frame2,
            width=100, 
            height=40,
            corner_radius=14,
            text="Submit", 
            font=self.btn, 
            command=submit_input)
        submit_button.grid(row = 1)


        # startup frame buttons
        #-----------------------
        button4 = customtkinter.CTkButton(master=self.startup_frame2, 
            image=add_file_icon,
            width=200, 
            height=50,
            compound="right",
            corner_radius=14,
            text="Create password file", 
            font=self.btn, 
            command=create_password_file_btn)
        button4.grid(row = 1, pady=10, padx=12, sticky="nwe")

        button5 = customtkinter.CTkButton(master=self.startup_frame1, 
            image=folder_icon,
            width=200, 
            height=50,
            compound="right",
            corner_radius=14,
            text="Load password file", 
            font=self.btn, 
            command=load_password_file_btn)
        button5.grid(row = 1, pady=10, padx=12, sticky="nwe")

        button6 = customtkinter.CTkButton(master=self.startup_frame2, 
            image=new_key_icon,
            width=200, 
            height=50,
            compound="right",
            corner_radius=14,
            text="Create a new key", 
            font=self.btn, 
            command=create_key_btn)
        button6.grid(row = 0, pady=10, padx=12, sticky="swe")

        button7 = customtkinter.CTkButton(master=self.startup_frame1, 
            image=key_icon,
            width=200, 
            height=50,
            compound="right",
            corner_radius=14,
            text="Load existing key",
            font=self.btn, 
            command=load_key_btn)
        button7.grid(row = 0, pady=10, padx=12, sticky="swe")


    # light mode/dark mode switch
        self.switch = customtkinter.CTkSwitch(self.root, text='Toggle Theme',
            font=self.btn,
            onvalue=1,
            offvalue=0,
            command=toggle_theme)
        self.switch.place(relx = 0.72, rely = 0.1)
        print(self.switch.get())

    # output message widget
        self.output_label = customtkinter.CTkLabel(master = self.frame2, text="", font = self.btn)
        self.output_label.grid(row = 2)


    # output password widget
        self.display_password = customtkinter.CTkTextbox(self.frame2, height=1, font=self.btn)
        self.display_password.grid(row=3)
        self.display_password.grid_remove()

    # output sites widget
        self.display_sites = customtkinter.CTkTextbox(self.frame2, height=2, font=self.btn)
        self.display_sites.grid(row=3, sticky="ns", pady=10)
        self.display_sites.grid_remove()


        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    