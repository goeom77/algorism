import tkinter as tk
import random

List=["박준표"
,"양은진"
,"엄형규"
,"정재훈"
,"차은혁"
,"황호선"]


root=tk.Tk()
cvs=tk.Canvas(width=800,height=600)
cvs.pack()
def click(e):
    random.shuffle(List)
    cvs.delete("PP")
    for i in range(6):
        cvs.create_text(50+80*(i%6),50+50*(i//6),text=List[i],font=("굴림체",15),fill="black",tag="PP")

root.bind("<Button>",click)
root.mainloop()