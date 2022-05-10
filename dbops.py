import json
import sqlite3
import uuid
import random

with open('config.json') as config_file:
    config = json.load(config_file)

db_name = config['db']['name']

class Database:
    
    def create_table():
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS barcodes (barcode_id TEXT PRIMARY KEY, product_name TEXT, product_description TEXT)")
        conn.commit()

    def add_barcode(barcode_id, product_name, product_description, a=None):
        try:
            conn = sqlite3.connect(db_name)
            c = conn.cursor()
            sql = "INSERT INTO barcodes (barcode_id, product_name, product_description) VALUES (?, ?, ?)"
            data = [
                (str(barcode_id), str(product_name), str(product_description))
            ]
            with conn:
                c.executemany(sql, data)
                conn.commit()
        except sqlite3.IntegrityError:
            conn = sqlite3.connect(db_name)
            c = conn.cursor()
            sql = "INSERT INTO barcodes (barcode_id, product_name, product_description) VALUES (?, ?, ?)"
            data = [
                (str(barcode_id) + str(random.randint(0,999999)), str(product_name), str(product_description))
            ]
            with conn:
                c.executemany(sql, data)
                conn.commit()


    def get_barcode(barcode_id: str, a=None):
        conn = sqlite3.connect(db_name)
        with conn:
            data = conn.execute(f"SELECT * FROM barcodes WHERE barcode_id = '{barcode_id}'")
            for row in data:
                print("""
Barcode ID: {row[0]}
Product Name: {row[1]}
Product Description: {row[2]}
""")
    
