# Reading Cinemas Program - Movies Internal

# Import sqlite3 to connect to the library
import sqlite3

#for delays in the code
import time
 
# Connect to database file and save connection to a variable
conn = sqlite3.connect("./movies_internal.db")

# Create a cursor for python to 'type' commands into
cursor = conn.cursor()

# codes for colouring strings
red = '\033[91m'
purple = '\033[95m'
yellow = '\033[93m'
blue = '\033[94m'
reset = '\033[0m'             #Reset to default colour

# Cool menu graphic - in courtesy of Mincetagram 
menu_graphic = R"""
_ __ ___   ___ _ __  _   _ 
| '_ ` _ \ / _ \ '_ \| | | |
| | | | | |  __/ | | | |_| |
|_| |_| |_|\___|_| |_|\__,_|"""


#start creating define statements that execute different querries

# Lists all the available movies in the cinema.
def show_all_available_movies():
   cursor.execute("SELECT id, title FROM movies;") 
   #save the result to a variable.
   movies = cursor.fetchall()
   #list of tuples
   print()
   print()
   time.sleep(.5)
   print(f"---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}")
   time.sleep(1)
   print("Bellow are the available movies showing in our cinema...")
   time.sleep(1.5)
   print(f"{red}Note: \"Must watch\" movies are starred.{reset}")
   time.sleep(1.5)
   for movie in movies:
      if movie[1] == "Titanic" or movie[1] == "Jurassic World" or movie[1] == "Avatar" or movie[1] == "Mamma Mia" or movie[1] == "The Conjuring" or movie[1] == "Ratatouille" or movie[1] == "Jaws" or movie[1] == "Toy Story" or movie[1] == "The Notebook" or movie[1] == "Twilight" or movie[1] == "Home Alone":
         print()
         time.sleep(.25)
         print(f"{movie[0]}: {movie[1]} ⭐️")
      else:
         print()
         time.sleep(.25)
         print(f"{movie[0]}: {movie[1]}")

#narrow down the different movies according to the user's preferance

# search by genre
def get_movie_by_genre():
   #I put all the available genres inside a list to make this program more robust and user friendly
   genre_list = ["Romance", "Musical", "Action", "Science Fiction", "Thriller", "Fantasy", "Horror" ]
   #print out all available genres so the user has something to choose from and showwhat is available.
   print()
   print(f"---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}")
   for index, genre in enumerate(genre_list):
      print(f"{index + 1}) {genre}\n")

   available_genres = ["1", "2", "3", "4", "5", "6", "7"]
   #ask the user
   user_genre = input(f"Which genre would you like to search for? Enter the number of the genre (1-7):\n{blue}> {reset}").strip()    #to make program more robust incase of a typo
   while user_genre not in available_genres:
      print()
      print("Sorry, I don't recognise that. Please enter numbers that are inside the range of 1 and 7.")
      print()
      user_genre = input(f"Which movie would you like to search for? (1-7):\n{blue}> {reset}").strip()

   if user_genre == "1":                      
      option = "Romance"
   elif user_genre == "2":
      option = "Musical"
   elif user_genre == "3":
      option = "Action"
   elif user_genre == "4":
      option = "Science Fiction"
   elif user_genre == "5":
      option = "Thriller"
   elif user_genre == "6":
      option = "Fantasy"
   elif user_genre == "7":
      option = "Horror"
   cursor.execute("SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year, id FROM movies WHERE genre = ?", (option, ))
   # this query is in this set up because it is quite tentative to get the user to type in the movie title as they would have to spell the movie title very accurately for this query to work.
   movie_info = cursor.fetchall()
   print()            #spaces to make the output look neater
   print()
   print(f"You selected the genre \"{option}\"")
   print()
   print(f"Here are the following movies for this genre...")   
   print()
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}\n\n")


