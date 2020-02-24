from flask import Flask, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from verificar import mensajesChat, mensajeUsuario
from sentimientos import formatendadoChats, formatendadoUsers
import json
from errorHandler import jsonErrorHandler
from recomendacion import cadaUsuario


client = MongoClient("mongodb://localhost:27017/")
db = client['Emotion']

app = Flask(__name__)


@app.route('/user/create/<name>')
def createUser(name):
    '''Importamos usuarios a MongoDB'''

    coll_user = db['User']
    usuario = coll_user.insert_one({
        "user": name

    }).inserted_id

    return str(usuario)


@app.route('/chats/create/<chats>')
def crateChats(chats):
    '''Importamos chats a MongoDB'''

    coll_chat = db['Chat']
    whatsapp = coll_chat.insert_one({
        "chat": chats,
        "users": []

    }).inserted_id

    return str(whatsapp)


@app.route('/insertUser/create/<chat_id>/<name>')
def insertUserChat(chat_id, name):
    '''Añadimos usuarios al chat'''

    coll_chat = db['Chat']
    insertUser = coll_chat.update({"_id": ObjectId(chat_id)}, {
                                  "$push": {"users": name}})

    return str(insertUser)


@app.route('/createMessage/create/<user_id>/<chat_id>/<message>')
def createMessage(user_id, chat_id, message):
    '''Añadimos mensajes a MongoDB de un ususario y de un chat'''

    # return verification(user_id, chat_id, message)
    coll_message = db['Message']
    mensaje = coll_message.insert_one({"chat": ObjectId(
        chat_id), "user": ObjectId(user_id), "message": message}).inserted_id

    return str(mensaje)


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


@app.route('/analize/chats/<chat_id>')
def sentiemintoChat(chat_id):
    sentChat = formatendadoChats(chat_id)
    return json.dumps(sentChat)


@app.route('/analize/users/<user_id>')
def sentiemintoUser(user_id):
    sentUser = formatendadoUsers(user_id)
    return json.dumps(sentUser)


@app.route('/recommend/users/<user_id>')
def recommendUser(user_id):
    recomUser = cadaUsuario(user_id)
    return json.dumps(recomUser)


app.run("0.0.0.0", 5000, debug=True)
