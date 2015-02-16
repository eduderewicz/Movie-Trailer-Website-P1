import media
import fresh_tomatoes

#create movies
departed = media.Movie("Departed",
                      "Cops or Criminals",
                      "http://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
                      "https://www.youtube.com/watch?v=auYbpnEwBBg")

superbad = media.Movie("The Hangover",
                       "Some guys just can't handle Vegas",
                       "http://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                       "https://www.youtube.com/watch?v=tcdUhdOlz9M")
edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "Live, Die, Repeat",
                               "http://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI")

boondocksaints = media.Movie("Boondock Saints",
                             "Brothers. Killers. Saints.",
                             "http://upload.wikimedia.org/wikipedia/en/1/1b/The_Boondock_Saints_poster.jpeg",
                             "https://www.youtube.com/watch?v=ydXojYfCF3I")

officespace = media.Movie("Office Space",
                          "Work Sucks.",
                          "http://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
                          "https://www.youtube.com/watch?v=_IwzZYRejZQ")


twenty_one_jumpstreet = media.Movie("21 Jump Street",
                           "They thought the streets were mean. Then they went back to high school.",
                           "http://upload.wikimedia.org/wikipedia/en/9/93/21JumpStreetfilm.jpg",
                           "https://www.youtube.com/watch?v=ZirgAYBcOgo")
#create list of movies
movies = [departed, superbad, edge_of_tomorrow, boondocksaints, officespace, twenty_one_jumpstreet]
#create move website
fresh_tomatoes.open_movies_page(movies)
