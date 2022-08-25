CopyrightSpider
===============

Prerequisites
-------------

- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- [PostgresSQL](https://www.postgresql.org/)

Also make sure, that you create a database and a table in Postgres. Save the correct values for the ".env" file in the folder "config". Please note, that there is a template for the ".env" file.

These instructions are executed on windows.

How to download the application
-------------------------------

1. Clone the Repo from GitHub

    ```bash
    git clone
    ```

2. Create venv.

    ```bash
    python3 -m venv venv
    ```

3. Activate virtual environment.

    ```bash
    venv\Scripts\activate.bat
    ```

4. Install requirements.

    ```bash
    pip install -r requirements.txt
    ```

How to run the spider
---------------------

1. Make sure that the database and the matching table exist.

2. Navigate into folder negCopyrightSider.

    ```bash
    cd negCopyrightSpider
    ```

3. Run Spider in terminal

    ```bash
    scrapy runspider articles.py
    ```

Amazing, now you used the Web Crawler!

How to load the prepared Data into your Database
------------------------------------------------

To be explained.
