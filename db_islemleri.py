from orm_db import *
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def yonetici_girisi(yonetici_tc,yonetici_sifre):
    try:
        ygirisi = session.query(Yonetim).filter(Yonetim.yonetici_tc==yonetici_tc, Yonetim.yonetici_sifre==yonetici_sifre).first()
        if ygirisi.yonetici_durum == 0:
            return True
        else:
            return False
    except:
        return False