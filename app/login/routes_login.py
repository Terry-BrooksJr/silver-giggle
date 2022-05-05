from app import get_redirect_target, is_safe_url, login_manager, redirect_back
from app.dashboard.routes_dashboard import dashboard_bp
from app.models import PlatformUser
from flask import make_response, Blueprint
from flask import current_app as app
from flask import (flash, g, redirect, render_template, request, session,
                   url_for)
from flask_login import UserMixin, current_user, login_required, login_user, logout_user, current_user  
from flask_wtf.csrf import CSRFError
from pendulum import now
from .forms_login import LoginForm

login_bp = Blueprint(
    'login_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

shenika_cunigan = PlatformUser("shenika_cunigan", 1, "Shenika", "Cunigan", "admin",
                        "Testing", "GLEN01", now(tz='America/Chicago'), None, None)


@login_manager.user_loader
def load_user(user_id):
    return PlatformUser.get(user_id)


# Blueprint Configuration
# * Need the these for for flask-login
@login_manager.user_loader
def load_user(user_id):
    return PlatformUser.query.get(int(user_id))

# * Looks for Previous USER Sessions and sets the global USER ID to the found value or NONE  # pylint: disable=import-outside-toplevel




@login_bp.route('/', methods=['GET', 'POST'])
@login_bp.route('/')
@login_bp.route('/home')
def login():
    form = LoginForm()
    return render_template('login.html.jinja', 
                            form=form, 
                            next=request.args.get('next'), 
                            title='<title> Safari Life Child Management System - Login </title>', 
                            template='login')
    # else:
    #     username = form.password.data
    #     password = form.username.data
    #     next = form.next.data
    #     #first see if username exists
    #     # if PlatformUser.query.filter_by(username=username).count() == 1:
    #         #get their encrypted pass and check it
            # platform_user = PlatformUser.query.filter_by(username=username).first()
        # if username == "TestUser":
        #     if password == "Password":
        #         login_user()
        #         return redirect(url_for(dashboard_bp.dashboard))
            # if PlatformUser.verify_passwor(password, platform_user.password) == True:
            #     if form.remember_me.data:
                    # login_user(platform_user, remember=True)
        #         else:
        #             login_user(platform_user)
        #             flash('Welcome back, {}.'.format(username))
        #     else:
        #         flash('Sorry, the password is incorrect.')
        # else:12
        #     flash('Username does not exist.')
        # if next:
            # return redirect(url_for(dashboard_bp.dashboard))
        # else:
        #     flash('Incorrect User and Password Combondation')
        #     return render_template('login.html.jinja', form=form, next=request.args.get('next'),  title='Safari Life Child Management System - Login', template='login',)

@login_bp.route('/authorize_user', methods=['POST'])
def verify_user():
#     """login flow"""
    user = shenika_cunigan
    user_password = shenika_cunigan.password
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    #     platform_user = PlatformUser.object(username=username).first() 
        if  username == user.username:
            if password == user_password:
                flash('You have successfully logged in!',
                  'alert alert-success')
                # login_user(iter(user))
                user.is_authenticated()
                return redirect(url_for('login_bp.dashboard'))          
    #     # platform_user = PlatformUser.query.filter_by(username=form.username.data).first() #TODO:Uncomment out lines 44 & 45 when Database is set 
    #     # if platform_user and PlatformUser.check_password(form.password.data):
        elif password != 'Testing' or username != 'TestUser':
            flash(f'The username {username} and the provided password combination is not in our system.\n Please check the credentials provided and reattempt your login.', 'alert alert-danger' )
            return redirect(url_for('login_bp.login'))
@login_bp.route('/dashboard', methods=['POST', 'GET'])
# @login_required
def dashboard():
    return render_template('dashboard_landing.jinja',
                        #    title='<title> Safari Life Child Management System - User Homepage </title>',
                           template='base',
                           location="homepage")



@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description, title='Security Error', template='base'), 400

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.jinja', error=404, title='Page Not Found', template='404')
@app.errorhandler(403)
def page_not_found(error):
    return render_template('403.html', error=403, title='Not Authoized', template='403')


# login_manager.unauthorized_handler()
# @login_bp.routes('/unauthorized')
# def unauthorized():
#     lm = LoginManager()
#     lm.login_view = "url_for('login')"
#     res = lm.unauthorized()
#     return render_templete('401.html') 