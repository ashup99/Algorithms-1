from random import randint


def generate_list(num_elements):
    ls = [randint(-5, 20) for i in range(num_elements)]
    return ls
