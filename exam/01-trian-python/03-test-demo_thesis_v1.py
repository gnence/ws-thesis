import lib.connect_db as conn
import lib.query_db as qr
import lib.manage_dlf as mgdia

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