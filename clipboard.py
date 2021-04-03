import keyboard
import xerox
import psycopg2

con = psycopg2.connect(database="clipboard", user="aravind", password="", host="localhost", port="5432")

cur = con.cursor()


def insert_db():
    cur.execute("SELECT * FROM public.clipboard_data where content = %s", (xerox.paste(),))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO public.clipboard_data(content) VALUES (%s)", (xerox.paste(),))
        con.commit()
        print('added')


def listen():
    keyboard.add_hotkey('cmd+c', insert_db)
    keyboard.wait()


while True:
    listen()
