# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
import pandas as pd
from sqlite3 import connect
from pathlib import Path
from .sql_execution import QueryMixin

# Define the path to the database file
cwd = Path(__file__).parent
db_path = cwd / 'employee_events.db'

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase(QueryMixin):
    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE
    name = ""
    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def names(self):    
        # Return an empty list
        # YOUR CODE HERE
        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE
    def event_counts(self, id):
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
        query = f"""
                SELECT event_date,
                SUM(positive_events) AS total_positive,
                SUM(negative_events) AS total_negative
                FROM {self.name}
                WHERE employee_id={id}
                GROUP BY event_date
                ORDER BY event_date;
                """
        return self.pandas_query(query)
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(self, id):
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE
        query = f"""
                SELECT n.note_date, n.note
                FROM notes n
                JOIN {self.name} e ON n.employee_id=e.employee_id
                WHERE e.employee_id={id};
                """
        return self.pandas_query(query)
