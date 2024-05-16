import unittest
import requests

class TestStarWarsAPI(unittest.TestCase):
    base_url = "https://swapi.dev/api/"

    def test__01_get_movie_list_and_count(self):
        # Get the list of movies and check if the movies count is 6
        self.assertTrue(self.count_movie_list(), "Movie count is not equal 6 as expected")

    def test_02_validate_movie_director(self):
        # Get the 3rd movie and check if the director of the movie is ‘Richard Marquand’
        movie_director = "Richard Marquand"
        movie_number = 3

        self.assertTrue(self.get_movie_by_number_and_director(movie_number, movie_director))

    def test_03_validate_movie_director_negative_test(self):
        # Get the 5th movie and assert that ’Producers’ are not ‘Gary Kurtz, George Lucas'
        movie_producer = "Gary Kurtz"
        movie_number = 5
        self.assertFalse(self.get_movie_by_number_and_producer(movie_number, movie_producer))

        # 5th movie director is infact 'George Lucas'
        movie_producer = "George Lucas"
        self.assertFalse(self.get_movie_by_number_and_producer(movie_number, movie_producer))

    def get_movie_list(self):
        endpoint_url = f"{self.base_url}/films"
        response = requests.get(endpoint_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        return data

    def count_movie_list(self):
        get_list = self.get_movie_list()
        self.assertIsNotNone(get_list, "List is empty")
        # Get the list of movies and check if the movies count is 6
        self.assertEqual(6, get_list["count"], "Total Movies expected is 6")
        return True

    def get_movie_by_number_and_director(self, movie_number, movie_director: str):
        endpoint_url = f"{self.base_url}/films/{movie_number}"
        response = requests.get(endpoint_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        get_movie_director = data["director"]
        if get_movie_director != movie_director:
            return False

        return True

    def get_movie_by_number_and_producer(self, movie_number, movie_producer: str):
        endpoint_url = f"{self.base_url}/films/{movie_number}"
        response = requests.get(endpoint_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        get_movie_producer = data["producer"]
        if get_movie_producer != movie_producer:
            return False

        return True


if __name__ == '__main__':
    unittest.main()
