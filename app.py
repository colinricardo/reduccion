from flask import Flask, request
from converter import markdown

app = Flask(__name__)

@app.route('/')
def index():
  url = request.args.get('url')

  if url:
    try:
      content = markdown(url)
    except Exception as e:
      print('ERROR --> ', e)
      return 'An error occurred with parser', 502

    if content:
      return content, 200, {'Content-Type': 'text/x-markdown; charset=UTF-8'}
    else:
      return '404 Not Found', 404
  else:
    return 'Please give a valid url', 501

if __name__ == '__main__':
  app.run(debug=True)
