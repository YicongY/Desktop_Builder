from flask import Flask, request, render_template, jsonify, Response,g
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer
from Desktop_Builder import Desktop_Builder
import json
from budget import basic_budget, gaming_budget, working_budget
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
@cross_origin(origin='*')
def render():
    return render_template('example.html')

@app.route('/first', methods =['POST'])
@cross_origin(origin='*')
def runRemine():
    data = request.data
    para = {}
    json_data = json.loads(data)
    para['money']= json_data["budget"]
    para['purpose']  = json_data["purpose"]

    builder = getattr(g, '_builder', None)
    if (builder is None):
        builder = Desktop_Builder(para)
        setattr(g, '_builder', builder)

    print(builder.para)
    print(builder.budget)
    option_para = {}
    url_list = builder.recommender('cpu', 'fast',option_para)
    print(url_list)
    return jsonify({'url': url_list})

@app.route('/second', methods =['POST'])
@cross_origin(origin='*')
def second():
    data = request.data

    para = {}
    builder = getattr(g, '_builder', None)
    if (builder is None):
        builder = Desktop_Builder(para)
        setattr(g, '_builder', builder)

    print(builder.para)
    print(builder.budget)
    option_para = {}
    url_list = builder.recommender('cpu', 'fast',option_para)
    print(url_list)
    return jsonify({'url': url_list})

if __name__=='__main__':
    #app.run(debug = True, host = '0.0.0.0',port=1111)
    # app.run(debug = True, host = 'localhost', port=5000)

    #create the tmux server to preload the model
    #TODO preload different models with different windows, ready for any model


    http_server = WSGIServer(('0.0.0.0', 1111), app)

    http_server.serve_forever()
