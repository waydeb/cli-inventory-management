from dbops import Database
from barcode.writer import ImageWriter
from barcode import Code128


class ImageGenerator:
    def create_image(barcode_id, product_name):
        with open(f'{str(barcode_id)}_{product_name.replace(" ", "-")}.jpeg', 'wb') as f:
            Code128(str(barcode_id), writer=ImageWriter()).write(f)
