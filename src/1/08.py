def main():
    s = input()
    ciphered = cipher(s)
    print(ciphered)
    print(cipher(ciphered))


def cipher(s):
    ciphered = ''
    for c in s:
        if c.isalpha() and c.islower():
            ciphered += chr(219 - ord(c))
        else:
            ciphered += c
    return ciphered


if __name__ == '__main__':
    main()
