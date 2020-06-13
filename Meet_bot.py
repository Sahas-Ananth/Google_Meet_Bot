from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep as delay

op = Options()
op.add_argument("start-maximized")
op.add_argument("use-fake-ui-for-media-stream")

op.add_argument(
    '--user-data-dir=C:/User/anant/AppData/Local/Google/Chrome/User Data/Profile 1')

# C:/User/Your_system_name/AppData/Local/Google/Chrome/User Data/Profile x I have chosen 1 cause it has my college mail id DO NOT USE Default it won't work

op.add_argument(
    '--profile-directory=Profile 1')

# --profile-directory=Profile x I have chosen 1 cause it has my college mail id DO NOT USE Default it won't work

driver = webdriver.Chrome(options=op)
driver.get("https://meet.google.com/fow-ypbp-hvi")

delay(3)

camera_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div')
camera_button.click()

mic_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[1]/div[1]/div[3]/div[1]/div/div/div')
mic_button.click()

preferences_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div[1]/div[1]/div[4]/div')
preferences_button.click()

delay(3)

settings_button = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div/span[2]')
settings_button.click()

delay(1)

video_tab = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div/div[1]/div[2]')
video_tab.click()

delay(1)

video_send_quality_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div/div[2]/span[2]/div[2]/div[1]/div[2]/div/div[1]')
video_send_quality_button.click()

delay(1)

video_send_quality_720p_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div/div[2]/span[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]')
video_send_quality_720p_button.click()

delay(1)

video_recieve_quality_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div/div[2]/span[2]/div[2]/div[2]/div[2]/div/div[1]')
video_recieve_quality_button.click()

delay(1)

video_recieve_quality_720p_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div/div[2]/span[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]')
video_recieve_quality_720p_button.click()

delay(1)

settings_done_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[2]/div')
settings_done_button.click()

delay(1)

enter_meeting_button = driver.find_element_by_xpath(
    '//*[@id="ow3"]/div/div/div[4]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]')
enter_meeting_button.click()

delay(10)
driver.quit()

#  This should run one time:
# Email = ''
# pw = ''
# account_switcher = driver.find_element_by_xpath(
#     "/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a")
# account_switcher.click()

# email_id = driver.find_element_by_xpath('//*[@id="identifierId"]')
# email_id.send_keys(Email)
# mail_next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]')
# mail_next_button.click()
# delay(3)
# password = driver.find_element_by_xpath(
#     "//*[@id=\"password\"]/div[1]/div/div[1]/input")
# password.clear()
# password.send_keys(pw)
# password_next_button = driver.find_element_by_xpath('//*[@id="passwordNext"]')
# password_next_button.click()
# delay(5)
