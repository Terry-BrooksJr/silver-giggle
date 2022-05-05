
# from psycopg2 import cursor, connection
#  from config import Config 
from decouple import config
from models import PlatformUser
from app import db
from sqlalchemy import Column, Integer, DateTime, String


class PlatformUsers(db.Model):
    username = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, primary_key=True, unique=True)
    user_first_name = db.Column(db.String)
    user_last_name = db.Column(db.String)
    password = db.Column(db.String)
    care_facility = db.Column(db.String, length)
    # assert isinstance(care_facility, str)
    date_account_created = date_account_created
    # assert isinstance(date_account_created, datetime)
    last_date_modified = last_date_modified
    # assert isinstance(last_date_modified, datetime)
    role = role
    # assert isinstance(role. str)
    last_logged_in = last_logged_in
# try:
#     dev_postgres_db = psycopg2.connect( 
#                                         host = config('AWS_db_HOST'),
#                                         database="postgres",
#                                         user=config('AWS_db_USER'),
#                                         password=config('AWS_db_PASSWORD')
#                                         )
#     # Open a cursor to perform database operat\ions
#     cursor = connection.cursor()
#     # Print PostgreSQL details
#     print("PostgreSQL server information")
#     print(connection.get_dsn_parameters(), "\n")
#     # Executing a SQL query
#     cursor.execute("SELECT version();")
#     # Fetch result
#     record = cursor.fetchone()
#     print("You are connected to - ", record, "\n")
# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
# # Insert data into the table

# def seed_db(first_name,last_name,daycare_facility, role):
#     password = PlatformUser
    
#     cursor.execute('INSERT INTO "PlatformUsers"(user_id, username, user_first_name, user_last_name, password_hash, daycare_facility, created_at, last_modified_at, is_archived, role, last_login')
#     cursor.execute("INSERT INTO books (user_id, username,first_)"
#             "VALUES (
#                 {},{},{},{},{},{},{},{},{},{},{}.format('(nextval(user_id)','bcasterton0@state.gov','Barth','Casterton','vIE1lb9v','37B4','','','false','user','2/16/2022')", 
#                 {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}.format('(nextval(user_id)', , 'srenault1@chronoengine.com', 'Sampson', 'Renault', 'vo67AE', '30S6', '', '2021-05-23 10:41:30', 'true', 'user', '9/14/2021')),


# connection.commit()

# cursor.close()
# connection.close()
