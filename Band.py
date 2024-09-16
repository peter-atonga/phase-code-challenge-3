from config import db_connection,db_cursor
class Band:
    all={}
    def __init__(self,name,hometown) -> None:
        self.name=name
        self.hometown=hometown

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS bands(id INTEGER PRIMARY KEY,name TEXT,hometown TEXT)
            """
        db_cursor.execute(sql)
        db_connection.commit()

    @classmethod
    def drop_table(cls):
        sql="""
            DROP TABLE IF EXISTS bands;
            """
        db_cursor.execute(sql)
        db_connection.commit()

    def save(self):
        sql="""
            INSERT INTO bands (name,hometown) VALUES(?,?)
            """
        db_cursor.execute(sql,(self.name,self.hometown))
        db_connection.commit()

        self.id=db_cursor.lastrowid
        Band.all[self.id]=self

    def delete(self):
        sql="""
            DELETE FROM bands WHERE name=?
            """
        db_cursor.execute(sql,(self.name,))
        db_connection.commit()

        #delete from th dictionary
        del Band.all[self.id]
        self.id=None

    def update(self):
        sql="""
            UPDATE bands SET name=?,hometown=? where id=?
            """
        db_cursor.execute(sql,(self.name,self.hometown,self.id))
        db_connection.commit()

    @classmethod
    def create(cls,name,hometown):
        band=cls(name,hometown)
        band.save()
        return band
    
    @classmethod
    def instance_from_db(cls,row):
        band=cls.all[row[0]]
        return band

    @classmethod
    def get_all(cls):
        sql="""
            SELECT * FROM bands
            """
        rows=db_cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls,id):
        sql="""
            SELECT * FROM bands WHERE id=?
            """
        row=db_cursor.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls,name):
        sql="""
            SELECT * FROM bands WHERE name=?
            """
        row=db_cursor.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row)
    
    def concerts(self):
        from concert import Concert
        sql="""
            SELECT * FROM concerts WHERE band=?
            """
        rows=db_cursor.execute(sql,(self.name,))
        return [Concert.instance_from_db(row) for row in rows]
    
    def venues(self):
        from concert import Concert
        sql="""
            SELECT * FROM concerts WHERE band=?
            """
        rows=db_cursor.execute(sql,(self.name,))
        return [Concert.instance_from_db(row).venue() for row in rows]
    
    def play_in_venue(self,venue,date):
        from concert import Concert
        from Venue import Venue
        sql="""
            SELECT * FROM venues WHERE title=?
            """
        rows=db_cursor.execute(sql,(venue,)).fetchone()
        row=Venue.instance_from_db(rows)
        return Concert.create(date,self,row)
    
    def all_introductions(self):
        return [f"Hello {item.venue().city}!!!!! We are {self.name} and we're from {self.hometown}" for item in self.concerts()]
    
    @classmethod
    def most_perfomances(cls):
        sql="""
            SELECT band,COUNT(*) FROM concerts GROUP BY band;
            """
        rows=db_cursor.execute(sql).fetchall()
        rows1=sorted(rows, key=lambda item:item[1])
        return rows1[-1][0]