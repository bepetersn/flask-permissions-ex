#!/usr/bin/env python
import IPython
import subprocess
import click
from ex import app, db as sqla_db
from ex.database import (connection_url,
    # This is useful to have in IPython's context
    User, UserMixin
)
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
        IPython.embed()

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
    click.echo('Database created.')


@db.command()
def init():
    sqla_db.create_all()
    click.echo('Database schema initialized.')


@db.command()
def drop():
    cursor = mysql_connection().cursor()
    cursor.execute(
        'DROP DATABASE IF EXISTS %s;' \
        % connection_url.database
    )
    click.echo('Database successfully dropped.')


@db.command()
def shell():
    mysql_running_string = 'mysql -u %s -p%s' % \
            (connection_url.username,
             connection_url.password)
    subprocess.call(mysql_running_string.split())


if __name__ == '__main__':
    main()
