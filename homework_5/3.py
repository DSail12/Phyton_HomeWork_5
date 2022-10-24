# Создайте программу для игры в "Крестики-нолики".

def step (list, who,list_ignore):
    if who == 0: lable = 'X'
    elif who == 1: lable = '0'
    position_x = int(input ("Введите позицию на которую поставим "+lable+': '))-1
    while position_x in list_ignore:
        position_x = int(input('Введена некорректная позиция. Введите позицию снова: ')) - 1
    list_ignore.append (position_x)     
    list[position_x] = lable
    
def print_list (list):
    for i in range (0,9,3):
        print (list [i], list[i+1],list [i+2])

def win (list,list_ignore):
    win = 0
    for i in range (0,9,3):
        if list [i] == list [i+1] == list [i+2]:
            win = 1
    for i in range (3):
        if list [i] == list [i+3] == list [i+6]:
            win = 1
    if list [0] == list [4] == list [8] or list [2]== list [4] == list [6]:
        win = 1
    if win == 1: print ('Победа!')
    if len (list_ignore) == 9 and win != 1:
        print ("Ничья!")
        win = 1
    return win

        

list =[(i+1) for i in range (0,9)]
list_ignore = []
who = 1
print_list (list)
while win (list,list_ignore) == 0: 
    if who == 1: who =0
    else: who = 1
    step (list,who,list_ignore)
    print_list (list)