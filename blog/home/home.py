from base import db


class Home:
    def get_trending_categories(self,date):
        sql = "SELECT count(categories.name),categories.name,categories.icon FROM articles FULL JOIN categories ON articles.category_id = categories.id WHERE EXTRACT(week FROM articles.created_at) = EXTRACT(week FROM timestamp %s) OR EXTRACT(month FROM articles.created_at) = EXTRACT(month FROM timestamp %s)  GROUP BY categories.name,categories.icon ORDER BY COUNT DESC"
        sqldata = (date,date)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_trending_articles(self,date):
        sql = "SELECT COUNT(article_id),articles.blocks, articles.id,publish_date,categories.icon FROM readers INNER JOIN articles ON readers.article_id = articles.id INNER JOIN categories ON articles.category_id = categories.id WHERE EXTRACT(week FROM readers.created_at) = EXTRACT(week FROM timestamp %s) OR EXTRACT(month FROM articles.created_at) = EXTRACT(month FROM timestamp %s) GROUP BY articles.id,publish_date,categories.icon ORDER BY COUNT DESC"
        sqldata = (date,date)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_last_visits(self, **kwargs):
        sql = "SELECT visits.id,visit_id,is_blogger,username,profile_image FROM visits INNER JOIN users ON visits.visit_id = users.id WHERE EXTRACT(month FROM visits.created_at) = EXTRACT(month FROM timestamp %s) AND user_id=%s ORDER BY visits.created_at DESC LIMIT 10"
        sqldata = (kwargs['date'],kwargs['user_id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor
    
    def get_bloggers_search(self, param):
        sql = "SELECT id,username,profile_image,fullname FROM users WHERE is_blogger = true AND LOWER(username) LIKE LOWER(%s) OR LOWER(fullname) LIKE LOWER(%s)"
        sqldata = (param + '%',param + '%')

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_categories_search(self, param):
        sql = "SELECT id,icon,name,background_color,text_color FROM categories WHERE LOWER(name) LIKE LOWER(%s)"
        sqldata = (param + '%', )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor 

    def get_articles_search(self, param):
        sql = "SELECT blocks -> 0 -> 'data' ->> 'text' AS name,publish_date,articles.id,users.username,user_id FROM articles INNER JOIN users ON articles.user_id = users.id WHERE LOWER(blocks -> 0 -> 'data' ->> 'text') LIKE LOWER(%s)"
        sqldata = (param + '%', )

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor 

    def get_latest_articles(self, **kwargs):
        if kwargs['followers_only']:
            sql = "SELECT blocks -> 0 -> 'data' ->> 'text' AS name,publish_date,articles.id,users.username,user_id FROM articles INNER JOIN users ON articles.user_id = users.id INNER JOIN FOLLOWERS ON articles.user_id = followers.FOLLOWING_USER WHERE FOLLOWER_USER=%s ORDER BY articles.created_at"
            sqldata = (kwargs['user_id'],)
        else:
            sql = "SELECT blocks -> 0 -> 'data' ->> 'text' AS name,publish_date,articles.id,users.username,user_id FROM articles INNER JOIN users ON articles.user_id = users.id ORDER BY articles.created_at"
            sqldata = ()
        
        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor 

    def articles(self,**kwargs):
        sql = "SELECT blocks -> 0 -> 'data' ->> 'text' AS name,publish_date,articles.id,users.username,articles.user_id FROM articles INNER JOIN users ON articles.user_id = users.id inner join categories on articles.category_id = categories.id where categories.name = %s order by ARTICLES.CREATED_AT desc limit %s offset %s"
        sqldata = (kwargs['category_name'],kwargs['limit'],kwargs['offset'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor 

    def category(self, name):
        sql = "SELECT id,name,icon,background_color,text_color FROM categories WHERE name=%s LIMIT 1"
        sqldata = (name,)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor 
    
    def get_articles_count(self, category_name):
        sql = "SELECT COUNT(*) FROM articles INNER JOIN categories ON articles.category_id = categories.id where categories.name=%s"
        sqldata = (category_name,)
        
        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor 