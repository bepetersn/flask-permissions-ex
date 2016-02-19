import MySQLdb
from .database import connection_url


def mysql_connection():
    return MySQLdb.connect(
        user=connection_url.username,
        passwd=connection_url.engine.url.password
    )

