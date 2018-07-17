import requests
from flask import Flask, render_template
app = Flask(__name__)


status = {
        '200': 'Operational',
        '500': 'Major Outage'
        }

@app.route('/<website>')
def index(website):
    url = 'http://' + website
    try:
        r = requests.get(url)
        return render_template('index.html', status=status.get(str(r.status_code), str(r.status_code)), url=url)
    except Exception as e:
        return render_template('index.html', status='Major Outage', url=url)

if __name__ == '__main__':
    app.run()
