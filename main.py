# Import sqlite3 to connect to the library
import sqlite3

# Connect to database file and save connection to a variable
conn = sqlite3.connect("./movies_internal.db")

# Create a cursor for python to 'type' commands into
cursor = conn.cursor()

#start creating define statements to execute different querries
def get_all_movies():
   cursor.execute("SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies;")
   #save the result to a variable.
   movies = cursor.fetchall()
   #list of tuples
   print("movies")
  
def get_movie_by_title():
   user_title = input("Which movie would you like to search for?\n> ")
   query = f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies FROM movies WHERE name = '{user_title}'"
   # this query does not convert the user input into a string but rather an sql query

def get_movie_by_genre ():
   user_genre = input("Which genre would you like to search for?\n> ")
   query = f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies FROM movies WHERE name = '{user_genre}'"
   # this query does not convert the user input into a string but rather an sql query

def movies_with_duration_less_than_90_minutes():
   cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE duration > {int(90)} ")
   #fix this to get the user to input a duration instead. 
   #is this a consice way to structure this? specifically look at the 90