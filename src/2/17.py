import pandas


def main():
    df = pandas.read_csv('hightemp.txt', delimiter='\t', header=None)
    col = df[0]
    print(col[~col.duplicated()])


if __name__ == '__main__':
    main()
