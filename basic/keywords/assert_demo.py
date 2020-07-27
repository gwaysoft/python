def div_num(num1, num2):
    assert isinstance(num1, int), "r"
    assert isinstance(num2, int) and num2 != 0, "e2"
    return num1 / num2


def main():
    div_num(1,0)


if __name__ == '__main__':
    main()
    pass
