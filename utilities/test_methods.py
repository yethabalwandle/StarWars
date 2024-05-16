import time

from utilities import web_elements
from utilities.selenium_driver import SeleniumDriver


class TestMethods(SeleniumDriver):

    url = " http://localhost:3000"

    locator = web_elements.LandingPageLocators()

    def open_new_browser(self):
        SeleniumDriver.open_browser(self, self.url)
        return True

    def validate_movie_list(self):
        SeleniumDriver.wait_for_element_byxpath(self, self.locator.table_column_title())
        SeleniumDriver.wait_for_element_byxpath(self, self.locator.table_column_episode())
        SeleniumDriver.wait_for_element_byxpath(self, self.locator.table_column_director())

        get_text = SeleniumDriver.get_text_by_xpath(self, self.locator.get_movie_title())
        sort_list = sorted(get_text)
        assert "The Phantom Menace" == sort_list[5]

        return True

    def view_movie_and_validate_species(self, movie_name: str, species_name: str):
        SeleniumDriver.wait_for_element_byxpath(self, self.locator.table_column_title())

        SeleniumDriver.click_elementby_xpath(self, self.locator.get_movie_by_title(movie_name))
        SeleniumDriver.wait_for_element_byxpath(self, self.locator.get_species_list())
        get_text = SeleniumDriver.get_text_by_xpath(self, self.locator.get_species_list())

        if species_name not in get_text:
            return False

        return True

    def validate_movie_planets(self, movie_title: str, planet_name : str):
        SeleniumDriver.wait_for_element_byxpath(self, self.locator.table_column_title())

        SeleniumDriver.click_elementby_xpath(self, self.locator.get_movie_by_title(movie_title))
        SeleniumDriver.wait_for_element_byxpath(self, self.locator.get_planets_list())
        get_planet_list = SeleniumDriver.get_text_by_xpath(self, self.locator.get_species_list())
        # assert not get_planet_list.__contains__(planet_name)
        if planet_name in get_planet_list:
            return False

        return True

    def click_button_back(self):
        if SeleniumDriver.wait_for_element_byxpath(self, self.locator.table_column_title()):
            SeleniumDriver.click_elementby_xpath(self, self.locator.button_back())

        return True



    def close_browser(self):
        SeleniumDriver.kill_driver(self)
        return True
