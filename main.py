from flask import Flask, render_template
from model import Model
from view import View
from controller import Controller

app = Flask(__name__)
model = Model()
view = View()
controller = Controller(model, view)

@app.route('/')
def index():
    task = model.get_tasks()
    return render_template('inde.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
