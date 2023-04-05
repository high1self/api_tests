## Проект API автотестов reqres.in

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="./attachments/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="./attachments/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="./attachments/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="./attachments/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="./attachments/logo/github.png"></code>
  <code><img width="5%" title="Allure Report" src="./attachments/logo/allure_report.png"></code>
  <code><img width="5%" title="Jenkins" src="./attachments/logo/jenkins.png"></code>
  <code><img width="5%" title="Requests" src="./attachments/logo/requests.png"></code>
</p>

### Что проверяется в проекте:
![This is an image](attachments/screenshots/tests_api.jpg)


## :computer: Запуск тестов из терминала
```bash
pytest tests/test_regres_in.py --env=prod
```

В проекте используется live logger:
![This is an image](attachments/screenshots/logger.jpg)

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="attachments/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/test_reqres_in/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение
![This is an image](attachments/screenshots/jenkins_api.jpg)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="attachments/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты сохраняются в виде Allure отчёта.

![This is an image](attachments/screenshots/allure_api.jpg)

##### Во вкладке Suites находится детализированный отчёт с логами

![This is an image](attachments/screenshots/allure_api_suites.jpg)
