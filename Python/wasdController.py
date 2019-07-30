import tkinter as tk
import time
# from Submarine import Submarine


class Example(tk.Frame):
    # thisSub = Submarine()
    previous = ''

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=400,  height=400)

        self.label = tk.Label(self, text="last key pressed:  ", width=20)
        self.label.pack(fill="both", padx=100, pady=100)

        self.label.bind("<w>", self.on_wasd)
        self.label.bind("<a>", self.on_wasd)
        self.label.bind("<s>", self.on_wasd)
        self.label.bind("<d>", self.on_wasd)
        self.label.bind("<q>", self.on_wasd)
        self.label.bind("<z>", self.on_wasd)
        # give keyboard focus to the label by default, and whenever
        # the user clicks on it
        self.label.focus_set()
        self.label.bind("<1>", lambda event: self.label.focus_set())

    def on_wasd(self, event):
        self.label.configure(text="last key pressed: " + event.keysym)
        if event.keysym == 'w':
            print("Went W")
            time.sleep(1)
            print("Unwent W")
            # thisSub.goForward()
        if event.keysym == 's':
            print("Went S")
            time.sleep(1)
            print("Unwent S")
            # thisSub.goBackward()

        # Submarine.goForward()


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
