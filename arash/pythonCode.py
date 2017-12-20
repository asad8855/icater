from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import hashlib

globUser = None

def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


app =Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

conn = pymysql.connect(host='websys3.stern.nyu.edu',
                       user='websysF17GB2',
                       password='websysF17GB2!!',
                       db='websysF17GB2',
                       charset='utf8mb4', use_unicode = True,
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to index
#chekc if user is in session
@app.route('/' , methods=['GET','POST'])
def index():
    cursor = conn.cursor()
    query = 'SELECT * FROM  restaurant_data;'
    cursor.execute(query)
    restaurantinfo = cursor.fetchall()
    cursor.close()
    error = None
    return render_template('index.html', restaurants = restaurantinfo, menus = restaurant_menu)
 

    #Menu function
@app.route('/menus' , methods=['GET','POST'])
def menus(rest_id):
    cursor = conn.cursor()
    query = 'SELECT * FROM appetizers_menu WHERE restaurant_id = %s UNION ALL SELECT * FROM mains_menu WHERE restaurant_id = %s UNION ALL SELECT * FROM desserts_menu WHERE restaurant_id = %s UNION ALL SELECT * FROM other_menu WHERE restaurant_id = %s;'
    cursor.execute(query,(rest_id,rest_id,rest_id,rest_id,))
    restaurant_menu = cursor.fetchall()
    cursor.close()
    error = None
    return render_template('index.html', menus = restaurant_menu)

@app.route('/order', methods=['GET', 'POST'])
def order():
    max_order_id = cursor.execute('select MAX(customer_id) FROM customer_data;')
    order_id = max_order_id + 1
    cursor = conn.cursor()
    item_name = request.form['item_name']
    item_quantity = request.form['quantity']
    item_price = request.form['price']
    user_id = request.form['user_id']
    restaurant_id = request.form['restaurant_id']
    ins = 'INSERT INTO orders VALUES (%s,%s,%s,%s,%s,%s)'
    cursor.execute(ins , (order_id,user_id,restaurant_id,item_name,item_quantity,item_price))
    conn.commit()
    cursor.close()
    return render_template('index.html')
	
	

    
    
    
@app.route('/user_reg' , methods=['GET', 'POST'])
def user_reg():
    #grab information from register page
    max_id = cursor.execute('select MAX(customer_id) FROM customer_data;')
    userid = max_id + 1
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']
    email = request.form['email']
    ins = 'INSERT INTO customer_data VALUES (%s,%s,%s,%s,%s)'
    cursor.execute(ins , (userid,firstname,lastname,password,email))
    conn.commit()
    cursor.close()
    return render_template('index.html')

@app.route('/user_address' , methods=['GET', 'POST'])
def user_address():
    #grab information from register page
    max_id = cursor.execute('select MAX(customer_id) FROM customer_address;')
    userid = max_id + 1
    street_name = request.form['street_name']
    street_number = request.form['street_number']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip']
    ins = 'INSERT INTO customer_address VALUES (%s,%s,%s,%s,%s,%s)'
    cursor.execute(ins , (userid,street_name,street_number,city,state,zip_code))
    conn.commit()
    cursor.close()
    return render_template('index.html')

@app.route('/user_card' , methods=['GET', 'POST'])
def user_card():
    #grab information from register page
    max_id = cursor.execute('select MAX(customer_id) FROM customer_payment;')
    userid = max_id + 1
    cardholder_name= request.form['cardholder_name']
    cardholder_company = request.form['cardholder_company']
    card_number = request.form['card_number']
    card_csv = request.form['card_csv']
    expiration_month = request.form['expiration_month']
    expiration_year = request.form['expiration_year']
    ins = 'INSERT INTO customer_payment VALUES (%s,%s,%s,%s,%s)'
    cursor.execute(ins , (userid,cardholder_name,cardholder_company,card_number,card_csv,expiration_month,expiration_year))
    conn.commit()
    cursor.close()
    return render_template('index.html')


@app.route('/logout')
def logout():
    global globUser
    globUser = None
    session.pop('username')
    return redirect('/')


if __name__ == "__main__":
    app.run()
