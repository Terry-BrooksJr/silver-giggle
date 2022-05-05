from urllib.parse import urlparse, urljoin

from flask import Flask, request, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_rbac import RBAC
from config import Config
from init_db import PlatformUsers



# Globally accessible libraries
db = SQLAlchemy()
# r = FlaskRedis()
login_manager = LoginManager()
rbac = RBAC()

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    login_manager.login_view = ''

    # Initialize Plugins
    with app.app_context():
        init_db()    # r.init_app(app)
        login_manager.init_app()
        rbac.init_app()



    with app.app_context():
        # Include our Routes
        from app.login import routes_login  # pylint: disable=import-outside-toplevel
        from app.admin import routes_admin # pylint: disable=import-outside-toplevel
        from app.dashboard import routes_dashboard  # pylint: disable=import-outside-toplevel
        from app.enrollment import routes_enrollment  # pylint: disable=import-outside-toplevel

        # Register Blueprints
        app.register_blueprint(routes_login.login_bp)
        app.register_blueprint(routes_admin.admin_bp)
        app.register_blueprint(routes_dashboard.dashboard_bp)
        app.register_blueprint(routes_enrollment.enrollment_bp)
    return app


# * Next 3 Function collectively will  confirm url after login flow is safe for redirects. Written in the app factory because these 3 functions will be used in each blue print routes
# * Function  1: that ensures that a redirect target will lead to the same server


def is_safe_url(target): #pylance:disable missi
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc

# * Function 2: that looks at various hints to find the redirect target uses function 1 as a helper
def get_redirect_target():
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target

# * Function 3: Ensures we do not redirect the initial POST request created at form submission by redirecting with a  slightly different argument (only use the submitted data, not the referrer
def redirect_back(endpoint, **values):
    target = request.form['next']
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)