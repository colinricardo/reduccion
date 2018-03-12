from flask import Flask, request
from converter import markdown

app = Flask(__name__)

@app.route('/')
def index():
  url = request.args.get('url')

  if url:
    content = markdown(url)

    if content:
      return content, 200, {'Content-Type': 'text/x-markdown; charset=UTF-8'}
    else:
      return '404 Not Found', 404
  else:
    return  'Please give a valid url', 501

if __name__ == '__main__':
  app.run(debug=True)
