from base import db

class User:
    def getUser(self, token):
        sql = "SELECT id,is_blogger,profile_image,fullname,username,email FROM users WHERE token=%s"
        sqldata = (token,)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def checkIfEmailExists(self, email):
        sql = "SELECT email FROM users WHERE email=%s"
        sqldata = (email, )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor


    def checkIfUsernameExists(self, username):
        sql = "SELECT username FROM users WHERE username=%s"
        sqldata = (username, )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def createUser(self, **kwargs):
        if kwargs['id'] == '':
            sql = "INSERT INTO users (is_blogger, fullname,username,email,password) VALUES(%s,%s,%s,%s,%s)"
            sqldata = (kwargs['is_blogger'],kwargs['full_name'],kwargs['username'],kwargs['email'],kwargs['password'])
        else:
            sql = "UPDATE users SET is_blogger=%s,fullname=%s,profile_image=%s,email=%s,password=%s WHERE id=%s"
            sqldata = (kwargs['is_blogger'],kwargs['full_name'],kwargs['profile_image'],kwargs['email'],kwargs['password'],kwargs['id'])
        
        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def loginUser(self, **kwargs):
        sql = "SELECT id FROM users WHERE email=%s AND password=%s LIMIT 1"
        sqldata = (kwargs['email'],kwargs['password'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()
        print(cursor)
        if len(cursor) > 0:
            
            for i in cursor:
                id = i.get('id')
            print(id)
            sql = "UPDATE users SET token=%s WHERE id=%s"
            sqldata = (kwargs['token'],id)
        
            c = db.cursor('blog', sql, sqldata)
            cursor = c.connect()

            return cursor
        return '404'

    def logoutUser(self, id):
        sql = "UPDATE users SET token=null WHERE id=%s"
        sqldata = (id,)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()
        return cursor 