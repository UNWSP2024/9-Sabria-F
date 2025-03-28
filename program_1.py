#By:Sabria Fafach
#Date: March 28, 2025
#Title:program_1.py


def count_file_lines():

    #Open names.txt file
    read_lines=open("names.txt","r")

    #Create accumulation variable
    total_lines=0

    #Read first line of the file
    line=read_lines.readline()

    #Loop that runs for each line in the file
    while line !="":
        #Adds one to the accumulator variable
        total_lines+=1
        #Reads next line of file
        line=read_lines.readline()
    #Close file
    read_lines.close()

    print('In the count_file_lines function')
    #Display the number of lines
    print(f"There are {total_lines} names in the names.txt file.")


# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()