from pypac import complicated
import sys


def main():
    print(sys.path)
    x = [1, 2, 3]
    y = [-1, -1, 1]

    print(x, y, complicated.dot_product(x, y))


if __name__ == '__main__':
    main()
