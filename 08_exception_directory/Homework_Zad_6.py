import io

def check():

    try:

        with open('quo','r') as fopen:
            fopen.readlines()
    except FileNotFoundError:
        print('wrong name of the file')

    try:
        with open('quotes.txt','w') as fopen:
            fopen.readlines()
    except io.UnsupportedOperation:
        print('not possible')

if __name__ == "__main__":
    check()
