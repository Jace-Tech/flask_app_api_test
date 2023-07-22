from mysql.connector import connect
from dotenv import dotenv_values

ENV = dotenv_values()

def get_connection():
  try:
    connection = connect(
      host=ENV["MYSQL_HOST"],
      user=ENV["MYSQL_USER"],
      password=ENV["MYSQL_PASSWORD"],
      database=ENV["MYSQL_DB"],
      port=ENV["MYSQL_PORT"],
    )

    cursor = connection.cursor(buffered=True, dictionary=True)

    return connection, cursor
  except Exception as e:
    print("DATABASE ERROR:", str(e))
    return None
    