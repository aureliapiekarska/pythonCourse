import fibonacciego

def main():
    value = int(input('Podaj wartość dla jakiej chcesz stworzyć ciąg fibbonaciego 1 -20 ->'))
    fibonacciego.generate_fibbonaci_seq(value)

if __name__ == '__main__':
    main()