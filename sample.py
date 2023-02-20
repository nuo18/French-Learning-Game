import tkinter as tk

class NewWindowDemo:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")

        self.button = tk.Button(self.master, text="Open New Window", command=self.open_new_window)
        self.button.pack()

    def open_new_window(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("New Window")
        self.new_window.geometry("200x200")

        self.label = tk.Label(self.new_window, text="This is a new window!")
        self.label.pack()
    
    def create_window(self):
        if not self.window_open:  # Check if window is already open
            self.new_window = tk.Toplevel(self.master)
            self.new_window.title("New Window")
            self.new_window.geometry("200x200")
            self.new_window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Set flag to True
        self.window_open = True


if __name__ == '__main__':
    root = tk.Tk()
    app = NewWindowDemo(root)
    root.mainloop()
