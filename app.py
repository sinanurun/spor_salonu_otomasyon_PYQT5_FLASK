from flask import *
from orm_db import *


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
dbsession = DBSession()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
kullanici = {}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/kontrol', methods=['POST', 'GET'])
def kontrol():
    try:
        if request.method == 'POST':
            tc_no = request.form.get('tc_no')
            sifre = request.form.get('sifre')

            try:
                egitmen = dbsession.query(Egitmen).filter(Egitmen.egitmen_tc == tc_no,
                                                          Egitmen.egitmen_sifre == sifre).first()
                if egitmen.egitmen_durum == 0:
                    kullanici['egitmen'] = egitmen
                    session['egitmen_id'] = egitmen.egitmen_id
                    return redirect(url_for('egitmen_sayfasi'))

            except:
                try:
                    uye = dbsession.query(Uye).filter(Uye.uye_tc == tc_no,
                                                      Uye.uye_sifre == sifre).first()

                    if uye.uye_durum == 0:
                        kullanici['uye'] = uye
                        session['uye_id'] = uye.uye_id
                        session['uye_adi'] = uye.uye_adi_soyadi
                        return redirect(url_for('uye_sayfasi'))
                except:
                    return redirect(url_for('/'))
    except:
        return redirect(url_for('/'))
    return redirect(url_for('/'))


@app.route('/uye_sayfasi')
def uye_sayfasi():
    if 'uye_id' in session:
        id = session['uye_id']
        antrenman_id = kullanici['uye'].antrenman_id
        egitmen_id = kullanici['uye'].egitmen_id
        uye = dbsession.query(Uye).filter(Uye.uye_id==id).first()
    return render_template("uye_sayfasi.html", uyebilgisi=uye)


@app.route('/egitmen_sayfasi')
def egitmen_sayfasi():
    return render_template("egitmen_sayfasi.html", egitmen_bilgisi=kullanici['egitmen'])


@app.route('/program_ekle')
def program_ekle():
    return render_template("program_ekle.html")


@app.route('/program_ekle_kontrol', methods=['GET', 'POST'])
def program_ekle_kontrol():
    if request.method == 'POST':
        antrenman_adi = request.form.get('antrenman_adi')
        antrenman_icerigi = request.form.get('antrenman_icerigi')
        antrenman_durum = request.form.get('antrenman_durum')
        antrenman_egitmen = kullanici['egitmen'].egitmen_id
        print(antrenman_adi)
        antrenman = Antrenman(antrenman_adi=antrenman_adi,
                              egitmen_id=antrenman_egitmen,
                              antrenman_durum=antrenman_durum,
                              antrenman_icerigi=antrenman_icerigi)
        dbsession.add(antrenman)
        dbsession.commit()
    return render_template("program_ekle.html", mesaj="Başarıyla Antrenman Programınız Eklenmiştir")


@app.route('/uye_antrenman_listesi', methods=['GET', 'POST'])
def uye_antrenman_listesi():
    uye_listesi = dbsession.query(Uye).filter(Uye.egitmen_id == session['egitmen_id']).all()
    return render_template("uye_antrenman_listesi.html", uyeler=uye_listesi)

@app.route('/egitmen_randevu_listesi', methods=['GET', 'POST'])
def egitmen_randevu_listesi():
    randevu_listesi = dbsession.query(Randevu).filter(Randevu.egitmen_id == session['egitmen_id'], Randevu.randevu_durum==0).all()
    return render_template("egitmen_randevu_listesi.html", randevular=randevu_listesi)

@app.route('/uye_randevu_listesi', methods=['GET', 'POST'])
def uye_randevu_listesi():
    randevu_listesi = dbsession.query(Randevu).filter(Randevu.egitmen_id == kullanici['uye'].egitmen_id, Randevu.randevu_durum==0).all()
    return render_template("uye_randevu_listesi.html", uye=kullanici['uye'], randevular=randevu_listesi)

