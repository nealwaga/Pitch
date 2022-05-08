from app import create_app
from app import create_app,db
from flask_script import Manager,Server
from app.models import User


app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitches = Pitches)


if __name__ == '__main__':
    manager.run()