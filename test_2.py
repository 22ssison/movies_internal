# Import sqlite3 to connect to the library
import sqlite3

# Connect to database file and save connection to a variable
conn = sqlite3.connect("./movies_internal.db")

# Create a cursor for python to 'type' commands into
cursor = conn.cursor()

#start creating define statements that execute different querries

# this block shows all the available movies in the database
def show_all_available_movies():
   cursor.execute("SELECT id, title FROM movies;") 
   #save the result to a variable.
   movies = cursor.fetchall()
   #list of tuples
   print()
   print()
   print("---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----")
   print("Bellow are the available movies showing in our cinema...")
   for movie in movies:
      print()
      print(f"{movie[0]}: {movie[1]}")

#narrow down the different movies according to the user's preferance
def get_movie_by_genre():
   #I put all the available genres inside a list to make this program more robust and user friendly
   genre_list = ["Romance", "Musical", "Action", "Science Fiction", "Thriller", "Fantasy", "Horror" ]
   #print out all available genres so the user has something to choose from and showwhat is available.
   print()
   print("---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----")
   for index, genre in enumerate(genre_list):
      print(f"{index + 1}) {genre}\n")

   available_genres = ["1", "2", "3", "4", "5", "6", "7"]
   #ask the user
   user_genre = input("Which genre would you like to search for? Enter the number of the genre (1-7):\n> ").strip()    #to make program more robust incase of a typo
   while user_genre not in available_genres:
      print()
      print("Sorry, I don't recognise that. Please enter numbers that are inside the range of 1 and 7.")
      print()
      user_genre = input("Which movie would you like to search for? (1-7):\n> ").strip()

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
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")


# option for the user to search for something specific. 
def get_movie_info_by_title():
   print()
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
   cursor.execute("SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE title = ?", (option, )) #fixed to prevent sql interjections
   movie_info = cursor.fetchall()
   for index, movie in enumerate(movie_info):
      print(f"\"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n")
 
def movies_with_duration_less_than_2_hours():
   cursor.execute(f"SELECT title, blurb, genre, actor, duration, director, budget, cinema, rating, year FROM movies WHERE duration < {120} ")
   #we can potentially feed it a bunch of data types and store it anyway - input validation 
   #fix this to get the user to input a duration instead. 
   movie_info = cursor.fetchall()
   print()
   print()
   print("I guess you're not a fan of long movies. Not a problem!")
   print()
   print("The following movies run for less than 2 hours...")
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")


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
      print(f"{index +1}) \"{movie_info[index][0]}\"\n\nBlurb: {movie_info[index][1]}\n\n\nGenre: {movie_info[index][2]}\n\nStarring: {movie_info[index][3]}\n\nDuration: {movie_info[index][4]}minutes\n\nRelease Year: {movie_info[index][9]}\n\nDirected by: {movie_info[index][5]}\n\nBudget: ${movie_info[index][6]}milion (USD)\n\nAudience Rating: {movie_info[index][8]}/5 stars\n\nShowing in cinema {movie_info[index][7]}\n\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----\n\n")


def movies_highest_to_lowest_rating():
   cursor.execute(f"SELECT title, rating FROM movies ORDER BY rating DESC;")
   movie_info = cursor.fetchall()
   print()
   print()
   print("---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----")
   print("Here are all our movies arranged by its audience rating from highest to lowest...")
   print()
   for index, movie in enumerate(movie_info):
      print(f"{index +1}) \"{movie_info[index][0]}\" - {movie_info[index][1]}/5 stars")
      print()

def exit_program():
   print()
   print("I guess you already have a movie in mind.\nEnjoy your movie!")

def start_of_program():
   print("This program executes a range of data from the movies showing in the cinema.")
   print()
   accepted_responses = ["y","n","yes","no"]
   run_program_or_exit = input("Would you like to use this program?(y/n):\n> ")
   while run_program_or_exit not in accepted_responses:
      print()
      print("Sorry, I don't recognise that. Enter either yes or no.")
      print()
      run_program_or_exit = input("Would you like to use this program?(y/n):\n> ")
   if run_program_or_exit == "no" or run_program_or_exit == "n":
      print()
      print("It seems like you already have a film in mind. Enjoy the movie!")
   elif run_program_or_exit == "yes" or run_program_or_exit == "y":
      print()
      print("great!")
      show_all_available_movies()
      #Gives the user options to further narrow down their search (to get movie info based on their preferance)
      print()
      print("---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----")

def narrow_down_user_search():
   print("Would you like to:")
   print()
   accepted_responses = ["1", "2", "3", "4", "5", "6"]
   choice = input("1. Search movie information based on title\n\n2. Search movie information based on genre\n\n3. Get movie info that run for less than 2 hours\n\n4. Get movie info that run for 2 hours or more\n\n5. Arranged movies by the audience rating (highest to lowest)\n\n6. Exit program\n> ")
   #call funcitons depending on the user's choice. 
   if choice == "1":
      get_movie_info_by_title()
   elif choice == "2":
      get_movie_by_genre()
   elif choice == "3":
      movies_with_duration_less_than_2_hours()
   elif choice == "4":
      movies_with_duration_2_hours_or_more()
   elif choice == "5":
      movies_highest_to_lowest_rating()
   elif choice == "6":
      exit_program()
   else:
      print("Invalid option. Please select one of the options (1, 2, 3, 4, 5, 6)")
      print()
      choice = input("1. Search movie information based on title\n2. Search movie information based on genre\n3. Get movie info that run for less than 2 hours\n4. Get movie info that run for 2 hours or more\n5. Get movie info arranged by the audience rating (highest to lowest)\n6. Exit program\n> ")

start_of_program()
narrow_down_user_search()