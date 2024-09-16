from config import db_connection,db_cursor
from Band import Band
class Concert:
    all={}

    def __init__(self,date,band1,venue1):
        self.date=date
        self.band1=band1
        self.venue1=venue1
        

    @property
    def band1(self):
        return self._band1
    
    @band1.setter
    def band1(self,band):
        if isinstance(band,Band):
            self._band1=band
        else:
            raise ValueError("Ensure your band is an existing instance of Band class!")
        
    @property
    def venue1(self):
        return self._venue1
    
    @venue1.setter
    def venue1(self,venue1):
        from Venue import Venue
        if isinstance(venue1,Venue):
            self._venue1=venue1
        else:
            raise AttributeError("Ensure your venue is an existing instance of Venue class!")
        
    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTs concerts (id INTEGER PRIMARY KEY,date TEXT,band TEXT,venue TEXT);
            """
        db_cursor.execute(sql)
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS concerts;
            """
        db_cursor.execute(sql)
        db_connection.commit()

    def save(self):
        sql="""
            INSERT INTO concerts(date,band,venue) VALUES(?,?,?)
            """
        db_cursor.execute(sql,(self.date,self.band1.name,self.venue1.city))
        db_connection.commit()

        self.id=db_cursor.lastrowid
        Concert.all[self.id]=self

    def update(self):
        sql="""
            UPDATE concerts SET date=?, band=?,venue=? WHERE id=?
            """
        db_cursor.execute(sql,(self.date,self.band,self.venue,self.id))
        db_connection.commit()

    def delete(self):
        sql="""
            DELETE FROM concerts WHERE id=?
            """
        db_cursor.execute(sql,(self.id,))
        db_connection.commit()
        del Concert.all[self.id]
        self.id=None

    @classmethod
    def create(cls,date,band,venue):
        concert_0=cls(date,band,venue)
        concert_0.save()
        return concert_0
    
    @classmethod
    def instance_from_db(cls,row):
        return cls.all[row[0]]
    
    @classmethod
    def find_by_id(cls,id):
        sql="""
            SELECT * FROM concerts WHERE id=?
            """
        row=db_cursor.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row)
    
    # @classmethod
    # def find_by_name(cls,name):
    #     sql="""
    #         SELECT * FROM concerts WHERE name=?
    #         """
    #     row=db_cursor.execute(sql).fetchone()
    #     return cls.instance_from_db(row)
    
    @classmethod
    def get_all(cls):
        sql="""
            SELECT * FROM concerts
            """
        rows=db_cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def band(self):
        return self.band1
    
    def venue(self):
        return self.venue1
    
    def hometown_show(self):
        sql="""
            SELECT * FROM concerts INNER JOIN bands ON concerts.venue=bands.hometown
            """
        rows=db_cursor.execute(sql).fetchall()
        return self in [Concert.instance_from_db(row) for row in rows]
    
    def introduction(self):
        return f"Hello {self.venue().city}!!!!! We are {self.band().name} and we're from {self.band().hometown}"