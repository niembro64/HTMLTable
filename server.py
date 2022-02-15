from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def funRoot():
    return 'ROOT, Please add /lists'


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template("lists.html", rrr=[3, 1, 5], user_list=users)


@app.route('/<row>/<col>/<color1>/<color2>')
def play(row, col, color1, color2):
    return render_template("index.html", Rcol=int(col), Rrow=int(row), Rcolor1=color1, Rcolor2=color2)


if __name__ == "__main__":
    app.run(debug=True)
