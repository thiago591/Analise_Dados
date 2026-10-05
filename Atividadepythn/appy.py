import streamlit as st
import pandas as pd


st.write("Olá, mundo")


# 6. Variáveis com nome e idade
nome = "Python"
idade = 20

st.write("Meu nome é", nome)
st.write("Minha idade é", idade)


# 10. Criando o dataframe
df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})


# 11. Título
st.title("Meu primeiro dash")


# 12. Subtítulo
st.subheader(nome)


# 13. Exibindo o dataframe
st.write(df)


# Separador
st.divider()


# 16. Caixa de seleção para supermercado
st.subheader("Lista de supermercado")

produto = st.selectbox(
    "Escolha um produto:",
    ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]
)


# Preços dos produtos
precos = {
    "Arroz": 25.00,
    "Feijão": 8.00,
    "Macarrão": 5.00,
    "Leite": 6.00,
    "Café": 18.00
}


# 17. Função para calcular o preço
def calcular_preco(produto):
    return precos[produto]


preco = calcular_preco(produto)

st.metric("Preço da compra", f"R$ {preco:.2f}")
