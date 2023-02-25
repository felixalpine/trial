n = int(input())

while True:
    if 1 <= n <= 100 and n % 2 == 0:
        if 2 <= n <= 5:
            print("even")
        else:
            print("Weird")
    else:
        print("Weird")
    break
