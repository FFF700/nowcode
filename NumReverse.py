while True:
    try:
        num = list(reversed(input()))
        s = ""
        for x in num:
            s = s + x
        print(s)

    except:
        break
