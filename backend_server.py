from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS, cross_origin
from gevent.wsgi import WSGIServer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
@cross_origin(origin='*')
def render():
    return render_template('example.html')


if __name__=='__main__':
    #app.run(debug = True, host = '0.0.0.0',port=1111)
    # app.run(debug = True, host = 'localhost', port=5000)

    #create the tmux server to preload the model
    #TODO preload different models with different windows, ready for any model


    http_server = WSGIServer(('0.0.0.0', 1111), app)

    http_server.serve_forever()
