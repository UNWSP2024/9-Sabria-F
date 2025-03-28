#By:Sabria Fafach
#Date: March 28, 2025
#Title:program_3.py


def sum_numbers_from_file():
    try:
        read_file=open("numbers.txt","r")
        total_numbers=0
        line=read_file.readline()
        while line!="":
            total_numbers+=float(line.strip())
            line=read_file.readline()
        print(f"The total of all the numbers in the numbers.txt file is {total_numbers:.2f}.")

        print('In the sum_numbers_from_file function')

    except IOError:
        print("Sorry the file you are trying to access does not exist, or a problem occurred while reading text from file.")
    except ValueError as err:
        print(err)


# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()