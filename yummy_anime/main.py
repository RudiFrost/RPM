from lib2to3.pgen2 import driver
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

login = 'sampleuser'
password = '12345678'

driver = webdriver.Chrome(executable_path="C:/Users/rudif/PycharmProjects/RPM/yummy_anime/chromedriver.exe")


def anime_comment(url):
    driver.get(url)

    register = driver.find_element("xpath", '/html/body/div[1]/div/header/div[2]')
    register.click()

    time.sleep(1)

    log_in = driver.find_element("id", "login_name")
    log_in.send_keys(login)

    time.sleep(1)
    password_anime = driver.find_element("id", "login_password")
    password_anime.send_keys(password)

    time.sleep(1)
    driver.find_element('id', "login_not_save").click()

    time.sleep(1)
    enter = driver.find_element('xpath', '/html/body/div[2]/form/div[1]/div[3]/button')
    enter.click()

    time.sleep(1)

    genres_list = driver.find_element('xpath', '/html/body/div[1]/div/div/aside/div[1]/ul/li[1]')
    genres_list.click()
    time.sleep(1)

    kids_genre = driver.find_element('xpath', '/html/body/div[1]/div/div/aside/div[1]/ul/li[1]/ul/li[18]/a')
    kids_genre.click()
    time.sleep(1)

    sixth = driver.find_element('xpath', '//*[@id="pagination"]/div/a[5]')
    sixth.click()

    find_anime = driver.find_element('xpath', '//*[@id="dle-content"]/a[8]/div[1]/img')
    find_anime.click()

    time.sleep(3)
    text = "блин, вот бы вернуться в 2003 и посмотреть его заново"

    formochka = driver.find_element(By.CSS_SELECTOR, "#comments_ifr")
    time.sleep(2)
    driver.switch_to.frame(formochka)
    time.sleep(2)

    required_field = driver.find_element("xpath", "/html/body/p")
    required_field.click()
    required_field.send_keys(text)
    time.sleep(2)

    time.sleep(2)
    driver.switch_to.default_content()

    time.sleep(3)
    send_button = driver.find_element('xpath', '//*[@id="add-comments-form"]/div[2]/div/button')
    send_button.click()
    time.sleep(3)

    # driver.close()
    # driver.quit()


anime_comment("https://yummyanime.org/")
