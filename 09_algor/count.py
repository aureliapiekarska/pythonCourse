def sum_naturals_for(n):
    sum_numbers=0

    for num in range(n+1):
        sum_numbers += num
    return sum_numbers

def main():
    result= sum_naturals_for(10)
    print('-----')
    print(result)

if __name__ == '__main__':
    main()