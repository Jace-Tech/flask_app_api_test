from . import get_connection

def create_user_table():
  db = get_connection()

  if not db: return

  connection, cursor = db
  sql = """CREATE TABLE IF NOT EXISTS user (
      user_id INT PRIMARY KEY AUTO_INCREMENT,
      email VARCHAR(100) UNIQUE NOT NULL,
      password VARCHAR(255) NOT NULL
  )"""

  cursor.execute(sql)
  connection.commit()
  print("TABLE CREATED!")
  connection.close()


def get_user_by_id(user_id):
  connection, cursor = get_connection()

  sql = "SELECT * FROM user WHERE user_id = %s"
  cursor.execute(sql, [user_id])
  
  user = cursor.fetchone()
  connection.close()
  return user