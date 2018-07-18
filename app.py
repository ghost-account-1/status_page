import requests
from flask import Flask, render_template
from flask_compress import Compress
app = Flask(__name__)
Compress(app)


STATUS = {
        '200': 'Operational',
        '500': 'Major Outage'
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<website>/')
def status_page(website):
    url = 'http://' + website
    try:
        r = requests.get(url)
        return render_template('status_page.html', status=STATUS.get(str(r.status_code), str(r.status_code)), url=url)
    except Exception as e:
        return render_template('status_page.html', status='Major Outage', url=url)

if __name__ == '__main__':
    app.run()
