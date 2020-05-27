while True:
    try:
        sen = list(reversed(input().split()))
        sen_r = ""
        for x in sen:
            sen_r = sen_r + x + " "
        print(sen_r)
    except:
        break
