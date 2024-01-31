
<h1 align="center">Проект по тестированию банка
<p align="center">
<a href="https://tl.af-ctf.ru/" target="_blank">
<img src="/media/screenshots/img7.png" alt="HackMeBank">
</p>
</p></h1>

<!-- Тест кейсы -->

## Автоматизировано тестирование функционала:
* Заполнение формы заявки для получения карты



# <a name="Technology">Технологии и инструменты</a>
<p  align="center">
  <code><img width="5%" title="Python" src="media/logo/python.png"></code>
  <code><img width="5%" title="Pycharm" src="media/logo/pycharm.png"></code>
  <code><img width="5%" title="Pytest" src="media/logo/pytest.png"></code>
  <code><img width="5%" title="Selenium" src="media/logo/selenium.png"></code>
  <code><img width="5%" title="Selene" src="media/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="media/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="media/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="media/logo/allure_report.png"></code>
  <code><img width="5%" title="Telegram" src="media/logo/tg.png"></code>
</p>


В данном проекте автотесты написаны на **Python** с использованием фреймворка **Pytest** и популярных библиотек **Selene, WebDriver-Manager, Selenium**.
Из **Jenkins** выполняется запуск тестов выполняется.
**Selenoid** используется для запуска браузеров в контейнерах **Docker**.
**Allure Report, Telegram Bot** используются для визуализации результатов тестирования.


# <a name="Jenkins">Запуск тестов в [Jenkins](https://jenkins.autotests.cloud/job/10_da-vasilev_qa-guru-hw25/)</a>
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C09-MaryMokretsova-unit15/">Ссылка на проект в Jenkins</a>

### Для запуска автотестов в Jenkins
1. Открыть проект
<img src="/media/screenshots/img1.png">
2. Выбрать пункт "Собрать с параметрами"
<img src="/media/screenshots/img2.png">
3. В случае необходимости изменить параметры и нажать на кнопку "build"
<img src="/media/screenshots/img3.png">


### Локальный запуск автотестов
1. Клонируйте репозиторий
```ruby
gh repo clone MaryMokretsova/HackMeBank
```
2. Создайте и активируйте виртуальное окружение
  ```ruby
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```ruby
  pip install -r requirements.txt
  ```
4. Запустите автотесты 
  ```ruby
  pytest -sv
  ```
5. Получите отчёт allure
```ruby
allure serve allure-results
``` 

   

# <a name="AllureReport">Отчет о результатах тестирования в [Allure Report](https://jenkins.autotests.cloud/job/10_da-vasilev_qa-guru-hw25/23/allure/)</a>

#### Общая информация
Главная страница Allure-отчета содержит следующие информационные блоки:

>- <code><strong>*ALLURE REPORT*</strong></code> - отображает дату и время прохождения теста, общее количество прогнанных кейсов, а также диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов

Результат запуска сборки можно посмотреть в отчёте Allure

При первом запуске не все селекторы отработали корректно
<p align="center">
<img src="/media/screenshots/img4.png" alt="Allure Report" width="750">)
</p>
При втором запуске тесты прошли успешно
<p align="center">
<img src="/media/screenshots/img5.png" alt="Allure Report" width="750">)
</p>



### Пример запуска теста в Selenoid
<p align="center">

<img src="/media/screenshots/test.gif" alt="Test example">
</p>

### Уведомления в Telegram
<p align="center">

  <img src="/media/screenshots/img6.jpeg" alt="Telegram" width="300"></a>
</p>
