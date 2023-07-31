# crawl_scores_thpt2023

1. pip install -r requirements.txt
2. download the web driver suit with the Chrome version at https://chromedriver.chromium.org/downloads
3. Download tesseract ocr at https://sourceforge.net/projects/tesseract-ocr-alt/files/
4. run: python main.py

#  I made this project to practice my programming Python by crawling and visualizing the scores from the Ministry of Education and Training through Dash. The logic is simple:
First I use pytesseract to connect tesseract ( a pre-train AI framework that could parse text from images). Selenium and Webdriver to interact with the website and parse data,
and save data by CSV file. This script could run until the host closes searching !!
Finally, the data that have been crawled will be cleaned up in data_cleaning.py. The visualization by starting dashboard_visualize.py

# The sever will run on port 6969

One more reminder: you can go to the source code and change the code of the province that I've put on the path in main.py
# I  only crawl 300 ids save in **crawl_thpt2023.csv** for testing.
