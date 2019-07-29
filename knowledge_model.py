from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

class Knowledge(Base):
    	__tablename__ = 'Articles'
    	Article_name = Column(String, primary_key=True)
    	year = Column(Integer)
    	rating = Column(String)

    	def __repr__(self):
    		return ("If you want to learn about {}, you should look at the Wikipedia article called {}. We gave this article a rating of {}").format(self.Article_name, self.year, self.rating)
    		

BHM= Knowledge(Article_name="Black History Month", year=2019, rating="10 out of 10!")
print(BHM)
Vaccination= Knowledge(Article_name="Vaccination", year=2019, rating="8 out of 10!")
print(Vaccination)
# Fast Food= Knowledge(Article_name="Fast Food", year=2019, rating=7/10)
# print(Fast Food)

