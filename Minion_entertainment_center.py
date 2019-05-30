import movie
import website

despicable_me = movie.Movie(movie_title = "Despicable Me", movie_storyline = "*FILL_IN_STORYLINE*",
poster_image = "https://m.media-amazon.com/images/M/MV5BMTY3NjY0MTQ0Nl5BMl5BanBnXkFtZTcwMzQ2MTc0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
trailer_youtube = "*FILL_IN_TRAILER*")  

despicable_me_2 = movie.Movie(movie_title = "Despicable Me 2", movie_sotryline = "*FILL_IN_STORYLINE*",
poster_image = "https://m.media-amazon.com/images/M/MV5BMjExNjAyNTcyMF5BMl5BanBnXkFtZTgwODQzMjQ3MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
trailer_youtube = "*FILL_IN_TRAILER*")


movies = [despicable_me, despicable_me_2 ]
website.open_movies_page(movies)
