from flask import render_template
from app import app

@app.route('/m')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title= 'Home-Welcome to The best Moie Review Website Online'
    return render_template('index.html',title = title)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id= movie_id)    
