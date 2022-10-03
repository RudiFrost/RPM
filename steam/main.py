from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:/Users/rudif/PycharmProjects/RPM/steam/chromedriver.exe")


def steamVR(url):
    driver.get(url=url)

    time.sleep(1)

    search = driver.find_element('id', 'store_nav_search_term')
    search.send_keys("action")
    search.send_keys(Keys.ENTER)

    time.sleep(1)

    for_one_player = driver.find_element('xpath', '//*[@id="TagFilter_Container"]/div[1]/span[1]')
    for_one_player.click()

    time.sleep(1)

    vr = driver.find_element('xpath', '//*[@id="TagFilter_Container"]/div[4]/span[1]')
    vr.click()
    time.sleep(1)

    button = driver.find_element('xpath', '//*[@id="additional_search_options"]/div[7]')
    button.click()

    time.sleep(1)
    vr_real = driver.find_element('xpath', '//*[@id="narrow_byVR"]/div[1]/span[1]/span/span[1]')
    vr_real.click()
    time.sleep(1)

    for i in range(10):
        driver.save_screenshot('vr_screenshot' + str(i) + '.png')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    driver.close()
    driver.quit()


steamVR("https://store.steampowered.com/")
