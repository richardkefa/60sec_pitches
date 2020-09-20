from app import db,create_app
from app.models import User,Pitch,Comment,Category

app = create_app('development')

@manager.shell
def make_shell_context():
  return dict(app = app,db = db,User = User,Pitch = Pitch,Comment = Comment,Category = Category)
if __name__ == "__main__":
    manager.run()