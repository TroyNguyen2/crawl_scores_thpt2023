from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_img import read_image , append_list_as_row
from time import sleep

"""
Change the province_code to get data base on province
ex: 01: Ha noi ; 02: HCM ; ..
"""
province_code = "01"
def main():
  source_url = "http://tracuudiem.thitotnghiepthpt.edu.vn/"
  driver = webdriver.Chrome()
  driver.get(source_url)
  sleep(1)

  for i in range(1,12000):

    soup = BeautifulSoup(driver.page_source, "html.parser")
    sleep(1)
    base64_string = soup.find(name='div', class_ = "captcha-code").find(name = 'img').get('src')
    captcha_text  = read_image(base64_string = base64_string)

    #Input captcha
    captcha_input = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div/input")
    captcha_input.send_keys(captcha_text)
    sleep(1)

    # Input the id (HCM)
    id_input= driver.find_element(By.XPATH,'/html/body/main/div[2]/div/div/div[1]/div[1]/input')
    id      = province_code + str("{:06d}".format(i))
    id_input.send_keys(id)
    sleep(1)
    
    # Hit enter
    search_button = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[1]/button")
    search_button.send_keys(Keys.ENTER)
    sleep(1)
    
    # Loop if the func read_img get wrong value
    while True:
      try:
        WebDriverWait(driver,1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        captcha_input.clear()
        driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[1]/div[2]/div/div/button/img").click()
        sleep(1)
        soup              = BeautifulSoup( driver.page_source, "html.parser")
        # captcha_input     = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div[2]/div/input")
        new_base64_string = soup.find(name='div', class_ = "captcha-code").find(name = 'img').get('src')
        new_captcha_text  = read_image(base64_string = new_base64_string)
        captcha_input.send_keys(new_captcha_text)
        search_button.send_keys(Keys.ENTER)
      except:
        break
    
    soup  = BeautifulSoup(driver.page_source, "html.parser")
    # Get the value
    scores= soup.find(name='div', class_='result').find('h4').get_text()
  
    # Write the header row to the CSV file
    data = [id, scores]
    append_list_as_row('thpt2023.csv', data)

    # Clear the input box
    captcha_input.clear()
    id_input.clear()
if __name__ =='__main__':
  main()

