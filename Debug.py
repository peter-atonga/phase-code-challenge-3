from config import db_connection,db_cursor
from Venue import Venue
from concert import Concert
from Band import Band

def run():
    Band.drop_table()
    Band.create_table()
    Venue.drop_table()
    Venue.create_table()
    Concert.drop_table()
    Concert.create_table()
    
    band1=Band.create("Rose","Sindo")
    band2=Band.create("Karanja","Kisumu")
    venue1=Venue.create("Kicc","Nairobi")
    venue2=Venue.create("Impala","Kisumu")
    concert1=Concert.create("2020",band1,venue2)
    concert2=Concert.create("2021",band2,venue1)
    concert3=Concert.create("2021",band2,venue1)
    concert4=Concert.create("2020",band2,venue2)
    band1.play_in_venue("Kicc","2025") 
    print(venue2.most_frequent_band())   
    print(band1.all_introductions()) 
  
run()
