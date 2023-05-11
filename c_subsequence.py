# C. Подпоследовательность


def input_data():
    return input(), input()


def subsequence(s, t):
    position = -1
    for i in s:
        position = t.find(i, position + 1)
        if position == - 1:
            return False
    return True


def test():
    assert subsequence('abc', 'ahbgdcu') is True
    assert subsequence('abcp', 'ahpc') is False
    assert subsequence(
        'ijha',
        'hmrqvftefyixinahlzgbkidroxiptbbkjmtwpsujevkulgrjiwiwzyhngulrodiwyg'
    ) is False


def main():
    print(subsequence(*input_data()))


if __name__ == '__main__':
    main()
    # test()