from dbops import Database
from imagegen import ImageGenerator
import uuid

d=Database
i=input("What do you want to do?\nAdd a barcode\nGet a barcode\nExit\n")
d.create_table()

def main(i):
    if i == "add":
        u = str(input("Do you want to make your own ID?\nYes\nNo\n"))
        if u == "yes":
            b = input("What is your barcode?\n")
        if u == "no":
            b = str(uuid.uuid4()).replace('-','')[:-20]
        
        p = input("What is your product name?\n")
        l = input("What is your product description?\n")
        d.add_barcode(barcode_id=b, product_name=p, product_description=l)
        print("Barcode added!")
        ImageGenerator.create_image(b)
        print("Image created!")
        return

    if i == "get":
        d.get_barcode(input("What is your barcode?\n"))
        return

    if i == "exit":
        print("Exiting...")
        exit()

    else:
        print("Invalid input")
        main(input("What do you want to do?\n1. Add a barcode\n2. Get a barcode\n3. Exit\n"))

main(i)
