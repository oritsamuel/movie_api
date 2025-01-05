# Movie Review API

This repository contains a Django-based RESTful API for managing movie reviews. Users can create, read, update, and delete reviews, and view reviews for specific movies.

**Features:**

* User authentication and registration
* Create, read, update, and delete movie reviews
* Assign ratings to movies (e.g., 1-5 stars)
* Add review content
* Search for movies by title
* Filter reviews by rating
* View reviews for a specific movie
* Pagination and sorting options for review lists

**Getting Started:**

curl commands
To get all products:
curl -X GET http://127.0.0.1:8000/movie/movies/
To get a single product:
curl -X GET http://127.0.0.1:8000/movie/movies/1/
To create a new product:
curl -X POST -H "Content-Type: application/json" -d '{"Title": "Dead Poet Society", "Review": "This is a new perspective", "Ratinge": "4.5"}' http://127.0.0.1:8000/movie/movies/
