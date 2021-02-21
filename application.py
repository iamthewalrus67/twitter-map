'''
Main Flask module.
'''

from flask import Flask, render_template, request, redirect
import twitter_helper
import webmap

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map', methods=['POST', 'GET'])
def create_map():
    if request.method == 'POST':
        twitter_username = request.form.get('username')
        try:
            user_friends = twitter_helper.get_user_friends(
                twitter_username, 100)
        except KeyError:
            return redirect('/failure')
        friends_coordinates = twitter_helper.get_users_coordinates(
            user_friends)

        friends_map = webmap.create_map()
        webmap.place_markers(friends_map, friends_coordinates)
        webmap.save_map(friends_map, 'templates/map.html')
        return render_template('map.html')


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/failure')
def failure():
    return render_template('failure.html')


if __name__ == '__main__':
    app.run(debug=True)
