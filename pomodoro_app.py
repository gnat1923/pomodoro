import customtkinter

class MyCustomSettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
            
        self.customise_label = customtkinter.CTkLabel(self, text="Customize Options", fg_color="gray30", corner_radius=6)
        self.customise_label.grid(row=0, column=0, padx=20, pady=(20,0))

        self.focus_time = customtkinter.CTkEntry(self, placeholder_text="Focus Duration - 25")
        self.focus_time.grid(row=1, column=0, padx=20, pady=(20,0), sticky="ew")
        self.break_time = customtkinter.CTkEntry(self, placeholder_text="Break Duration - 5")
        self.break_time.grid(row=2, column=0, padx=20, pady=(20,0), sticky="ew")
        self.cycle_counter = customtkinter.CTkEntry(self, placeholder_text="No. of cycles - 4")
        self.cycle_counter.grid(row=3, column=0, padx=20, pady=(20,0), sticky="ew")

        self.button_submit = customtkinter.CTkButton(self, text="Submit", command=self.submit_config)
        self.button_submit.grid(row=5, column=0, padx=20, pady=20)


    def submit_config(self):
        # Some code here
        print("config submitted")

class MyOperationFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1, 2,3), weight=1)
        self.grid_rowconfigure((0, 1, 2,4,5,6), weight=1)

        self.operations_label = customtkinter.CTkLabel(self, text="Pomodoro", fg_color="gray30", corner_radius=6)
        self.operations_label.grid(row=0, column=1, columnspan=4, padx=20, pady=(20,0), sticky="ew")

        self.timer_label = customtkinter.CTkLabel(self, text="TIMER", corner_radius=6)
        self.timer_label.grid(row=1, column=1, columnspan=4, padx=20, pady=(20,0), sticky="ew")

        self.message_label = customtkinter.CTkLabel(self, text="MESSAGE", corner_radius=6)
        self.message_label.grid(row=2, column=1, columnspan=4, padx=20, pady=(20,20), sticky="ew")

        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal")
        self.progressbar.grid(row=3, column=1, padx=20, pady=(20,0), columnspan=4, sticky="ew")

        self.spacer_label1 = customtkinter.CTkLabel(self, text="", corner_radius=6)
        self.spacer_label1.grid(row=2, column=1, rowspan=2, padx=20, pady=(20,0), sticky="ew")
        
        self.button_start = customtkinter.CTkButton(self, text="START", command=self.start_timer)
        self.button_start.grid(row=6, column=1, columnspan=4, pady=20, padx=20, sticky="ew")

    def start_timer(self):
        # Some code here
        print("Start")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("650x300")
        self.title("Extreme Pomodoro")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=3)

        self.customize_frame = MyCustomSettingsFrame(self)
        self.customize_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nse")

        self.operation_frame = MyOperationFrame(self)
        self.operation_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsw")

        

        # add widgets to app
        #self.button = customtkinter.CTkButton(self, command=self.button_click)
        #self.button.grid(row=0, column=0, padx=20, pady=10)

        


    # add methods to app
    def button_click(self):
        print("button click")


app = App()
app.mainloop()