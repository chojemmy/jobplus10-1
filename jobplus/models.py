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
            onupdate=datetime.utcnow)

user_job = db.Table(
        'user_job',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')),
        db.Column('job_id', db.Integer, db.ForeignKey('job.id', ondelete='CASCADE'))
        )

class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    real_name = db.Column(db.String(32))
    phone = db.Column(db.String(32))
    work_years =db.Column(db.SmallInteger)
    resume = db.Column(db.String(64))
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    collect_jobs = db.relationship('Job', secondary=user_job)
    detail = db.relationship('CompanyDetail',uselist=False)
    is_disable = db.Column(db.Boolean, default=False)

    # 用户对应的简历
    def __repr__(self):
        return '<User:{}>'.format(self.name)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY

    @property
    def is_staff(self):
        return self.role == self.ROLE_USER

class CompanyDetail(Base):
    __tablename__ = 'company_detail'

    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(64), nullable=False)
    site = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(24), nullable=False)
    # ?????
    description = db.Column(db.String(100))
    # ???????????
    about = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    user = db.relationship('User', uselist=False, backref=db.backref('company_detail', uselist=False))

    def __repr__(self):
        return '<CompanyDetail {}>'.format(self.id)

class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    #职位名称
    name = db.Column(db.String(23))
    #职位薪资范围
    salary_low = db.Column(db.Integer, nullable=False)
    salary_high = db.Column(db.Integer, nullable=False)
    #职位地点
    location = db.Column(db.String(24))
    #职位标签
    tags = db.Column(db.String(128))

    company_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))

    company = db.relationship('User', uselist=False, backref=db.backref('jobs', lazy='dynamic'))

    def __repr__(self):
        return '<Job {}>'.format(self.name)

    @property
    def tag_list(self):
        return self.tags.split(',')

class Resume(Base):
    __tablename__ = 'resume'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', uselist=False)
