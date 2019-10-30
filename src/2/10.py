def main():
    # CPythonの場合はcloseされるようだけど、他の実装だと怪しいので、基本的にはwithでちゃんとcloseしたほうがよい
    # https://stackoverflow.com/questions/18840880/will-using-list-comprehension-to-read-a-file-automagically-call-close
    print(sum([1 for _ in open('hightemp.txt')]))


if __name__ == '__main__':
    main()
