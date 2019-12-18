import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask App ...INIT'

if __name__ == '__main__':
    app.run(host = os.enviorn.get('IP'),port = int(os.environ.get('PORT')),debug = True)
