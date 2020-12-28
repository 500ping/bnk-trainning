#!/usr/bin/env python3


def solve(text):
    '''Kiểm tra text có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 1 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")

    result = text.lower() == text[::-1].lower()

    return result


def main():
    cases = [('ana', True),
             ('Civic', True),
             ('Python', False),
             ('', False),
             ('P', False),
             (' P  ', False),
             (' P ', False),
             ('Able was I ere I saw Elba', True)]

    for case in cases:
        print(solve(case[0]))
    # print(solve('Able was I ere I saw Elba'))


if __name__ == "__main__":
    main()
