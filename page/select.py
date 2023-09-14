import streamlit as st
import controller.tarefa as tarefa

def consultar():

    st.title('Ver tarefas')

    colunas = st.columns((1,2,1))
    campos = ['Id','Descrição','Concluido']
    for coluna, campo in zip(colunas,campos):
        coluna.write(campo)

    for item in tarefa.ver_tarefas():
        col1,col2,col3 = st.columns((1,2,1))
        col1.write(item[0])
        col2.write(item[1])
        col3.write("Sim" if item[2] == 1 else "Não")
    