from base import db


class Home:
    def get_trending_categories(self,date):
        sql = "SELECT count(categories.name),categories.name,categories.icon FROM articles FULL JOIN categories ON articles.category_id = categories.id WHERE EXTRACT(week FROM articles.created_at) = EXTRACT(week FROM timestamp %s)  GROUP BY categories.name,categories.icon ORDER BY COUNT DESC"
        sqldata = (date,)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_trending_articles(self,date):
        sql = "SELECT COUNT(article_id),articles.blocks, articles.id,publish_date,categories.icon FROM readers INNER JOIN articles ON readers.article_id = articles.id INNER JOIN categories ON articles.category_id = categories.id WHERE EXTRACT(week FROM readers.created_at) = EXTRACT(week FROM timestamp %s) GROUP BY articles.id,publish_date,categories.icon ORDER BY COUNT DESC"
        sqldata = (date,)

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor

    def get_last_visits(self, **kwargs):
        sql = "SELECT visits.id,visit_id,is_blogger,username,profile_image FROM visits FULL JOIN users ON visits.visit_id = users.id WHERE EXTRACT(month FROM visits.created_at) = EXTRACT(month FROM timestamp %s) AND user_id=%s ORDER BY visits.created_at DESC LIMIT 10"
        sqldata = (kwargs['date'],kwargs['user_id'])

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor