from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/")
def index():
    print("Index method was triggered")
    return "In index method"

@app.route("/name/<string:user_name>/<int:number>")
def say_name(user_name, number):
    print(f"In say_name method, hi {user_name}")
    # know how many form have submitted?
    session.setdefault('count_of_forms', 0)
    # session['count_of_forms'] = 0
    print(f"# of forms submitted {session['count_of_forms']}")

    return render_template("index.html", name_for_template = user_name, num_for_template = number)

@app.route("/process_form", methods=['POST'])
def process():
    print(request.form['user_name'])
    # save the info to the db
    session['count_of_forms'] += 1
    

    return redirect('/name/Phil/0')

@app.route('/start_over')
def reset_form_count():
    session.clear()
    return redirect('/name/Phil/0')

app.run(debug=True)



'''
    Post request
    Session
    Redirect
'''

