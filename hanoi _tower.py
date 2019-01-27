# coding:utf8


def hanoi_tower(num):
    if num >= 1:
        if num == 1:
            return 1
        else:
            return hanoi_tower(num - 1) * 2 + 1
    else:
        return 'please input a number >= 1'


if __name__ == '__main__':
    print(hanoi_tower(0))
