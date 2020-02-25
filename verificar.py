from flask import Flask, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from errorHandler import jsonErrorHandler
import json

client = MongoClient("mongodb://localhost:27017/")
db = client['Emotion']


'''
def verification(user_id, chat_id, message):

#Verificar si existe el usuario y si pertenece al chat donde se va a importar ese mensaje

    coll_user = db['User']
    find_id = coll_user.find({'_id': {'$eq': ObjectId(user_id)}})

    coll_chat = db['Chat']
    find_chat = coll_chat.find(
        {"$and": [{"_id": {"$eq": ObjectId(chat_id)}}, {"users": {"$eq": ObjectId(user_id)}}]})

    if find_chat.count() <= 0:
        raise NameError(f"Not found chat with id: {chat_id}")

    elif find_id.count() <= 0:
        raise NameError(f"Not found user with id: {user_id}")

    else:
        coll_message = db['Message']
        mensaje = coll_message.insert_one({"chat": ObjectId(
            chat_id), "user": ObjectId(user_id), "message": message}).inserted_id
        return str(mensaje)
'''


def mensajesChat(chat_id):
    '''
    Obtenemos los mensajes escritos en un unico chat
    '''

    coll_chat = db['Chat']
    list_message = coll_chat.find({'_id': {'$eq': ObjectId(chat_id)}})
    if list_message.count() == 0:
        raise NameError(f"Not found chat with id {chat_id}")
    else:
        coll_message = db['Message']
        allMessages = list(coll_message.find(
            {'chat': {"$eq": ObjectId(chat_id)}}, {'_id': 0, 'message': 1}))

    return allMessages


def mensajeUsuario(user_id):
    '''
    Obtenemos los mensajes escritos por un usuario en cualquier chat
    '''

    coll_user = db['User']
    find_user = coll_user.find({'_id': {'$eq': ObjectId(user_id)}})

    if find_user.count() <= 0:
        raise NameError(f"Not found User with this Id: {user_id}")
    else:
        coll_message = db['Message']
        mensajesUsuario = list(coll_message.find(
            {'user': {"$eq": ObjectId(user_id)}}, {'_id': 0, 'message': 1}))

    return mensajesUsuario
