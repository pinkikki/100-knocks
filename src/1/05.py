import re


def main():
    s = 'I am an NLPer'
    print(ngram(s, 2))
    ss = re.split('[ ,]', s)
    print(ngram(ss, 2))


def ngram(t, n):
    return [t[idx:idx + n] for idx in range(len(t) - n + 1)]


if __name__ == '__main__':
    main()
