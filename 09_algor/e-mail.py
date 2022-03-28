def search(my_email,email_list):
    for email in email_list:
        if email == my_email:
            return True
    return False

def main():
    users_email =['aaaa@a.pl','bbb@b.pl','ccccc@c.pl']
    wanted_email='bbb@b.pl'
    result= search(wanted_email,users_email)
    print('email on list',result)

if __name__ == '__main__':
    main()


