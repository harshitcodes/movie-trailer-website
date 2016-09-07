# movie-trailer-website
Runs favorite movie trailer on youtube in a bootstrap modal.

## What is the project?
The project helps to learn basic programming concepts of python and Object Oriented Programming. By building a website which entails several movies and their information stored in a python class inside a module called media. [fresh_tomatoes](https://github.com/harshitcodes/movie-trailer-website/blob/master/fresh_tomatoes.py) is the module which takes the information from the [box-office.py](https://github.com/harshitcodes/movie-trailer-website/blob/master/box_office.py) file and creates the webpage which renders all the movies with their information like box-imagery, trailer url, storyline,etc.

### Screenshots
![alt screenshots](https://github.com/harshitcodes/movie-trailer-website/blob/master/Screenshot%20from%202016-09-07%2018-09-15.png "Full screenshot")




## Installation
Using CLI:
Clone the repository : [https://github.com/harshitcodes/movie-trailer-website](https://github.com/harshitcodes/movie-trailer-website)
```
git clone https://github.com/harshitcodes/movie-trailer-website
```

Cd into the movie-trailer-website directory
```
cd movie-trailer-website
```

Then use python command to run the box_office.py
```
python box_office.py
```
And you have the Blockbuster Trailers live in your web browser.


## Modules

fresh_tomatoes
--------------
It renders the content of movies through an html file called fresh_tomatoes.html which is rendered using the webbrowser module.

media
-----
It contains the server-side code which is the blue-print for the data to be stored using python data structure.