a = int(input())
b = int(input())
c = int(input())

all_sec = a + b + c

minutes = all_sec // 60
seconds = all_sec % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')

