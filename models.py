def create_classes(db):
    class Covid_tr(db.Model):

        __tablename__ = 'covid_trends'

        id = db.Column(db.Integer, primary_key=True)
        date= db.Column(db.String(64))
        numconf=db.Column(db.Float)
        numtestedtoday=db.Column(db.Float)
        numtoday=db.Column(db.Float)
        numdeathstoday=db.Column(db.Float)
        numactive=db.Column(db.Float)
        CERB=db.Column(db.Float)
        Mask=db.Column(db.Float)
        Bike=db.Column(db.Float)
        Zoom=db.Column(db.Float)
        Patio=db.Column(db.Float)

    class Covid_case (db.Model):

        __tablename__= "canada_covid"
        id = db.Column(db.Integer, primary_key=True)
        prname = db.Column(db.String(64))
        date= db.Column(db.String(64))
        numconf=db.Column(db.Float)
        numdeaths=db.Column(db.Float)
        numtoday=db.Column(db.Float)
        numdeathstoday=db.Column(db.Float)
        numtested=db.Column(db.Float)
        numtestedtoday=db.Column(db.Float)
        numrecover=db.Column(db.Float)
        numrecoveredtoday=db.Column(db.Float)
        numactive=db.Column(db.Float)
        population =db.Column(db.Float)
        latitude = db.Column(db.Float)
        longitude = db.Column(db.Float)
      

      
        def __repr__(self):
            return '<Covid_Vision %r>' % (self.name)
    return Covid_tr, Covid_case
