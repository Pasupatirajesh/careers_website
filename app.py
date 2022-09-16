from flask import Flask, render_template, jsonify, current_app, g
import os, sqlite3
import db
import auth

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY = 'dev',
    DATABASE=os.path.join(
      app.instance_path, "spark.sqlite"))
  db.init_app(app)
  
  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)
  
  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
    
  @app.route("/")
  def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Spark')
  
  @app.route("/jobs")
  def list_jobs():
    return jsonify(JOBS)

  app.register_blueprint(auth.bp)
  
  return app



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
    'salary': '$ 175,000'
  },
  {
    'id': 4,
    'title': 'CEO',
    'location': 'Remote',
    'salary': '$ 1,000,000'
  }

]

if __name__ == "__main__":
  app= create_app()
  app.run(host='0.0.0.0', debug=True)
