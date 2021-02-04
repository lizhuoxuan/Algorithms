# 2，5，7面值的硬币，使用最少的硬币数组成￥27
# f(x)=min(f(x-2)+1, f(x-5)+1, f(x-7)+1)
# 从1到27
import sys

max_int = sys.maxsize


def dp(m, coin_list):
    m_list = [0]
    for i in range(m + 1):
        if i > 0:
            m_list.append(max_int)
        for coin in coin_list:
            # 如果钱数大于等于
            if i - coin >= 0 and m_list[i - coin] != max_int:
                m_list[i] = min(m_list[i], m_list[i - coin] + 1)
    if m_list[m] == max_int:
        m_list[m] = -1
    return m_list[m]


if __name__ == '__main__':
    coin_list = [2, 5, 7]
    print(dp(27, coin_list))
