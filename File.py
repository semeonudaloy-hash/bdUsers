import streamlit as st
import requests

apiUrl2 = "http://127.0.0.1:5000/users"

st.title("Админ-панель")

tab1, tab2, tab3 = st.tabs(["Вывод списка пользователей", "Изменение данных", "Удаление пользователей"])

with tab1:
    st.subheader("Вывод всех данных пользователей")
    
  
    if st.button("Вывод всех данных"):
    
        st.success("жмал")
        
        response = requests.get(f"{apiUrl2}/users")
        
        if response.status_code == 200:
            users_data = response.json() # Превращаем ответ сервера в список/словарь
            st.write(users_data)         # Выводим на экран
        else:
            st.error("Не удалось загрузить список")
        
with tab2:
    st.subheader("Изменение данных пользователей")
    
    with st.form("updateForm"):
        login = st.text_input("Введите логин пользователя для изменения данных")
        newName = st.text_input("Новое имя")
        newSurname = st.text_input("Новая фамилия")
        newAge = st.number_input("Новый возраст", min_value=1, max_value=120, step=1)
        newBirthdate = st.date_input("Новая дата рождения")
        newPassword = st.text_input("Новый пароль", type="password")
        
        
        submitted = st.form_submit_button("Изменить данные")
        
        if not all([login, newName, newSurname, newAge, newBirthdate, newPassword]):
            st.warning("Заполните все обязательные поля!")
        else:
            st.success(f"Пользователь {login} успешно создан!")
            
with tab3:
    st.subheader("Удаление пользователей")
    
    with st.form("deleteForm"):
        IDdelete = st.text_input("Введите id пользователя для удаления")
        
        deleteSubmitted = st.form_submit_button("Удалить пользователя")
        
        if deleteSubmitted:
            if not IDdelete:
                st.warning("Введите id пользователя для удаления!")
            else:
                
                st.success(f"Пользователь {IDdelete} успешно удален!")