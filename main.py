import json
from secrets import token_urlsafe
from pprint import pprint

new_password = {}


def json_load():
    with open('Save_password.json', 'r', encoding="UTF-8") as fjson:
        return json.load(fjson)


while True:
    print('')

    match input():
        case 'saved password':
            name__password = str(input('name password: '))
            json_data = json_load()["save password"]
            source_code = 1
            for i in range(0, len(json_data)):
                index_password = 0
                while index_password != len(json_data[i]):
                    try:
                        print(json_data[i][str(index_password)][name__password])
                        source_code = 0
                        break
                    except KeyError:
                        index_password += 1
            if source_code == 1:
                print(f"password {name__password} does not exist")
                print("you may have entered the wrong username if you forgot the password"
                      "name, you can find the name using the command all password")
        case 'all password':
            data = json_load()["save password"]
            # a list of unnecessary type to output to the console
            replace_list = ['{', '}', "'", '[', ']', '0:', '1:', '2:', '3:', '4:', '5:', ' ']

            for i in range(len(data)):
                clean_data = str(data[i])
                for symbol_i in range(len(replace_list)):
                    clean_data = clean_data.replace(replace_list[symbol_i], '')
                if clean_data != '':
                    pprint(clean_data)
        case 'new password':
            while True:
                ok = ':)'
                data = json_load()["save password"]
                name_password = str(input("name password: "))

                for i in range(len(data)):
                    for key in range(len(list(data[i].key()))):
                        if name_password == list(data[i][str(key)].key())[0]:
                            ok = ':('
                            print("a password with that name already exists")
                if ok == ':)':
                    password = token_urlsafe(20)
                    print(f"new password: {password}")
                    new_password[len(new_password)] = {name_password: password}
                    break
        case 'exit':
            data = json_load()
            with open('Save_password.json', 'w', encoding="UTF-8") as f:
                try:
                    json.dump({"{}": new_password, "save password": [data["{}"], data["save password"]]}, f, indent=4)
                except (Error := KeyError):
                    json.dump({"{}": new_password}, f, indent=4)

            try:
                if Error == KeyError:  # NameError
                    data = json_load()
                    with open('Save_password.json', 'w', encoding="UTF-8") as f2:
                        json.dump({"{}": new_password, "save password": data["{}"]}, f2, indent=4)
            except NameError:
                pass
            pure_json = str(json_load()["save password"]).replace('[', '').replace(']', '')

            with open('Save_password.json', 'w', encoding="UTF-8") as f:
                json.dump({"{}": new_password, "save password": eval(pure_json)}, f, indent=4)
            break  # exiting the program
        case _:
            print("no such command exists, you may have made a spelling mistake when writing the command")
