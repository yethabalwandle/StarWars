from selenium.webdriver.common.by import By


class LandingPageLocators(object):

    def table_column_title(self):
        return  '//th[text() = "Title"]'

    def table_column_episode(self):
        return '//th[text() = "Episode"]'

    def table_column_director(self):
        return '//th[text() = "Director"]'

    def movie_title(self):
        return "//tr/td/a[text() = 'The Phantom Menace']"

    def get_movie_title(self):
        return "//tbody/tr/td/a"

    def get_movie_by_title(self, movie_title: str):
        return "//tbody/tr/td/a[text() = '"+movie_title+"']"

    def get_species_list(self):
        return "//h1[text() = 'Species']/../../ul/li"

    def button_back(self):
        return "//*[text() = 'Back']"

    def get_planets_list(self):
        return "//h1[text() = 'Planets']/../../ul/li"




