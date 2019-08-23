def main():
    a = float(input("Number a: "))
    # Zero is  not a prime number
    if a == 0:
        print("Is not  prime")
        return
    # Jump the non required numbers
    half = a // 2
    current = 2
    while current <= half:
        if a % current == 0:
            print("Is not prime")
            return
        current += 1
    print("Is prime")


if __name__ == '__main__':
    main()
