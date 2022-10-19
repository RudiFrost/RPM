from flask import Flask
from data import db_session
from data.users import User
from data.news import News
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Вторая новость", content="Уже вторая запись!",
                user=user, is_private=False)
    db_sess.add(news)
    db_sess.commit()


if __name__ == '__main__':
    main()
