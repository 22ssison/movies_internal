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
   user_title = input("Which movie would you like to search for?\n> ") #.lower 
   query = f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies FROM movies WHERE name = '{user_title}'"
   # this query does not convert the user input into a string but rather an sql query
   

def get_movie_by_genre():
   user_genre = input("Which genre would you like to search for?\n> ") #.lower
   query = f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies FROM movies WHERE name = '{user_genre}'"
   # this query does not convert the user input into a string but rather an sql query

# # Delete these two functions and save it for next trial - create a more simple version
# # Consider user's input (preferance?)
# def movies_with_duration_less_than_2_hours():
#    cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE duration > {120} ")
#    #we can potentially feed it a bunch of data types and store it anyway - input validation 
#    #fix this to get the user to input a duration instead. 

# def movies_with_duration_2_hours_or_more():
#    cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE duration <= {120}")


#make this more user friendly by greating them first and telling them what this program is about. include import time and put emojies (star options) for movies that are a "must watch."
# HEART = chr(9829)
# print(HEART)

# while True:
# include this in second test. So that the user will be able to get asked again and again. 
# make this more user friendly especially for f

# while True:
#    search_option = input("1. Get all movies\n2. Get specific movie title\n3. Get by movie genre\n4. Exit")
#    if search_option == "1": #or search_option == "one":
#       get_all_movies()
#       #structure this better rather than a bunch of tuples. 
#    elif search_option == "2": #or search_option == "two":
#       get_movie_by_title() 
#       #""
#    elif search_option == "3": #or search_option == "tree":
#       get_movie_by_genre()
#       #""
#    elif search_option == "3": #or search_option == "four":
#       break
#       #""
#    else:
#       print("I don't recognise that, please choose option 1, 2, 3 or 4:")



#they can see all movie names, they can see all movies from highest to lowest rated, they can see all movies 
print(Showing:)