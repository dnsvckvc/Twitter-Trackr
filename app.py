from flask import (Flask, jsonify)
from flask_cors import CORS
from auth import requires_auth, AuthError

def create_app():
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    return app


app = create_app()


@app.route('/slavko')
@requires_auth('get:asset_price_histories')
def get_index_page():
    return 'Ovo radi'


# Error Handling

@app.errorhandler(AuthError)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)