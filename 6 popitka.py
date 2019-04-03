from tkinter import Tk
from tkinter import filedialog as fd
import turtle
import math
import time


def openFile():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    file_name = fd.askopenfilename()
    f = open(file_name)
    l1 = []
    for line in f:
        l1.append(line.strip())
    f.close()
    l1[2] = l1[2].split(' ')
    l1[3] = l1[3].split(' ')
    for i in range(6, len(l1)):
        l1[i] = l1[i].split(' ')
    # print(l1)
    return l1


def getValues(l1):
    keys = []
    values = []
    for i in range(6, len(l1)):
        keys.append(l1[i][0])
        values.append(l1[i][1])
    mas = dict(zip(keys, values))
    # print(mas)
    return mas


def changeAxiom(l1, mas):
    axiom = list(l1[5])
    depth = int(l1[1])
    for i in range(0, depth):
        j = 0
        while j < len(axiom):  # идем по аксиоме, если находим то, что надо заменить, то заменяем
            for k in mas.keys():
                if k == axiom[j]:
                    axiom.pop(j)
                    st = mas.get(k)
                    for t in range(0, len(st)):
                        axiom.insert(j, st[t])
                        j += 1
                    break
            # здесь надо вставить, на что заменяется буква по правлам аксиомы
            else:
                j += 1
        axiom = list(axiom)
    # print(axiom)
    return(axiom)


def draw(l1, axiom):
    joe = turtle.Turtle()
    joe.speed(1000)
    joe.hideturtle()
    stack = []
    betta = int(math.pi / 2)
    x2 = int(l1[2][0])
    y2 = int(l1[2][2])
    shag = int(l1[3][1])
    ygol = float(l1[3][0])
    # joe.bgcolor("black")
    joe.color("green")
    joe.pensize(1)
    joe.penup()
    joe.goto(x2, y2)
    for i in range(len(axiom)):
        c = axiom[i]
        if c == 'F':
            x2 += shag * math.cos(betta)
            y2 += shag * math.sin(betta)
            joe.pendown()
            joe.goto(x2, y2)
            joe.penup()
        elif c == '+':
            betta += ygol
        elif c == '-':
            betta -= ygol
        elif c == '[':
            stack.append([x2, y2, betta])
        elif c == ']':
            string = stack.pop()
            x2 = string[0]
            y2 = string[1]
            betta = string[2]
        # надо вынуть нормально три значения, понять, что за структура
    time.sleep(5)


l1 = openFile()
mas = getValues(l1)
axiom = changeAxiom(l1, mas)
draw(l1, axiom)