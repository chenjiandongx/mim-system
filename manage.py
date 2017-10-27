from app import app, db
from app.models import Agency, Medicine, Client
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """ 启动 shell 时导入所需模块
    """
    return dict(app=app, db=db,
                Agency=Agency, Medicine=Medicine, Client=Client)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
