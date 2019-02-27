from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
            default=datetime.utcnow,
            onundate=datetime.utcnow)
user_job = db.Table(
        'user_job',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')),
        db.Column('job_id', db.Integer, db.ForeignKey('job.id', ondelete='CASCADE' ))
        )

# 用户表
class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER ＝10
    ROLE_STAFF = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unqiue=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    # 用户对应的简历
    resume = db.Column(db.String(1084))
    # 用户投递的职位,可能是多个，其之间是一对多的关系
    collect_job = db.relationship('Job', secondary=user_job)
    upload_resume_url = db.Column(db.String(64))
    
    def __repr__(self):
        return '<User:{}>'.format(self.name)

    '''设置密码的方式，判断企业用户，管理员登录的密码等'''

# 职位表
class Job(Base):
    __tablename__ = 'job'

    pass

# 企业表
class Company(Base):
    __tablename__ = 'company'
    pass
    
# 简历投递记录
class Dilivery(Base):
    __tablename__ = 'delivery'
    pass

