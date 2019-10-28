def main():
    print(generate(12, '気温', 22.4))


def generate(x, y, z):
    return f'{x}時の{y}は{z}'


if __name__ == '__main__':
    main()
