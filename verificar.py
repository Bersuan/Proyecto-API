
from flask import Flask, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from errorHandler import jsonErrorHandler
import json

client = MongoClient("mongodb://localhost:27017/")
db = client['Emotion']
'''
@jsonErrorHandler
def verification(user_id, chat_id, message):
    coll_user = db['User']
    find_id = list(coll_user.find({'_id':{'$eq':ObjectId(user_id)}})) 

    coll_chat = db['Chat']
    find_chat = list(coll_chat.find({"$and":[{"_id":{"$eq":ObjectId(chat_id)}},{"users":{"$eq":ObjectId(user_id)}}]}))

    if len(find_id) == 0:
        raise NameError(f"Not found user with id {user_id}")

    elif len(find_chat) ==0:
        raise NameError(f"Not found chat with id {chat_id}")

    else:
        '''
def listMessage (chat_id):
    coll_chat = db['Chat']
    list_message = coll_chat.find({'_id':{'$eq':ObjectId(chat_id)}})
    if list_message.count() == 0:
        raise NameError(f"Not found chat with id {chat_id}")
    else:
        coll_message = db['Message']
        allMessages = list(coll_message.find({'chat':{"$eq":ObjectId(chat_id)}},{'_id':0, 'message':1}))
        print (allMessages)
    return allMessages