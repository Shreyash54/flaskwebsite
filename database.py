from sqlalchemy import create_engine


db_connection_string = "mysql+pymysql://3ticmhd8ztxcgpj3k108:pscale_pw_EMnAtS8E5deGJ8fyhB2VDtSWxnW2iNTwUFot8tr9RDR@aws.connect.psdb.cloud/shreyashguptaflask?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
                       connect_args={
                         "ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                         }})
