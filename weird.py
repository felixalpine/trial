n = int(input())

while True:
    if 1 <= n <= 100 and n % 2 == 0:
        if 2 <= n <= 5 or n > 20:
            print("not weird")
            if 6 <= n <=20:
                print("weird")
        else:
            print("Weird")
    else:
        print("Weird")
    break
