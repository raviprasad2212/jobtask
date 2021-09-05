from sqlite3.dbapi2 import DatabaseError
from flask_restful import Resource, Api, request
from flask import jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from database import cursor, conn

auth = HTTPBasicAuth()



# User exists or not.
# I am not creating any users data.
# I am using only static data for user authentication purpose.
# Please copy user name and password whenever testing this application.
def check_user(username, password):
    data = {
        "user1": "Ravi@143",
        "user2": "Kalyan@143",
        "ramdev": "prasad@45545"
    }

    if (username in data):
        if (data[username] == password):
            return True
        else:
            return False


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    else:
        data = check_user(username, password)
        if (data == True):
            return {username: password}

# RESTful API
class Tasks(Resource):
    @auth.login_required
    def get(self):
        try:
            fetch_data = ('select * from task')
            cursor.execute(fetch_data)
            result = cursor.fetchall()
            conn.commit()
            conn.close()
            return {"data": result}
        
        except DatabaseError as error:
            return jsonify({'error':(str(error))})

    
    @auth.login_required
    def post(self):
        # Mostly we are using json
        try:

            if (request.json):
                data = request.json
            if (request.form):
                data = request.form

            if (data['id']):
                id = data['id']
                title = data['title']
                description = data['description']
                done = data['done']

                database_query = ('insert into task(id, title, description, done) values(%s, %s, %s, %s)')
                cursor.execute(database_query, (id, title, description, done))
                conn.commit()
                conn.close()
                return jsonify({'task': "Task is created"})
            else:
                return jsonify({'data': 'required id'})

        except DatabaseError as error:
            return jsonify({'error': str(error)})


class Tasks2(Resource):
    @auth.login_required
    def get(self, id):

        try:
            get_particular_data = ('select * from task where id=%s')
            cursor.execute(get_particular_data,(id,))
            result = cursor.fetchall()
            if (len(result) == 0):
                return jsonify({'data': 'The id {} is not exist'})
            return jsonify({'data': result})
        except DatabaseError as error:
            return jsonify({'error': str(error)})
    
    @auth.login_required
    def put(self, id):
        try:
            if (request.json):
                data = request.json
            if (request.form):
                data = request.form

            if (id):
                id = id
                title = data['title']
                description = data['description']
                done = data['done']

                get_particular_data = ('select * from task where id=%s')
                cursor.execute(get_particular_data,(id,))
                result = cursor.fetchall()
                if (len(result) == 0):
                    return jsonify({'data': '{} not exist'.format(id)})

                params = []
                update_block = []
                if (title):
                    update_block.append(' title = %s ')
                    params.append(title)


                if (description):
                    update_block.append(' description = %s ')
                    params.append(description)


                if (done):
                    update_block.append(' done = %s ')
                    params.append(done)
                
                update_str = ','.join(update_block)
                update_query = ('update task set {} where id=%s'.format(update_str))
                params.append(id)
                cursor.execute(update_query, params)
                conn.commit()

                return jsonify({'data': 'successfully updated the task'})

        except DatabaseError as error:
            return jsonify({'error': str(error)})

    @auth.login_required
    def delete(self, id):
        try:
            # check id exists or not
            check_id = ('select id from task where id=%s')
            cursor.execute(check_id, (id, ))
            result = cursor.fetchone()
            print(result)
            # If the result is zero return id not exists
            if (result == None):
                return jsonify({'data': 'The id {} not exist'.format(id)})
            
            delete_query = ('delete from task where id=%s')
            cursor.execute(delete_query, (id,))
            conn.commit()
            return jsonify({'data': '{} successfully deleted'.format(id)})

        except DatabaseError as error:
            return jsonify({'error': str(error)})
