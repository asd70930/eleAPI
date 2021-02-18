from flask import Flask, jsonify
from flask import make_response
from flask import request
import elevatorAPI
import pickle

app = Flask(__name__)

# p = {}
# file = open('pickle.pickle', 'wb')
# pickle.dump(p, file)
# file.close()

@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/eleapi/compares', methods=['POST'])
def compare():
    data = request.get_json()
    id = data['id']
    ip = data['ip']
    with open('pickle.pickle', 'rb') as file:
        alllist = pickle.load(file)
    camrea_existing = id in alllist
    if camrea_existing:
        camera = alllist[id]
        result = {"result": camera.compare(ip)}
        return jsonify(result)
    else:
        return jsonify({"result": "id not existing"})

@app.route('/eleapi/initials', methods=['POST'])
def initial():
    data = request.get_json()
    id = data['id']
    ip = data['ip']
    with open('pickle.pickle', 'rb') as file:
        alllist = pickle.load(file)
    camrea_existing = id in alllist
    if camrea_existing:
        return jsonify({"result": "id has existed"})
    else:
        camera = elevatorAPI.ele(ip)
        alllist[id] = camera
        file = open('pickle.pickle', 'wb')
        pickle.dump(alllist, file)
        file.close()
        return jsonify({"result": "done"})

@app.route('/eleapi/reinitials', methods=['POST'])
def reinitial():
    data = request.get_json()
    id = data['id']
    ip = data['ip']
    with open('pickle.pickle', 'rb') as file:
        alllist = pickle.load(file)
    camrea_existing = id in alllist
    if camrea_existing:
        camera = alllist[id]
        camera.reinitial(ip)
        file = open('pickle.pickle', 'wb')
        pickle.dump(alllist, file)
        file.close()
        return jsonify({"result": "done"})
    else:
        return jsonify({"result": "id not existing"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=False, port=8000)

