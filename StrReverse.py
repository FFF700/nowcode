while True:
    try:
        s = list(reversed(input()))
        ss = ""
        for x in range(len(s)):
            ss += s[x]
        print(ss)
    except:
        break
