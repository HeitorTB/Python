import streamlit as st

st.title('Cadastro de clientes')

nome = st.text_input("Digite o nome do cliente")
endereço = st.text_input("Digite o endereço")
dt_nasc = st.date_input("Selecione a data de nascimento")
tipo_cliente = st.selectbox("Tipo de cliente", ["Pessoa Física", "Pessoa Jurídica"])
cadastrar=st.button("Cadastrar Cliente")
if cadastrar:
    with open("clientes.csv", "a", encoding="utf-8") as arquivo:
        arquivo.write(f'{nome},{endereço},{dt_nasc},{tipo_cliente}\n')
        st.success('Cliente cadastrado com sucesso')