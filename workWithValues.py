# файл: первая строка - название,
# глубина рекурсии,
# начальные координаты
# угол   шаг
# по какому символу рисуем
# аксиома
# далее - правила изменения аксиомы

axiom = list(input())
depth = int(input())
keys = ['F']
values = ['FF-[-F+F+F]+[+F-F-F]']
mas = dict(zip(keys, values))  # словарь с правилами изменения аксиомы, ключ - что меняем, значение - на что меняем

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

print(axiom)

# stack = []
# stack.append()
# stack.pop()
