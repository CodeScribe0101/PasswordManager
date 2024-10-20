import json
from secrets import token_urlsafe
from pprint import pprint

new_password = {}


def json_load():
    with open('Save_password.json', 'r', encoding="UTF-8") as fill_json:
        return json.load(fill_json)


while True:
    print('')
    command = input()

    match command:
        case 'saved password':
            name__password = str(input('name password: '))
            json_data = json_load()["save password"]
            index = 0
            for i in range(0, len(json_data)):
                try:
                    print(json_data[i][str(index)][name__password])
                    break
                except KeyError:
                    # while
                    def password(index_password=1):
                        try:
                            try:
                                json_data[i][str(index_password)]
                            except KeyError:
                                if i == len(json_data) - 1:
                                    print(f"password {name__password} does not exist")
                                    print('you may have entered the wrong username if you forgot the password'
                                          'name, you can find the name using the command all password')
                                return ''  # exit from recursion
                            print(json_data[i][str(index_password)][name__password])
                        except KeyError:
                            password(index_password + 1)


                    password()
        case 'all password':
            data = json_load()["save password"]
            for i in range(len(data)):
                pprint(str(data[i]).replace('{', '').replace('}', '')
                       .replace("'", '').replace("[", '').replace("]", '')
                       .replace("0:", '').replace("1:", '').replace("2:", '')
                       .replace("3:", '').replace("4:", '').replace("5:", ''))
        case 'new password':
            while True:
                ok = ':)'
                data = json_load()["save password"]
                name_password = str(input("name password: "))

                for i in range(len(data)):
                    keys_data = list(data[i].keys())
                    for keys in range(len(keys_data)):
                        if name_password == list(data[i][str(keys)].keys())[0]:
                            ok = ':('
                if ok == ':)':
                    password = token_urlsafe(20)
                    print(f"new password: {password}")
                    new_password[len(new_password)] = {name_password: password}
                    break
                else:
                    print("a password with that name already exists")
        case 'exit':
            data = json_load()
            with open('Save_password.json', 'w', encoding="UTF-8") as f:
                try:
                    json.dump({"{}": new_password, "save password": [data["{}"], data["save password"]]}, f, indent=4)
                except (Error := KeyError):
                    json.dump({"{}": new_password}, f, indent=4)

            try:
                if Error == KeyError:
                    data = json_load()
                    with open('Save_password.json', 'w', encoding="UTF-8") as f2:
                        json.dump({"{}": new_password, "save password": data["{}"]}, f2, indent=4)
            except NameError:
                pass
            pure_json = str(json_load()["save password"]).replace('[', '').replace(']', '')

            with open('Save_password.json', 'w', encoding="UTF-8") as f:
                json.dump({"{}": new_password, "save password": eval(pure_json)}, f, indent=4)
            break  # exit while
        case _:
            print("no such command exists, you may have made a spelling mistake when writing the command")
