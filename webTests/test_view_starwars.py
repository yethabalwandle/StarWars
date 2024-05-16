import unittest

from utilities import test_methods
from utilities.selenium_driver import SeleniumDriver


class TestViewStarWars(unittest.TestCase):

    movie_name = "The Empire Strikes Back"
    species_name = "Wookie"
    planet_name = "Camino"
    function = test_methods.TestMethods()
    def setUp(self):
        self.function.open_new_browser()


    def test_01_validate_movie_list(self):
        print("Sort movies by Title")
        # Sort movies by ’Title’ and assert the last movie in the list is ‘The Phantom Menace’
        self.assertTrue(self.function.validate_movie_list(), "Last Movie should be "+self.movie_name)

    def test_02_validate_movie_details(self):
        print("Select Movie and validate species name is found")
        # View the movie ‘The Empire Strikes Back’ and check if the ‘Species’ list has ‘Wookie’
        self.assertTrue(self.function.view_movie_and_validate_species(self.movie_name, self.species_name),
                        "Species name not found :"+self.species_name)

    def test_03_validate_movie_planets(self):
        print("Validate movie planets")
        # Assert that ‘Planets’ ‘Camino’ is not part of the movie ‘The Phantom Menace
        self.movie_name = "The Phantom Menace"
        self.function.click_button_back()
        self.assertTrue(self.function.validate_movie_planets(self.movie_name, self.planet_name),
                        self.planet_name + " Planet should not be found on this movie: " + self.movie_name)
