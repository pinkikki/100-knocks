import pandas


def main():
    n = input()
    df = pandas.read_csv('hightemp.txt', delimiter='\t', header=None)
    print(df[:int(n)])


if __name__ == '__main__':
    main()
