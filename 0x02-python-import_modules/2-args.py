from sys import argv

if __name__ == "__main__":
    na = len(argv) - 1

    if na == 0:
        print("0 arguments.")
    else:
        args = "s" if na > 1 else ""
        print("{} argument{}:".format(na, args, "s" if na > 1 else "."))

        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
