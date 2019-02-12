from flask import Flask, request, abort, render_template, jsonify
from flask_cors import CORS
import ConnectDB as conn
import QueryDB as qr
import ManageDialogflow as mgdia
import json

db_host = '127.0.0.1'
db_user = 'root'
db_pw = ''
db_name = 'infouser'

dlf_project_id = 'fir-thesis-v1'
dlf_session_id = 'a409931f1c2ea9842c238469417ae2ac490b36bd'

mgDLF = mgdia.manageDLF(projectID=dlf_project_id,
                        sessionID=dlf_session_id)

conDB = conn.connectDB(host=db_host,
                       username=db_user,
                       password=db_pw,
                       database=db_name)

qy = qr.queryDB(conDB.getConnection())

text_train_list = qy.querySelect(selectPart='fact_name',
                                fromPart='fact_data',
                                wherePart='1')

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/test-deploy', methods=['POST'])
def test_deploy():
    msg = request.json.get('msg')
    return jsonify(msg)

@app.route('/train-dlf', methods=['POST'])
def train_dlf():
    result_data_list = []
    result_data = None
    for text_train in text_train_list:
        #print(text_train[0])
        dlf_display = "{}".format(text_train[0])
        dlf_train_phr = {"{}".format(text_train[0])}
        dlf_message_txt = {"{}".format(text_train[0])}
        print('{} {} {}'.format(dlf_display, dlf_train_phr, dlf_message_txt))

        res = mgDLF.create_intent(display_name=dlf_display,
                                training_phrases_parts=dlf_train_phr,
                                message_texts=dlf_message_txt)

        if res is 0:
            print('Intent {} is already exist.'.format(dlf_display))
        else :
            print(res)
        result_data = {
            "exist" : res,
            "intent" : text_train[0]
        }
        result_data_list.append(result_data)
    result_data = {
        "result_list" : result_data_list
    }
    return json.dumps(result_data)

if __name__ is '__main__':
    app.run()