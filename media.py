# Movie class to store all the relevant story about each movie we want to see in our website
import webbrowser

class Movie():
	instant_ctr = 0
	def __init__(self, movie_title, movie_storyline, movie_poster_image, 
		movie_trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image
		self.trailer_youtube_url = movie_trailer_youtube
		self.id = Movie.instant_ctr
		Movie.instant_ctr += 1

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)	