from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'SE 3',
    'location': 'San Francisco, CA',
    'salary': '$ 100,000'
  },
  {
    'id': 3,
    'title': 'SWE 2',
    'location': 'Chicago, IL',
    'salary': '$ 75,000'
  },
  {
    'id': 4,
    'title': 'CEO',
    'location': 'Remote',
    'salary': '$ 1,000,000'
  }

]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Spark')
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
