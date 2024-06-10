# Import sqlite3 to connect to the library
import sqlite3

# Connect to database file and save connection to a variable
conn = sqlite3.connect("./movies_internal.db")

# Create a cursor for python to 'type' commands into
cursor = conn.cursor()

#start creating define statements that execute different querries


# To show the user the list of different movies that is available.
def get_all_movie_titles():
   cursor.execute("SELECT id, title FROM movies;") #WHERE id > {11}; make pages have only 10 movies on each page. ask the user if they want to continue or not if they found a movie that they want to watch. 
   #save the result to a variable.
   movies = cursor.fetchall()
   #list of tuples
   for movie in movies:
      print()
      print(f"{movie[0]}: {movie[1]}")
      # print(movie)
   

def get_movie_by_genre():
   user_genre = input("Which genre would you like to search for?\n> ")
   cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year, id FROM movies WHERE genre = '{user_genre}'")
   # this query does not convert the user input into a string but rather an sql query
   movie_info = cursor.fetchall()
   print()
   print()
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")




# # print("This program will give you information about different movies that is showing in our cinema.")
# # print()
# # print()
# # print("Here is a list of all the movies showing:")
# # get_all_movie_titles()

# # choice = input("Would you like to:\n1. Get movie information by title\n2. Get movie information by genre\n3. Get movie information for movies that run less than 2 hours\n4. Get movie information for movies that run for 2 hours or more")
# # # if choice == 1:
   
get_movie_by_genre()