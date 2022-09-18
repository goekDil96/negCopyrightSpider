import os
import psycopg2

from dotenv import load_dotenv

cdir = os.path.join(os.getcwd(),  "config", ".env")
load_dotenv(cdir)  # take environment variables from config/.env.

hostname = str(os.getenv("HOSTNAME"))
username = str(os.getenv("USER"))
password = str(os.getenv("PASSWORD"))
database = str(os.getenv("DATABASE"))
tablename = str(os.getenv("TABLENAME"))

conn = psycopg2.connect(
            host=hostname, user=username, password=password,  
            dbname=database)
# cur = conn.cursor()

# with open(os.path.join(os.getcwd(), 'data', 'copyright_spider_data.csv'), 'r', encoding="utf8") as f:
  
#     next(f) #  To Skip the header row.
#     cur.copy_from(f, tablename, sep=',')

# conn.commit()