from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/contact_list')
def contact_list():
  return render_template('contact_list.html')

if __name__ == '__main__':

  app.run(debug=True)