def main():
    s1 = 'paraparaparadise'
    s2 = 'paragraph'
    x = ngram(s1, 2)
    y = ngram(s2, 2)
    print(x | y)
    print(x & y)
    print(x - y)
    print('se' in x)
    print('se' in y)


def ngram(t, n):
    return {t[idx:idx + n] for idx in range(len(t) - n + 1)}


if __name__ == '__main__':
    main()
