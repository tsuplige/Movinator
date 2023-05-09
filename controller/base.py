from typing import List
from model.movie import Movie
import json
import os
import random

if os.path.exists("data") and os.path.isdir("data"):
    pass
else:
    os.makedirs('data')

class Controller:

    def __init__(self, view):
        
        self.movie_list: List[Movie] = []
        self.more_movie = True
        self.view = view
        # if os.path.exists("data/movies.json"):
        #     with open('data/movies.json', 'r') as f:
        #         datas = f.read()
        #         for data in json.loads(datas):
        #             self.movie_list.append(Movie(data["name"], data["realisateur"], data["year"], data["resume"], data["watch"]))

    def launch(self):
        self.load_data()
        self.main_menu()
        self.save_movie_data()

    def main_menu(self):

        menu_input = self.view.main_menu_prompt()

        if menu_input == '1':
            self.add_movie_to_list()
        elif menu_input == '2':
            ask_to_continue = self.view.show_movie_list_prompt(self.movie_list)
            self.main_menu()
        elif menu_input == '3':
            self.choose_movie()
            self.main_menu()
        elif menu_input == '4':
            return
        else:
            self.main_menu()

    def add_movie_to_list(self):
        if self.more_movie == False:
            self.more_movie = True
        while self.more_movie == True:
            
            name, realisateur, year, resume = self.view.add_movie_to_list_list_prompt()

            self.movie_list.append(Movie(name, realisateur, year, resume))
            
            ask_to_continue = input(self.view.question_color("voulez vous ajouter d'autre joueur ? \n o pour oui\n n pour non\n"))
            if ask_to_continue == "o" or ask_to_continue == "O":
                self.more_movie = True
            elif ask_to_continue == "n" or ask_to_continue == "N":
                self.more_movie = False

        self.save_movie_data()
        self.main_menu()

    def save_movie_data(self):
        movie_data = []
        for movie in self.movie_list:
            data = movie.convert_to_json_data()
            movie_data.append(data)
        
        with open('data/movies.json', 'w') as f:
            json.dump(movie_data, f)
    
    def load_data(self):
         if os.path.exists("data/movies.json"):
            with open('data/movies.json', 'r') as f:
                datas = f.read()
                for data in json.loads(datas):
                    self.movie_list.append(Movie(data["name"], data["realisateur"], data["year"], data["resume"], data["watch"]))

    def choose_movie(self):

        random_movie = random.choice(self.movie_list)

        while random_movie.watch == True:
            random_movie = random.choice(self.movie_list)

        self.view.print_movie_randomly_choose(random_movie)

        for movie in self.movie_list:
            if movie.name == random_movie.name:
                movie.have_watch()

        self.save_movie_data()
