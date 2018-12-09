import mysql.connector

conn = None
cur = None


def __init__(database):
    global conn, cur
    '''
    :param database:
    '''
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='linebot',
        password='',
        database=database,
    )

    connected = conn.is_connected()
    if (not connected):
        conn.ping(True)
    cur = conn.cursor(buffered=True)


def insert(sql, datas):
    '''
        -example-
        sql = 'insert into test values (%s, %s)'
        datas = [
            (2, 'foo'),
            (3, 'bar')
        ]
    :param sql:
    :param datas:
    :return:
    '''
    global conn, cur
    cur.execute(sql, datas)
    conn.commit()


def update(sql):
    '''
    -example-
        sql = 'update userdata set answer_count=1,right_rate=1 where id=2'
    :param sql:
    :return:
    '''
    global conn, cur
    cur.execute(sql)
    conn.commit()


def select(sql, data):
    '''
        -example-
        sql = 'select * from test where id = %s'
        datas = [
            (2),
            (3)
        ]
    :param sql:
    :return:
    '''
    global conn, cur
    cur.execute(sql, data)
    return cur.fetchall()
