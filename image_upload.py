#6D/19090125/ramdon baehaki nur faiz
#6D/19098001/saksono bayu ajie sumantri

import datetime
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
app = Flask(__name__)

app_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///image.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class gambar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80))
    image = db.Column(db.LargeBinary)
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
db.create_all()

@app.route('/upload', methods=['POST'])
def upload():
    dataname = request.form.get('filename')
    dataimage = request.files['image']
    
    if 'image' not in request.files:
        return jsonify({'msg': 'Tidak Boleh Kosong'})

    elif dataname and dataimage:
        data = gambar(filename=dataname, image=dataimage.read())
        db.session.add(data)
        db.session.commit()
        return jsonify({'msg': 'Upload Berhasil'})
    else:
        return jsonify({'msg': 'Upload Gagal'})
    
if __name__ == "__main__":
    app.run(debug=True)
