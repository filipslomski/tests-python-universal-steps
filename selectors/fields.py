from selenium.webdriver.common.by import By

fields = {
    #google_page
    'search_field': (By.ID, "lst-ib"),
    'email_name': (By.XPATH, ".//input[@name='email']"),
    'email_password': (By.XPATH, ".//input[@name='password']")
}