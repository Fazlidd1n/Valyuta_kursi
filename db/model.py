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
    course_price: Mapped[float] = mapped_column()

    def insert(self, data: dict):
        session.execute(
            insert(Course),
            [
                {"course_name": "USD", "course_price": float(data.get("USD").replace(" ", ""))},
                {"course_name": "RUB", "course_price": float(data.get("RUB").replace(" ", ""))},
                {"course_name": "EUR", "course_price": float(data.get("EUR").replace(" ", ""))},
            ]
        )
        session.commit()

    def select(self):
        course_data = session.execute(select(Course.course_name, Course.course_price)).fetchall()
        course_datas = {}
        for i in course_data:
            course_datas[i[0]] = i[1]
        return course_datas

    def select_currencies(self):
        response = requests.get("https://bank.uz/uz/currency")
        soup = BeautifulSoup(response.text, 'html.parser')
        s = 0
        currencies = {}
        for i in soup.find_all("li", 'nav-item'):
            if s == 3:
                break
            currency_elements = i.find_all('span', class_='medium-text')
            for j in range(0, len(currency_elements), 3):
                currency_code = currency_elements[j].text.strip()
                currency_rate = currency_elements[j + 1].text.strip()
                currencies[currency_code] = currency_rate
            s += 1
        return currencies

    def update(self):
        currencies = Course.select_currencies(Base)
        for i in currencies.keys():
            query = update(Course).where(Course.course_name == i).values(
                course_price=float(currencies.get(i).replace(" ", "")))
            session.execute(query)
            session.commit()

Base.metadata.create_all(engine)

if not Course.select(Base):
    Course.insert(Base, Course.select_currencies(Base))

else:
    Course.update(Base)
