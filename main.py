from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

username = "your username"

password = "Your Password"
insta_url = "https://www.instagram.com/"

driver = webdriver.Chrome()

driver.get(url=insta_url)
time.sleep(1)

user = driver.find_element(By.NAME, "username")
user.send_keys(username)
passw = driver.find_element(By.NAME, "password")
passw.send_keys(password)
passw.send_keys(Keys.ENTER)
time.sleep(5)

save = driver.find_elements(By.TAG_NAME, "button")
save_range = len(save)

# print(save[save_range-1].text)
save[save_range-1].click()
time.sleep(5)
not_now = driver.find_elements(By.TAG_NAME, "button")
# print(not_now)
not_now_range = len(not_now)
not_now[not_now_range-1].click()
time.sleep(2)
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys("/")
time.sleep(2)
# body.send_keys("pk")
search = driver.find_elements(By.TAG_NAME, "input")
search = search[0]
search.send_keys("Person name to search")
time.sleep(5)
search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)
# search.click()
time.sleep(6)
follow = driver.find_element(By.PARTIAL_LINK_TEXT, "following")
follow.click()

time.sleep(5)
start = driver.find_elements(By.TAG_NAME, "button")
for j in start:

    print(j.text)
    if j.text == "Follow":
        j.click()

print("Finished")

