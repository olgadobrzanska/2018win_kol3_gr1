from copy import deepcopy
def add_decorator(func):
    def add_wrapper(self, rhs):
        if isinstance(rhs, int):
            return Matrix(*[[self.values[i][j] + rhs for j in range(self.dim)] for i in range(self.dim)])
        return func(self, rhs)
    return add_wrapper


def mult_decorator(func):
    def mult_wrapper(self, rhs):
        if isinstance(rhs, int):
            return func(self, Matrix(*[[rhs for j in range(self.dim)] for i in range(self.dim)]))
        return func(self, rhs)
    return mult_wrapper


class Matrix:
    def __init__(self, *args):
        if len(args) != len(args[0]):
            raise Exception(f'''{len(args)} != {len(args[0])}Number of rows and columns should be equal.''')
        elif False in (isinstance(i, list) for i in args):
            #generator expression above
            raise TypeError('''Provide list of lists of same length.''')
        self.dim = len(args)
        self.values = deepcopy(args)


    @add_decorator
    def __add__(self, rhs):
        if self.dim != rhs.dim:
            raise Exception("Matrices can not be added.")


        result = deepcopy(self.values)
        for i in range(self.dim):
            for j in range(self.dim):
                result[i][j] += rhs.values[i][j]
        return Matrix(*result)



    @mult_decorator
    def __mul__(self, rhs):
        if self.dim != rhs.dim:
            raise Exception("Matrices can not be multiplied.")

        result = deepcopy(self.values)

        for k in range(self.dim):
            for i in range(self.dim):
                sum = 0
                for j in range(self.dim):
                    sum += self.values[k][j] * rhs.values[j][i]
                result[k][i] = sum
        return Matrix(*result)

    def __str__(self):
        strr = ""
        for i in self.values:
            for j in i:
                strr += str(j) + " "
            strr += '\n'
        return strr


def useless_function():
    print("useless function that demonstrates effects of using <if __name__ ...>. Normally it should not be executed.")

if __name__ == '__main__':
    useless_function()