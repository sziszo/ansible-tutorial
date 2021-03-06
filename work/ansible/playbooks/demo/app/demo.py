from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, socket

print('DATABASE_URI:' + os.environ['DATABASE_URI'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)
hostname = socket.gethostname()

@app.route('/')
def index():
  return 'Hello, from sunny %s!\n' % hostname

@app.route('/db')
def dbtest():
  try:
      db.create_all()
  except Exception as e:
      return "error: {0}\n".format(e)
  return 'Database Connected from %s!\n' % hostname

if __name__ == '__main__':
  app.run()
