from app import db,loginmanager
from flask_login import UserMixin

@loginmanager.user_loader
def load_user(user_id):
    return User.query.filter(User.ID == user_id).first()
class User(db.Model, UserMixin):
    __tablename__ = 'syuser'
    id = db.Column(db.String(36), primary_key=True)
    userName=db.Column(db.String(100), unique=True, index=True)
    passWord=db.Column(db.String(255))
