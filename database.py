from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://pscale_pw_KhSMxIK1SvGsuDds53TAdbMsr1ovLvO3hCxQZuoNRgC:pscale_pw_KhSMxIK1SvGsuDds53TAdbMsr1ovLvO3hCxQZuoNRgC@aws.connect.psdb.cloud/real_estate_listings?charset=utf8mb4"

engine=create_engine(
  db_connection_string,
  connect_args={
    ssl      = {
      "ssl ca": "/etc/ssl/cert.pem"
    }      
  })
                     
