from selenium.webdriver.common.by import By

elements = {
    #google_results_page
    'result_stats': (By.ID, "resultStats"),

    #google_page
    'search_suggestion': (By.XPATH, ".//ul[@role='listbox']/li//div[string(.)='{argument}']"),
    'sign_in': (),
    'account_icon': (),
    'logged_user': ()
}