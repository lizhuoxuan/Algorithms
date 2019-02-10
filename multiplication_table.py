# coding:utf8


def multiplication():
    num = 10
    for i in range(1, num):
        for j in range(1, i+1):
            print("%d * %d = %d" % (j, i, i * j), end='\t')
        print("\n")


if __name__ == '__main__':
    multiplication()
