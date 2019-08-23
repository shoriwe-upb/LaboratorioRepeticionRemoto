def main():
    even_numbers = 0
    odd_numbers = 0
    while True:
        number = float(input(f"Number {even_numbers + odd_numbers + 1}: "))
        if number == 0:
            break
        if number % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    print(f"Numeros pares {even_numbers}")
    print(f"Numeros impares {odd_numbers}")


if __name__ == '__main__':
    main()