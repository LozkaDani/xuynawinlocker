import tkinter as tk
import asyncio

async def openWindow(i):
   new_win = tk.Toplevel()
   new_win.title(f"Окно-пидарас Номер {i+1}")
   new_win.geometry("1920x1080")
   tk.Label(new_win, text="И я тоже питарас!").pack()

def main():
    win = tk.Tk()
    win.title("Не винлокер")
    win.geometry("1920x1080")
    tk.Label(win, text="я питарас").pack()

    for i in range(69):
        asyncio.run(openWindow(i))
    win.mainloop()

if (__name__ == "__main__"):
    main()