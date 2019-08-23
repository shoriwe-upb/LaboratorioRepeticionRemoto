def main():
    zeros = 0
    negatives = 0
    positives = 0
    for step in range(10):
        number = float(input(f"Number {step + 1}: "))
        if number > 0:
            positives += 1
        elif number < 0:
            negatives += 1
        else:
            zeros += 1
    print(f"Number of zeros: {zeros}")
    print(f"Number of negatives: {negatives}")
    print(f"Number of negatives: {positives}")


if __name__ == '__main__':
    main()