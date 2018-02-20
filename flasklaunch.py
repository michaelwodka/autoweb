# serve.py
from flask import Flask
from flask import render_template
from selenium import webdriver
import os

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():  
    return render_template('index.html')

@app.route('/static/html/start.html')
def process():
    chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
    opts = webdriver.ChromeOptions()
    opts.binary_location = chrome_bin
    driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=opts)
    driver.get('https://michaelwodka.com/')
    driver.find_element_by_name("name").send_keys("hi")
    driver.find_element_by_id("email").send_keys("msw233@cornell.edu")
    driver.find_element_by_name("_subject").send_keys("hi")
    driver.find_element_by_name("message").send_keys("hi")
    driver.find_element_by_xpath('/html/body/section[4]/div/div/form/div[5]/div/button').click()
    return driver.page_source

# run the application
if __name__ == "__main__":  
    app.run()