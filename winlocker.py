import tkinter as tk

win = tk.Tk()

win.title("Не винлокер")
win.geometry("1920x1080")

tk.Label(win, text="я питарас").pack()

for i in range(999):
   new_win = tk.Toplevel()
   new_win.title(f"Окно-пидарас Номер {i+1}")
   new_win.geometry("1920x1080")

   tk.Label(new_win, text="И я тоже питарас!").pack()
   new_win.mainloop()

win.mainloop()
