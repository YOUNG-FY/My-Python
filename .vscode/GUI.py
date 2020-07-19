import tkinter as tk


class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.hi_there = tk.Button(frame, text="Say Hi", bg="black", fg="blue", command=self.OnButton)
        self.hi_there.pack()
    
    def OnButton(self):
        print("2 hong is little female dog.")

rootDlg = tk.Tk()
rootDlg.title("Test Dlg")

frame1 = tk.Frame(rootDlg)
frame1.pack()

pic = tk.PhotoImage(file="test.gif")
#app = APP(rootDlg)

img1 = tk.Label(frame1, image=pic)
img1.pack()

frame2 = tk.Frame(rootDlg)
frame2.pack(side=tk.LEFT)
text1 = tk.Label(frame2, 
                text="It is a cute cat. \nNo, It is a Q picture with lovly boy.",
                justify=tk.LEFT,
                image=pic,
                compound=tk.CENTER,
                fg="white",
                font=("仿宋",10),
                padx = 20)
text1.pack()

rootDlg.mainloop()

