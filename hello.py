#def geeks():
#    value = {
#        "language": language,
#        "company": company,
#        "Itemid": Itemid,
#        "price": price
#    }
#    return jsonify(value)
    #return json.dump(value)

#print(geeks())

# Route for CoinToss
from flask import Flask
@app.route("/test", methods=['GET', "POST"])
def test():
   data = {"picked": "1"}
    j = json.dumps(data)
    return jsonify(j)

#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!"

#if __name__ == "__main__":
#    app.run()
