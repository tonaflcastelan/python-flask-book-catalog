from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='tona').first():
            User.create_user(user='tona', email='tona@gmail.com', password='secret')
    except exc.IntegrityError:
        flask_app.run()
