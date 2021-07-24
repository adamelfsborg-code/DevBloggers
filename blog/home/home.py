from base import db


class Home:
    def get_trending_categories(self):
        sql = "SELECT count(categories.name),categories.name,categories.icon FROM articles FULL JOIN categories ON articles.category_id = categories.id GROUP BY categories.name,categories.icon ORDER BY count DESC"
        sqldata = ()

        c = db.cursor('blog', sql, sqldata)
        cursor = c.connect()

        return cursor