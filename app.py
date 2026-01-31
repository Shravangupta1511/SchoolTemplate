from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/course.html')
def course():
    return render_template('course.html')

@app.route('/teacher.html')
def teacher():
    return render_template('teacher.html')

if __name__ == '__main__':
    app.run()