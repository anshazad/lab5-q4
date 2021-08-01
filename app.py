import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 

    jsonStr = request.get_json()
    #print(jsonStr)
    jsonObj = json.loads(jsonStr)
    response = ""
    n=int(jsonObj['n'])
    
    def recursive_binaryconverter(N,s="1"):
        if N==0:
            return "0"
        elif N==1:
            return s
        else:
            s=recursive_binaryconverter(N//2,s)+str(n%2)
            return s 
        
    
    response+=recursive_binaryconverter(n)
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
