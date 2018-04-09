from flask import Flask, request
from flask_cors import CORS
from converter import markdown

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    url = request.args.get('url')

    if url:
        try:
            content = markdown(url)
        except Exception as e:
            print('ERROR --> ', e)
            return 'error', 502

        if content:
            return content, 200, {'Content-Type': 'text/x-markdown; charset=UTF-8'}
    else:
        return 'Please give a valid url', 501


if __name__ == '__main__':
    app.run(debug=True)
