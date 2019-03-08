from flask import Blueprint, render_template, redirect, url_for, request, flash
from jobplus.models import User
from flask_login import login_required, current_user
from jobplus.forms import CompanyProfileForm

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.filter(
            User.role ==User.ROLE_COMPANY
    ).order_by(User.created_at.desc()).paginate(
            page=page,
            per_page=12,
            error_out=False)
    return render_template('company/index.html', pagination=pagination, active='company')

@company.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    if not current_user.is_company:
        flash('您还不是企业用户', 'warning')
        return redirect(url_for('front.index'))
    form = CompanyProfileForm(obj=current_user.company_detail)
    form.username.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('企业信息更新成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('company/profile.html', form=form)
