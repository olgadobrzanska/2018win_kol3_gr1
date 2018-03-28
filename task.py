#NOTE!!! python3.6 or newer is required.
# new string format was used. (f"string: {variable}")
# generator was used in line 24 in file Matrix.py

from Matrix import Matrix

if __name__ == '__main__':
    matr1 = Matrix([1, 1, 1], [1, 1, 1], [2, 2, 2])
    print("matrix 1")
    print (matr1)

    matr2 = Matrix([1, 1, 1], [1, 1, 1], [2, 2, 2])
    print("matrix 2")
    print (matr2)

    matr3 = matr1 + matr2
    matr3_1 = matr1 + 1

    print("matr1 + matr2")
    print(matr3)
    print("matr1 + 1")
    print(matr3_1)
    
    matr4 = matr1 * matr2
    matr4_1 = matr1 * 1
    
    print("matr1 * matr2")
    print(matr4)
    print("matr1 * 1")
    print(matr4_1)