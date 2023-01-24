import spacy
nlp = spacy.load('en_core_web_md')

#Movie class
class Movie():

    #Initialize fields
    def __init__(self, title, descrip):
        self.title = title
        self.descrip = descrip
        self.similar = 0

#This function predicts the next movie to watch 
#using nlp similarity function.
def watch_next(description):
    
    first_movie_description = nlp(description)
    
    for movie in movies:
        movie_description = nlp(movie.descrip)
        movie.similar = movie_description.similarity(first_movie_description)

    highest_similarity = max(movies, key = lambda s: s.similar)
    return print(f'The following movie is recommended: "{highest_similarity.title}"')
    
movies = [] #Create empty list to add movies to
#Read in movies from movies.txt file
with open('movies.txt','r') as movies_file:
    for line in movies_file:
        #Split title and description of each movie
        title, description = line.strip().split(' :')
        #Create an object of each movie using Movie class
        movie = Movie(title, description)
        #Add each movie to the movies list
        movies.append(movie)

#Create the initial movie to compare all other movies to
first_movie = Movie("Planet Hulk",
            ''' Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
                the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk 
                can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into 
                slavery and trained as a gladiator''')

#Call watch_next() function which prints the highest similarity movie
watch_next(first_movie.descrip)
