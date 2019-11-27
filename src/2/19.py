import pandas


def main():
    df = pandas.read_csv('hightemp.txt', delimiter='\t', header=None)
    col = df[0]
    print(col.value_counts().sort_values(0, ascending=False))


if __name__ == '__main__':
    main()
