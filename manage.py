from app import db,create_app
from app.models import User

app = create_app('development')

@manager.shell
def make_shell_context():
  return dict(app = app,db = db,User = User)
if __name__ == "__main__":
    manager.run()