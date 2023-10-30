from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app=Flask(__name__)

def load_buyer_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from buyer"))
    buyers = []
    for rows in result.all():
      buyers.append(dict(row))
  


@app.route("/")
def hello_estates():
  return render_template('home.html'
                        jobs=JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)