from app import db
from flask_login import UserMixin
class IndexImg(db.Model, UserMixin):
    __tablename__ = 'sliderImg'
    imgUrl = db.Column(db.String(36))
    relation=db.Column(db.String(100), unique=True, index=True)

