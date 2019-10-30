import pandas


def main():
    df = pandas.read_csv('hightemp.txt', delimiter='\t', header=None)
    df[0].to_csv('col1.txt', header=False, index=False)
    df[1].to_csv('col2.txt', header=False, index=False)
    print(df)


if __name__ == '__main__':
    main()
