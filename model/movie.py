class Movie:
    def __init__(self, name, realisateur, year, resume, watch = False):
        self.name = name
        self.realisateur = realisateur
        self.year = year
        self.resume = resume
        self.watch = watch

    def have_watch(self):
        if self.watch == False:
            self.watch = True

    def convert_to_json_data(self):
        movie_data = {
                "name": self.name,
                "realisateur": self.realisateur,
                "year": self.year,
                "resume": self.resume,
                "watch" : self.watch
            }
        
        return movie_data