@app.route('/uye_randevu_al/<int:randevu_id>/<int:uye_id>/<int:randevu_zamani>', methods=['GET', 'POST'])
@app.route('/uye_randevu_al', methods=['GET', 'POST'])
def uye_randevu_al(randevu_id=0,uye_id=0,randevu_zamani=0):
    if randevu_zamani == 0:
        randevu_listesi = dbsession.query(Randevu).filter(Randevu.egitmen_id == kullanici['uye'].egitmen_id, Randevu.randevu_durum==0, Randevu.randevu_tarihi>= datetime.date(datetime.utcnow())).all()

        return render_template("uye_randevu_al.html", uye=kullanici['uye'], randevular=randevu_listesi)
    else:
        randevu_zamani={"randevu_saat" + str(randevu_zamani):uye_id}
        dbsession.query(Randevu).filter_by(randevu_id=randevu_id).update(randevu_zamani)
        dbsession.commit()
        return redirect(url_for("uye_randevu_listesi"))

@app.route('/uye_antrenman', methods=['GET', 'POST'])
@app.route('/uye_antrenman/<int:id>', methods=['GET', 'POST'])
def uye_antrenman(id=0):
    if id != 0:
        uye_id = id
        uye = dbsession.query(Uye).filter(Uye.egitmen_id == session['egitmen_id']).first()
        antrenman = dbsession.query(Antrenman).filter(Uye.egitmen_id == session['egitmen_id']).all()
        return render_template("uye_antrenman.html", uye_bilgileri=uye,antrenman_bilgileri=antrenman)
    else:
        uye_id = request.form.get('uye_id')
        antrenman_id = request.form.get('antrenman_id')
        ozel_antrenman = request.form.get('ozel_antrenman')
        dbsession.query(Uye).filter(Uye.uye_id == uye_id).update({
            Uye.antrenman_id: antrenman_id, Uye.ozel_antrenman : ozel_antrenman })
        dbsession.commit()
        return redirect("uye_antrenman/"+str(uye_id))


@app.route('/antrenman_sil/<int:id>')
def antrenman_sil(id):
    antrenman_id = id
    dbsession.query(Antrenman).filter(Antrenman.antrenman_id == antrenman_id).delete()
    dbsession.commit()
    return redirect(url_for('program_guncelle_sil'))

@app.route('/antrenman_guncelle', methods=['GET', 'POST'])
@app.route('/antrenman_guncelle/<int:id>', methods=['GET', 'POST'])
def antrenman_guncelle(id=0):
    if id != 0:
        antrenman_id = id
        antrenman = dbsession.query(Antrenman).filter(Antrenman.antrenman_id == antrenman_id,
                                                      Antrenman.egitmen_id==session['egitmen_id']).first()
        return render_template("antrenman_guncelle.html", antrenmanlar=antrenman)
    else:
        antrenman_id = request.form.get('antrenman_id')
        antrenman_adi = request.form.get('antrenman_adi')
        antrenman_icerigi = request.form.get('antrenman_icerigi')
        antrenman_durum = request.form.get('antrenman_durum')
        dbsession.query(Antrenman).filter(Antrenman.antrenman_id == antrenman_id).update({
            Antrenman.antrenman_adi: antrenman_adi,Antrenman.antrenman_icerigi: antrenman_icerigi,
            Antrenman.antrenman_durum: antrenman_durum
        })
        dbsession.commit()
        antrenman = dbsession.query(Antrenman).filter(Antrenman.egitmen_id==session['egitmen_id']).all()
        return render_template("program_guncelle_sil.html", antrenmanlar=antrenman)


@app.route('/program_guncelle_sil', methods=['GET', 'POST'])
def program_guncelle_sil():
    if request.method == 'POST':
        antrenman_adi = request.form.get('antrenman_adi')
        antrenman_icerigi = request.form.get('antrenman_icerigi')
        antrenman_durum = request.form.get('antrenman_durum')
        antrenman_egitmen = kullanici['egitmen'].egitmen_id
        antrenman = Antrenman(antrenman_adi=antrenman_adi,
                              egitmen_id=antrenman_egitmen,
                              antrenman_durum=antrenman_durum,
                              antrenman_icerigi=antrenman_icerigi)
        dbsession.add(antrenman)
        dbsession.commit()
    else:
        antrenman = dbsession.query(Antrenman).filter(Antrenman.egitmen_id==session['egitmen_id']).all()

    return render_template("program_guncelle_sil.html", antrenmanlar=antrenman)


if __name__ == '__main__':
    app.run(debug=True)
