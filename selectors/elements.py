from selenium.webdriver.common.by import By

elements = {
    #google_results_page
    'result_stats': (By.ID, "resultStats"),

    #google_page
    'search_suggestion': (By.XPATH, ".//ul[@role='listbox']/li//div[string(.)='{argument}']"),
    'sign_in': (By.XPATH, ".//a[@id='gb 70']"),
    'account_icon': (By.XPATH, ".//span[@id='gb_7a']"),
    'logged_user': (By.XPATH, ".//*[contains(@class,'gb_xb')]")
}