# serve.py
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from bs4 import BeautifulSoup


# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def initiate():
    return render_template('index.html')

@app.route('/results.html', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=C:\\Users\\mwodka\\AppData\\Local\\Google\\Chrome\\Automation Profile')
        driver = webdriver.Chrome(executable_path='C:\Selenium\Chrome\chromedriver.exe', chrome_options=options)
        driver.get('https://www.linkedin.com')
        if driver.current_url != "https://www.linkedin.com/feed/":
            driver.find_element_by_id("login-email").send_keys(request.form['emaily'])
            driver.find_element_by_id("login-password").send_keys(request.form['passy'])
            driver.find_element_by_id("login-submit").click()
        search = driver.find_element_by_css_selector("input[placeholder='Search']")
        search.send_keys(request.form['criteria'])
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        height = driver.get_window_size()['height']
        scroll_text = "window.scrollTo(0, {})".format(height)
        driver.execute_script(scroll_text)
        time.sleep(3)

        links = []
        names = []
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        li = soup.find("ul", {"class": "search-results__list"})
        div = li.find_all("div", {"class": "search-result__info"})

        for item in div:
            for url in item.find_all("a", {"class": "search-result__result-link"}):
                if url.get('href').startswith("/in/"):
                    links.append("https://www.linkedin.com" + url.get('href'))
                    for item in url.find_all('span', {"class": "name"}):
                        names.append(item.getText())

        final_list = list(zip(names, links))

        return render_template('results.html', final_list=final_list)

# run the application
if __name__ == "__main__":
    app.run()