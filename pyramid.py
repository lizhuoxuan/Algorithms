# coding:utf8


def pyramid():
    num = 4
    for i in range(1, num):
        for m in range(num - i):
            print(" ", end='\t')
        for j in range(i * 2 - 1):
            print("*", end='\t')
        print("\n")


if __name__ == '__main__':
    pyramid()
