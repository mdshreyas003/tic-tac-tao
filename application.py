from flask import Flask, render_template,session,url_for,redirect
app = Flask(__name__)

grid = [[None,None,None],[None,None,None],[None,None,None]]
turn = 'X'

@app.route("/")
def index():
    return render_template('./game.html',grid = grid, turn=turn)

@app.route("/<int:row>/<int:col>")
def play(row,col):
    grid[row][col] = turn
    return redirect(url_for('index'))



