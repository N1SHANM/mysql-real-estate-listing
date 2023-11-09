from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://bv4gc0428pe25v0qovkm:pscale_pw_KzGYy90sgYHkCSikYCJZOeAc69IkpyedWWPzpUXoabs@aws.connect.psdb.cloud/qwerty?charset=utf8mb4"

engine=create_engine(
  db_connection_string,
  connect_args={
    "ssl"      : {
      "ssl ca": "/etc/ssl/cert.pem"
    }      
  })

with engine.connect() as conn:
  result = conn.execute(text("select * from property"))
  print(result.all())
  

          