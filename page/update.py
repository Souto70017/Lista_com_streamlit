import streamlit as st
import controller.tarefa as tarefa

 
def marcar():
    if "upda" not in st.session_state:
        st.session_state.upda = False

    st.title('Marcar se Concluiu')
  

    update_id = st.number_input(label='Insira o Id', format='%d', step=1)
    button_update_select = st.button('Consultar')

    if button_update_select:
        st.session_state.upda = True

    if st.session_state.upda == True:
        concluido = tarefa.selecionar_id(update_id)[0]
        with st.form(key='update'):
            concluido = st.selectbox(label="Selecione o status de conclusão:", options=["Sim", "Não"])
            button_update = st.form_submit_button('Alterar')

            if button_update:
                tarefa.marcar_tarefa(update_id, concluido == "Sim")
                st.success('Alterado com sucesso!!!')
                st.session_state.upda = False

marcar()
