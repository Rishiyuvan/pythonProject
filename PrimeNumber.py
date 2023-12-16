num = int(input("Enter any number:"))
if num>1:
    for i in range(2, num):
        if num % i == 0:
            print("Given number is not a prime number")
            break
    else:
        print("Given number is prime number")
else:
    print("Given number is not a prime number")



