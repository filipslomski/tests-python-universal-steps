from selenium import webdriver


def before_all(context):
  context.driver = webdriver.Chrome('./chromedriver')
  context.base_url = 'http://'

    
def after_all(context):  
  context.browser.close()