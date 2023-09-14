import streamlit as st

import controller.tarefa as tarefa


def deletar():
    if "dele" not in st.session_state:
        st.session_state.dele = False

    st.title('Deletar tarefa')

    delete_id = st.number_input(label='Insira o Id', format='%d', step=1)
    button_delete_select = st.button('Consultar')

    if button_delete_select:
        st.session_state.dele = True

    if st.session_state.dele == True:
        item = tarefa.selecionar_id(delete_id)[0]
        st.write(item)
        button_delete = st.button('Deletar')

        if button_delete:
            tarefa.deletar(item[0])
            st.success('tarefa deletada com sucesso!!!')
            st.session_state.dele = False
