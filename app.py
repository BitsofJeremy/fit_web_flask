"""fit_web app"""
# Import the app
from fit_web import app


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
    )
