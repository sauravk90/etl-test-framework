# External packages
import sqlite3
import pymysql
import pandas as pd
from sqlalchemy import create_engine

# Internal packages
from framework.test_base import TestBase

class TestCompare(TestBase):

    def test_login_successful(self):
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