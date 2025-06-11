from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ktp')
def ktp():
    return render_template('ktp.html')

@app.route('/kmzh')
def kmj():
    return render_template('kmzh.html')

@app.route('/keepingfit')
def keepingfit():
    return render_template('keepingfit.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mytest')
def mytest():
    questions = [
        {"question": "What is the capital of the UK?", "options": ["London", "Manchester", "Liverpool", "Birmingham"], "answer": "London"},
        {"question": "Which color is made by mixing red and blue?", "options": ["Purple", "Green", "Yellow", "Pink"], "answer": "Purple"},
        {"question": "How many days are there in a leap year?", "options": ["365", "366", "364", "360"], "answer": "366"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": "Mars"},
        {"question": "Which language is primarily spoken in Brazil?", "options": ["Spanish", "Portuguese", "French", "English"], "answer": "Portuguese"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Mark Twain", "Charles Dickens", "J.K. Rowling"], "answer": "William Shakespeare"},
        {"question": "Which animal is known as the king of the jungle?", "options": ["Tiger", "Lion", "Elephant", "Wolf"], "answer": "Lion"},
        {"question": "What is the boiling point of water in Celsius?", "options": ["90°C", "100°C", "80°C", "110°C"], "answer": "100°C"},
    ]
    return render_template('mytest.html', questions=questions)




if __name__ == '__main__':
    app.run(debug=True)
