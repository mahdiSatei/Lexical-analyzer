import re

dic = {
    "keyword": {"int": 1,
                "read": 2,
                "write": 3,
                "loop": 4,
                "if": 5,
                "so": 6,
                "until": 7},
    "operators": {"=": 8,
                  "==": 9,
                  "+": 10,
                  "-": 11,
                  "*": 12,
                  "/": 13,
                  "--": 14,
                  "++": 15,
                  "%": 16,
                  "<": 17,
                  ">": 18,
                  ">=": 19,
                  "<=": 20},
    "signs": {"(": 21,
              ")": 22,
              "[": 23,
              "]": 24,
              "{": 25,
              "}": 26,
              ";": 27,
              "<<": 28,
              ">>": 29,
              '"': 30,
              "endl": 31},
    "identifier": {},
    "number": {},
    "string": {}
}

value = 32


def tokenize(list_key):
    global value
    final = []
    for key in list_key:
        flag = True
        if key == "//":
            return final
        for keys in dic:
            if key in dic[keys].keys():
                flag = False
                final.append((dic[keys][key], keys))
        if flag:
            if check_identifier(key):
                dic["identifier"].update({key: value})
                value += 1
                final.append((value - 1, "identifier"))
            elif check_string(key):
                dic["string"].update({key: value})
                value += 1
                final.append((value - 1, "String"))
            elif check_number(key):
                dic["number"].update({key: value})
                value += 1
                final.append((value - 1, "number"))
            else:
                raise TypeError
    return final


def check_identifier(string):
    if string[0].isalpha():
        return True
    return False


def check_string(string):
    if string[0] == string[len(string) - 1] == '"':
        return True
    return False


def check_number(number):
    if number.isnumeric():
        return True
    return False


def split(line):
    my_list = re.split(r'(\+\+)|("[^"]*")|([ ;\n()])', line)
    my_list = [item for item in my_list if item != '']
    my_list = [item for item in my_list if item != ' ']
    my_list = list(filter(None, my_list))
    if "\n" == my_list[len(my_list) - 1]:
        my_list.pop(len(my_list) - 1)
    return my_list
