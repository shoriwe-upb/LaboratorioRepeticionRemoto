def main():
    a = abs(float(input("Number a: ")))
    # Zero is  not a prime number
    if a == 0:
        print("Is not  prime")
        return
    # Jump the non required numbers
    half = a // 2
    for number in range(2, int(half)+1):
        if a % number == 0:
            print("Is not prime")
            return
    print("Is prime")


if __name__ == '__main__':
    main()
