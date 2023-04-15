import os
from flask_app import create_app
from dotenv import load_dotenv

# GLOBALS
FLASK_DEBUG = os.getenv("FLASK_DEBUG", 0)
FLASK_PORT = os.getenv("FLASK_PORT", 5000)

load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(
        host="0.0.0.0", 
        port=FLASK_PORT,)
