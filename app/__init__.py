from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.server_list import server_list
    app.register_blueprint(server_list)

    from app.modlist import modlist
    app.register_blueprint(modlist)

    from app.index import index
    app.register_blueprint(index)

    return app
