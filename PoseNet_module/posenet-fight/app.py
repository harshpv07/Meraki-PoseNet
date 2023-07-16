from flask import Flask, escape, request,jsonify
import pymongo
import dns
app = Flask(__name__)

@app.route('/push' , methods = ['POST' , 'GET'])
def pushUpdate():
    location = request.form['loc']  
    client = pymongo.MongoClient("mongodb+srv://harsh:harsh@cluster0-yp4le.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.client
    msg = "WARNING !! Possibility of violence has been reported in this " + str(location) + ". Please avoid these areas "
    db.cls.insert_one({"news": msg})
    return jsonify({'flag':1})
    ##  mongo push

@app.route('/pull' , methods = ['POST' , 'GET'])
def pullUpdate():
    client = pymongo.MongoClient("mongodb+srv://harsh:harsh@cluster0-yp4le.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.client
    l = client.client.cls.distinct("news")
    print(l)
    return jsonify({'result':l})
    ##  mongo pull return

@app.route('/alert' , methods = ['POST' , 'GET'])
def pulllocation():
    userloc = request.form["curr"]
    print(userloc)
    return userloc

if __name__ == "__main__":
    app.run(debug = True,host = "0.0.0.0",port = 5001)