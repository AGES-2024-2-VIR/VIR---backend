from flask import Flask
from config import Config
from models import db
from routes import bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# Registrar blueprint das rotas
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()
