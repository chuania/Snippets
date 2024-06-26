Проект **"Snippets"** - это сайт, реализовaнный посредством **Django**🐍, где каждый *зарегистрированный* пользователь может оставлять фрагменты кода(сниппеты), изменять их, просматривать и комментировать код других пользователей. У сниппета два режима просмотра - *публичный* и *приватный*. Публичные фрагменты доступны также *незарегистрированным* пользователям.


## Инструкция по запуску проекта после клонирования

1. Создаем venv: `python3 -m venv venv_name`
где venv_name название виртуального окружения
2. Активируем venv: `source venv_name/bin/activate`
3. Устанавливаем зависимости из файла requirements.txt: `pip install -r requirements.txt`
4. Создаем базу(применяя миграции): `python manage.py migrate`
5. Запускаем проект командой: `python3 manage.py runserver`

## Вспомогательные команды
1. Остановка сервера в терминале: Ctrl+C 
2. Запуск python-shell с контекстом django: `python manage.py shell_plus --ipython`
3. Выход из python-shell: Ctrl+D
4. Выход из venv: `deactivate`  


#### Сайт имеет следующий графический интерфейс:
<p>
  <img width="600" height="400" src="https://github.com/chuania/Snippets/blob/main/overview/screen1.png">
</p>
<p></p>
<p>
  <img width="600" height="400" src="https://github.com/chuania/Snippets/blob/main/overview/screen2.png">
</p>
<p></p>
<p>
  <img width="600" height="400" src="https://github.com/chuania/Snippets/blob/main/overview/screen3.png">
</p>
