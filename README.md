# Flask App

This is a sample Flask application that demonstrates how to use SQLAlchemy and SQLite3 to interact with a database.

## Getting Started

1. Clone this repository:
```
git clone git@github.com:davidhfrankelcodes/flask-auth-starter.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Make a .env file and fill it out like the example below.
```
nano .env
```
```
FLASK_DEBUG=1
FLASK_SIGNUP_DISABLED=0
FLASK_PORT=5000
FLASK_SECRET_KEY=your-secret-key
FLASK_SQLALCHEMY_TRACK_MODIFICATIONS=1
```

4. Create a new database:
```
export FLASK_APP=run.py && flask db init
flask db migrate
flask db upgrade
```

5. Start the development server:
```
python run.py
```

6. After the database has been created, the prod server can run in docker using
```
docker-compose up -d --build
```
