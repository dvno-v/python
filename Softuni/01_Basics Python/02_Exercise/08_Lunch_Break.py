from math import ceil
serial = input()
episode_time = int(input())
break_time = int(input())
time_to_eat = break_time / 8
time_to_rest = break_time / 4
remaining_break_time = break_time - time_to_eat - time_to_rest
if remaining_break_time < episode_time:
    print(f'You don\'t have enough time to watch {serial}, you need {ceil(episode_time - remaining_break_time)} more minutes.')
else:
    print(f'You have enough time to watch {serial} and left with {ceil(remaining_break_time - episode_time)} minutes free time.')