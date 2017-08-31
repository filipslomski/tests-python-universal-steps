from browser import Browser
from selenium import webdriver
from selectors.baseSelectors import BaseSelectors
from selenium.webdriver.common.by import By


class GoogleResultsSelectors(BaseSelectors):



    def open(self):
        self.visit(self.URL)

    def get_number_of_results(self):
        result_string = self.result_stats.get_element().get_text()
        number_of_results = ""
        for s in result_string.split():
            if s.isdigit():
                number_of_results += s
            elif number_of_results != "":
                break

        return int(number_of_results)