from time import sleep
import emoji
for i in range(10, -1, -1):
    print(f'\033[035m{i:^20}')
    sleep(1)
for i in range(0, 9):
    print(f'{emoji.emojize(":fireworks:") * 10}')
    sleep(0.25)
