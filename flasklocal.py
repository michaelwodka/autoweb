# serve.py
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from selenium import webdriver
import os

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
        driver.find_element_by_id("login-email").send_keys(request.form['emaily'])
        driver.find_element_by_id("login-password").send_keys(request.form['passy'])
        driver.find_element_by_id("login-submit").click()
        '''return render_template('results.html')'''
        '''return driver.find_element_by_xpath('//*[@id="feed-nav-item"]/a/span[2]').text'''
        return driver.current_url

    '''if request.method == 'GET':
        return render_template('results.html')'''

'''@app.route("/results.html")
def results():
        return render_template('results.html')'''

# run the application
if __name__ == "__main__":
    app.run()