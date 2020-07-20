from pymongo import MongoClient
import pickle
import time
client = MongoClient('192.168.2.110',
                     username='root',
                     password='root')
collection = client.test.job
for post in collection.find({}).limit(12):
    print('id: ',post['_id'],'next_run_time: ',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(post['next_run_time'])))
    print('job detail: ',pickle.loads(post['job_state']))
client.close()