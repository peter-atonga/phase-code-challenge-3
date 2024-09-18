                                Mock Code Challenge - Concerts - Compulsory
            
            Submitting a website url

        For this assignment, we'll be working with a Concert domain.

                        We have three tables: 
        Band (name and hometown), Venue (title and city), and Concert.

        For our purposes, a Band has many concerts, a Venue has many concerts, and a Concert belongs to a band and to a venue. Band-Venue is a many-to-many relationship.

        Note: You should sketch your domain on paper or on a whiteboard before starting to code.

                                Important:

        You will not be using SQLAlchemy for this challenge. Instead, use raw SQL queries. Write SQL queries directly in your Python methods to perform the necessary operations on the database.

                            What You Should Have:
            Your schema should look like this:

                                        bands Table:
                                        Column	Type
                                        name	String
                                        hometown	String
                                        venues Table:
                                        Column	Type
                                        title	String
                                        city	String
        You will need to create the schema for the concerts table, using the attributes specified in the deliverables below. You will also need to create the migrations for the above tables, following the same structure.

                        Deliverables
        You will be writing methods that execute raw SQL queries to interact with your database. Use Python’s sqlite3 or psycopg2 library to run SQL commands.

        Make sure to set up your database and tables using raw SQL commands before working on the deliverables.

                        Migrations
        Before working on these deliverables, you need to create migrations for the concerts table. This is assuming you have already created and migrated the band and venues tables.

        A Concert belongs to a Band and a Venue. In your migration, create any columns your concerts table will need to establish these relationships.

                        The concerts table should also have:

        A date column that stores a string.
        After creating the concerts table, use raw SQL to create instances of your data so you can test your code.

        Object Relationship Methods
    For the following methods, write SQL queries to retrieve the necessary data from the database.

                                Concert

        Concert.band(): should return the Band instance for this concert.
        Concert.venue(): should return the Venue instance for this concert.

                            Venue

Venue.concerts(): returns a collection of all concerts for the venue.
Venue.bands(): returns a collection of all bands who performed at the venue.

                            Band

Band.concerts(): should return a collection of all concerts the band has played.
Band.venues(): should return a collection of all venues the band has performed at.
Aggregate and Relationship Methods

                            Concert

Concert.hometown_show(): returns true if the concert is in the band's hometown, false if it is not. Use SQL joins to compare the band's hometown with the concert's venue city.
Concert.introduction(): returns a string with the band's introduction for this concert:
"Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"

                            Band

Band.play_in_venue(venue, date): takes a venue (venue title) and date (as a string) as arguments, and creates a new concert for the band at that venue on that date. Insert the concert using raw SQL.
Band.all_introductions(): returns an array of strings representing all the introductions for this band.
Each introduction is in the form: "Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"
Band.most_performances(): returns the Band that has played the most concerts. Use SQL GROUP BY and COUNT to identify the band with the most concerts.

                            Venue

Venue.concert_on(date): takes a date (string) as an argument and finds the first concert on that date at the venue.
Venue.most_frequent_band(): returns the band that has performed the most at the venue. You will need to count how many times each band has performed at this venue using a SQL GROUP BY query.

                            Guidelines
                            
Use raw SQL exclusively for all queries.
Utilize JOINs, GROUP BY, and COUNT operations where appropriate.
You can use Python's database connection libraries (e.g., sqlite3 or psycopg2) to execute SQL queries in your methods.
