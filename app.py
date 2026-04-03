from flask import Flask
from database.db import db
from routes.user_routes import user_routes
from flask_jwt_extended import JWTManager
import config

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(user_routes)

@app.before_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

from flask_jwt_extended import JWTManager

# configurar secret key
app.config["JWT_SECRET_KEY"] = "super-secret"  # pode ser qualquer string segura
jwt = JWTManager(app)