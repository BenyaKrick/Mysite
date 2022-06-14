#базовый каркас сайта
from flask import Flask, render_template  #render_template - функция для подключения HTML шаблонов

app = Flask(__name__)  #создаем объект


@app.route('/')  #декоратор для функции рут прописываем url для отслеживания
@app.route('/home')  #отслеживаем вторую страницу
def index():  #функция отсеживания главной странички
  #return "Hello World" отображение на главной страничке hello world
    return render_template("index.html") #прописываем путь к index.html для отображения на главной(ищет в папке template)



@app.route('/about')
def about():  #функция отсеживания страницы about
  # #return "About page" отображение на странице about
    return render_template("about.html") #прописываем путь к about.html для отображения на главной(ищет в папке template)



@app.route('/user/<string:name>/<int:id>')
def user(name, id):  #функция отсеживания страницы user
    return "User page: " + name + " - " + str(id)  #отображение на странице user(имя и id)


if __name__ == "__main__":  #определяем главный файл для запуска
    app.run(debug=True)  #показываем ошибки на сайте
