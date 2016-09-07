# importing project based modules
import media
import fresh_tomatoes


# Creating instances of the Movie class of the media module

iron_man = media.Movie("Iron Man 3", 
	"When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.", 
	"http://ia.media-imdb.com/images/M/MV5BMTkzMjEzMjY1M15BMl5BanBnXkFtZTcwNTMxOTYyOQ@@._V1_SX300.jpg",
	"https://www.youtube.com/watch?v=oYSD2VQagc4",
	"7.2")

zodiac = media.Movie("Zodiac",
	"A San Francisco cartoonist becomes an amateur detective obsessed with tracking down the Zodiac killer", 
	"http://ia.media-imdb.com/images/M/MV5BMTQxNjc2NzAwNF5BMl5BanBnXkFtZTcwMDg3NzMzMw@@._V1_SX300.jpg",
	"https://www.youtube.com/watch?v=q6q_MfcDEEE",
	"7.7")

avatar = media.Movie("Avatar", 
	"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home", 
	"http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY",
	"7.9")

revenant = media.Movie("The Revenant", 
	"A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.", 
	"http://ia.media-imdb.com/images/M/MV5BMjU4NDExNDM1NF5BMl5BanBnXkFtZTgwMDIyMTgxNzE@._V1_SX300.jpg",
	"https://www.youtube.com/watch?v=LoebZZ8K5N0",
	"8.1")

hangover = media.Movie("The Hangover", 
	"Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing.",
	"http://ia.media-imdb.com/images/M/MV5BMTU1MDA1MTYwMF5BMl5BanBnXkFtZTcwMDcxMzA1Mg@@._V1_SX300.jpg",
	"https://www.youtube.com/watch?v=TZc39afdeXU",
	"7.2")

prestige = media.Movie("The prestige", 
	"Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.", 
	"http://ia.media-imdb.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_SX300.jpg",
	"https://www.youtube.com/watch?v=6VaCFcNGTHo",
	"8.5")


#sending the list of movie instances to the open_movies_page method of fresh_tomatoes module
movies = [iron_man, zodiac, avatar, revenant, hangover, prestige]
fresh_tomatoes.open_movies_page(movies)







