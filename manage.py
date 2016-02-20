#!/usr/bin/env python
import code
import subprocess
import click
from click_defaults import main
from ex import app, db as sqla_db
from ex.database import connection_url, User
from ex.db_utils import mysql_connection


@click.group()
def main():
    pass


@main.command()
@click.option('--debug', '-d', is_flag=True)
@click.option('--host', '-h')
@click.option('--port', '-p')
def run(debug, host, port):
    app.run(host=host, port=port, debug=debug)


@main.command()
def shell():
    with app.test_request_context():
        code.interact(local={
            'app': app, 'db': sqla_db, 'User': User
        })

@main.group()
def db():
    pass


@db.command()
def create():
    cursor = mysql_connection().cursor()
    cursor.execute(
        'CREATE DATABASE IF NOT EXISTS %s;' \
        % connection_url.database
    )

@db.command()
def init():
    sqla_db.create_all()


@db.command()
def drop():
    cursor = mysql_connection().cursor()
    cursor.execute(
        'DROP DATABASE IF EXISTS %s;' \
        % connection_url.database
    )


@db.command()
def shell():
    mysql_running_string = 'mysql -u %s -p%s' % \
            (connection_url.username,
             connection_url.password)
    subprocess.call(mysql_running_string.split())


if __name__ == '__main__':
    main()
