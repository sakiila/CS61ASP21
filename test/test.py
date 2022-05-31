def hmmm(x):
    def f(y):
        return y
    return f

if __name__ == '__main__':
    print(hmmm(5)(6))

    x = 4
    x = 8
    print(x)