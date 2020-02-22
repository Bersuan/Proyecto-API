from flask import Flask, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from verificar import mensajesChat, mensajeUsuario
import json
from errorHandler import jsonErrorHandler


client = MongoClient("mongodb://localhost:27017/")
db = client['Emotion']

app = Flask(__name__)


@app.route('/user/create/<name>')
def createUser(name):
    '''Importamos usuarios a MongoDB'''

    coll_user = db['User']
    usuario = coll_user.insert_one({"user": name}).inserted_id
    return str(usuario)


@app.route('/chats/create/<chats>')
def crateChats(chats):
    '''Importamos chats a MongoDB'''

    coll_chat = db['Chat']
    whatsapp = coll_chat.insert_one({"chat": chats, "users": []}).inserted_id
    return str(whatsapp)


@app.route('/insertUser/create/<chat_id>/<user_id>')
def insertUserChat(chat_id, user_id):
    '''Añadimos usuarios al chat'''

    coll_chat = db['Chat']
    insertUser = coll_chat.update({"_id": ObjectId(chat_id)}, {
                                  "$push": {"users": [ObjectId(user_id)]}})
    return str(insertUser)


@app.route('/createMessage/create/<chat_id>/<user_id>/<message>')
def createMessage(chat_id, user_id, message):
    '''Añadimos mensajes a MongoDB de un ususario y de un chat'''

    coll_message = db['Message']
    mensaje = coll_message.insert_one({"chat": ObjectId(
        chat_id), "user": ObjectId(user_id), "message": message}).inserted_id
    return str(mensaje)
  #  return verification(chat_id, user_id, message)


@jsonErrorHandler
@app.route('/list/chats/<chat_id>')
def createListMessage(chat_id):
    lst = mensajesChat(chat_id)
    return json.dumps(lst)


@jsonErrorHandler
@app.route('/list/user/<user_id>')
def listaMensajesUsuario(user_id):
    newList = mensajeUsuario(user_id)
    return json.dumps(newList)


app.run("0.0.0.0", 5000, debug=True)
