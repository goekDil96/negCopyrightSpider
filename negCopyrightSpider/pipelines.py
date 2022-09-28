#
# SPDX-FileCopyrightText: Copyright 2022 Dilara Göksu
#

import os
from itemadapter import ItemAdapter
import psycopg2

from dotenv import load_dotenv

cdir = os.path.join(os.pardir, "config", ".env")
load_dotenv(cdir)  # take environment variables from config/.env.

hostname = str(os.getenv("HOSTNAME"))
username = str(os.getenv("USER"))
password = str(os.getenv("PASSWORD"))
database = str(os.getenv("DATABASE"))
tablename = str(os.getenv("TABLENAME"))

class NegcopyrightspiderPipeline:

        #Define function to configure the connection to the database & connect to it
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password,  
            dbname=database)
        self.connection.set_client_encoding('UTF8')
        self.cur = self.connection.cursor()
        

    #Define function to disconnect from database
    def close_spider(self, spider):
        self.cur.execute(f"SELECT * FROM {tablename};")
        self.connection.commit()
        list_tables = self.cur.fetchall()
        print(list_tables[:10])
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
	    #Execute SQL command on database to insert data in table
            self.cur.execute(f"insert into {tablename}(copyright_string,source,datetime) values(%s,%s,%s)", (item['copyright_string'], item['source'], item['datetime']))
            self.connection.commit()
        except:
            self.connection.rollback()
            raise
        return item
