# окно для рисования
from tkinter import *

canvas_width = 1000
canvas_height = 500


def button_clicked():
    import turtle
    import math
    import time

    joe = turtle.Turtle()
    joe.speed(100)
    joe.hideturtle()

    # stack = []

    def draw(axiom):
        stack = []
        betta = int(math.pi / 2)
        x2 = int(-50)
        y2 = int(-200)
        shag = int(20)
        ygol = int(15)
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

    def val(axiom, depth):
        keys = ['F']
        values = ['FF-[-F+F+F]+[+F-F-F]']
        mas = dict(
            zip(keys, values))  # словарь с правилами изменения аксиомы, ключ - что меняем, значение - на что меняем

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
        draw(axiom)

    axiom = list(input())
    depth = int(input())
    val(axiom, depth)


master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

w.create_rectangle(10, 10, 990, 490, fill="white")
w.create_rectangle(20, 20, 980, 480, fill="black")
w.create_text(canvas_width / 2,
              canvas_height / 2,
              text="L-systems", fill="white", font="Algerian 54")

button = Button(master, bg="white", text="Start", command=button_clicked)

button.pack()
mainloop()
