# Configuration
from sqlalchemy import create_engine
# for configuration
from sqlalchemy.orm import scoped_session, sessionmaker
# for creating foreign key relationship between the tables
from sqlalchemy.ext.declarative import declarative_base
# For mappper code 
# import sys 



# Create_engine instance
engine = create_engine('mysql://root:Littlealchemy1!@localhost:3306/nbastats')

db_session = scoped_session(
    sessionmaker(autocommit=False,autoflush=False,bind=engine)
)

#Create delcatative base instance
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)










Base.metadata.create_all(engine)