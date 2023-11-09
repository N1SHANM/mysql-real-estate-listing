from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app=Flask(__name__)

def load_buyer_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from property"))
    property = []
    for rows in result.all():
      property.append(dict(row))
    return property
  


@app.route("/")
def hello_estates():
  return render_template('home.html',property=property)

@app.route("/properties")
def list_jobs():
  return jsonify(JOBS)

@app.route("/properties/<id>")
def show_jobs(id):
  job = load_job_from_db(id)
  if not job:
    return "Not found",404
  return render_template('jobpage.html',job=job)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)