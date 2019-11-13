import pandas


def main():
    df1 = pandas.read_csv('col1.txt', delimiter='\t', header=None)
    df2 = pandas.read_csv('col2.txt', delimiter='\t', header=None)
    df1[1] = df2
    df1.to_csv('col1_2.txt', sep='\t', header=False, index=False)
    print(df1)


if __name__ == '__main__':
    main()
