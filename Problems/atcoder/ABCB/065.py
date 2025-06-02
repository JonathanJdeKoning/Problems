N = int(input())
buttons = [int(input())-1 for _ in range(N)]

pressed = set()
toPress = 0
steps = 0
while True:
    if toPress in pressed: exit(print(-1))
    if toPress == 1: exit(print(steps))
    steps += 1
    pressed.add(toPress)
    toPress = buttons[toPress]