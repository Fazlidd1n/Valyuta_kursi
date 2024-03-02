from bs4 import BeautifulSoup
import requests
from sqlalchemy import BIGINT, select, update, insert
from sqlalchemy.orm import Mapped, mapped_column

from db.config import engine, Base, session

engine.connect()


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(__type_pos=BIGINT, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True, __type_pos=BIGINT)
    fullname: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)

    def insert(self, user_id, fullname, username):
        user_data = {
            "user_id": user_id,
            "fullname": fullname,
            "username": username,
        }
        user: User | None = session.execute(select(User).where(User.user_id == user_id)).fetchone()
        if not user:
            query = insert(User).values(**user_data)
            session.execute(query)
            session.commit()

    def select(self):
        users_datas = session.execute(select(User.user_id, User.fullname, User.username)).fetchall()
        return users_datas

    def delete(self):
        pass


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(__type_pos=BIGINT, autoincrement=True, primary_key=True)
    course_name: Mapped[str] = mapped_column()
    course_buy: Mapped[float] = mapped_column()
    course_sell: Mapped[float] = mapped_column()

    def insert(self, data: dict):
        session.execute(
            insert(Course),
            [
                {"course_name": "USD", "course_buy": float(data.get("USD")[0]),
                 "course_sell": float(data.get("USD")[1])},
                {"course_name": "EUR", "course_buy": float(data.get("EUR")[0]),
                 "course_sell": float(data.get("EUR")[1])},
                {"course_name": "RUB", "course_buy": float(data.get("RUB")[0]),
                 "course_sell": float(data.get("RUB")[1])},
                {"course_name": "GBP", "course_buy": float(data.get("GBP")[0]),
                 "course_sell": float(data.get("GBP")[1])},
                {"course_name": "CHF", "course_buy": float(data.get("CHF")[0]),
                 "course_sell": float(data.get("CHF")[1])},
                {"course_name": "JPY", "course_buy": float(data.get("JPY")[0]),
                 "course_sell": float(data.get("JPY")[1])},
                {"course_name": "KZT", "course_buy": float(data.get("KZT")[0]),
                 "course_sell": float(data.get("KZT")[1])},
            ]
        )
        session.commit()

    def select(self):
        course_data = session.execute(select(Course.course_name, Course.course_buy, Course.course_sell)).fetchall()
        course_datas = {}
        for i in course_data:
            course_datas[i[0]] = [i[1], i[2]]
        return course_datas

    def select_currencies(self):
        response = requests.get("https://nbu.uz/uz/exchange-rates/")
        soup = BeautifulSoup(response.text, 'html.parser')
        s = 0
        currencies = {}
        for i in soup.find_all("tr"):
            if s == 8:
                break
            currency_elements = i.find_all('td')
            if currency_elements:
                currency_name = currency_elements[0].text.split(', ')[1].strip()
                currency_buy = currency_elements[1].text
                currency_sell = currency_elements[2].text
                currencies[currency_name] = [currency_buy, currency_sell]
            s += 1
        return currencies

    def update(self):
        currencies = Course.select_currencies(Base)
        for i in currencies.keys():
            query = update(Course).where(Course.course_name == i).values(
                course_buy=float(currencies.get(i)[0]),
                course_sell=float(currencies.get(i)[1]))
            session.execute(query)
            session.commit()


Base.metadata.create_all(engine)

if not Course.select(Base):
    Course.insert(Base, Course.select_currencies(Base))

else:
    Course.update(Base)
