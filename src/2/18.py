import pandas


def main():
    df = pandas.read_csv('hightemp.txt', delimiter='\t', header=None)
    print(df.sort_values(2, ascending=False))


if __name__ == '__main__':
    main()
