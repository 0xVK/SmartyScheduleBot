import os

VERSION = '8.2'

DATABASE = 'SmartyS_DB.sqlite'

BOT_TOKEN = '<TOKEN>'

POLLING_INTERVAL = 2

USE_CACHE = False

USE_WEBHOOK = True

WEBHOOK_URL = ''

WEBHOOK_PATH = '/whook'

TIMETABLE_URL = 'https://dekanat.zu.edu.ua/cgi-bin/timetable.cgi'

HTTP_USER_AGENT = 'Telegram-SmartySBot'

SEND_ERRORS_TO_ADMIN = True

ADMINS_ID = ['204560928']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEACHERS = [
    'Франовський Анатолій Цезарович',
    'Халін Валерій Володимирович',
    'Шевчук Андрій Володимирович',
    'Яценко Світлана Леонідівна',
    'Вискушенко Андрій Петрович',
    'Журавльова Лариса Петрівна',
    'Кутек Тамара Борисівна',
    'Рожнова Тетяна Євгенівна',
    'Спірін Олег Михайлович',
    'Михайленко Василь Васильович',
    'Малежик Михайло Павлович',
    'Аннамухаммедов Азат Овезмухамедович',
    'Усатий Андрій В`ячеславович',
    'Башманівський Валерій Іванович',
    'Близнюк Андрій Сергійович',
    'Недашківська Тетяна Євгенівна',
    'Юрчук Олена Олександрівна',
    'Мосієнко Олена Володимирівна',
    'Стародубець Галина Миколаївна',
    'Кордон Микола Володимирович',
    'Ярмошик Іван Іванович',
    'Козловець Микола Адамович',
    'Семенюк Ірина Сергіївна',
    'Андрійчук Наталя Михайлівна',
    'Жуковська Вікторія Вікторівна',
    'Чирков Олександр Семенович',
    'Киричук Галина Євгеніївна',
    'Гарбар Олександр Васильович',
    'Стадниченко Агнеса Полікарпівна',
    'Томашик Василь Миколайович',
    'Поліщук Олена Петрівна',
    'Коновальчук Іван Іванович',
    'Плотницька Оксана Віталіївна',
    'Антонова Олена Євгеніївна',
    'Підгурська Валентина Юріївна',
    'Самойлюкевич Інна Володимирівна',
    'Саух Петро Юрійович',
    'Вікарчук Ольга Іванівна',
    'Дмитрієва Світлана Михайлівна',
    'Сейко Наталія Андріївна',
    'Корнійчук Наталія Миколаївна',
    'Ахметов Рустам Фагимович',
    'Грибан Григорій Петрович',
    'Яворська Тетяна Євгенівна',
    'Калініна Лариса Вадимівна',
    'Портницька Наталія Федорівна',
    'Батраченко Іван Георгійович',
    'Савиченко Ольга Михайлівна',
    'Весельська Алла Леонідівна',
    'Вишина Алла Юріївна',
    'Гавриловська Ксенія Петрівна',
    'Голентовська Ольга Святославівна',
    'Горбунова Вікторія Валеріївна',
    'Пирог Ганна Володимирівна',
    'Горностай Павло Петрович',
    'Гречуха Ірина Анатоліївна',
    'Кулаковська Ольга Григорівна',
    'Дем`янчук Юлія Юріївна',
    'Журавська Олена Вікторівна',
    'Заброцький Михайло Михайлович',
    'Загурська Інна Станіславівна',
    'Кирильчук Інна Василівна',
    'Кириченко Віктор Васильович',
    'Климчук Віталій Олександрович',
    'Коломієць Тетяна Володимирівна',
    'Котлова Людмила Олександрівна',
    'Кулаковський Тарас Юрійович',
    'Мазяр Олег Васильович',
    'Мойсієнко Ярослав Вікторович',
    'Никончук Наталія Олександрівна',
    'Степанюк Інна Андріївна',
    'Тичина Ірина Миколаївна',
    'Фальковська Людмила Миколаївна',
    'Хазратова Нігора Вікторівна',
    'Хоменко Наталія Василівна',
    'Шаран Ольга Сергіївна',
    'Шаюк Алла Василівна',
    'Шикирава Наталія Миколаївна',
    'Шапран Тетяна Миколаївна',
    'Ренькас Броніслава Мирославівна',
    'Шмиглюк Геннадій Аксентійович',
    'Шмиглюк Оксана Геннадіївна',
    'Чабанюк Наталія Іванівна',
    'Калініченко Олена Олександрівна',
    'Козюк Катерина Сергіївна',
    'Литвинчук Алла Іванівна',
    'Журавльов Валерій Пилипович',
    'Рудницький Сергій Владиславович',
    'Марчук Катерина Анатоліївна',
    'Рацілевич Андрій Петрович',
    'Саух Ірина Василівна',
    'Уразов Анатолій Устинович',
    'Скаковська Ольга Анатоліївна',
    'Горай Оксана Валентинівна',
    'Клімова Інна Олександрівна',
    'Зорницька Ірина Валеріївна',
    'Чумак Володимир Валентинович',
    'Венгерська Вікторія Олексіївна',
    'Вискушенко Дмитро Андрійович',
    'Жуковський Олександр Іванович',
    'Найфонов Давид Артурович',
    'Піддубна Оксана Михайлівна',
    'Чаплінська Оксана Вікторівна',
    'Миколишена Тетяна Вікторівна',
    'Анічкіна Олена Василівна',
    'Кусяк Наталія Володимирівна',
    'Камінський Олександр Миколайович',
    'Хоменко Тамара Іванівна',
    'Денисюк Роман Олександрович',
    'Листван Віталій Володимирович',
    'Листван Володимир Миколайович',
    'Янович Ірина Володимирівна',
    'Тітов Юрій Олександрович',
    'Євдоченко Олена Сергіївна',
    'Кондратенко Олена Ульянівна',
    'Романишина Людмила Михайлівна',
    'Кусяк Андрій Петрович',
    'Кичкирук Ольга Юріївна',
    'Уваєва Олена Іванівна',
    'Василенко Ольга Миколаївна',
    'Хом`як Іван Владиславович',
    'Онищук Ірина Петрівна',
    'Коцюба Ірина Юріївна',
    'Костюк Віталій Степанович',
    'Алпатова Оксана Миколаївна',
    'Кухарчук Алла Євгенівна',
    'Мостіпака Тетяна Петрівна',
    'Іщук Олена Миколаївна',
    'Перепелиця Людмила Олександрівна',
    'Муж Галина Василівна',
    'Астахова Лариса Євгенівна',
    'Першко Ірина Олександрівна',
    'Гарбар Діана Анатоліївна',
    'Шелюк Юлія Святославівна',
    'Луференко Ліна Юріївна',
    'Константиненко Людмила Анатоліївна',
    'Міхеєва Галина Миколаївна',
    'Пацюк Марина Костянтинівна',
    'Кутина Анастасія Олександрівна',
    'Швайко Ольга Дмитріївна',
    'Корево Ніна Іванівна',
    'Савенко Оксана Анатоліївна',
    'Акімов Ігор Андрійович',
    'Межжерін Сергій Віталійович',
    'Трускавецький Євген Степанович',
    'Янович Лариса Миколаївна',
    'Мельниченко Руслана Костянтинівна',
    'Єрмошина Тетяна Вікторівна',
    'Танська Валентина Володимирівна',
    'Павлюченко Олеся Вікторівна',
    'Власенко Руслана Петрівна',
    'Шевчук Світлана Юріївна',
    'Сорочинська Оксана Андріївна',
    'Сіваєва Катерина Володимирівна',
    'Гарлінська Алла Миколаївна',
    'Тарасова Юлія Вікторівна',
    'Васільєва Людмила Анатоліївна',
    'Весельський Микола Францович',
    'Буравський Олександр Антонович',
    'Кузьмін Олександр Сергійович',
    'Власюк Ігор Миколайович',
    'Міщук Галина Анатоліївна',
    'Гуцало Людмила Вікторівна',
    'Опанащук Петро Володимирович',
    'Седляр Анатолій Володимирович',
    'Хададова Марина Володимирівна',
    'Шандра Валентина Степанівна',
    'Новик Микола Кузьмович',
    'Падалко Анатолій Ілліч',
    'Рудницька Ольга Павлівна',
    'Магась-Демидас Юлія Іванівна',
    'Хоменко Олена Олександрівна',
    'Маркевич Оксана Валентинівна',
    'Зосімович Олена Юріївна',
    'Новик Валерій Анатолійович',
    'Шевчук Богдан Леонідович',
    'Викладачі СІД _',
    'Бабінська Марина Сергіївна',
    'Ковтуненко Ольга Іванівна',
    'Натикач Петро Іванович',
    'Рудницька Наталія Василівна',
    'Рафальська Тетяна Леонідівна',
    'Білобровець Ольга Матвіївна',
    'Ковальчук Іван Васильович',
    'Дребот Володимир Іванович',
    'Максимов Олександр Вікторович',
    'Новіцька Юлія Йосипівна',
    'Хитровська Юлія Валентинівна',
    'Сичевський Антон Олександрович',
    'Канівець Борис Андрійович',
    'Герасимчук Андрій Андрійович',
    'Бутковська Наталія Юріївна',
    'Стародубець Володимир Олексійович',
    'Сухачов Станіслав Якимович',
    'Вітюк Ірина Костянтинівна',
    'Горохова Людмила Вікторівна',
    'Гордійчук Ольга Олегівна',
    'Рускевич Анатолій Васильович',
    'Ковтун Наталія Михайлівна',
    'Слюсар Вадим Миколайович',
    'Заглада Віктор Миколайович',
    'Богачевська Ірина Вікторівна',
    'Борисенко Наталя Дмитрівна',
    'Вітвицька Світлана Сергіївна',
    'Березюк Олена Станіславівна',
    'Єремеєва Віра Модестівна',
    'Ковальчук Валентина Антонівна',
    'Сидорчук Нінель Герандівна',
    'Борейко Олександр Михайлович',
    'Власенко Ольга Миколаївна',
    'Мирончук Наталія Миколаївна',
    'Павленко Віта Віталіївна',
    'Агапов Юрій Юрійович',
    'Сбруєва Аліна Анатоліївна',
    'Круковська Ірина Миколаївна',
    'Копетчук Валентина Анатоліївна',
    'Новіцька Інеса Василівна',
    'Рудницька Неля Юрівна',
    'Вознюк Олександр Васильович',
    'Москвіна Тетяна Пилипівна',
    'Гужанова Тетяна Сергіївна',
    'Басюк Наталія Анатоліївна',
    'Федорова Марія Анатоліївна',
    'Максимова Олена Олександрівна',
    'Мурашевич Юлія Михайлівна',
    'Тарнавська Наталія Петрівна',
    'Коновальчук Інна Миколаївна',
    'Васянович Григорій Петрович',
    'Наумчук Тетяна Володимирівна',
    'Ковальчук Майя Олегівна',
    'Колесник Наталія Євгенівна',
    'Шмельова Тетяна Всеволодівна',
    'Ямчинська Галина Володимирівна',
    'Яцик Ірина Станіславівна',
    'Маловицька Людмила Флавіївна',
    'Коваль Тетяна Вікторівна',
    'Фурманюк Світлана Миколаївна',
    'Голубовська Ірина Владиславівна',
    'Гордієнко Олена Анатоліївна',
    'Левківська Олена Антонівна',
    'Марущак Олександра Миколаївна',
    'Підлужна Галина Володимирівна',
    'Усатий В`ячеслав Дмитрович',
    'Чупріна Олена Вадимівна',
    'Гуманкова Ольга Сергіївна',
    'Михайлова Оксана Сергіївна',
    'Карпенко Євгенія Миколаївна',
    'Литньова Ірина Федорівна',
    'Мазко Олена Петрівна',
    'Прохорова Світлана Миколаївна',
    'Зорницький Андрій Володимирович',
    'Мосейчук Олександр Михайлович',
    'Нідзельська Юлія Михайлівна',
    'Полховська Марина Володимирівна',
    'Топачевський Сергій Костянтинович',
    'Поліщук Людмила Петрівна',
    'Вискушенко Світлана Андріївна',
    'Асмукович Ірина Василівна',
    'Карпінський Юрій Владиславович',
    'Омецинська Ольга Володимирівна',
    'Пушкар Тетяна Миколаївна',
    'Марченко Євген Юрійович',
    'Буяльська Тетяна Іванівна',
    'Вотінова Дар`я Олексіївна',
    'Дем`янчук Ірина Владиславівна',
    'Кондратюк Ірина Борисівна',
    'Баладинська Ірина Владиславівна',
    'Бєлова Алла Дмитрівна',
    'Дем`янчук Олександр Никанорович',
    'Кияк Тарас Романович',
    'Олійник Світлана Василівна',
    'Фролова Ірина Євгеніївна',
    'Євченко Віра Володимирівна',
    'Соловйова Лариса Федорівна',
    'Моісєєва Маргарита Аркадіївна',
    'Рудик Ірина Миколаївна',
    'Савчук Інна Іванівна',
    'Андрушенко Олена Юріївна',
    'Щерба Наталія Сергіївна',
    'Бовсунівська Наталія Миколаївна',
    'Цюряк Ірина Олександрівна',
    'Папіжук Валентина Олександрівна',
    'Тарабріна Наталя Анатоліївна',
    'Кузьменко Олена Юріївна',
    'Сидорович Любов Євгенівна',
    'Черниш Оксана Андріївна',
    'Цюник Геннадій Михайлович',
    'Матушевська Наталія Володимирівна',
    'Доскач Катерина Василівна',
    'Буніятова Ізабелла Рафаїлівна',
    'Луценко Віктор Васильович',
    'Лісова Юлія Олександрівна',
    'Гузун Тетяна Іванівна',
    'Гузун Михайло Семенович',
    'Лозко Оксана Вікторівна',
    'Рутецький Василь Володимирович',
    'Татуревич Наталія Сергіївна',
    'Сичевська Валентина Василівна',
    'Комаренко Вероніка Василівна',
    'Плющик Єлизавета Василівна',
    'Неретін Валерій Олександрович',
    'Травкіна Наталія Михайлівна',
    'Федорченко Валентин Кузьмич',
    'Барало Людмила Володимирівна',
    'Новосадова Світлана Артемівна',
    'Суботницький Ігор Миколайович',
    'Роговська Єлизавета Владиславівна',
    'Демченко Ельвіра Азамжонівна',
    'Борисенко Наталія Сергіївна',
    'Котнюк Людмила Григорівна',
    'Чернишова Анна Михайлівна',
    'Онопрієнко Тетяна Миколаївна',
    'Тютюнник Ірина Федорівна',
    'Сніховська Ірена Едуардівна',
    'Даниленко Таісія Борисівна',
    'Малярчук Олена Валентинівна',
    'Остапчук Світлана Ігорівна',
    'Калінін Вадим Олександрович',
    'Григор`єва Тетяна Юріївна',
    'Войналович Людмила Петрівна',
    'Гаращук Кирил Володимирович',
    'Дячук Наталія Валеріївна',
    'Хорошун Ольга Олександрівна',
    'Примак Ольга Валеріїна',
    'Криворучко Тетяна Василівна',
    'Мартинова Ольга Миколаївна',
    'Чумак Людмила Миколаївна',
    'Білюк Інна Леонідівна',
    'Коломійчук Олександра Сергіївна',
    'Масель Юлія Сергіївна',
    'Малинівська Ольга Анатоліївна',
    'Мозговенко Оксана Ігорівна',
    'Євтушенко Анна Олегівна',
    'Горобченко Наталія Володимирівна',
    'Соколовська Світлана Францівна',
    'Ліпісівіцький Микола Леонідович',
    'Ковальова Тетяна Павлівна',
    'Борова Людмила Олексіївна',
    'Бараняк Марія Михайлівна',
    'Рудницька Наталія Миколаївна',
    'Анхим Олексій Іванович',
    'Максимчук Олена Леонідівна',
    'Долгополова Лілія Анатоліївна',
    'Баюн Крістіна Йосипівна',
    'Фант Микола Олександрович',
    'Федоренко Лариса Олександрівна',
    'Тараба Ірина Олександрівна',
    'Богайчук Інна Володимирівна',
    'Свириденко Ірина Миколаївна',
    'Фенчук Олена Олександрівна',
    'Мальченко Михайло Сергійович',
    'Король Євгенія Олександрівна',
    'Макаренко Наталія Вікторівна',
    'Сардак Олена Володимирівна',
    'Коляда Олег Васильович',
    'Закалюжний Леонід Володимирович',
    'Карплюк Світлана Олександрівна',
    'Кривонос Олександр Миколайович',
    'Горобець Сергій Миколайович',
    'Жуковський Сергій Станіславович',
    'Щехорський Анатолій Йосипович',
    'Михайленко Станіслав Васильович',
    'Вакалюк Тетяна Анатоліївна',
    'Федорчук Анна Леонідівна',
    'Усата Олена Юріївна',
    'Сікора Ярослава Богданівна',
    'Шимон Олександр Миколайович',
    'Яценко Оксана Іванівна',
    'Постова Світлана Анатоліївна',
    'Кривонос Мирослава Петрівна',
    'Мінгальова Юлія Ігорівна',
    'Загацька Наталія Олександрівна',
    'Головня Олена Сергіївна',
    'Сарана Олександр Анатолійович',
    'Таргонський Андрій Леонідович',
    'Осадчий Микола Мефодійович',
    'Подвисоцький Роман Володимирович',
    'Погоруй Анатолій Олександрович',
    'Севостьянов Євгеній Олександрович',
    'Григор`єва Інна Германівна',
    'Королюк Олена Миколаївна',
    'Дідківська Тетяна Вікторівна',
    'Сверчевська Ірина Анатоліївна',
    'Чемерис Ольга Анатоліївна',
    'Фонарюк Олена Василівна',
    'Ленчук Іван Григорович',
    'Міхеєв Віктор Васильович',
    'Федьович Микола Васильович',
    'Мосіюк Олександр Олександрович',
    'Поліщук Зоя Петрівна',
    'Прус Алла Володимирівна',
    'Ковальчук Олена Антонівна',
    'Орел Лілія Олександрівна',
    'Ткаченко Олександр Кирилович',
    'Зіновчук Андрій Васильович',
    'Степанчиков Дмитро Абрамович',
    'Нестеров Валерій Аркадійович',
    'Прокопенко Микола Миколайович',
    'Левківський Анатолій Миколайович',
    'Кіпаєва Тетяна Леонідівна',
    'Харченко Марія Миколаївна',
    'Новицький Сергій Вадимович',
    'Грищук Андрій Миколайович',
    'Грищук Віктор Валентинович',
    'Буханевич Наталія Віталіївна',
    'Васильєва Регіна Юхимівна',
    'Вербовський Ігор Андрійович',
    'Каленська Віталіна Петрівна',
    'Малинівська Людмила Іванівна',
    'Мелещенко Алла Анатоліївна',
    'Семенець Лариса Миколаївна',
    'Яценко Олександр Сергійович',
    'Вовченко Інна Іванівна',
    'Ляшко Юлія Станіславівна',
    'Тамашевський Іван Якович',
    'Левчук Леонід Іванович',
    'Лайчук Андрій Миколайович',
    'Мисечко Ольга Євгеніївна',
    'Кузнєцова Ганна Валеріївна',
    'Кузнєцова Ірина Володимирівна',
    'Кравець Олена Євгенівна',
    'Філіна Валентина Анатоліївна',
    'Шаверський Віктор Костянтинович',
    'Плахотнюк Наталія Павлівна',
    'Білошицька Тетяна Юріївна',
    'Біляк Ірина Валеріївна',
    'Большакова Надія Олександрівна',
    'Воробей Тамара Петрівна',
    'Гусаревич Олександр Валентинович',
    'Крук Алла Зенонівна',
    'Вольницька Дар`я Олегівна',
    'Хмара Вікторія Володимирівна',
    'Гарбуза Ірина Вікторівна',
    'Давидович Степан Сергійович',
    'Кафтанова Тетяна Віталіївна',
    'Дєнічева Ольга Ігорівна',
    'Саранча Микола Петрович',
    'Кухарьонок Світлана Степанівна',
    'Левківська Кристіна Валеріївна',
    'Лисецька Юлія Василівна',
    'Макаревич Олег Олександрович',
    'Маслюк Марина Ігорівна',
    'Мичка Іван В`ячеславович',
    'Мокіна Анна Геннадіївна',
    'Толкач Василь Павлович',
    'Очковська Анна Павлівна',
    'Сердійчук Лариса Петрівна',
    'Макарчук Людмила Петрівна',
    'Ямкова Ганна Іванівна',
    'Ляшевич Альона Михайлівна',
    'Грищук Сергій Миколайович',
    'Тименко Тамара Григорівна',
    'Дмитрієва Іванна Володимирівнв',
    'Яриновська Альона Анатоліївна',
    'Ващенко Тетяна Юріївна',
    'Чернуха Ірина Семенівна',
    'Радкевич Віта Володимирівна',
    'Ярош Валерія Валеріївна',
    'Гордійчук Світлана Вікторівна',
    'Крук Микола Зенонович',
    'Айунц Валентина Іванівна',
    'Блажиєвський Геннадій Валентинович',
    'Погребенник Людмила Іллівна',
    'Жуковська Маргарита Олексіївна',
    'Савитська Надія Олександрівна',
    'Трухан Леонід Васильович',
    'Твердохліб Жанна Олексіївна',
    'Яблонська Алла Миколаївна',
    'Осипенко Валерій Євгенійович',
    'Костюк Юлія Сергіївна',
    'Жуковський Євгеній Іванович',
    'Гончаренко Катерина Павлівна',
    'Довідна Марина Петрівна',
    'Василюк Ірина Миколаївна',
    'Місяць Наталія Купріянівна',
    'Макарова Ольга Юріївна',
    'Хмелінська Руслана Матвіївна',
    'Башманівський Олексій Леонідович',
    'Прищепа Олександр Васильович',
    'Вигівський Валерій Лук`янович',
    'Приймак Алла Миколаївна',
    'Волкова Олена Олександрівна',
    'Велика Аліна Михайлівна',
    'Самійлик Світлана Володимирівна',
    'Мельник Марина Володимирівна',
    'Білоус Петро Васильович',
    'Горбань Анфіса Василівна',
    'Чайковська Ванда Тадеушівна',
    'Франчук Марина Валеріївна',
    'Левченко Галина Дмитрівна',
    'Бондаренко Галина Федорівна',
    'Соболевська Галина Іванівна',
    'Астрахан Наталія Іванівна',
    'Рудюк Ольга Вікторівна',
    'Кацемба Юліана Леонідівна',
    'Талько Олена Борисівна',
    'Конторчук Ганна Кирилівна',
    'Доброльожа Галина Миронівна',
    'Гримашевич Галина Іванівна',
    'Дяченко Наталія Миколаївна',
    'Яценко Сергій Адамович',
    'Шарапа Марина Василівна',
    'Вольська Юлія Вікторівна',
    'Титаренко Валентина Миколаївна',
    'Ящук Леся Валеріївна',
    'Шевчук Тетяна Олександрівна',
    'Весельська Галина Станіславівна',
    'Пультер Станіслав Олександрович',
    'Білоус Ніна Миколаївна',
    'Лісовський Антон Михайлович',
    'Грибан Галина Василівна',
    'Кучерук Оксана Анатоліївна',
    'Шевцова Лариса Станіславівна',
    'Башманівська Любов Андріївна',
    'Маліновська Тетяна Володимирівна',
    'Пустохіна Вікторія Ігорівна',
    'Герасимчук Сніжана Вадимівна',
    'Дюжева Катерина Валеріївна',
    'Євченко Олександр Вікторович',
    'Клименко Тетяна Євгенівна',
    'Навальна Марина Іванівна',
    'Свінціцька Олена Іванівна',
    'Стадник Микола Миколайович',
    'Чернюк Сніжана Леонідівна',
    'Головецький Василь Миколайович',
    'Безверха Тетяна Миколаївна',
    'Василюк Валентина Іванівна',
    'Горбова Ірина Олексіївна',
    'Давидова Людмила Вікторівна',
    'Зайко Леся Яківна',
    'Зелінська Наталіна Миколаївна',
    'Масловська Марія Володимирівна',
    'Миколаєнко Надія Миколаївна',
    'Русецька Олена Борисівна',
    'Станкеєва Ірина Миколаївна',
    'Чорна Світлана Аркадіївна',
    'Денисевич Олена Вікторівна',
    'Павлінчук Тетяна Іванівна',
    'Максимець Світлана Миколаївна',
    'Фриз Ірина Володимирівна',
    'Стахова Ольга Олександрівна',
    'Ніколаєнко Сергій Миколайович',
    'Пойта Ірина Олександрівна',
    'Міщук Ірина Сергіївна',
    'Ніцак Ольга Борисівна',
    'Юрківська Людмила Йосипівна',
    'Боцян Тетяна Вікторівна',
    'Карпюк Ольга Анатоліївна',
    'Кащук Катерина Миколаївна',
    'Кіндрась Ольга Володимирівна',
    'Мартинов Сергій Вікторович',
    'Мосійчук Ірина Вікторівна',
    'Павловська Людмила Денисівна',
    'Юрківський Олександр Йосипович',
    'Філіпенко Тетяна Вячеславівна',
    'Янковська Ольга Іванівна',
    'Коляденко Світлана Миколаївна',
    'Ситняківська Світлана Михайлівна',
    'Павлик Надія Павлівна',
    'Ілліна Ольга Володимирівна',
    'Літяга Інна Володимирівна',
    'Товщик Сергій Андрійович',
    'Тарасенко Наталія Леонідівна',
    'Котловий Сергій Анатолійович',
    'Залібовська-Ільніцьк Зоя Володимирівна',
    'Палько Інна Миколаївна',
    'Бутузова Лариса Петрівна',
    'Король Лідія Миколаївна',
    'Мачушник Олена Леонідівна',
    'Сидоренко Наталія Іванівна',
    'Лісова Світлана Валеріївна',
    'Корінна Людмила Віталіївна',
    'Остапчук Олена Леонідівна',
    'Литвак Оксана Йосипівна',
    'Біляченко Галина Петрівна',
    'Безсмертна Вікторія Ігорівна',
    'Климова Катерина Яківна',
    'Дубравська Наталія Миколаївна',
    'Баргілевич Наталія Володимирівна',
    'Дудар Оксана Петрівна',
    'Клименко Дмитро Віталійович',
    'Чернобровкіна Віра Андріївна',
    'Мойсієнко Віктор Михайлович',
    'Недзельська Людмила Володимирівна',
    'Цибульський Василь Олександрович',
    'Коротун Наталя Григорівна',
    'Пилипко Олена Василівна',
    'Кхеліл Олеся Ігорівна',
    'Можарівська Ірина Олегівна',
    'Марчук Юлія Леонідівна',
    'Янчук Наталія Володимирівна',
    'Можаровська Тетяна Вікторівна',
    'Ількевич Наталія Сергіївна',
    'Корнійчук Платон Павлович',
    'Гирина Альона Асанівна',
    'Шугаєв Андрій Володимирович',
    'Ребрій Олександр Володимирович',
    'Литньова Тамара Вікторівна',
    'Шанскова Тетяна Ігорівна',
    'Бондар Аліна Миколаївна',
    'Юмашева Олександра Олександрівна',
    'Авдєєва Ольга Юріївна',
    'Бовсуновська Марина Олександрівна',
    'Фещук Володимир Васильович',
    'Шиманська Вікторія Василівна',
    'Мірошниченко Олена Анатоліївна',
    'Горбенко Галина Василівна',
    'Дунаєва Олена Ігорівна',
    'Чайка Микола Володимирович',
    'Білявська Вікторія Сергіївна',
    'Нікішова Тетяна Євгенівна',
    'Писаренко Сніжана Василівна',
    'Меленівська Людмила Іванівна',
    'Тищенко Михайло Станіславович',
    'Горик-Чубатюк Марина Олександрівна',
    'Трохимчук Ольга Володимирівна',
    'Ковальська Єва Юліанівна',
    'Світельська Олександра Володимирівна',
    'Луженецька Олена Петрівна',
    'Шинкарук Ірина Володимирівна',
    'Никончук Ірина Михайлівна',
    'Викладачі Історія України _',
    'Орищук Лілія Вікторівна',
    'Дунєва Олена І',
    'Арешонков Володимир Юрійович',
    'Бойчук Ірина Дмитрівна',
    'Андрійчук Тамара Вячеславівна',
    'Новосадова Наталія Григорівна',
    'Кот Юлія Сергіївна',
    'Савенко Оксана Петрівна',
    'Кадлубовська Наталія Станіславівна',
    'Захарченко Наталія Іванівна',
    'Фальківська Людмила Петрівна',
    'Музика Лідія Володимирівна',
    'Найдьонов Михайло Іванович',
    'Булгаков Олексій Ігорович',
    'Скалій Олександр Вячеславович',
    'Скалій Тетяна Валеріївна',
    'Набоков Юрій Анатолійович',
    'Левченко Ольга Миколаївна',
    'Дєньгаєва Світлана Вікторівна',
    'Прокопчук Наталія Романівна',
    'Сотська Галина Іванівна',
    'Огороднійчук Марія Володимирівна',
    'Моляко Валентин Олексійович',
    'Руда Іванна Василівна',
    'Горбачова Надія Ігорівна',
    'Щепанський Томаш __',
    'Кушева Жанна Іванівна',
    'Косигіна Олена Володимирівна',
    'Тимошенко Наталія Сергіївна',
    'Захарчук Вікторія Вікторівна',
    'Викладачі Всесвітня Історія',
    'Грицюта Наталія Миколаївна',
    'Бекетова Оксана Анатоліївна',
    'Мулярчук Інна Миколаївна',
    'Жуковець Аліна Миколаївна',
    'Толстова Ольга Вікторівна',
    'Васильєв Євгеній Михайлович',
    'Іщук Степан Іванович',
]
