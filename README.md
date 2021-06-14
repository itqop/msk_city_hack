# msk_city_hack
## Track 03
**решение от команды Aurorians**
# Структура репозитория:
- ## [data_prep](https://github.com/itqop/msk_city_hack/tree/main/data_prep "data_prep") - подготовка данных
>В этом разделе вы можете найти iPython notebooks с поэтапной обработкой данных
- ### [Stage_1](https://github.com/itqop/msk_city_hack/tree/main/data_prep/Stage_1 "Stage_1") - самая базовая обработка
>В этой папке лежит код для сжатия датасета в 21 ГБ. Парсятся timestamps. Сессии разделяются на окна по часу, пользователи суммируются
- ### [Stage2](https://github.com/itqop/msk_city_hack/tree/main/data_prep/Stage2 "Stage2") - создание новых фичей по времени
>Код в этой папке создает дополнительные колонки, где находятся данные по дням недели, времени суток
- ### [Stage3](https://github.com/itqop/msk_city_hack/tree/main/data_prep/Stage3 "Stage3")- написаны функции для обработки данных OpenStreetMap 
>Здесь написаны отдельные запросы к базе OSM, для разделения по сфере деятельности
- ### [Stage4](https://github.com/itqop/msk_city_hack/tree/main/data_prep/Stage4 "Stage4") - добавляем данные с прошлого этапа к общей базе и добавляем информацию по метро
>Считаем количество возможных конкурентов в округе. Высчитываем ближайшую станцию метро к центру зоны и ищем расстояние до станции.
 - ### [Parsers](https://github.com/itqop/msk_city_hack/tree/main/data_prep/Parsers "Parsers")- содержит парсеры для сервисов и обработанные данные по объявлениям ЦИАН
- ## [ranking_script](https://github.com/itqop/msk_city_hack/tree/main/ranking_script "ranking_script") - готовый модуль для обработки запросов с сервера
 > [modelcb.cbm](https://github.com/itqop/msk_city_hack/blob/main/ranking_script/modelcb.cbm "modelcb.cbm") - обученная модель catboost для ранжирования
 > [model.py](https://github.com/itqop/msk_city_hack/blob/main/ranking_script/model.py "model.py") - содержит функцию, принимающую вид деятельности и количество точек, возвращающую массив из точек с описаниями для карты

