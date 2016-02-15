import MySQLdb


def mysql_connection(sqla_db):
    return MySQLdb.connect(
        user=sqla_db.url.username,
        passwd=sqla_db.url.password
    )

