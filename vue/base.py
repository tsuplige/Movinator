class View:

    def __init__(self):
        pass
        self.color_red = "\033[31m"
        self.color_green = "\033[32m"
        self.color_yellow = "\033[33m"
        self.color_blue = "\033[34m"
        self.color_magenta = "\033[35m"
        self.color_cyan = "\033[36m"
        self.color_white = "\033[37m"
        self.color_reset = "\033[0m"

    def main_menu_prompt(self):

        print( self.title_prompt("menu principal"))

        start_input = input(self.question_color("\n1 pour ajouter des film a la liste de film à voir \n"
                                                "2 pour consulter la liste de film à voir\n3 pour tirer au sort un film\n4 pour quitter \n"))

        return start_input
    
    def add_movie_to_list_list_prompt(self):
        name = input(self.exemple_color("tapez le nom du film : "))
        while not name:
            print(self.error_color("champs vide"))
            name = input(self.exemple_color("tapez le nom du film : "))
        realisateur = input(self.exemple_color("tapez le nom du realisateur : "))
        while not realisateur:
            print(self.error_color("champs vide"))
            realisateur = input(self.exemple_color("tapez le nom du realisateur : "))
        annee = input(self.exemple_color("tapez l'année de sortie du film : "))
        while not annee:
            print(self.error_color("champs vide"))
            annee = input(self.exemple_color("tapez l'année de sortie du film : "))
        resume = input(self.exemple_color("tapez le resumé du film : "))
        while not resume:
            print(self.error_color("champs vide"))
            resume = input(self.exemple_color("tapez le resumé du film : "))

        return name, realisateur, annee, resume
    
    def show_movie_list_prompt(self, movie_list):

        print(self.title_prompt('Liste de films'))
        
        for movie in movie_list:

            print("         ", movie.name, "  |   année : ", movie.year, "  |   réalisateur : ", movie.realisateur)
            print("   _______________________________________________________________________________________\n")

    def print_movie_randomly_choose(self, movie):
        print(self.error_color(f"\n regardez {movie.name} de {movie.realisateur}"))

    def title_prompt(self, title_content):
        print(self.title_color(f"\n______________________{title_content}____________________\n"))

    def question_color(self, question):
        return self.color_yellow + question + self.color_reset
    
    def exemple_color(self, exemple):
        return self.color_cyan + exemple + self.color_reset
    
    def title_color(self, title_color):
        return self.color_magenta + title_color + self.color_reset
    
    def error_color(self, error):
        return self.color_red + error + self.color_reset
