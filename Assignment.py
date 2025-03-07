from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = 'Hariharaganesh'  
    username = os.getenv("USER") or os.getenv("USERNAME")
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <pre>
    Name: {name}
    User: {username}
    Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}

    TOP Output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
