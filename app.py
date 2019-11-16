from flask import Flask, render_template

app = Flask(__name__)

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for portfolio page
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
