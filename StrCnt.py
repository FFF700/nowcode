while True:
    try:
        s = list(set(list(input())))
        length = 0
        for x in s:
            if 127 >= ord(x) >= 0:
                length += 1
        print(length)

    except:
        break
