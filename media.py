import webbrowser

# Movie class to store all the relevant information about each movie we want to see in our website
class Movie():
	def __init__(self, movie_title, movie_storyline, movie_poster_image, 
		movie_trailer_youtube,movie_rating):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image
		self.trailer_youtube_url = movie_trailer_youtube
		self.rating = movie_rating

	def show_trailer(self):
		# opens up the browser with the provided url.
		webbrowser.open(self.trailer_youtube_url)	