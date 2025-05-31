from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/user/<int:id>')
def user(id):
    # Greet the user
    return render_template("user.html", id=id)

# Pass the required route to the decorator.
@app.route("/about")
def about():
    return render_template("about.html")
  
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # Set debug=True for development
# To run the application, use the command: python main.py