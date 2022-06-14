#базовый каркас сайта
from flask import Flask

app = Flask(__name__)  #создаем объект


@app.route('/')  #декоратор для функции рут прописываем url для отслеживания
@app.route('/home')  #отслеживаем вторую страницу
def index():  #функция отсеживания главной странички
    return "Hello World"  #отображение на главной страничке


@app.route('/about')
def about():  #функция отсеживания страницы about
    return "About page"  #отображение на странице about


@app.route('/user/<string:name>/<int:id>')
def user(name, id):  #функция отсеживания страницы user
    return "User page: " + name + " - " + str(id)  #отображение на странице user(имя и id)


if __name__ == "__main__":  #определяем главный файл для запуска
    app.run(debug=True)  #показываем ошибки на сайте
