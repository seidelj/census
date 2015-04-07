from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('postgresql://postgres:joseph@localhost/census')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Address(Base):
	__tablename__ = 'address'
	id = Column(Integer, Sequence("state_id_seq"), primary_key=True)
	user = Column(String)
	street = Column(String)
	city = Column(String)
	state = Column(String)
	zipcode = Column(String)
	geography_id = Column(Integer, ForeignKey('geography.id'))

	geography = relationship('Geography', backref=backref('address', order_by=id))

class Geography(Base):
	__tablename__ = 'geography'
	id = Column(Integer, Sequence("geography_id_seq"), primary_key=True)
	state = Column(String)
	county = Column(String)
	tract = Column(String)
	blockgrp = Column(String)
	block = Column(String)


Base.metadata.create_all(engine)

