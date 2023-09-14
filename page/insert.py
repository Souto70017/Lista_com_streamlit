import streamlit as st
import controller.tarefa as tarefa


def inserir():
    st.title('Adicionar uma tarefa')
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira a Descrição')
        button_submit = st.form_submit_button('Enviar')

        if button_submit:
            tarefa.adicionar(input_name)
            st.success('Tarefa incluido com sucesso!!!')