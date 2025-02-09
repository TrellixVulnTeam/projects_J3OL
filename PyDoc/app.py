from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from application.apps.pydoc import create_app,db

app = create_app('developemen')

manager = Manager(app)

Migrate(app,db)

manager.add_command('db', MigrateCommand)


@app.route('/')
def inde():
    return 'hello world'
if __name__ == '__main__':
    manager.run()
