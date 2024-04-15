from flask import Flask, request, render_template, session, redirect, url_for, flash
import db

app = Flask(__name__)
app.secret_key = "hallelujah"

@app.route('/')
def home():
    if "signed_in" not in session:
        return render_template("index.html")  
    if 'student_id' in session['data']:      
        return render_template("dash.html", name=session['data']['name'], complaints=db.get_complaints(session['data']['student_id'], "student"))
    return render_template("admin_dash.html", name=session['data']['name'], complaints=db.get_complaints(session['data']['hostel'], "admin"))


@app.route('/signin-student', methods=['POST'])
def signin_student():
    form_data = request.form
    print(form_data)
    if db.verify_student(form_data):
        session["signed_in"] = True
        session["data"] = db.get_data(form_data['student_id'], 'student')
        flash("Logged in!", category="success")
        return redirect(url_for("home"))
    else:
        flash("Invalid Credentials", category="error")
        return redirect(url_for("home"))


@app.route('/signin-admin', methods=['POST'])
def signin_admin():
    form_data = request.form
    if db.verify_admin(form_data):
        session["signed_in"] = True
        session["data"] = db.get_data(form_data['admin_hostel'], 'admin')
        flash("Logged in!", category="success")
        return redirect(url_for("home"))
    else:
        flash("Invalid Credentials", category="error")
        return redirect(url_for("home"))

@app.route("/signup-student", methods=["POST"])
def signup_student():
    form_data = request.form
    if not db.verify_student(form_data):
        db.insert_student(form_data)
        session["signed_in"] = True
        session["data"] = db.get_data(form_data['student_id'], 'student')
        flash("Logged in!", category="success")
    return redirect(url_for("home"))

@app.route("/signup-admin", methods=["POST"])
def signup_admin():
    form_data = request.form
    if not db.verify_admin(form_data):
        db.insert_admin(form_data)
        session["signed_in"] = True
        session["data"] = db.get_data(form_data['admin_hostel'], 'admin')
        flash("Logged in!", category="success")
    return redirect(url_for("home"))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/new_complaint", methods=["GET", "POST"])
def new_complaint(): 
    if request.method == "GET":
        if "student_id" not in session['data']:
            return redirect(url_for("home"))
        return render_template("complaint.html")
    form_data = request.form
    db.insert_complaint(form_data, session)
    return redirect(url_for("home"))

@app.route('/complaint/<id_>', methods=['GET', 'POST'])    
def show_complaint(id_):
    if request.method == "GET":
        complaint = db.get_complaint(id_)
        return render_template("blank.html", the_id=id_, type=complaint[2], text=complaint[3], status=complaint[5])

    db.update_complaint_status(id_, request.form['status'])
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
