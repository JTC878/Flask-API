# config.py

import pathlib
import connexion
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

load_dotenv()

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mssql+pyodbc:///?odbc_connect="
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={os.environ.get('SERVER')};"
    f"DATABASE={os.environ.get('DATABASE')};"
    f"UID={os.environ.get('UID')};"
    f"PWD={os.environ.get('PWD')};"
    "TrustServerCertificate=yes;"
    "Encrypt=yes;"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)