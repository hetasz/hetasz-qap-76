**Финальное тестовое задание**

В качестве подопытного был выбран интернет-магазин aliexpress.ru\
В задании представлен 51 автоматизированный тест с использованием PyTest и Selenium.

**test_auth_page.py** — проверка авторизации\
#01 Неверный пароль\
#02 Неверный формат email\
#03 Позитивный тест

**test_main_page_smoke.py** — smoke-проверка инструментария главной страницы\
#04 Ссылка в логотипе\
#05 Рекламный баннер в шапке\
#06 Ссылка на мобильное приложение\
#07 Личный кабинет для бизнеса (с раскрытием выпадающего списка)\
#08 Закрытие куки-бара\
#09 Клик по раскрывающейся категории\
#10 Кнопка «Подробнее»\
#11 Промо для новых пользователей\
#12 Несуществующая страница — возврат 404\
#13 Копирайт на дне\
#14 Поиск с параметризацией\
#15 Доступность файла robots.txt

**test_shopcart.py** — корзина\
#16 Открытие пустой корзины\
#17 Добавление рандомного товара\
#18 Калькуляция суммы\
#19 Увеличение объёма заказа кнопками +/−\
#20 Удаление позиции\
#21 Кнопка «Оформить»\
#22 Открытие корзины с главной страницы

**test_filter.py** — проверка фильтрации и навигации\
#23 При переходе по хлебным крошкам не сбиваются фильтры\
#24 Переход на страницу категории со страницы с фильтрами\
#25 Работа ограничения цены «снизу»\
#26 Работа ценовых диапазонов\
#27 Фильтр по «быстрой доставке»\
#28 Фильтр по «звёздочкам»\
#29 Фильтр по возрастанию количества заказов\
#30 Переход с «плитки» в представление «лист»\
#31 Пагинация кнопками\
#32 Пагинация «прыжком» к нужной странице с вводом валидных значений\
#33 Пагинация «прыжком» негативная

**test_item.py** — проверка страницы товара\
#34 Хлебные крошки\
#35 Получение купонов\
#36 Ссылка на лидеров продаж\
#37 Выбор цвета (опций) товара\
#38 Увеличение объёма заказа кнопками +/−\
#39 Смена главного изображения в зоне просмотра с помощью «наведения» на превьюшки\
#40 Ссылки на категории товаров\
#41 Раскрытие списка отзывов\
#42 Фильтр отзывов по звёздам\
#43 Фильтр отзывов по стране\
#44 Пагинация отзывов\
#45 Ссылка блока «похожие предложения»

**test_search.py** — проверка поиска\
#46 Поиск по кнопке\
#47 Поиск по клавише Enter\
#48 Исправление грамматических ошибок\
#49 Исправление неверной раскладки клавиатуры\
#50 Сообщение об отсутствии найденных товаров при сложном запросе\
#51 Сравнение количества карточек товара с числом на метке «результат»

В файле /test/**bugs.py** я разместил заготовки тестов по найденным мною дефектам.

Запуск:\
pip install -r requirements\
python3 -m pytest -v -s --driver Firefox --driver-path ../geckodriver.exe tests/test*
