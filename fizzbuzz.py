def affiche():
    output = []
    for i in range(1, 101):
        if i % 15 == 0:
            output.append("FrisBee")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    print(''.join(output))
