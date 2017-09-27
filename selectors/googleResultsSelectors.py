from selectors.baseSelectors import BaseSelectors
from selenium.webdriver.common.by import By


class GoogleResultsSelectors(BaseSelectors):

    selectors = {'result_stats': (By.ID, "resultStats")}