from pymongo import MongoClient

class dbhelper:
	'''
	What this class does is:
	to define what fields inside json to be stored 
	Perform some conditions checking in Mongodb
	Store into the database
	'''
	_client=None
	_db=None
	def setup():
		if(not dbhelper._client):
			dbhelper._client=MongoClient('localhost',27017)
			dbhelper._db=dbhelper._client["main_db"]
	
	def insert_many(docs,coll_name):
		try:
			dbhelper._db[coll_name].insert_many(docs)
			return True
		except Exception as e:
			print("Error at insert_many {}".format(e))
			return False
	