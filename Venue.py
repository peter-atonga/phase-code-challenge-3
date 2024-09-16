from config import db_connection,db_cursor
class Venue:
    all={}
    def __init__(self,title,city):
        self.title=title
        self.city=city

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS venues (id INTEGER PRIMARY KEY,title TEXT,city TEXT)
            """
        db_cursor.execute(sql)
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS venues;
            """
        db_cursor.execute(sql)
        db_connection.commit()

    def save(self):
        sql="""
            INSERT INTO venues (title,city) VALUES(?,?)
            """
        db_cursor.execute(sql,(self.title,self.city))
        db_connection.commit()
        self.id=db_cursor.lastrowid
        Venue.all[self.id]=self

    def delete(self):
        sql="""
            DELETE FROM venues WHERE id=?
            """
        db_cursor.execute(sql,(self.id,))
        db_connection.commit()
        del Venue.all[self.id]
        self.id=None

    def update(self):
        sql="""
            UPDATE venues SET title=?,city=? WHERE id=?
            """
        db_cursor.execute(sql,(self.title,self.city,self.id))
        db_connection.commit()

    @classmethod
    def create(cls,title,city):
        venue1=cls(title,city)
        venue1.save()
        return venue1
    
    @classmethod
    def instance_from_db(cls,row):
        return cls.all[row[0]]
    
    @classmethod
    def find_by_id(cls,id):
        sql="""
            SELECT * FROM venues WHERE id=?
            """
        row=db_cursor.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row)
    
    @classmethod
    def find_by_name(cls,name):
        sql="""
            SELECT * FROM venues WHERE name=?
            """
        row=db_cursor.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row)
    
    @classmethod
    def get_all(cls):
        sql="""
            SELECT * FROM venues
            """
        rows=db_cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def concerts(self): #a collection of all concerts for a specific venue
        from concert import Concert
        sql="""
            SELECT * FROM concerts WHERE venue=?
            """
        rows=db_cursor.execute(sql,(self.city,)).fetchall()
        return [Concert.instance_from_db(row) for row in rows]

    def bands(self):# a collection of all bands who performed at that venue
        from concert import Concert
        sql="""
            SELECT * FROM concerts WHERE venue=?
            """
        rows=db_cursor.execute(sql,(self.city,)).fetchall()
        return [Concert.instance_from_db(row).band() for row in rows]
    
    def concert_on(self,date):
        from concert import Concert
        sql="""
            SELECT * FROM concerts WHERE date=? AND venue=?
            """
        row=db_cursor.execute(sql,(date,self.city)).fetchone()
        return Concert.instance_from_db(row) if row else None
    
    def most_frequent_band(self):
        from concert import Concert
        sql="""
            SELECT band , COUNT(*) FROM concerts WHERE venue=? GROUP BY band 
            """
        rows=db_cursor.execute(sql,(self.city,)).fetchall()
        row1=sorted(rows,key=lambda item:item[1])
        return row1[-1][0]