# crawl_scores_thpt2023

1. pip install -r requirements.txt
2. download the web driver suit
3. with the chrome version at https://chromedriver.chromium.org/downloads
4. Download tesseract ocr at https://sourceforge.net/projects/tesseract-ocr-alt/files/
5. run: python main.py

#  I made this project to practice my programming Python by crawling the scores from the Ministry of Education and Training. The logic is simple:
First I use pytesseract to connect tesseract ( a pre-train AI framework that could parse text from images). Selenium and Webdriver to interact with the website and parse data,
and finally, save data by CSV file. This script could run until the host closes searching !!

One more reminder: you can go to the source code and change the code of the province that I've put on the path in main.py
# I just only crawl 300 ids save in **crawl_thpt2023.csv** for testing.
