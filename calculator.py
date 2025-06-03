import argparse


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b


def main():
    parser = argparse.ArgumentParser(description='Simple calculator')
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help='Operation to perform')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')
    args = parser.parse_args()

    ops = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
    }

    try:
        result = ops[args.operation](args.a, args.b)
    except Exception as e:
        parser.error(str(e))
    else:
        print(result)


if __name__ == '__main__':
    main()
