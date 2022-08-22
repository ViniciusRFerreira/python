import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn.linear_model import LinearRegression #Regressão linear
from sklearn import metrics #Cálculo do erro
import streamlit as st

st.title('Vinicius') #Título para a página

aptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')

bairro = st.selectbox('Bairro desejado: ', ['Botafogo', 'Copacabana', 'Gávea','Grajaú','Ipanema','Leblon','Tijuca'])
st.write('Bairro escolhido: ', bairro)

bairro2 = aptos['bairro']==bairro
i = bairro2['quartos'].min()

quartos = st.slider('Número de quartos: ', i, 3, 2)
st.write('Quantidade de quartos escolhidos: ',quartos)



area = st.slider('Area: ', j, 475, 237)
st.write('Área escolhida: ',area)

rl = LinearRegression()

x = aptos[['quartos','area']].values.reshape(-1,2)
y = aptos['preco'].values.flatten()
rl.fit(x,y)

x = [[540],[35]]#Valor para a variável independente
x_arr = np.array(x).reshape(-1,2) #prepara para o formato adequado
y_pred  = rl.predict(x_arr) #calcula a predição
st.write('Condominio, Area: ',x_arr.flatten())
st.write('Preço : ', y_pred.flatten())

