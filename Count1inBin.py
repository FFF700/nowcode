while True:
    try:
        dec = int(input())
        print(bin(dec).count('1'))
        cnt = 0
        while dec != 1:
            '''
            if dec % 2 == 1:
                cnt += 1
            '''
            cnt += dec % 2
            dec = dec // 2
        cnt += 1
        print(cnt)
    except:
        break
