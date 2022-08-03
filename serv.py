from flask import Flask, render_template, request
import base64
import secrets
import string
import random
import pymongo

connection_url = "NULL"

ui = Flask(__name__)
def call1(value):
    value = value.encode("utf-8")
    value = base64.b64encode(value)
    value = value.decode("utf-8")
    return value
def call0(value):
    return value[::-1]
def decTobin(n):
    return bin(n).replace("0b", "")
def limlog(number):
    return ''.join(secrets.choice(string.digits)for time in range(number))
def chooselen(bini, value):
    if bini == '1':
        return call1(value)
    if bini == '0':
        return call0(value)
def uncall1(finalnormal):
    finalnormal = finalnormal.encode("utf-8")
    finalnormal = base64.b64decode(finalnormal)
    finalnormal = finalnormal.decode("utf-8")
    return finalnormal
def uncall0(finalnormal):
    return finalnormal[::-1]
def chooselde(bini, finalnormal):
    if bini == '1':
        return uncall1(finalnormal)
    if bini == '0':
        return uncall0(finalnormal)
def decTobin(n):
    return bin(n).replace("0b", "")



@ui.route('/', methods=['GET'])
def welcome():
    return render_template('main.html')

@ui.route('/en', methods=['GET'])
def en():
    return render_template('en.html')

@ui.route('/de', methods=['GET'])
def de():
    return render_template('de.html')


@ui.route('/t_encrypt', methods=['POST'])
def ten():
    mongo_connect = pymongo.MongoClient(connection_url)
    mydb = mongo_connect['deen']
    mytrashbin = mydb['trashbin']
    value = request.json['message']
    if value == '':
        return 'err_val'
    else:
        numtree = random.randint(128, 256)
        tree = limlog(numtree)
        tree = str(tree)
        tmep = 0
        for i in range(len(tree)):
            tmep = tmep + int(tree[i])
        appendex = str(tmep)
        tree = decTobin(tmep)
        tree = str(tree)
        for i in range(len(tree)):
            value = chooselen(tree[i], value)
        noee = 0
        nofe = 0
        for i in range(len(value)):
            if value[i] != '=':
                nofe = i
                break
        value = value[::-1]
        for i in range(len(value)):
            if value[i] != '=':
                noee = i
                break
        value = value[::-1]
        value = value[nofe:len(value)-noee]
        check = mytrashbin.find_one({'key':value, 'method': appendex, 'nofe':nofe, 'noee':noee})
        if check == None:
            mytrashbin.insert_one({'key':value, 'method': appendex, 'nofe':nofe, 'noee':noee, 'isvalid':True})
            return value
        else:
            return str(0)





@ui.route('/t_decrypt', methods=['POST'])
def tde():
    mongo_connect = pymongo.MongoClient(connection_url)
    mydb = mongo_connect['deen']
    mytrashbin = mydb['trashbin']
    key = request.json['message']
    flag = mytrashbin.find_one({'key':key})
    if flag == None:
        return 'unga bunga key detected!'
    elif flag['isvalid'] == False:
        return 'Key is expired!'
    else:
        exnum = flag['method']
        nofe = flag['nofe']
        noee = flag['noee']
        mytrashbin.update_one({'key':key}, {'$set':{'isvalid':False}})
        nofes = ''
        noees = ''
        for i in range(nofe):
            nofes = nofes + '='
        for i in range(noee):
            noees = noees + '='
        key = nofes + key + noees
        exnum = decTobin(int(exnum))
        exnum = str(exnum)
        exnum = exnum[::-1]
        for i in range(len(exnum)):
            key = chooselde(exnum[i], key)
        return key
