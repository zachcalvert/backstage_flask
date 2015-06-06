from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from datetime import datetime

from utils import calculate_difference

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Calculation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	last_requested = db.Column(db.DateTime, default=datetime.utcnow())
	number = db.Column(db.Integer)
	value = db.Column(db.Integer)
	occurrences = db.Column(db.Integer, default=1)

	def __str__(self):
		return 'the calculated difference with {0} as input is: {1}'.format(self.number, self.value)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/difference/<int:number>')
def difference(number):

	try:
		c = Calculation.query.filter_by(number=number).first()
		c.occurrences += 1
		db.session.add(c)
		db.session.commit()

	except Exception, e:
		value = calculate_difference(number)
		c = Calculation(number=number, value=value)
		db.session.add(c)
		db.session.commit()

	d = {}
	d['number'] = c.number
	d['value'] = c.value
	d['occurrences'] = c.occurrences
	d['last_requested'] = datetime.now()

	return jsonify(**d)

if __name__ == '__main__':
	manager.run()
	app.run(debug=True)
