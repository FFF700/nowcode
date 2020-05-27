while True:
    try:
        cnt = int(input())
        words = []
        for i in range(cnt):
            words.append(input())
        words.sort()
        for i in words:
            print(i)
    except:
        break
