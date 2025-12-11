import tkinter as tk

class Person:
    def __init__(self, name: str):
        self.name = name

class HobbyPerson(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.hobbies = []  

    def add_hobby(self, hobby: str):
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)

    def clear_hobbies(self):
        self.hobbies.clear()

root = tk.Tk()
root.title("문제 2")
root.geometry("380x260")


stu = HobbyPerson("김덕성") #객체 생성
title = tk.Label(root, text=f"이름: {stu.name}", font=("맑은 고딕", 11, "bold"))
title.pack(pady=6)

frm_main = tk.Frame(root)
frm_main.pack(pady=10)

var_g  = tk.IntVar(value=0)
var_r  = tk.IntVar(value=0)
var_e  = tk.IntVar(value=0)

tk.Label(frm_main, width=15).pack()
tk.Radiobutton(frm_main, text="게임",  variable=var_g).pack(side="left", padx=10)
tk.Radiobutton(frm_main, text="독서",  variable=var_r).pack(side="left", padx=10)
tk.Radiobutton(frm_main, text="운동", variable=var_e).pack(side="left", padx=10)


result = tk.StringVar(value="취미를 선택하고 [등록하기]를 누르세요.")
lb = tk.Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=8)


def register():
    stu.clearCourses()
    if var_g.get(): stu.add_hobby("게임")
    if var_r.get(): stu.add_hobby("독서")
    if var_e.get(): stu.add_hobby("운동")

    if stu.hobbies:
        result.set(f"현재 취미: {stu.hobbies}")
    else:
        result.set("선택된 취미가 없습니다.")

def reset():
    var_g.set(0); var_r.set(0); var_e.set(0)
    stu.clearCourses()
    result.set("모든 선택을 해제했습니다.")


frm_btn = tk.Frame(root)
frm_btn.pack(pady=5)
tk.Button(frm_btn, text="등록하기", width=12, command=register).pack(side="left", padx=15)
tk.Button(frm_btn, text="초기화", width=12, command=reset).pack(side="left", padx=15)

root.mainloop()