# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_connected_hexagons(rows, col):
    if col % 2 == 0:
        col = col // 2
        print(" ___""    " * col)
        print("/   \\___" * col )
        for i in range(rows):

            print("\\___/   " * col + "\\")
            if i == rows - 1:
                print("    \\___/" + "   \\___/"* (col-1) )
            else:
               print("/   \\___" * col + "/")


    else:
        col = col // 2 + 1
        print(" ___""    " * col)
        for _ in range(rows):

         print("/   \\___" * (col -1) + "/   \\")

         print("\\___/   " * col)



inputs = input("inputs: ").split()
rows, col = map(int, inputs)
print_connected_hexagons(rows, col)