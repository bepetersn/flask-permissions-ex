#!/usr/bin/env python
import code
import click
from click_defaults import main
from ex import app, db as sqla_db
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
            'app': app
        })

@main.group()
def db():
    pass


@db.command()
def create():
    cursor = mysql_connection(sqla_db).cursor()
    cursor.execute(
        'CREATE DATABASE IF NOT EXISTS %s;' \
        % sqla_db.url.database
    )

@db.command()
def init():
    sqla_db.create_all()


@db.command()
def drop():
    cursor = mysql_connection(sqla_db).cursor()
    cursor.execute(
        'CREATE DATABASE IF NOT EXISTS %s;' \
        % sqla_db.url.database
    )


if __name__ == '__main__':
    main()
