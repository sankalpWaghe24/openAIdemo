from flask import Flask,request,jsonify

app = Flask(__name__)


# @app.route("/post/<int:id>")
# def show_post(id):
#     # Shows the post with given id.
#     return f"This post has the id {id}"


# @app.route("/user/<username>")
# def show_user(username):
#     # Greet the user
#     return f"Hello {username} !"

@app.route("/users",methods=['POST'])
def create_user():
    request_body = request.get_json()
    new_user = {
        'name':request_body['name'],
        'age':request_body['age'],
    }
    return jsonify(new_user)


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

# Pass the required route to the decorator.
@app.route("/hello")
def hello():
    return "Hello, Welcome to GeeksForGeeks"


@app.route("/")
def index():
    return "Homepage of GeeksForGeeks"


if __name__ == "__main__":
    app.run(debug=True)
