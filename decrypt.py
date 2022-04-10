from sys import argv
from src.common import new_file_path
from src.lib import decrypt


def main():
    if len(argv) == 2 and argv[1]:
        code = open(argv[1], "r").read()
        result = decrypt(code)
        with open(new_file_path('d', argv[1]), "w") as f:
            f.write(result)
    else:
        print("Arguments:\n"
              "\tpath\tthe path to the file\n"
              "Output:\n"
              "\tCreat a file with the basename of the given path with e or d at the start separate by a '_'")


if __name__ == '__main__':
    main()
