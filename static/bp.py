from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
bp=SQLAlchemy()

class Zaposlenik(bp.Model):
    __tablename__="Zaposlenik"

    id=bp.Column(bp.Integer, primary_key=True)
    ime= bp.Column(bp.String(100),nullable=False)
    prezime=bp.Column(bp.String(100),nullable=False)
    datumrodenja= bp.Column(bp.Date,nullable=False)
    spol=bp.Column(bp.String(100),nullable=False)
    kontakt=bp.Column(bp.String(100),nullable=False)
    odjel=bp.Column(bp.String(100),nullable=False)
    titula= bp.Column(bp.String(100),nullable=False)
    datumzaposlenja=bp.Column(bp.Date,nullable=False)
    datumupisa=bp.Column(bp.DateTime)

    def __init__(self,ime,prezime,datumrodenja,spol, kontakt,odjel,titula,datumzaposlenja,datumupisa):
        self.ime= ime
        self.prezime = prezime
        self.datumrodenja = datumrodenja
        self.spol= spol
        self.kontakt=kontakt
        self.odjel=odjel
        self.titula= titula
        self.datumzaposlenja=datumzaposlenja
        self.datumupisa=datumupisa