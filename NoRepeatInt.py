while True:
    try:
        num = input()
        num_reverse = list(reversed(num))
        num_encoded = ""
        for i in num_reverse:
            if num_encoded.find(i) == -1:
                num_encoded = num_encoded + i

        print(num_encoded)
    except:
        break
