from selenium import webdriver
from selenium.webdriver.common.by import By

from collections import Counter
import re

import matplotlib.pyplot as plt


sites = ["https://tsn.ua"]


periods = [("2021", "10", "1"), ("2021", "10", "2"), ("2021", "10", "3")]


driver = webdriver.Chrome()

texts = {}

def process_page_news_page(href: str):
    driver.get(href)
    print('processing', href)
    main = driver.find_element(By.CSS_SELECTOR, "main")
    text = main.text
    driver.back()
    print(text)
    return text

for site in sites:
    for year, month, day in periods:

        key = f"{year}_{month}_{day}"


        text = process_page_news_page(f"{site}/archive/{year}/{month}/{day}")
        words = re.findall(r'\b(?!АРХІВ\b|Дата\b\b|публікації\b\b|від\b\b|що\b\b|як\b\b|публікації\b\b|за\b\b|до\b\b|час\b\b|Україні\b\b|відео\b\b|про\b\b|Перегляди\b\b|на\b\b|з\b\b|в\b\b|у\b\b|та\b\b|і\b\b|B\b)\b[a-z]+\b', text, flags=re.IGNORECASE)
        word_counts = Counter(words)


        top_10_words = word_counts.most_common(10)
        top_10_words_list = [(word, count) for word, count in top_10_words]

        texts[key] = [text, top_10_words_list]



driver.quit()
print(texts)
words, counts = zip(*top_10_words_list)


plt.bar(words, counts, color='blue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Words')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.show()
