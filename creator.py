from fake_food_spider.connection import engine
import fake_food_spider.database as database

if __name__ == '__main__':
    database.StartUrl.__table__
    database.Base.metadata.create_all(engine)
