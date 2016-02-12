#!/usr/bin/env python
import code

import click
from ex import app, db


@click.group()
def main():
    pass


@main.command()
def init_db():
    db.create_all()


@main.command()
@click.option('--debug', '-d', is_flag=True)
@click.option('--host', '-h')
@click.option('--port', '-p')
def run(debug, host, port):
    app.run(host=host, port=port, debug=debug)


@main.command()
def shell():
    with app.test_request_context():
        code.interact('', local={
            'app': app, 'db': db
        })


if __name__ == '__main__':
    main()
