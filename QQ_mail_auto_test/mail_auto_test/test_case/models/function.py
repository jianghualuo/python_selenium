from selenium import webdriver


def get_screenshot(driver, filename):
    driver.getscreenshot_as_file(filename)
