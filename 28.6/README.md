**Финальное тестовое задание**

В качестве подопытного был выбран магазин aliexpress.ru\
В файле \test\bugs.py я временно разместил заготовки для регрессионных тестов по найденным мною дефектам.


Запуск:\
pip install -r requirements\
python3 -m pytest -v -s --driver Firefox --driver-path ../geckodriver.exe tests/*
