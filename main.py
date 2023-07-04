import customtkinter as ctk

class App:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('250x200') #making a set frame so the user won't mess with it 
        self.master.resizable(False, False)
        self.master.wm_title('increment Counter')

        # Displaying counter (always is displayed in str that's why we chose the type as STR)
        self.Counter: str = '0'

        # Creates a label
        self.label = ctk.CTkLabel(self.master, text=self.Counter, font=('Helvetica bold', 26))
        self.label.place(relx=0.5, rely=0.4, anchor='center')

        # Creates a button
        self.button = ctk.CTkButton(self.master, text='Inccrement', command=self.increment, corner_radius=20)
        self.button.place(relx=0.5, rely=0.6, anchor='center')

        self.reset_button: ctk.CTkButton | None = None
    
    
    
    def increment(self):# Increments the counter
        try:
            self.Counter = str(int(self.Counter) + 1)
            self.label.configure(text=self.Counter)

            if int(self.Counter) == 1:
                self.reset_button = ctk.CTkButton(self.master, text="Reset", command=self.reset, corner_radius=20, fg_color='red', hover_color='darkred')
                self.reset_button.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            print('Error', e)

    def reset(self):# Resets the counter
        try:
            self.Counter = '0'
            self.label.configure(text=self.Counter)

            self.reset_button.destroy()
        except Exception as e:
            print('Error', e)


if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()