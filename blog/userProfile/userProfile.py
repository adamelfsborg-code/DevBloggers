from base import db


class Profile:
    def add_article(self, **kwargs):
        if kwargs['article_id'] == '':
            sql = "INSERT INTO articles (user_id, blocks,publish_date,category_id) VALUES (%s,%s,%s,%s) RETURNING id"
            sqldata = (kwargs['user_id'],kwargs['blocks'],kwargs['publish_date'],kwargs['category_id'])
        else:
            sql = "UPDATE articles SET blocks=%s,category_id=%s WHERE id=%s RETURNING 'updated' AS article_updated"
            sqldata = (kwargs['blocks'],kwargs['category_id'],kwargs['article_id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def add_category(self, **kwargs):
        if kwargs['id'] == '':
            sql = "INSERT INTO categories (user_id,name,icon,background_color,text_color) VALUES (%s,%s,%s,%s,%s) RETURNING id"
            sqldata = (kwargs['user_id'],kwargs['name'],kwargs['icon'],kwargs['background_color'],kwargs['text_color'])
        else:
            sql = "UPDATE categories SET name=%s,icon=%s,background_color=%s, text_color=%s WHERE id=%s RETURNING 'updated' AS category_updated"
            sqldata = (kwargs['name'],kwargs['icon'],kwargs['background_color'],kwargs['text_color'],kwargs['id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor
    
    def get_user_categories(self,user_id):
        sql = "SELECT id,user_id,name,icon,text_color,background_color FROM categories WHERE user_id=%s"
        sqldata = (user_id, )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_user_articles(self, **kwargs):
        sql = "SELECT   articles.id as id,articles.user_id,blocks,publish_date,categories.id as category_id, categories.name, categories.background_color, categories.text_color,categories.icon FROM articles FULL JOIN categories ON categories.id = articles.category_id WHERE articles.user_id=%s ORDER BY articles.created_at DESC LIMIT {0} OFFSET {1}".format(kwargs['limit'],kwargs['offset'])
        sqldata = (kwargs['user_id'], )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_articles_count(self, user_id):
        sql = "SELECT COUNT(user_id) FROM articles WHERE user_id=%s GROUP BY user_id"
        sqldata = (user_id, )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_followers_growth(self, **kwargs):
        sql = "SELECT COUNT(following_user) FROM followers WHERE following_user=%s GROUP BY following_user"
        sqldata = (kwargs['user_id'], )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        if len(cursor) > 0:
            for i in cursor:
                total = i.get('count')
        else:
            return 0
        
        sql = "SELECT COUNT(following_user) FROM followers WHERE EXTRACT(week FROM created_at) = EXTRACT(week FROM timestamp %s) AND FOLLOWING_USER =%s GROUP BY following_user"
        sqldata = (kwargs['date'],kwargs['user_id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        if len(cursor) > 0:
            for i in cursor:
                growth = i.get('count')
        else:
            return 0

        percentage  = int(growth) / int(total) 
        followers = {
            'percentage': "{:.0%}".format(percentage),
            'total': total,
        }

        return followers
    def get_readers_growth(self, **kwargs):
        sql = "SELECT COUNT(blogger_id) FROM readers WHERE blogger_id=%s GROUP BY blogger_id"
        sqldata = (kwargs['user_id'], )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        if len(cursor) > 0:
            for i in cursor:
                total = i.get('count')
        else:
            return 0

        sql = "SELECT COUNT(blogger_id) FROM readers WHERE EXTRACT(week FROM created_at) = EXTRACT(week FROM timestamp %s) AND blogger_id=%s GROUP BY blogger_id"
        sqldata = (kwargs['date'],kwargs['user_id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        if len(cursor) > 0:
            for i in cursor:
                growth = i.get('count')
        else:
            return 0

        percentage = int(total) / int(growth)

        readers = {
            'percentage': "{:.0%}".format(percentage),
            'total': total
        }

        return readers 

    def get_likes_growth(self, **kwargs):
        sql = "SELECT COUNT(blogger_id) FROM likes WHERE blogger_id=%s GROUP BY blogger_id"
        sqldata = (kwargs['user_id'],)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        if len(cursor) > 0:
            for i in cursor:
                total = i.get('count')
        else:
            return 0

        sql = "SELECT COUNT(blogger_id) FROM likes WHERE EXTRACT(week FROM created_at) = EXTRACT(week FROM timestamp %s) AND blogger_id=%s GROUP BY blogger_id"
        sqldata = (kwargs['date'],kwargs['user_id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        if len(cursor) > 0:
            for i in cursor:
                growth = i.get('count')
        else:
            return 0

        percentage = int(total) / int(growth)

        likes = {
            'percentage': "{:.0%}".format(percentage),
            'total': total
        }

        return likes       

    def get_comments_growth(self, **kwargs):
        sql = "SELECT COUNT(blogger_id) FROM comments WHERE blogger_id=%s GROUP BY blogger_id"
        sqldata = (kwargs['user_id'],)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        if len(cursor) > 0:
            for i in cursor:
                total = i.get('count')
        else:
            return 0

        sql = "SELECT COUNT(blogger_id) FROM comments WHERE EXTRACT(week FROM created_at) = EXTRACT(week FROM timestamp %s) AND blogger_id=%s GROUP BY blogger_id"
        sqldata = (kwargs['date'],kwargs['user_id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        if len(cursor) > 0:
            for i in cursor:
                growth = i.get('count')
        else:
            return 0

        percentage = int(total) / int(growth)

        comments = {
            'percentage': "{:.0%}".format(percentage),
            'total': total
        }

        return comments     

    def get_notifications(self,user_id):
        sql = "SELECT id,notification FROM notifications WHERE user_id=%s ORDER BY created_at DESC"
        sqldata = (user_id, )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_message_rooms(self,user_id):
        sql = "SELECT message_rooms.id,is_unread,unread_user,u_1.id as u1_id ,u_1.username as u1_username ,u_1.profile_image as u1_profile_image,u_2.id as u2_id,u_2.username as u2_username ,u_2.profile_image as u2_profile_image FROM MESSAGE_ROOMS FULL JOIN users u_1 ON message_rooms.USER_1 = u_1.id FULL JOIN users u_2 ON message_rooms.USER_2 = u_2.id WHERE user_1=%s OR user_2=%s ORDER BY is_unread DESC"
        sqldata = (user_id,user_id)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_messages(self, room_id):
        sql = "SELECT room_id,sender,receiver,message FROM messages WHERE room_id=%s"
        sqldata = (room_id, )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor