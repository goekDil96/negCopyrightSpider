CopyrightSpider
===============

Project to collect and save Documents that contain the word "copyright" in a postgres database.

Prerequisites
-------------

- [Anaconda](https://www.anaconda.com/products/distribution)
- [PostgresSQL](https://www.postgresql.org/)

Save the correct values for the ".env" file in the folder "config". Please note, that there is a template for the ".env" file.

These instructions are executed on windows.

How to download the application
-------------------------------

1. Clone the Repo from GitHub

    ```bash
    git clone 
    ```

How to create the database in postgres
--------------------------------------

1. Open Application "SQL Shell (psql)" on your machine.

2. Run command

    ```bash
    CREATE TABLE <.env TABLENAME> (
        copyright_string VARCHAR PRIMARY KEY,
        source VARCHAR,
        datetime VARCHAR,
        is_no_copyright_statement INT
    );
    ```

How to start the conda container
--------------------------------

1. Create Container.

    ```bash
    conda env create -f environment.yml
    ```

2. Activate virtual environment.

    ```bash
    conda activate venv_scraper
    ```

3. If requirements changed: Update Container.

    ```bash
    conda env update -f environment.yml
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
