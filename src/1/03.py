import re


def main():
    s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    ss = re.split('[ ,]', s)
    lens = []
    for c in ss:
        lens.append(len(c))
    print(lens)


if __name__ == '__main__':
    main()
