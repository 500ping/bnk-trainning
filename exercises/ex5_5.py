#!/usr/bin/env python3


data = ['Trang', 'Trung', 'Tien',
        'Dai', 'Duong', 'Dung', 'Hung', 'Huy', 'Hoang']

MAGIC_NUMBER = 20200000


def solve(students, N=5):
    '''Biết những bạn có tên bắt đầu bằng chữ `D` sẽ ngồi phòng thi số N,
    các bạn có tên bắt đầu chữ `H` ngồi phòng thi số N+1, và các bạn còn lại,
    nếu có tên kết thúc là `ng` sẽ ngồi cùng phòng các bạn tên `H`, còn lại
    ngồi cùng phòng `D`.
    Tất cả các học viên đều sinh năm 1990.
    Mã học viên được tính bằng: hash(NAME) % MAGIC_NUMBER
    (chú ý số này mỗi lần chạy sẽ khác nhau).
    Ví dụ: mã học viên của 'Dung' là: hash('Dung') % MAGIC_NUMBER

    Trả về result là list các tuple chứa
    (mã sinh viên, tên học viên, năm sinh, phòng thi), sắp xếp
    theo thứ tự tên học viên.
    '''

    result = []
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")

    for name in data:
        if name[0] == 'D':
            result.append((hash(name) % MAGIC_NUMBER, name, 1990, N))
        elif name[0] == 'H':
            result.append((hash(name) % MAGIC_NUMBER, name, 1990, N+1))
        elif name[-2:] == 'ng':
            result.append((hash(name) % MAGIC_NUMBER, name, 1990, N+1))
        else:
            result.append((hash(name) % MAGIC_NUMBER, name, 1990, N))

    result = sorted(result, key=lambda stu: stu[1])
    print(result)

    return result


def main():
    students = data
    # Cho danh sách học viên students
    for msv, *ignore, room in solve(students):
        print(msv, room)
        print("DEBUG", ignore, type(ignore), len(ignore))


if __name__ == "__main__":
    main()
