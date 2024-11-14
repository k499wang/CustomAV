from flask import Flask

def create_app(db, trie):
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['db'] = db
    app.config['trie'] = trie
    
    from .routes import anti
    app.register_blueprint(anti)

    return app