# option for the user to search for something specific. 
def get_movie_info_by_title():
   print()
   time.sleep(1)
   print(f"---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}")
   user_title = input(f"Which movie would you like to search for? Enter the number of the movie (1-30):\n{blue}> {reset}").strip()
   #to make sure that the user has inputted the correct expected input, we will use a while loop to ask them if they entered an unexpected input. 
   available_movies = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
   while user_title not in available_movies:
      print("Sorry, I don't recognise that. Please enter numbers that are inside the range of 1 and 30.")
      print()
      user_title = input(f"Which movie would you like to search for? (1-30):\n{blue}> {reset}").strip()
   print(f"---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}")
   time.sleep(1)
   if user_title == "1":                        # I did it in this specific format because it is better for us and the user, 
      option = "Titanic"                        # given that they need to enter the exact same title because the data is located in the database,
   elif user_title == "2":                      #  so when we want it to fetch this, the sql querry should be correct word per word.
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
   cursor.execute("SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE title = ?", (option, )) #fixed to prevent sql interjections
   movie_info = cursor.fetchall()
   for index, movie in enumerate(movie_info):
      print(f"{red}\"{movie_info[index][0]}\"{reset}")
      print()
      time.sleep(.3)
      print(f"Blurb: {movie_info[index][1]}")
      print()
      time.sleep(.3)
      print(f"Genre: {movie_info[index][2]}")
      print()
      time.sleep(.3)
      print(f"Starring: {movie_info[index][3]}")
      print()
      time.sleep(.3)
      print(f"Duration: {movie_info[index][4]}minutes")
      print()
      time.sleep(.3)
      print(f"Release Year: {movie_info[index][9]}")
      print()
      time.sleep(.3)
      print(f"Directed by: {movie_info[index][5]}")
      print()
      time.sleep(.3)
      print(f"Budget: ${movie_info[index][6]}milion (USD)")
      print()
      time.sleep(.3)
      print(f"Audience Rating: {movie_info[index][8]}/5 stars")
      print()
      time.sleep(.3)
      print(f"Showing in cinema {movie_info[index][7]}")
      print()
      time.sleep(.5)
      print(f"---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}\n\n")
 
def movies_with_duration_less_than_2_hours():
   cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE duration < {120} ")
   movie_info = cursor.fetchall()
   print()
   print()
   print("I guess you're not a fan of long movies. Not a problem!")
   print()
   print("The following movies run for less than 2 hours...")
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}\n\n")


def movies_with_duration_2_hours_or_more():
   cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE duration >= {120}")
   movie_info = cursor.fetchall()
   print()
   print()
   print("Great choice, Long movies are the best!")
   print()
   print("The following movies run for 2 or more hours...")
   print()
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}\n\n")


def movies_highest_to_lowest_rating():
   cursor.execute(f"SELECT title, rating FROM movies ORDER BY rating DESC;")
   movie_info = cursor.fetchall()
   print()
   print()
   print(f"---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}")
   print("Here are all our movies arranged by its audience rating from highest to lowest...")
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\" - {movie_info[index][1]}/5 stars")
      print()
   print()
   print(f"---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}")
   print()

def exit_program():
   print()
   print("I guess you already have a movie in mind.")
   print()
   time.sleep(1)
   print(f"{yellow}Enjoy your movie!{reset}")

   
def reverting_user_menu():
   accepted_responses = ["a", "b", "c", "d", "e", "f"]
   print(red + menu_graphic + reset) #make it more appealing
   #display options
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
   #to make the while loop true, start with an empty string.
   menu_choice = ""

   while menu_choice != "f":
      time.sleep(.25)
      menu_choice = input(f"{blue}> {reset}")
   #conditions
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
         break
      else:    #incase of an unexpected input
         print()
         time.sleep(.25)
         print(f"{red}Invalid option.{reset}")
         print()
         time.sleep(1)
         print(f"Please select one of the options (a, b, c, d, e, f)")




def run_program():
   print()
   print(f"{blue}This program executes a range of data from the movies showing in the cinema.{reset}")
   print()
   accepted_responses = ["y","n","yes","no"]
   time.sleep(1.5)
   run_program_or_exit = input(f"Would you like to use this program?(y/n):\n{blue}> {reset}")
   while run_program_or_exit not in accepted_responses:
      print()
      print("Sorry, I don't recognise that. Enter either yes or no.")
      print()
      time.sleep(1.5)
      run_program_or_exit = input(f"Would you like to use this program?(y/n):\n{blue}> {reset}")

   if run_program_or_exit == "no" or run_program_or_exit == "n":
      print()
      exit_program()
   elif run_program_or_exit == "yes" or run_program_or_exit == "y":
      print()
      print()
      time.sleep(.5)
      print(f"{yellow}great! 😄{reset}")
      show_all_available_movies()
      #Gives the user options to further narrow down their search (to get movie info based on their preferance)
      print()
      time.sleep(1.5)
      print(f"---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset} ---- {blue}----{reset}")
      reverting_user_menu()



run_program()
