import flask


import models
import game

from flask import (
    Flask,
    Request,
    Response,
    render_template,
    request
)
from flask.app import Flask as FlaskApp


app: FlaskApp = Flask(__name__)
users:list[models.User]= []
games: list[game.Game] = []


@app.route('/')
def main_page():   
    return render_template(
        template_name_or_list="index.html"
    
    )
   

@app.route('/lk', methods=['GET','POST'])
def lk_page():
    new_game : list[game.Game] = []
    name:list[models.User] = [users]
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        price = request.form.get('price')
        genre = request.form.get('genre')
        release_date = request.form.get('release_date')
        new_game = {'title': title, 'description': description, 'price': price, 'genre': genre, 'release_date':release_date}
        games.append(new_game)

    return render_template(
        "lk.html",ctx_games=enumerate(games), user=name
    )
   


@app.route('/create_post', methods=['GET','POST'])
def create_post() -> flask.Response:
    return render_template(
        template_name_or_list="create_post.html",
    )
    

@app.route('/<id>')
def current_game(id: str):
    try:
        return render_template(
            template_name_or_list="info.html",
            ctx_game=games[int(id)]
        )
    except:
        return "Произошла ошибка"

@app.route('/reg', methods=['GET','POST'])
def registration() -> flask.Response:
    if flask.request.method == "POST":
        data:dict[str,str] = flask.request.form
        users.append(
            models.User.create(**data, users=users)
            
        )
    return render_template('reg.html')

@app.route("/search", methods=['GET','POST'])
def search_games():
    find_data:str = request.form.get('search')
    result: list[games.Game]=[]
    for game in games:
        if find_data in game['title']:
            result.append(game)
    if len(result) <= 0:
        return "no post"
        
    return render_template(
        template_name_or_list="search.html", 
        ctx_games=enumerate(result)
    )

@app.route('/login', methods=['GET','POST'])
def login() -> flask.Response:
    if flask.request.method == "POST":
        data:dict = flask.request.form
        for i in users:
            if (i.login == data.get('login')
            ) and (
                i.password == data.get('password')
            ):  
                for i in users:
                    return render_template('lk.html', user=i)
            else:
                return render_template('error.html')
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8050,
        debug=True
    )