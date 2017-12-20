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
    #events of past 3 days
    print(globUser)
    cursor = conn.cursor()
    query = 'SELECT * FROM an_event WHERE start_time >= cast((now()) as date) AND start_time < cast((now() + interval 29 day) as date)'
    cursor.execute(query)
    nextThreeDays = cursor.fetchall()
    cursor.close()
    error = None
    if(nextThreeDays):
        return render_template('index.html', posts = nextThreeDays, message = globUser)
    else:
        error = "Sorry, no upcoming events"
        return render_template('index.html', errorUpcoming = error, message = globUser)

@app.route('/logout')
def logout():
    global globUser
    globUser = None
    session.pop('username')
    return redirect('/')


if __name__ == "__main__":
    app.run()