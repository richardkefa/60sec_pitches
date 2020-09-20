from app import db,create_app
from app.models import User,Pitch,Comment,Category
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
  return dict(app = app,db = db,User = User,Pitch = Pitch,Comment = Comment,Category = Category)

if __name__ == "__main__":
    manager.run()