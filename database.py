import psycopg2


def connect():
  return psycopg2.connect(user='postgres', password='Octobre1910', database='learming', host='localhost')
