import mariadb
import mybot

def dbadd_user(uid, uname):
    try:
        conn = mybot.conn
        cur = conn.cursor()
        values = (uid, uname)
        mariadb_insert_query = 'INSERT INTO users (tele_id, name) VALUES (%s, %s)'
        cur.execute(mariadb_insert_query, values)
        conn.commit()
        print('Пользователь добавлен')
        cur.close()
    except mariadb.Error as error:
        print('Ошибка при подключении:', error)
    finally:
        if (conn):
            conn.close()
            print('Соединение закрыто')


def dbadd_exercise_title(dbtitle, uid, uname):
    try:
        conn = mybot.conn
        cur = conn.cursor()
        value = (uid, uname, dbtitle)
        mariadb_insert_query = 'INSERT INTO users (tele_id, name, exercise_title) VALUES (?, ?, ?)'
        cur.execute(mariadb_insert_query, value)
        conn.commit()
        print('Название добавлено')
        cur.close()
    except mariadb.Error as error:
        print('Ошибка при подключении:', error)
    finally:
        if (conn):
            conn.close()
            print('Соединение закрыто')


def dbadd_exercise_name(dbtitle, uid, uname, dbexercise_name):
    try:
        conn = mybot.conn
        cur = conn.cursor()
        value = []
        for name in dbexercise_name:
            tuple_data = (uid, uname, dbtitle, name)
            value.append(tuple_data)
        mariadb_insert_query = 'INSERT INTO users (tele_id, name, exercise_title, exercise_name) VALUES (?, ?, ?, ?)'
        cur.executemany(mariadb_insert_query, value)
        conn.commit()
        print('Название добавлено')
        cur.close()
    except mariadb.Error as error:
        print('Ошибка при подключении:', error)
    finally:
        if (conn):
            conn.close()
            print('Соединение закрыто')


def dbget_exercise_name(dbtitle, uid):
    try:
        conn = mybot.conn
        cur = conn.cursor()
        value = (dbtitle, uid)
        text = []
        mariadb_insert_query = 'SELECT exercise_name FROM users WHERE exercise_title = ? and tele_id = ?'
        cur.execute(mariadb_insert_query, value)
        exercise_name = cur.fetchall()
        cur.close()
        return exercise_name
    except mariadb.Error as error:
        print('Ошибка при подключении:', error)
    finally:
        if (conn):
            conn.close()
            print('Соединение закрыто')
