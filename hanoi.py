# coding:utf8


def hanoi(n):
    if n >= 1:
        if n == 1:
            return 1
        else:
            return hanoi(n - 1) * 2 + 1
    else:
        return 'please input a number >= 1'


def hanoi_steps(n, x, y, z):
    if n >= 0:
        if n == 0:
            pass
        else:
            hanoi_steps(n - 1, x, z, y)
            print('%s -> %s' % (x, y))
            hanoi_steps(n - 1, z, y, z)
    else:
        return 'please input a number >= 0'


if __name__ == '__main__':
    num = 3
    print(hanoi(num))
    hanoi_steps(num, 'a', 'b', 'c')
