import math
import random
import os
import time

os.system('clear')
print('''
$$$_____$$$$$$$_$$$$$$$_$$$_______$$$_$$$$$$$$$$
$$$____$$$____$$$____$$$_$$$_____$$$__$$$_______
$$$____$$$_____$_____$$$_$$$_____$$$__$$$_______
$$$_____$$$_________$$$___$$$___$$$___$$$$$$$$__
$$$______$$$_______$$$_____$$$_$$$____$$$_______
$$$_______$$$_____$$$______$$$_$$$____$$$_______
$$$$$$$$$___$$$$$$$_________$$$$$_____$$$$$$$$$$
               \033[91mDeveloped by:  \033[93mZIHAD HOSSAIN
''')
time.sleep(1)
print("\033[95mLoading", flush=True, end='')
for i in range(3):
    time.sleep(1)
    print('.', flush=True, end='')
print("\n\n")
spaces = 40
word = input("\033[96m[?] Enter the sentence that you want to design \033[91m(Example: Happy Birthday) \033[93m:")
print(" ")
text = word.split()



def sine():
    for angle in range(0, 360, 10):
        space = int((spaces / 2) * math.sin(math.radians(angle)))
        serial = int((angle/10) % len(text))
        print((int(spaces / 2) + space) * ' ' + text[serial])


def v():
    for i in range(12):
        serial = int(i % len(text))
        print(i * ' ' + text[serial] + i * '  ' + text[serial])
    for j in range(11, -1, -1):
        serial = int(j % len(text))
        print(j * ' ' + text[serial] + j * '  ' + text[serial])


def sincos():
    for angle in range(0, 180, 10):
        space1 = int((spaces / 2) * math.sin(math.radians(angle + 180)))
        space2 = int((spaces / 2) * math.sin(math.radians(angle)))
        serial = int((angle/10) % len(text))
        print((int(spaces / 2) + space1) * ' ' + text[serial] + ((int(spaces / 2)) - 15 - space1 + space2) * ' ' + text[serial])


def randoms():
    choice = random.randint(1, 3)
    if choice == 1:
        sine()
    if choice == 2:
        v()
    if choice == 3:
        sincos()


choices = input('\033[96mWhat type? \n\033[91m[s] Sine shape (Look ike a snake)\n[sc] Sine Cosine shape (Look like a snake and a reverse) \n[v] V shape (Look like "V")\n[r] Random (Randomize previous shapes)\n \033[93m\n[?] ')
print(" ")
num = int(input("\033[96m[?] How much? \033[91m(Enter a number like '10' or anything. Higher number give a long output): \033[93m"))
os.system('clear')
for i in range(num):
    if choices == 'r':
        randoms()
    if choices == 's':
        sine()
    if choices == 'sc':
        sincos()
    if choices == 'v':
        v()
