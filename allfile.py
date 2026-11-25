import streamlit as st

# Настраиваем навигацию по вашим двум файлам
pg = st.navigation([
    st.Page("users.py", title="Пользователи"),
    st.Page("admin.py", title="Админ-панель")
])

# Запускаем выбранную страницу
pg.run()