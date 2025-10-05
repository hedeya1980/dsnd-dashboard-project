from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE
from pathlib import Path

# Define the path to the database file
cwd = Path(__file__).parent
db_path = cwd / 'employee_events.db'

# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    #### YOUR CODE HERE
    def pandas_query(self, sql_query: str) -> pd.DataFrame:
        """
        Executes an SQL query and returns the result as a pandas DataFrame.
        """
        with connect(db_path) as conn:
            return pd.read_sql_query(sql_query, conn)

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    def query(self, sql_query: str) -> list:
        """
        Executes an SQL query and returns the result as a list of tuples.
        """
        with connect(db_path) as conn:
            cursor = conn.cursor()
            result = cursor.execute(sql_query).fetchall()
        return result

 
# Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query
