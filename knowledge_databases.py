from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(Article_name, year, rating):
    article_object = Knowledge(
        Article_name=Article_name,
        year=year,
        rating=rating)
    session.add(article_object)
    session.commit()

# add_article("SQL", 2018, "10 out of 10!")


def query_all_articles():
    article = session.query(
        Knowledge).first()
    return article


print(query_all_articles())

def query_article_by_topic(their_name):
	article = session.query(
       Knowledge).filter_by(
       name=their_name).first()
    return student


def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
