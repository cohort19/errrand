"""This handles all database connection"""
import datetime
from personal import db



class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(),primary_key=True,auto_increment=True)
    post_title = db.Column(db.String(255),nullable=False)
    post_content = db.Column(db.Text(),nullable=False)
    post_created_on = db.Column(db.DateTime(),default=datetime.datetime.utcnow)



    def __repr__(self):
        return "<{}:{}>".format(self.id,self.post_title[:10])
