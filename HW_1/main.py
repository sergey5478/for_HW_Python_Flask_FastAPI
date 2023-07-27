"""Задание №9.
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Запускаем главную страницу"""
    return render_template('base1.html')


@app.route('/clothing')
def clothing():
    """Запускаем Одежду"""
    return render_template('clothing.html')


@app.route('/shoes')
def shoes():
    """Запускаем Обувь"""
    return render_template('shoes.html')


@app.route('/jacket')
def jacket():
    """Запускаем Куртки"""
    return render_template('jacket.html')


if __name__ == '__main__':
    app.run(debug=True)
