import numpy as np

from flask import Flask, request, jsonify
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'welcome, This is a new generation HIS'

@app.route('/predict', methods=['POST'])
def postInput():
    insertValues =request.get_json()
    print('1234')
    print(insertValues)
    condition=insertValues['condition']
    encounter=insertValues['encounter'] 
    medication=insertValues['medication']
    observation=insertValues['observation']
    patient=insertValues['patient']

    input=np.array(condition)

    print(input)
    return jsonify({'return': 'ok' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) #debug可以讓修改程式存檔後 不用control +c 他可以直接用新的code重啟