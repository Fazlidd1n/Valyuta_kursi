from db.model import Course, Base

begin_text = """ - bizning botga xush kelibsiz ❗️\n
－   Bu bot orqali siz Valyuta 💵 kurslari haqida malumot ola olasiz ❗\n
－   Quyidagi tugmalardan birini tanlang ⤵️ """
course_datas = Course.select(Base)
courses = f""" : valyuta kurslari\n
－   🇺🇸 1 AQSH dollari = {course_datas.get("USD")} so'm
－   🇪🇺 1 EVRO = {course_datas.get("EUR")} so'm
－   🇷🇺 1 Rossiya rubli = {course_datas.get("RUB")} so'm
"""
