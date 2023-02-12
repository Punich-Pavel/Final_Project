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
  
   - влияет ли число детей, пенсионеров и других социально уязвимых групп на уровень социального благополучия в регионе;
    
   - связан ли уровень социального благополучия с производством и потреблением в регионе;
    
   - какие ещё зависимости можно наблюдать относительно социально незащищённых слоёв населения.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?   

  - Создание обобщенной БД в виде excel-книги и csv-файла; 
  - Анализ и подготовка данных;
  - Разработка ML-модели, анализ метрик модели;
  - Анализ кластеризации;
  - Разработка сервисов: uWSGI, uWSGI+NGINX, Docker.



### Краткая информация о данных

Для работы над проектом онлайн-школой SkillFactory были предоставлены данные из открытых источников интернета, которые в процессе работы над проектом были дополнены.

  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  

* Этап 1: Создание [обобщенной БД](./data/soc_pasport.xlsx): [Часть_1](./Part_1)

* Этап 2: Анализ и отчистка данных. Разведочный анализ (EDA):[Часть_2](./Part_2);

* Этап 3: Разработка ML-модели, анализ метрик модели. Описание и анализ кластеров: [Часть_3](./Part_3);

* Этап 4: Разработка сервисов (uWSGI, uWSGI+NGINX, Docker): [Часть_4](./Part_4).



:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты: 

  1. Технические:
  
   * реализована git-архитектура проекта GitHub Flow: в проект добавлены 4 ветви (part_1, part_2, part_3 и part_4) для работы над частями проекта и базова ветвь (master);

   * созданы:
   
     - обобщенная база данных;
    
     - инструменты обработки, анализа и визуализации;

     - модель кластеризации;

     - архитектура сервисов (uWSGI, uWSGI+NGINX, Docker);
    
   * произведены:
   
     - подготовка данных;

     - отчистка и разведочный анализ данных;

     - кластеризация данных с оптимальными гиперпараметрами.
  
  2. Информационно-аналитические:
  
   * проанализированны предоставленные данные;

   * данные дополнены из открытых источников;

   * созданны дополнительные признаки для кластеризации и оценки качества кластеризации.
  
  3. Социально-экономические:
  
   * определены:
   
     - социально-значимые признаки для кластеризации;

     - характеристики кластеров и их поименование;
    
   * произведены:

     - проверка выдвинутых гипотез;

     - новая гипотеза и ее проверка. 


:arrow_up:[к оглавлению](.README.md#Оглавление)

### Выводы:

  1. Технические:
  
   * поставленные задачи удалось реализовать;

   * были выявлены и заполнены пробелы знаний в предметных областях;

   * закреплены и углублены компетенции в работе с git, RabbitMQ, flask, docker.
  
  2. Информационно-аналитические:
    
   * для более точного определения принадлежности регионов к кластеру необходимо обновить и дополнить пустые значения более 'свежими' данными.
  
  3. Социально-экономические:

   * подтверждены гипотезы:
   
     - колличество детей, пенсионеров и инвалидов в регионе влияют на уровень социального благополучия региона;

     - уровень социального благополучия связан с региональным производством;
     
   * выдвинута и опровергнута гипотеза:
    
     - количество заболеваний зависит от уровня социального благополучия региона.
          

В процессе работы над проектом были использованны  материалы онлайн-школы SkillFactory, наработки и идеи студентов SkillFactory публиччного доступа. Огромное им за это СПАСИБО!

:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️


## ["Ссылка на резюме"](https://kansk.hh.ru/resume/f3540f86ff097e4b7c0039ed1f315969523431)
