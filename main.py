from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'DATA ANALYST',
  'location': 'Bengaluru ,India',
  'salary': 'Rs 1,00,000',
}, {
  'id': 2,
  'title': 'DATA SCIENTIST',
  'location': 'Delhi ,India',
  'salary': 'Rs 2,00,000',
}, {
  'id': 3,
  'title': 'DATA ANALYST',
  'location': 'Mumbai ,India',
  'salary': 'Rs 14,00,000',
}, {
  'id': 4,
  'title': 'DATA MINER',
  'location': 'MP ,India',
  'salary': 'Rs 11,00,000',
}]


@app.route('/')
def hello():
  return render_template('home.html', jobs=JOBS , companyname = 'Harry')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
