from base import db


class Profile:
    def addArticle(self, **kwargs):
        if kwargs['article_id'] == '':
            sql = "INSERT INTO articles (user_id, blocks,publish_date) VALUES (%s,%s,%s) RETURNING id"
            sqldata = (kwargs['user_id'],kwargs['blocks'],kwargs['publish_date'])
        else:
            sql = "UPDATE articles SET blocks=%s WHERE id=%s RETURNING 'updated' AS article_updated"
            sqldata = (kwargs['blocks'],kwargs['article_id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def addCategory(self, **kwargs):
        if kwargs['id'] == '':
            sql = "INSERT INTO category (user_id,name,icon,background_color,text_color) VALUES (%s,%s,%s,%s,%s) RETURNING id"
            sqldata = (kwargs['user_id'],kwargs['name'],kwargs['icon'],kwargs['background_color'],kwargs['text_color'])
        else:
            sql = "UPDATE category SET name=%s,icon=%s,background_color=%s, text_color=%s WHERE id=%s RETURNING 'updated' AS category_updated"
            sqldata = (kwargs['name'],kwargs['icon'],kwargs['background_color'],kwargs['text_color'],kwargs['id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor