f = 0


def someFunction():
    global f
    f = "def"
    print(f)

someFunction
print(f)