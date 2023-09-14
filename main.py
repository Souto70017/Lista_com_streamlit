import streamlit as st
import page.insert as insert
import page.select as select
import page.delete as delete
import page.update as update



st.sidebar.title('Tarefas')
page = st.sidebar.selectbox('Menu',['Inserir','Consultar','Marcar','Deletar'])

if page == 'Consultar':
    select.consultar()
if page == 'Inserir':
    insert.inserir()
if page == 'Marcar':
    update.marcar()
if page == 'Deletar':
    delete.deletar()
