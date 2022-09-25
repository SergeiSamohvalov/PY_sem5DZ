# Создайте программу для игры в ""Крестики-нолики"".

# import tkinter as tk
# from tkinter import messagebox as mb
# import random as rnd

# # создаём окно
# window = tk.Tk() 
# window.title("GB / 5-2 / Крестики-нолики")

# pole = [None] * 9
# btn_num_clicked = list(range(9))
# step = 0

# def is_win(player):
#     if (pole[0] == pole[1] == pole[2] == player) or (pole[3] == pole[4] == pole[5] == player) or (pole[6] == pole[7] == pole[8] == player) \
#         or (pole[0] == pole[3] == pole[6] == player)  or (pole[1] == pole[4] == pole[7] == player) or (pole[2] == pole[5] == pole[8] == player) \
#         or (pole[0] == pole[4] == pole[8] == player) or (pole[2] == pole[4] == pole[6] == player):
#         for i in btn:
#             i.config(bg="lightgray", state="disabled")
#         mb.showinfo("Игра окончена", "Победитель " + player + " ))")


# def btn_disabled(num, t):
#     if len(btn_num_clicked) > 0:
#         pole[num] = t
#         btn[num].config(text=t, state="disabled")
#         btn_num_clicked.remove(num)

# def btn_click(btn_num):
#     global step   
#     window.title(btn_num)
#     btn_disabled(btn_num, "X")
#     is_win("X")
#     if btn_num == 4 and step == 0:
#         btn_num_pl2 = rnd.choice(btn_num_clicked)
#     elif btn_num != 4 and step == 0:        
#         btn_num_pl2 = 4
#     if step > 0:
#         btn_num_pl2 = 8 - btn_num
#         if btn_num_pl2 not in btn_num_clicked:
#             btn_num_pl2 = rnd.choice(btn_num_clicked)
#     btn_disabled(btn_num_pl2, "O")
#     is_win("O")
#     step += 1
        
# btn = [tk.Button(font=28, height=3, width=6, command = lambda num=i: btn_click(num)) for i in range(9)]

# row = 1
# col = 0
# for i in range(len(btn)):
#     btn[i].grid(row=row, column=col)
#     col += 1
#     if col == 3:
#         row += 1
#         col = 0

# window.mainloop()

from tkinter import *
import random
root = Tk()
root.title('Criss-cross')
game_run = True
field = []
cross_count = 0
BLACK = (0, 0, 0)
def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')
def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=3, 
                        font=('Verdana', 20, 'bold'),
                        background = 'lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='Новая Игра', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()