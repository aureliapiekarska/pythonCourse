import os

def openfile(filename):

    with open(filename) as fopen:
        quotes = fopen.readlines()

    print(quotes)


def size(filename):
    if os.path.getsize(filename) == 0:
        print('Empty file')
    else:
        print('File with the filling')


def update_file(filename):
    with open(filename) as r:
        user=input('Do you want to update the file (y/n)?')
        if user=='y':
            user_update=input('What update ill be performed?')
            r.write(user_update)
            print('Update finalized')
        else:
            print('No update to be performed')



def file_present(filename):
    if os.path.exists(filename ) is True:
        print('File exisiting')




filename = input('Please provide the name of the file')
openfile(filename)
update_file(filename)
size(filename)
file_present(filename)
