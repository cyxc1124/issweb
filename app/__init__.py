from flask import Flask





def create_app():
    app = Flask(__name__)

    from app.xiaocaoserverlist import xiaocaoserverlist
    app.register_blueprint(xiaocaoserverlist)

    from app.tuanziserverlist import tuanziserverlist
    app.register_blueprint(tuanziserverlist)

    from app.otherserverlist import otherserverlist
    app.register_blueprint(otherserverlist)

    from app.modlist import modlist
    app.register_blueprint(modlist)

    from app.index import index
    app.register_blueprint(index)

    return app