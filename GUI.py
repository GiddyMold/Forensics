import tkinter as tk
from tkinter import filedialog

class DirectoryChooserApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Directory Chooser")

        self.full_name_var = tk.StringVar()
        self.source_drive_var = tk.StringVar()
        self.first_copy_var = tk.StringVar()
        self.second_copy_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.create_entry_panel("Full Name:", self.full_name_var, row=0)
        self.create_entry_panel("Source Drive Path:", self.source_drive_var, row=1, choose_directory=True)
        self.create_entry_panel("First Copy Path:", self.first_copy_var, row=2, choose_directory=True)
        self.create_entry_panel("Second Copy Path:", self.second_copy_var, row=3, choose_directory=True)

        ok_button = tk.Button(self.master, text="OK", command=self.return_values)
        ok_button.grid(row=4, column=1, pady=10)

    def create_entry_panel(self, label_text, var, row, choose_directory=False):
        entry_label = tk.Label(self.master, text=label_text)
        entry_label.grid(row=row, column=0, padx=5, pady=5, sticky=tk.E)

        entry = tk.Entry(self.master, textvariable=var, width=30)
        entry.grid(row=row, column=1, padx=5, pady=5, sticky=tk.W)

        if choose_directory:
            button = tk.Button(self.master, text="Choose", command=lambda: self.choose_directory(var))
            button.grid(row=row, column=2, padx=5, pady=5)

    def choose_directory(self, var):
        directory_path = filedialog.askdirectory()
        var.set(directory_path)

    def return_values(self):
        self.master.destroy()  # Close the window after clicking OK


def return_GUI():
    root = tk.Tk()
    app = DirectoryChooserApp(root)
    root.mainloop()
    
    return app.full_name_var.get(), app.source_drive_var.get(), app.first_copy_var.get(), app.second_copy_var.get()