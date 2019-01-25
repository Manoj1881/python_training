import pymysql
import re
from app import app
from tables import Results
from dbconfig import mysql
from flask import flash, render_template, request, redirect
@app.route('/new_user')
def add_user_view():
    return render_template('add.html')
@app.route('/add', methods=['POST'])
def add_user():
   _name=request.form['inputName']
   _email=request.form['inputEmail']
   _password=request.form['inputPassword']
   _conformpassword=request.form['inputconformpassword']
   _gender=request.form['inputgender']
   _mobileno=request.form['inputmobileno']
   _address=request.form['inputaddress']
		# validate the received values
   match_mob= re.search(r'((?:\(?\+?91\)?)?0?\d{10})',_mobileno)
   if match_mob:
       print(match_mob.group(0))
   else:
       print("not valid")
       return "please enter correct mobile no"
   match = re.search(r'[\w.-]+@[\w.-]+.\w+',_email)
   if match:
               print( "valid email :::", match.group())
   else:
              print ("not valid:::")
              return "please enter correct email id"
   if _password== _conformpassword:
                print("valid")
   else:
                print("not valid")
                return "please enter correct password"
   try:
        if _name and _email and _password and _conformpassword and _mobileno and _gender and _address and request.method == 'POST':
			#do not save password as a plain text
            #_hashed_password = generate_password_hash(_password)
			# save edits
            sql = "INSERT INTO task2(user_name,user_email,user_password,user_conformpassword,user_mobileno,user_gender,user_address) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            data = (_name,_email,_password,_conformpassword,_mobileno,_gender,_address,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('User added successfully!')
            return redirect('/')
        else:
            return 'Error while adding user'
   except Exception as e:
	    	print(e)
   finally:
        cursor.close() 
        conn.close()
@app.route('/')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM task2")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('users.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
@app.route('/edit/<int:id>')
def edit_view(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM task2 WHERE user_id=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Error loading #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
@app.route('/update', methods=['POST'])
def update_user():
    _name=request.form['inputName']
    _email=request.form['inputEmail']
    _password=request.form['inputPassword']
    _conformpassword=request.form['inputconformpassword']
    _gender=request.form['inputgender']
    _mobileno=request.form['inputmobileno']
    _address=request.form['inputaddress']
    _id=request.form['id']
		# validate the received values
    match_mob= re.search(r'((?:\(?\+?91\)?)?0?\d{10})',_mobileno)
    if match_mob:
        print(match_mob.group(0))
    else:
        print("not valid")
        return "please enter correct mobile no"
    match = re.search(r'[\w.-]+@[\w.-]+.\w+',_email)
    if match:
        print( "valid email :::", match.group())
    else:
        print ("not valid:::")
        return "please enter correct email id"
    if _password== _conformpassword:
        print("valid")
    else:
        print("not valid")
        return "please enter correct password"
    try:
        if _name and _email and _password and _conformpassword  and _mobileno and _gender and _address and  _id and request.method == 'POST':
			#do not save password as a plain text
		#	_hashed_password = generate_password_hash(_password)
			# save edits
            sql = "UPDATE task2 SET user_name=%s, user_email=%s, user_password=%s, user_conformpassword=%s, user_mobileno=%s, user_gender=%s, user_address=%s WHERE user_id=%s"
            data = (_name,_email,_password,_conformpassword,_mobileno,_gender,_address, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('User updated successfully!')
            return redirect('/')
        else:
             return 'Error while updating user'
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
		
@app.route('/delete/<int:id>')
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM task2 WHERE user_id=%s", (id,))
		conn.commit()
		flash('User deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
if __name__ == "__main__":
    app.debug = True
    app.run()# -*- coding: utf-8 -*-

