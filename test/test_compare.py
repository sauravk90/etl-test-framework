# External packages
import sqlite3
import pandas as pd
import os
from sqlalchemy import create_engine

# Internal packages
from framework.test_base import TestBase
from framework.utils import replace_null

class TestCompare(TestBase):

    def test_fetch_from_dbl(self):
        """ Test to compare to datasets """
        self.assertTrue(2>1)

        # Create your connection.
        # Sqlite
        conn = sqlite3.connect('saurav.db')
        df = pd.read_sql_query("SELECT * FROM report_notification", conn)
        print(df)

        # MySQL
        sqlEngine = create_engine("mysql://root:root@localhost/test", pool_recycle=3600)
        dbConnection = sqlEngine.connect()

        frame = pd.read_sql("select * from test.users", dbConnection);

        pd.set_option('display.expand_frame_repr', False)

        print(frame)


    def test_fetch_large_data(self):
        sqlEngine = create_engine("mysql://root:root@localhost/demo", pool_recycle=3600)
        db_connection = sqlEngine.connect()

        # Step 1: fetched records from target table into df_target using chunk_size
        chunk_size = 100000
        sql_query = "select * from demo.employees"
        df_list = []

        for chunk in pd.read_sql(sql_query, db_connection, chunksize=chunk_size):
            df_list.append(chunk)

        df_target = pd.concat(df_list, ignore_index=True)
        print(len(df_target))

        # Step 2: read source data from csv
        test_file_path = os.getcwd() + "/../test_data/employees.csv"
        df_source = pd.read_csv(test_file_path)
        print(len(df_source))

        # Step 3: Pre-processing
        df_target = replace_null(df_target)
        df_source = replace_null(df_source)

        # Assertion
        self.assertEqual(len(df_source), len(df_target), "Record length mismatch b/w source and target...")

        headers_in_source = len(df_source.columns.values)
        headers_in_target = len(df_target.columns.values)
        self.assertTrue(headers_in_source == headers_in_target)

        # Step 4: Comparison
        # TODO : assignment
