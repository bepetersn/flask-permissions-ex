
# flask-permissions-ex

Example usage of [the flask-permissions project](https://github.com/raddevon/flask-permissions). Please see that project for most details.

To run this project, use the `./manage.py` executable file. I bundled a bunch of useful utilities in it, some common flask project commands like `run`, and `shell`, as well several under `db`:  `create`, `init`, `drop`, and its own `shell` command to start mysql with your configuration.

To test that the configuration & flask-permissions are working, do the following...

1. Make sure you have a database URI configured at the `SQLALCHEMY_DATABASE_URI` environment variable.
2. Make sure you have created that database (You could use `./manage.py db create [dbname]`).
3. Create this project's tables with `./manage.py db init`.
4. You can then run `./manage.py shell`, and try creating some users or roles, to actually test out the project.
