import re


def main():
    edited = ''
    with open('hightemp.txt') as fr:
        edited += re.sub('\t', ' ', fr.read())
    print(edited)


if __name__ == '__main__':
    main()
