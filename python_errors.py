def python_error():
    try:
        from my_math_caculation import sqrt
    except ModuleNotFoundError:
        print("THis module is not found, use builtins instead")
        from math import sqrt
    return


def main():
    python_error()  # generate exception error


if __name__ == "__main__":
    main()
