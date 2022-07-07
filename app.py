from flask import Flask, jsonify, request, render_template
#from model import ChatBot
from model1 import *
import json 
import warnings
warnings.filterwarnings('ignore')


if __name__=='__main__':
    pass

    
# app
app = Flask(__name__)

# routes

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])

def predict():
    # chatbot = ChatBot()
    data = request.get_json(force=True)
    print(data)
    #reply = chatbot.get_reply(data['message'])
    reply = generate_res(data['message'])

    #bodyFat = predictBodyFat(np.asarray(data['raw_img']).astype(np.uint8))
    print(reply)
    # send back to browser
    
    # return data 
    return jsonify(results=reply)


if __name__ == '__main__':
    app.run(port =7000, debug=True)