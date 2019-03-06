from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from jobplus.models import User, db, Job
from jobplus.forms import LoginForm

front = Blueprint('front', __name__)

@front.route('/')
def index():
    newest_jobs = Job.query.order_by(Job.created_at.desc()).limit(9)
    newest_companies = User.query.filter(
            User.role==User.ROLE_COMPANY
    ).order_by(User.created_at.desc()).limit(8)
    return render_template(
            'index.html',
            active = 'index',
            newest_jobs = newest_jobs,
            newest_companies=newest_companies,
            )

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        next = 'user.profile'
        if user.is_admin:
            next = 'admin.index'
        elif user.is_company:
            next = 'company.profile'
        return redirect(url_for(next))
    return render_template('login.html', form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已登录成功', 'success')
    return redirect(url_for('.index'))
