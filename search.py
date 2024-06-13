#This program is just for drafting potential functions we can use for our main program found in main.py

# Import sqlite3 to connect to the library
import sqlite3

# Connect to database file and save connection to a variable
conn = sqlite3.connect("./movies_internal.db")

# Create a cursor for python to 'type' commands into
cursor = conn.cursor()

#start creating define statements that execute different querries

def get_movie_by_genre():
   user_genre = input("Which genre would you like to search for?\n> ")
   available_genres = ["romance", "comedy", "romance"]
   cursor.execute("SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year, id FROM movies WHERE genre = ?", (user_genre, ))
   # this query does not convert the user input into a string but rather an sql query
   movie_info = cursor.fetchall()
   print()
   print()
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")


def get_movie_info_by_title():
   user_title = input("Which movie would you like to search for? Enter the number of the movie (1-30):\n> ").strip()
   #to make sure that the user has inputted the correct expected input, we will use a while loop to ask them if they entered an unexpected input. 
   available_movies = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
   while user_title not in available_movies:
      print("Sorry, I don't recognise that. Please enter numbers that are inside the range of 1 and 30.")
      print()
      user_title = input("Which movie would you like to search for? (1-30):\n> ")

   if user_title == "1":                        # instead of doing all of this, rather get the sql querry for 
      option = "Titanic"
   elif user_title == "2":
      option = "The Greatest Showman"
   elif user_title == "3":
      option = "Jurassic World"
   elif user_title == "4":
      option = "Avatar: The Way Of Water"
   elif user_title == "5":
      option = "Avatar"
   elif user_title == "6":
      option = "The Shallows"
   elif user_title == "7":
      option = "The Amazing Spider-Man"
   elif user_title == "8":
      option = "Mamma Mia"
   elif user_title == "9":
      option = "Coraline"
   elif user_title == "10":
      option = "Wonka"
   elif user_title == "11":
      option = "Mary Poppins Returns"
   elif user_title == "12":
      option = "The Notebook"
   elif user_title == "13":
      option = "Pride and Prejudice"
   elif user_title == "14":
      option = "The Conjouring"
   elif user_title == "15":
      option = "Red Notice"
   elif user_title == "16":
      option = "The Truman Show"
   elif user_title == "17":
      option = "Stardust"
   elif user_title == "18":
      option = "Maleficent"
   elif user_title == "19":
      option = "Twilight"
   elif user_title == "20":
      option = "Moana"
   elif user_title == "21":
      option = "the Princess Diaries"
   elif user_title == "22":
      option = "Elf"
   elif user_title == "23":
      option = "Legally Blonde"
   elif user_title == "24":
      option = "Ratatouille"
   elif user_title == "25":
      option = "Mr. Bean's Holiday"
   elif user_title == "26":
      option = "IT"
   elif user_title == "27":
      option = "Jaws"
   elif user_title == "28":
      option = "Toy Story"
   elif user_title == "29":
      option = "Home Alone"
   elif user_title == "30":
      option = "Clueless"
   print()
   print()
   cursor.execute("SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE title = ?", (option, ))
   movie_info = cursor.fetchall()
   for index, movie in enumerate(movie_info):
      print(f"\"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")
 


# Delete these two functions and save it for next trial - create a more simple version
# Consider user's input (preferance?)
def movies_with_duration_less_than_2_hours():
   cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE duration < {120} ")
   #we can potentially feed it a bunch of data types and store it anyway - input validation 
   #fix this to get the user to input a duration instead. 
   movie_info = cursor.fetchall()
   print()
   print()
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")



def movies_with_duration_2_hours_or_more():
   cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE duration >= {120}")
   movie_info = cursor.fetchall()
   print()
   print()
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")


def movies_highest_to_lowest_rating():
   cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies ORDER BY rating DESC;")
   movie_info = cursor.fetchall()
   print()
   print()
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\" \n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")

movies_highest_to_lowest_rating()









def reverting_user_menu():

   accepted_responses = ["a", "b", "c", "d", "e", "f"]
   display_menu_graphic() #make it more appealing
   display_menu()
   if menu_choice == "a":
      get_movie_info_by_title()
   elif menu_choice == "b":
      get_movie_by_genre()
   elif menu_choice == "c":
      movies_with_duration_less_than_2_hours()
   elif menu_choice == "d":
      movies_with_duration_2_hours_or_more()
   elif menu_choice == "e":
      movies_highest_to_lowest_rating()
   elif menu_choice == "f":
      exit_program()
   else:
      print()
      time.sleep(.5)
      print(f"{red}Invalid option.{reset}")
      time.sleep(1)
      print(f"Please select one of the options (a, b, c, d, e, f)")
      print()
      print(f"{purple}a.{reset} Search movie information based on title")
      print()
      time.sleep(.5)
      print(f"{purple}b.{reset} Search movie information based on genre")
      print()
      time.sleep(.25)
      print(f"{purple}c.{reset} Get movie info that run for less than 2 hours")
      print()
      time.sleep(.25)
      print(f"{purple}d.{reset} Get movie info that run for 2 hours or more")
      print()
      time.sleep(.25)
      print(f"{purple}e.{reset} Arranged movies by the audience rating (highest to lowest)")
      print()
      time.sleep(.25)
      print(f"{purple}f.{reset} {yellow}Exit program{reset}")
      print()
      time.sleep(.25)
      menu_choice = input(f"{blue}> {reset}")