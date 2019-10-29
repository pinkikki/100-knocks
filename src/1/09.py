import random


def main():
    str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .'"
    cs = str.split()
    results = list()
    for c in cs:
        if len(c) > 4:
            s = c[:1]
            m = c[1:-1]
            e = c[-1:]
            ms = ''.join(random.sample(m, len(m)))
            results.append(s + ms + e)
        else:
            results.append(c)
    print(results)


if __name__ == '__main__':
    main()
