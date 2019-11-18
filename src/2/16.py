import pandas


def main():
    n = input()
    fr = pandas.read_csv('hightemp.txt', delimiter='\t', header=None, chunksize=int(n))
    for r in fr:
        print(r)


if __name__ == '__main__':
    main()
