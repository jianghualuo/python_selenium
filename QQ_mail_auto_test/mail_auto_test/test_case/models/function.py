from selenium import webdriver


def get_screenshot(driver, filename):
    driver.get_screenshot_as_file(filename)


# if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     driver.get("https://www.baidu.com")
#     driver.get_screenshot_as_file("./../../report/img/baidu.jpg")
#     driver.quit()

