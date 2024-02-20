# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def high_imdb(movie):
    return movie["imdb"] >=5.5

def above_5_5(movies):
    filtered_movies = [movie for movie in movies if movie['imdb'] > 5.5]
    return filtered_movies

def by_category(movies, category_name):
    filtered_movies = [movie for movie in movies if movie['category'] == category_name]
    return filtered_movies

def average_score(movies):
    total = 0
    num_movies = len(movies)
    for movie in movies:
        total += movie['imdb']
        return total / num_movies
    
def average_score_category(movies, category_name):
    new_list = by_category(movies, category_name)
    return average_score(new_list)


print(by_category(movies, "Suspense"))
