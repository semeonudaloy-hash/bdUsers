import streamlit as st
from datetime import date
import requests


st.title("Профиль пользователя")

# Создаем две вкладки
tab1, tab2 = st.tabs(["Регистрация", "Вход"])

apiUrl = "http://127.0.0.1:5000/login"


with tab1: # создание новых пользователей
    st.subheader("Создание профиля")
    
    with st.form("registedForm"):
        # Поля для регистрации
        lastname = st.text_input("Фамилия")
        firstname = st.text_input("Имя")
        age = st.number_input("Возраст", min_value=1, max_value=120, step=1)
        birthdate = st.date_input("Дата рождения", min_value=date(1900, 1, 1))
        
        # Логин и пароль
        login = st.text_input("Логин")
        password = st.text_input("Пароль", type="password")
        
        
        submitted = st.form_submit_button("Зарегистрироваться")
        
        if submitted:
            
            if not all([lastname, firstname, login, password]):
                st.warning("Заполните все  поля")
            else:
                
                # response = requests.put(
                #     f"{apiUrl}/users/{lastname}",
                #     json={"name": lastname, "age": age, "surname": firstname, "birthdate": birthdate, "password": password})
                response = requests.put(
                    f"{apiUrl}/users/{lastname}",
                    json={"lastname": lastname,
                          "firstname": firstname,
                          "age": age,
                          "birthdate": birthdate.isoformat(),
                          "login":login,
                          "password": password
                    }
                )
                if response.status_code == 200:
                    st.success("Данные успешно загружены!")
                else:
                    st.error(f"Ошибка сервера. Код: {response.status_code}")
                
            #  st.success(f"Пользователь {login} успешно создан!")

# --- ВКЛАДКА 2: ВХОД ---
with tab2:
    st.subheader("Вход в систему")
    
    with st.form("loginForm"):
        login = st.text_input("Логин")
        password = st.text_input("Пароль", type="password")
        
        login_submitted = st.form_submit_button("Войти")
        
        if login_submitted:
            # Здесь вы вызываете свою функцию проверки из базы
            # Например: user = db.check_user(login_in, password_in)
            
            if not login or not password:
                st.warning("Введите логин и пароль!")
            else:
                # Заглушка для визуала
                response = requests.put(
                    apiUrl,
                    json={"login": login,
                          "password": password
                    }
                )