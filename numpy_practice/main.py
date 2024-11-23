import numpy as np
from operationclass import IntArray


def productivity_of_company(order, data_frame):
    return np.sum(data_frame[order])


def max_productivity(data_frame):
    i = 0
    best_company = i + 1
    num_products = 0

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        if result > num_products:
            num_products = result
            best_company = i + 1

    print(
        f"The best company is the {best_company}. Company with {num_products} number of products."
    )


def min_productivity(data_frame):
    i = 0
    worst_comapny = i + 1
    num_products = productivity_of_company(0, data_frame)

    for i in range(len(data_frame)):
        result = productivity_of_company(i, data_frame)
        if result <= num_products:
            num_products = result
            worst_comapny = i + 1

    print(
        f"The worst company is the {worst_comapny}. Company with {num_products} number of products."
    )


def file_handling():
    lines = []
    with open("company.txt", "r") as file:
        for line in file:
            values = line.strip().split(",")
            int_values = [int(val) for val in values]
            lines.append(int_values)

        data_frame = np.array([np.array(row) for row in lines], dtype="object")
        return data_frame


def main():
    data_frame = file_handling()
    print(data_frame)

    first_branch = IntArray(data_frame[0])
    first_branch.display()
    first_branch.salary()
    first_branch.show_data()
    min_productivity(data_frame)
    max_productivity(data_frame)


main()
