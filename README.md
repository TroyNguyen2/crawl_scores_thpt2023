# crawl_scores_thpt2023

1. pip install -r requirements.txt
2. download the web driver suit
3. with the chrome version at https://chromedriver.chromium.org/downloads
4. Download tesseract ocr at https://sourceforge.net/projects/tesseract-ocr-alt/files/
5. run: python main.py

#  I made this project to practice my programming Python by crawling the scores from the ministry of Education and training. The logic is simple:
First I use pytesseract to connecting tesseract ( a pretrain AI framework that could parse text from image ) , then Selenium and webdriver to interact the website and parse data,
finally save data by csv file. 

# I just only crawl 300 id for testing.
