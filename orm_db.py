"""
bu bölümde orm yapısı kullanılarak db iş ve işlemleri gerçekleştirilmektedir.
tablo tanımları vb işlmler

"""
# from sqlalchemy import Column, ForeignKey, Integer, String # yerine * da olabilirdi
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *  #tablolar arası ilişki kurmak için
from sqlalchemy import *
from datetime import datetime

Base = declarative_base()


# Yönetim işlemleri için db orm yapısı
class Yonetim(Base):
    #tablo adı
    __tablename__ = 'yonetim'
    #tablo sutunları ve özellikleri varsa da ilişkileri
    yonetici_id = Column(Integer, unique= True, primary_key=True, autoincrement=True)
    yonetici_adi = Column(String(10), nullable=False)
    yonetici_tc = Column(String(11), unique=True)
    yonetici_sifre = Column(String(10), nullable=False)
    yonetici_durum = Column(Integer, default=1)

# eğitmen ile ilgili orm için nesne yapısı
class Egitmen(Base):
    __tablename__ = 'egitmen'

    egitmen_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    egitmen_adi_soyadi = Column(String(100))
    egitmen_tc = Column(String(100), unique=True)
    egitmen_sifre = Column(String(100))
    egitmen_tel = Column(String(15))
    egitmen_adres = Column(String(500))
    egitmen_durum = Column(Integer, default=1)

# antreman için gerekli orm yapısı
class Antrenman(Base):
    __tablename__ = 'antrenman'

    antrenman_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    antrenman_adi = Column(String(40))
    egitmen_id = Column(Integer,ForeignKey('egitmen.egitmen_id'))
    egitmenid = relationship(Egitmen,foreign_keys=[egitmen_id])
    antrenman_durum = Column(Integer, default=0)
    antrenman_icerigi = Column(String(1000))


# Üye işlemleri için db orm yapısı
class Uye(Base):
    __tablename__ = 'uye'

    uye_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    uye_adi_soyadi = Column(String(40))
    uye_tc = Column(String(11), unique=True)
    uye_sifre = Column(String(8))
    uye_tel = Column(String(10))
    uye_adres = Column(String(100))
    uye_notu = Column(String(500))
    egitmen_id = Column(Integer,ForeignKey("egitmen.egitmen_id"))
    egitmenid = relationship(Egitmen,foreign_keys=[egitmen_id])
    antrenman_id = Column(Integer,ForeignKey("antrenman.antrenman_id"))
    antrenmanid = relationship(Antrenman,foreign_keys=[antrenman_id])
    ozel_antrenman = Column(String(500))
    uye_tarihi = Column(String(15))
    uye_kalan = Column(Integer)
    uye_durum = Column(Integer, default=1)


class Randevu(Base):
    __tablename__ = 'randevu'

    randevu_id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    egitmen_id = Column(Integer, ForeignKey("egitmen.egitmen_id"))
    egitmenid = relationship(Egitmen, foreign_keys=[egitmen_id])

    randevu_saat1=Column(Integer, ForeignKey("uye.uye_id"),default=0)
    randevuuye1 = relationship(Uye, foreign_keys=[randevu_saat1])

    randevu_saat2=Column(Integer, ForeignKey("uye.uye_id"),default=0)
    randevuuye2 = relationship(Uye, foreign_keys=[randevu_saat2])

    randevu_saat3=Column(Integer, ForeignKey("uye.uye_id"),default=0)
    randevuuye3 = relationship(Uye, foreign_keys=[randevu_saat3])

    randevu_saat4=Column(Integer, ForeignKey("uye.uye_id"),default=0)
    randevuuye4 = relationship(Uye, foreign_keys=[randevu_saat4])

    randevu_saat5=Column(Integer, ForeignKey("uye.uye_id"),default=0)
    randevuuye5 = relationship(Uye, foreign_keys=[randevu_saat5])

    randevu_saat6=Column(Integer, ForeignKey("uye.uye_id"),default=0)
    randevuuye6 = relationship(Uye, foreign_keys=[randevu_saat6])

    randevu_saat7=Column(Integer, ForeignKey("uye.uye_id"),default=0)
    randevuuye7= relationship(Uye, foreign_keys=[randevu_saat7])

    randevu_saat8=Column(Integer, ForeignKey("uye.uye_id"),default=0)
    randevuuye8= relationship(Uye, foreign_keys=[randevu_saat8])

    randevu_araligi =Column(Integer, default=0)
    randevu_tarihi = Column(DATE)
    randevu_durum = Column(Integer, default=0)



# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///sporsalonu.sqlite',connect_args={"check_same_thread": False})

# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(engine)
