from tkinter import*

root  = Tk()
Label(root, text="선호하는 언어를 모두 선택하시오:").grid(row=0, sticky=W)

Label1 = IntVar()
Checkbutton(root, text="Python", variable=Label1).grid(row=1, sticky=W)
Label2 = IntVar()
Checkbutton(root, text="C", variable=Label2).grid(row=2, sticky=W)
Label3 = IntVar()
Checkbutton(root, text="Java", variable=Label3).grid(row=3, sticky=W)
Label4 = IntVar()
Checkbutton(root, text="Swift", variable=Label4).grid(row=4, sticky=W)

root.mainloop()