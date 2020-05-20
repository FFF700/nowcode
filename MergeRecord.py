while True:
    try:
        cnt = int(input())

        rcd = {}
        for i in range(cnt):
            k, v = map(int, input().split())
            rcd[k] = rcd.setdefault(k, 0) + v

        for x in sorted(rcd.keys()):
            print(x, str(rcd[x]))


    except:
        break
