from selenium.webdriver.common.by import By

elements = {
    'result_stats': (By.ID, "resultStats"),
    'search_suggestion': (By.XPATH, ".//ul[@role='listbox']/li//div[string(.)='{argument}']")
}