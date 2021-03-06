#!/usr/bin/env python3
import math

'''
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
'''


def solve(input_data):
    result = None
    # Viết code vào đây set result làm kết quả của tính toán
    #
    #
    #

    result = (math.factorial(2*input_data)) / (math.factorial(input_data))**2

    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
