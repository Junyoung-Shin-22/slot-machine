from random import randint
import os

def clear():
    if os.name == 'posix':
        os.system('clear')
    
    elif os.name == 'nt':
        os.system('cls')
    
    else:
        raise OSError

def draw_box(num):
    a, b, c = num

    s = '-------------\n' +\
        f'[ {a} | {b} | {c} ]\n' +\
        '-------------'
    print(s)

def count_same(num):
    for i in '123456789':
        count = num.count(i)
        if count > 1: return count
    return 1

def play(start_money):
    money = start_money

    num = '%03d' % randint(0, 999)
    result = count_same(num)

    if result == 1:
        money -= 10
    
    elif result == 2:
        money += 10
    
    elif result == 3:
        money += 100

        if num == '777':
            money += 900
    
    return num, money

def main():
    money = 1000
    num = '000'

    while True:
        clear()
        print(f'money: ${money}\n')
        draw_box(num)
        input('hit enter to play ($10)')
        num, money = play(money)

        if money == 0: break
    
    clear()
    input("you are broke.")

if __name__ == '__main__':
    main()