# import connectDialogflow as testI
#
# projectID = "testfirsttime-cc18f"
# sessionID = "2e313f9fc554d4529f05f85810452f53b3041869"
# text = "มีอาการเจ็บบริเวณคอ"
# display = "มีอาการเจ็บคอ"
# tt_pp = {"มีอาการเจ็บคอ"}
# m_t = {"มีอาการเจ็บคอ"}
#
# '''testI.create_intent(projectID, display, tt_pp, m_t);'''
# testI.detect_intent_texts(project_id=projectID,
#                           session_id=sessionID,
#                           texts=text,
#                           language_code="th")

import lib.connect_db as conn
import lib.query_db as qr
import lib.manage_dlf as mgdia

db_host = '127.0.0.1'
db_user = 'root'
db_pw = ''
db_name = 'infouser'

# dlf_project_id = 'fir-thesis-v1'
# dlf_session_id = 'a409931f1c2ea9842c238469417ae2ac490b36bd'

# mgDLF = mgdia.manageDLF(projectID=dlf_project_id,
#                         sessionID=dlf_session_id)

conDB = conn.connectDB(host=db_host,
                       username=db_user,
                       password=db_pw,
                       database=db_name)

qy = qr.queryDB(conDB.getConnection())

dis_data = ['มีอารมณ์ซึมเศร้า','มีอารมณ์หงุดหงิด','มีอารมณ์ก้าวร้าว','ขาดความสนใจสิ่งรอบข้าง','ไม่ค่อยมีสมาธิเวลาทำสิ่งต่างๆ','รู้สึกอ่อนเพลีย','ทำอะไรก็เชื่องช้า','่รับประทานอาหารมากขึ้น','รับประทานน้อยลง','นอนมากขึ้น','นอนน้อยลง','ตำหนิตัวเองเป็นอันดับแรกถ้ามีอะไรพลาด','พยายามฆ่าตัวตาย']


print(dis_data)

for dis in dis_data :
    query = 'INSERT INTO fact_data(fact_name) VALUES (\'{}\')'.format(dis)
    