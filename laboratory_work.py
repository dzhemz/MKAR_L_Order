import functools
import os

alternatives = {}
criteria_order = []
criteria_options = {}


def main():
    read_file()
    alternative = best_alternative()
    display_alternative(alternative)


def read_file():
    with open("input.txt", "r", encoding="utf8") as input_file:
        [process_line(line.rstrip("\n")) for line in input_file.readlines()]


def process_line(line):
    global alternatives
    global criteria_options
    global criteria_order
    arguments = line.split()
    if len(arguments) == 0:
        return

    if "alternative" == arguments[0]:
        alternative_name = arguments[1].replace("_", " ")
        criteria_order.append(alternative_name)
        alternatives[arguments[1]] = list(map(int, arguments[2:]))
        return

    if "criteria" == arguments[0]:
        criteria_name = arguments[1].replace("_", " ")
        criteria_order.append(criteria_name)
        criteria_options[criteria_name] = arguments[2]
        return


def best_alternative():
    return max(alternatives.keys(), key=functools.cmp_to_key(compare_alternatives))


def compare_alternatives(alternative_a, alternative_b):
    values_a = alternatives[alternative_a]
    values_b = alternatives[alternative_b]
    for criteria_index in range(len(values_a)):
        comparison = compare_by_criteria(values_a[criteria_index], values_b[criteria_index], criteria_index)
        if comparison != 0:
            return comparison
    return 0


def compare_by_criteria(value_a, value_b, criteria_index):
    if criteria_options[criteria_order[criteria_index]] == "minMax":
        return value_a - value_b
    else:
        return value_b - value_a


def display_alternative(alternative):
    arguments = ", ".join(map(str, alternatives[alternative]))
    print(f"Самая оптимальная альтернатива {alternative} c значениями по критериям {arguments}")


if __name__ == "__main__":
    main()
