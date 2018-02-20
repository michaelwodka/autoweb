# serve.py
from flask import Flask
from flask import render_template
from selenium import webdriver

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():  
    return render_template('index.html')

@app.route('/static/html/start.html')
def process():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument('/autowebform/.apt/usr/bin/google-chrome')
    driver = webdriver.Chrome(executable_path='/autowebform/.chromedriver/bin/chromedriver', chrome_options=options)
    driver.get("https://www.google.com")
    driver.save_screenshot("screenshot.png")

# run the application
if __name__ == "__main__":  
    app.run()