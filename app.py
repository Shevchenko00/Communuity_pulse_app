from community_app import create_app
from community_app.models.questions import Questions
from community_app.models.response import Responses


SQLALCHEMY_TRACK_MODIFICATIONS = False


if __name__ == '__main__':
    app = create_app()
    app.run()