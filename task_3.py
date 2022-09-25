# Создайте программу для игры в ""Крестики-нолики"".

import tkinter as tk
from tkinter import messagebox as mb
import random as rnd

# создаём окно
window = tk.Tk() 
window.title("GB / 5-2 / Крестики-нолики")

pole = [None] * 9
btn_num_clicked = list(range(9))
step = 0

def is_win(player):
    if (pole[0] == pole[1] == pole[2] == player) or (pole[3] == pole[4] == pole[5] == player) or (pole[6] == pole[7] == pole[8] == player) \
        or (pole[0] == pole[3] == pole[6] == player)  or (pole[1] == pole[4] == pole[7] == player) or (pole[2] == pole[5] == pole[8] == player) \
        or (pole[0] == pole[4] == pole[8] == player) or (pole[2] == pole[4] == pole[6] == player):
        for i in btn:
            i.config(bg="lightgray", state="disabled")
        mb.showinfo("Игра окончена", "Победитель " + player + " ))")


def btn_disabled(num, t):
    if len(btn_num_clicked) > 0:
        pole[num] = t
        btn[num].config(text=t, state="disabled")
        btn_num_clicked.remove(num)

def btn_click(btn_num):
    global step   
    window.title(btn_num)
    btn_disabled(btn_num, "X")
    is_win("X")
    if btn_num == 4 and step == 0:
        btn_num_pl2 = rnd.choice(btn_num_clicked)
    elif btn_num != 4 and step == 0:        
        btn_num_pl2 = 4
    if step > 0:
        btn_num_pl2 = 8 - btn_num
        if btn_num_pl2 not in btn_num_clicked:
            btn_num_pl2 = rnd.choice(btn_num_clicked)
    btn_disabled(btn_num_pl2, "O")
    is_win("O")
    step += 1
        
btn = [tk.Button(font=28, height=3, width=6, command = lambda num=i: btn_click(num)) for i in range(9)]

row = 1
col = 0
for i in range(len(btn)):
    btn[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

window.mainloop()
