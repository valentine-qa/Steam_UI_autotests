# Проект по тестированию интернет-магазина <a target="_blank" href="https://store.steampowered.com/">Steam</a>

![main page screenshot](screenshots/steam_main_page.png)

---
### Список проверок, реализованных в web автотестах
1. Переход на вкладку "Community".
2. Смена языка на сайте на французский.
3. Поиск указанной игры.
4. Переход на страницу авторизации.
5. Добавление игры в корзину.
6. Удаление игры из корзины.
7. Очистка всей корзины.

---

### Используемые инструменты
<img title="Python" src="screenshots/icons/python.svg" height="40" width="40"/> 
<img title="Pytest" src="screenshots/icons/pytest.svg" height="40" width="40"/> 
<img title="Allure Report" src="screenshots/icons/allure_report.png" height="40" width="40"/> 
<img title="GitHub" src="screenshots/icons/github.svg" height="40" width="40"/> 
<img title="Selenoid" src="screenshots/icons/selenoid.png" height="40" width="40"/> 
<img title="Selene" src="screenshots/icons/selene.png" height="40" width="40"/> 
<img title="Pycharm" src="screenshots/icons/pycharm-original.svg" height="40" width="40"/> 
<img title="Telegram" src="screenshots/icons/telegram.png" height="40" width="40"/> 
<img title="Jenkins" src="screenshots/icons/jenkins-original.svg" height="40" width="40"/> 
<img title="Allure TestOps" src="screenshots/icons/allure_testops.svg" height="40" width="40"/> 
<img title="Jira" src="screenshots/icons/jira.svg" height="40" width="40"/>

---

### Запуск автотестов осуществляется с использованием Jenkins
> [Ссылка на сборку в Jenkins](https://jenkins.autotests.cloud/job/zmamedov-qa_guru_Steam_ui_test/)

#### Для запуска автотестов в Jenkins
1. Открыть [задачу в Jenkins](https://jenkins.autotests.cloud/job/zmamedov-qa_guru_Steam_ui_test/)

![jenkins job main page](pictures/Jenkins_job_main_page.png)

2. Нажать "**Build Now**".

---

### Allure отчет

#### Общие результаты
![allure_report main page](pictures/allure_report_main_page.png)

#### Результаты прохождения тестов
![allure_report suites](pictures/allure_report_suites.png)

#### Графики
![allure_report graph_1](pictures/allure_report_graph_1.png)
![allure_report graph_2](pictures/allure_report_graph_2.png)

---

### Интеграция с Allure TestOps
> [Дашборд с общими результатами](https://allure.autotests.cloud/project/4223/dashboards)

![allure_testops dashboard](pictures/allure_testops_dashboard.png)

> [Тест-кейсы](https://allure.autotests.cloud/project/4223/dashboards)

![allure_testops test_cases](pictures/allure_testops_test_cases.png)

---

### Интеграция с Jira
> [Задача в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1234)
 
![jira task](pictures/jira_task.png)

---

### Уведомления в Телеграм

![telegram_notification](pictures/tg_notification.png)

---

### Прохождение автотеста

![autotest](pictures/clear_cart.gif)