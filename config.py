DB_USER = "root"
DB_PASSWORD = "123456"  # sua senha aqui
DB_HOST = "localhost"
DB_NAME = "devconnect"

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = "jwt-secret"