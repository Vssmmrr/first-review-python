import turtle, time

# форматирование contrl + alt + L

joe = turtle.Turtle()
joe.speed(10)

def starFILL(n, length):
    joe.begin_fill()
    star(n, length)
    joe.end_fill()


def star(n, length):

    if n % 2 != 0:
        for i in range(n):
            joe.forward(length)
            angle = n // 2 * 360 / n
            joe.left(angle)


n = int(input())
length = int(input())
starFILL(n, length)
time.sleep(3)
# joe.reset() отчищает экран до начального состояния
