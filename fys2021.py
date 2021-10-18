from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/docs')

@app.route('/<path:path>')
def send_docs(path):
    return send_from_directory('docs', path)

@app.route('/style/<path:path>')
def send_docs_style(path):
    return send_from_directory('docs/style', path)


if __name__ == "__main__":
    app.run()
