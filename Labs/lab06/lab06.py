import sys


def print_args():
    for i in range(len(sys.argv)):
        print(sys.argv[i])


def check():
    if sys.argv[1] == "-p":
        return True
    elif sys.argv[1] == "-i":
        return True
    elif sys.argv[1] == "-h":
        return True
    elif sys.argv[1] == "-r":
        return True
    elif sys.argv[1] == "-w":
        return True
    else:
        return False


def flags(lst):
    if lst[1] == "-p":
        printable = lst[2:]
        for item in printable:
            print(item)
    elif lst[1] == "-i":
        print("Hello World")
    elif lst[1] == "-h":
        # print(
        #     "Valid Flags:"
        #     "-p : prints out all the command line arguments after the -p"
        #     '-i : prints "Hello World"'
        #     "-h : prints out a help command"
        # )
        print('Valid flags:\n'
              '-p : prints out all the command line arguments after the -p\n'
              '-i : prints "Hello World"\n'
              '-h : prints out a help command')
    elif lst[1] == "-w":
        if len(lst) > 3:
            filename = lst[2]
            writeout = lst[3:]
            output_file = open(filename, "w")
            for item in writeout:
                output_file.write(item + "\n")
            output_file.close()
        else:
            print("No Content Provided")
    elif lst[1] == "-r":
        filename = lst[2]
        input_file = open(filename, "r")
        lines_read = input_file.readlines()
        for i in lines_read:
            print(i, end="")
        print("")
        input_file.close()


if check() is True:
    flags(sys.argv)
else:
    print_args()




