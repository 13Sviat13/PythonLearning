print("Enter year")
n = int(input())
if n % 4 == 0:
    if n % 100 == 0 and n % 400 != 0:
        print("nunber is високосний")
    else:
        print("не високосний")
else:
    print("не високосний")