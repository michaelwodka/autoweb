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
    driver.get('https://https://login.salesforce.com/')
    driver.find_element_by_id("username").send_keys("mwodka@cebglobal.com")
    driver.find_element_by_id("password").send_keys("Opti158015")
    driver.find_element_by_id("Login").click()
    return driver.current_url

# run the application
if __name__ == "__main__":  
    app.run()