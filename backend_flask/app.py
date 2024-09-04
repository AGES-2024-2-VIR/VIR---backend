from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from routes.users import bp as users_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run()
