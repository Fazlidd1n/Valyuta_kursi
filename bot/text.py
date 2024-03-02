from db.model import Course, Base

begin_text = """ - bizning botga xush kelibsiz ❗️\n
－   Bu bot orqali siz Valyuta 💵 kurslari haqida malumot ola olasiz ❗\n
－   Quyidagi tugmalardan birini tanlang ⤵️ """
course_datas = Course.select(Base)
courses = f""" : valyuta kurslari\n
－   🇺🇸 1 AQSH dollari :                                                    
 Sotib olish - {course_datas.get("USD")[0]} so'm ; 
 Sotish - {course_datas.get("USD")[1]} so'm ;
 
－   🇪🇺 1 EVRO :
 Sotib olish - {course_datas.get("EUR")[0]} so'm ;
 Sotish - {course_datas.get("EUR")[1]} so'm ;
 
－   🇷🇺 1 Rossiya rubli :
 Sotib olish - {course_datas.get("RUB")[0]} so'm ;
 Sotish - {course_datas.get("RUB")[1]} so'm ;
 
－   🇬🇧 1 Angliya funt sterlingi :
 Sotib olish - {course_datas.get("GBP")[0]} so'm ;
 Sotish - {course_datas.get("GBP")[1]} so'm ;
 
－   🇨🇭 1 Shveytsariya franki :
 Sotib olish - {course_datas.get("CHF")[0]} so'm ;
 Sotish - {course_datas.get("CHF")[1]} so'm ;
 
－   🇯🇵 1 Yaponiya iyenasi :
 Sotib olish - {course_datas.get("JPY")[0]} so'm ;
 Sotish - {course_datas.get("JPY")[1]} so'm ;
 
－   🇰🇿 1 Qozog‘iston tengesi :
 Sotib olish - {course_datas.get("KZT")[0]} so'm ;
 Sotish - {course_datas.get("KZT")[1]} so'm ;
"""
