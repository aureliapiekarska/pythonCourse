import json

password = [{'zwierzeta':'malpa'},\
            {'zwierzeta':'kon'},\
            {'jedzenie':'hamburger'},\
            {'jedzenie' : 'pizza'}]
with open ('password_json_detail.json', "w") as studs:
    json.dump(password,studs)

print("JSON Created.....")