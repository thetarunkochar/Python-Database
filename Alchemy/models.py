from sqlalchemy import create_engine, Column, Integer, String, or_, and_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///final.db', echo=False)
# create_engine('postgresql:///dakshbindal:123@localhost:5432/python_test')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', lastname='%s')>" % (self.name, self.fullname, self.lastname)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

# user_a = User(name="", fullname="", lastname="")
# session.add(user_a)
# session.commit()
# session.close()

rows=session.query(User).get(1)
rows_where=session.query(User).filter(User.name.ilike('Sara')).all()
# print(rows_where)

# print(session.query(User).filter(and_(User.name.ilike('S%'), User.lastname.ilike('G%'))).all())

#update query, sycn -> after updating it will return the id of updated data
session.query(User).filter(User.name=='Rohit').update({"lastname":"Tendulkar"}, synchronize_session='fetch')
session.commit() 