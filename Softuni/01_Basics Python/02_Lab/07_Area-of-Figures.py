from math import pi

type_figure = input()
area = 0

# match type_figure:
#     case 'square':
#        a = float(input())
#        print(round(a * a, 3))
#     case 'rectangle':
#         a = float(input())
#         b = float(input())
#         print(round(a * b, 3))
#     case 'circle':
#         a = float(input())
#         print(round(a ** 2 * pi, 3))
#         pass
#     case 'triangle':
#         a = float(input())
#         b = float(input())
#         print(round(a * b / 2, 3))

if type_figure == 'square':
    a = float(input())
    print(round(a * a, 3))
elif type_figure == 'rectangle':
    a = float(input())
    b = float(input())
    print(round(a * b, 3))
elif type_figure == 'circle':
    a = float(input())
    print(round(a ** 2 * pi, 3))
elif type_figure == 'triangle':
    a = float(input())
    b = float(input())
    print(round(a * b / 2, 3))
