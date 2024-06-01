# پروژه سری اول
# اعضای گروه : مهدی ساطعی 40121753 , سروش رضوانی 40134193

from tokenize import split, tokenize, dic
import json


def main():
    file = open("Code.txt", 'r', encoding="utf8")
    for line in file:
        line_list = split(line)
        f = tokenize(line_list)
        if len(f):
            print(f)
    print()
    json_str = json.dumps(dic, ensure_ascii=False, indent=4).encode('utf-8').decode()
    print("table : " + json_str)


main()
