import re


def main():
    s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    ss = re.split('[ ,]', s)

    d = {}
    slice_1_target = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    for i, c in enumerate(ss):
        idx = i + 1
        if i in slice_1_target:
            d[idx] = c[:1]
        else:
            d[idx] = c[:2]

    print(d)


if __name__ == '__main__':
    main()
