from flask_app import flask_app, db
from flask_app.models import Nat_avg,School_details, Zip_to_latlong, Wiki_summary, Message

z = db.session.query(Zip_to_latlong).filter_by(zip_code="00602").first()
print z.id, z.lat_, z.long_

w = db.session.query(Wiki_summary).filter_by(id=5).first()
print w.inst_nm, w.wiki_summary, w.date_extracted, w.wiki_url

n = db.session.query(Nat_avg).filter_by(CCBASIC=24).first()
print n.NPT4_COMB, n.RET_FT4_COMB, n.PFTFTUG1_EF

s = db.session.query(School_details).filter_by(id=5).first()
print s.r_fin_NPT4_COMB, s.r_fin_RET_FT4_COMB, s.r_fin_PFTFTUG1_EF


message_list = db.session.query(Message).all()

for msg in message_list:
    print msg.id, msg.body, msg.email, msg.timestamp
