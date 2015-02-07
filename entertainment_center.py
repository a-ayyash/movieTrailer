import fresh_tomatoes
import media

def populate_movies_list():
	#Creating instances of our favorite movies. 
	#each movie instance is constructed with
	#Movie Name
	#Storyline
	#Movie Poster
	#Movie Trailer
	movies_list = list()#empty list

	#1
	movies_list.append(#adds movie instance to the list
			media.Movie("Se7en",
						"The Seven Sins", 
						"http://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg", 
						"http://www.youtube.com/watch?v=J4YV2_TcCoE")
			)#close the list.append()


	#2
	movies_list.append(
		media.Movie("Pulp Fiction", 
					"The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.", 
					"http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg", 
					"www.youtube.com/watch?v=wZBfmBvvotE") 
		)

	#3
	movies_list.append(
		media.Movie("Spirited Away", 
					"Lost girl in a city of spirits", 
					"http://upload.wikimedia.org/wikipedia/ar/a/a0/%D8%B1%D8%AD%D9%84%D8%A9_%D8%AA%D8%B4%D9%8A%D9%87%D9%8A%D8%B1%D9%88.jpg", 
					"https://www.youtube.com/watch?v=ByXuk9QqQkk") 
		)

	#4
	movies_list.append(
		media.Movie("Amelie", 
					"The Fabulous Destiny of Amelie Poulain", 
					"http://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg", 
					"https://www.youtube.com/watch?v=sECzJY07oK4") 
		)

	#5
	movies_list.append(
		media.Movie("Gandhi", 
					"A Great Leader Biography", 
					"https://upload.wikimedia.org/wikipedia/en/1/10/Gandhi-poster.png", 
					"https://www.youtube.com/watch?v=6oWqlb_TlLQ") 
		)

	#6
	movies_list.append(
		media.Movie("Lord of The Rings", 
					"An Epic Trilogy", 
					"http://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg", 
					"https://www.youtube.com/watch?v=V75dMMIW2B4") 
		)
	return movies_list

#function responsible for putting things together
def renders_home_page():
	movies_list = populate_movies_list()
	fresh_tomatoes.open_movies_page(movies_list);

renders_home_page()
