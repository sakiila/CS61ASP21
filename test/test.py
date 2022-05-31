def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make


if __name__ == '__main__':
    bake(1, "mashed potatoes")
