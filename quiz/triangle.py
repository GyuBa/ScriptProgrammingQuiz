import copy
import time

def big(a, b):
    if a > b:
        return a
    else:
        return b

def calculate(tri, level):
    for i in range(level):
        tri[level-1][i] += big(tri[level][i], tri[level][i+1])
    return tri;

def main(tri, height):
    for i in range(0, height):
        print(tri)
        tri = calculate(tri, height - i - 1)
    return tri

if __name__ == '__main__':
    H = int(input())
    int_triangle = []
    for i in range(H):
        input_ = input()
        line = list(map(int, input_.split(' ')))
        assert len(line) == i + 1
        int_triangle.append(line)
    s = time.time()
    int_triangle = main(int_triangle, H)
    e = time.time()

    print("수행 시간 : {0:3.6f}초".format(e - s))
    print("결과 : {}".format(int_triangle[0][0]))
