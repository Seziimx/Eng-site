from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Папка для загрузок
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# Основные страницы
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ktp')
def ktp():
    return render_template('ktp.html')

@app.route('/kmzh', methods=['GET', 'POST'])
def kmzh():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Файл таңдалмады', 400
        file = request.files['file']
        if file.filename == '':
            return 'Файл атауы бос', 400
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    # Получаем список файлов из папки uploads
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('kmzh.html', files=files)


@app.route('/keepingfit')
def keepingfit():
    return render_template('keepingfit.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Страница с тестами
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


# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)
