#!/usr/bin/env python3

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("find - Delete a movie")
    print("exit - Exit program")
    print()    

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for movie in movie_list:
            row = movie
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")", str(row[2]), row[3])
            i += 1
        print()

def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    price = input("Price: ")
    movie = []
    movie.append(name)
    movie.append(year)
    movie.append(price)
    movie_list.append(movie)
    print(movie[0] + " was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0] + " was deleted.\n")

def find(movie_list):
    movie_year = int(input("Year: "))
    for movie in movie_list:
        if movie[1] == movie_year:
            print(movie[0], "was released in", movie[1], "\n")
def main():
    movie_list = [["Monty Python and the Holy Grail", 1975, "@", 9.95],
                  ["On the Waterfront", 1954, "@", 5.59],
                  ["Cat on a Hot Tin Roof", 1958, "@", 7.95],
                  ["Gone with the wind", 1939, "@", 14.95]]  
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "find":
            find(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()