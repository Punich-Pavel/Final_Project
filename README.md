# <center>Определение уязвимых групп населения

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта  

 Согласно опросу «инФОМ» от декабря 2021 года, у 27% россиян хватает денег только на еду, а ещё 9% не могут позволить себе полноценное питание.Эти люди особенно внимательно следят за ценами, а темп роста  цен на продукты обычно превышает средний темп инфляции. При этом Росстат считает, что расходы на продукты питания должны составлять примерно 36% от среднемесячных расходов россиянина (ещё около 10% приходится на услуги ЖКХ и жильё, 4 % — на лекарства). 

 До 2021 года «черта бедности» (жизнь на сумму ниже прожиточного минимума) в России определялась стоимостью минимальной продуктовой корзины.в том же году правительство «отвязало» уровень бедности от цен на базовые продукты: с 2021 года прожиточный минимум рассчитывается как 44.2 % от медианного дохода граждан РФ за прошлый год. В распоряжении есть данные о доходах, заболеваемости, социально незащищённых слоях населения России и другие экономические и демографические данные.

 **Задача:**

  ➔ кластеризовать регионы Россиии определить, какие из них наиболее остро нуждаются в помощи малообеспеченным/неблагополучным слоям населения;

  ➔ описать группы населения, сталкивающиеся с бедностью;

  ➔ определить:

     ◆ влияет ли число детей, пенсионеров и других социально уязвимых групп на уровень бедности в регионе;

     ◆ связаны ли уровень бедности/социального неблагополучия с производством и потреблением в регионе;

     ◆ какие ещё зависимости можно наблюдать относительно социально незащищённых слоёв населения.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?   

  - Разработка инструментов проекта, создание обобщенной БД в виде excel-книги; 
  - Анализ и подготовка данных (data engineering);
  - Разработка ML-модели, анализ метрик модели;
  - Разработка сервисов: uWSGI, uWSGI+NGINX, Docker.



### Краткая информация о данных


  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  

* Этап 1: Разработка [инструментов проекта](./tools), создание [обобщенной БД](./data/soc_pasport.xlsx): [part_1](./part_1.ipynb)

* Этап 2: Разведывательный анализ (EDA):[part_2](./part_2.ipynb);

* Этап 3: Разработка ML-модели, анализ метрик модели. Описание и анализ кластеров: [part_3](./part_2.ipynb);

* Этап 4: Разработка сервисов (uWSGI, uWSGI+NGINX, Docker): [service](./).



:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты: 



:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:




:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами


## ["Ссылка на резюме"](https://kansk.hh.ru/resume/f3540f86ff097e4b7c0039ed1f315969523431)