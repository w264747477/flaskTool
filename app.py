# from mahua import mahua
from tools._init_ import create_app,db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
loginmanager = LoginManager()
loginmanager.session_protection = 'strong'
loginmanager.login_view = 'base.login'
#创建flask的应用对象
app=create_app("develop")
# app=create_app("product")
manager = Manager(app)
Migrate(app,db)
manager.add_command("db",MigrateCommand)
@app.route('/index')
def index():
   return 'index'
if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    # manager.run(host="0.0.0.0", port=5000,debug=True)
    manager.run()
    # app.run(host="127.0.0.1", port=5000, debug=True)
