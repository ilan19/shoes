from database import connect

class User:
  def __init__(self, first_name, last_name, username, password, admin):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.password = password
    self.admin = admin


  def __repr__(self):
    return "<User {}>".format(self.username)


  def user_exists(self, username):
    with connect() as connection:
      with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user_data = cursor.fetchone()
        if user_data != None:
          return True
    return False


  def save_to_db(self):
    if self.user_exists(self.username):
      return False

    with connect() as connection:
      with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users(first_name, last_name, password, username, admin) VALUES(%s, %s, %s, %s, %s)", (self.first_name, self.last_name, self.password, self.username, self.admin))
    return True


  def update(self):
    with connect() as connection:
      with connection.cursor() as cursor:
        cursor.execute("UPDATE users SET first_name=%s, last_name=%s WHERE username=%s", (self.first_name, self.last_name, self.username))


  @classmethod
  def find(cls, username, password):
    with connect() as connection:
      with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user_data = cursor.fetchone()
        if user_data == None:
          return None
        else:
          return cls(first_name=user_data[1], last_name=user_data[2], username=user_data[4], password=user_data[3], admin=user_data[5])


  @classmethod
  def find_by_username(cls, username):
    with connect() as connection:
      with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user_data = cursor.fetchone()
        if user_data == None:
          return None
        else:
          return cls(first_name=user_data[1], last_name=user_data[2], username=user_data[4], password=user_data[3], admin=user_data[5])


  @classmethod
  def list(cls):
    users = []
    with connect() as connection:
      with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users_data = cursor.fetchall()
        for user_data in users_data:
          user = cls(first_name=user_data[1], last_name=user_data[2], username=user_data[4], password=user_data[3], admin=user_data[5])
          users.append(user)

    return users
















