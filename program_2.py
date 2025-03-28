#By:Sabria Fafach
#Date: March 28, 2025
#Title:program_2.py


import random
NUMBER_QUANTITY=int(input("Enter the number of random numbers you want to write to the file (up to 1000):"))

def main():
    r_number_file=open("random_numbers.txt","a")
    for number in range(0,NUMBER_QUANTITY):
        random_number=random.randint(1,500)
        r_number_file.write(f"{random_number}\n")

    r_number_file.close()

if __name__ == '__main__':
    main()








