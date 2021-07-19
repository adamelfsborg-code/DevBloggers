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