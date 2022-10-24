import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsmedia1stproject'
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY') or '2sA0VV3PtshhNPjAmePpHIXZmgreoSw6WcRXi0ZWUm67QpgWmp0yR4x45XeGYM0S+e8oEOeNitTj+ASt4rindg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get(
        'SQL_SERVER') or 'project1-udacity-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms-prject1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'dbadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@ssword1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + \
        SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + \
        SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "wC-8Q~6FxTK7s4lZUsMj2DlVcPnhycIYt8RrNbls"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/common"
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "caa8dd87-0154-473f-ad55-551baa51c158"

    # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/getAToken"

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
