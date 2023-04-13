from termcolor import colored
board = list(range(1,10))
winners = ( (0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8 ), (2,4,6))
moves = ((1,7,3,9),(5,),(2,4,6,8))
#تابع چاپ تخته بازی
def print_board():
    j = 1
    for i in board:
        end = "   "
        if j % 3 == 0:
            end = "\n\n"
        if i == "x":
            print(colored(f"[{i}]","blue"),end = end)
        elif i == "o":
            print(colored(f"[{i}]","yello"),end = end)
        else:
            print(f"[{i}]", end = end)
        j += 1


# تابع برسی برد و فرد حرکت کننده و حرکت انجام شده
def make_move(brd,plyr,mve,undo=False):
    if can_move(brd,mve):
        brd[mve-1] = plyr
        win = is_winner(brd,plyr)
        if undo:
            brd[mve-1] = mve
        return True, win
    return False,False

#تابع برسی انتخاب درست حرکت کاربر
def can_move(brd,mve):
    if mve in range(1,10) and isinstance(brd[mve-1],int): # آیا انتخاب بین 1 تا 9 هست و اینکه آیا خانه انتخاب شده عدد هست یا نه
        return True
    return False
# تابع برسی برنده بودن یا نبودن کاربر
def is_winner(brd,plyr):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if brd[j]!=plyr: #در اینجا چک میکنه اگر x ک برای کاربر هست توی خونه های برنده نبود وین غلط بشود
                win = False
                break
        if win:
            break
    return win


#تابع برای چک کردن وجود خانه خالی در بورد
def has_ampty_space():
    return board.count("x") + board.count("o") != 9

# تابع حرکت کامپیوتر
def computer_move():
    mv = -1
    #آیا کامپیوتر میتواند برنده شود؟
    for i in range(1,10):
        if make_move(board,computer,i,True)[1]: #  و 1 برای اینکه حرکتی ک انجام دادم میتونم برنده بشم یا نه داخل میک موی (True در اینجا به برای صحیح کردن آندو میباشد)
            mv = i
            break
    # اگر کاربر میتواند برنده شود جلوی آن را بگیر
    if mv == -1:
        for j in range(1,10):
            if make_move(board,player, j, True)[1]:
                mv = j
            break
    # حرکت کن
    if mv == -1:
        for tup in moves: #اولویت حرکت برای کامپیونر
            for m in tup:
                if mv==-1 and can_move(board,m): #در اینجا منفی یک برای اینه ک اگر یک بار حرکت رو انتخاب کرد دوباره حرکت جدید جای قبلی نگیرد
                    mv= m
                    break
    return make_move(board,computer,mv)

#تعریف نماد های بازیکنان و چاپ  آن
player, computer = "x", "o"
print("player: x\ncomputer: o")

while has_ampty_space(): # تا زمانی ک جای خالی در برد وجود دارد ادامه بده
    print_board()
    move = int(input("Choose the move(1-9) : "))
    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid Number! Try again! ")
        continue
    if won:
        print(colored("you win!", "red"))
        break
    elif computer_move()[1]:
        print(colored("you lose!", "yellow"))
        break

print_board()



