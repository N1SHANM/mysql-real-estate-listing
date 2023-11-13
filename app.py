from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app=Flask(__name__)


def load_properties_from_db():
    properties_list = []
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM property"))
        columns = result.keys()
        for row in result:
            try:
                properties_list.append({col: val for col, val in zip(columns, row)})
            except Exception as e:
                print(f"Error converting row {row} to dictionary: {e}")
    return properties_list


  


@app.route("/")
def hello_estates():
    properties_list = load_properties_from_db()
    return render_template('home.html', properties_list=properties_list)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        user_type = request.form['user_type'] 

        if user_type == 'buyer':
            insert_to_table('buyer', name, email, phone)
        elif user_type == 'seller':
            insert_to_table('seller', name, email, phone)

        return redirect('/')
@app.route('/signin')
def signin():
    return render_template('signin.html')
@app.route('/get_buyer_id', methods=['POST'])
def get_buyer_id():
    if request.method == 'POST':
        buyer_name = request.form.get('name')
        buyer_password = request.form.get('password')

        # Query the database to get the buyer_id
        buyer = Buyer.query.filter_by(name=buyer_name, password=buyer_password).first()

        if buyer:
            buyer_id = buyer.id
            return f'Buyer ID: {buyer_id}'
        else:
            return 'Buyer not found'

@app.route('/buyer_properties/<int:buyer_id>')
def display_buyer_properties(buyer_id):
    buyer = Buyer.query.get(buyer_id)

    if buyer:
        properties = buyer.properties
        return render_template('buyer_properties.html', properties=properties)
    else:
        return 'Buyer not found'


  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)