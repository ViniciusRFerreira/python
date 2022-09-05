import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn.linear_model import LinearRegression #Regressão linear
from sklearn import metrics #Cálculo do erro
import streamlit as st

st.title('Vinicius') #Título para a página

aptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')

bairros = aptos['bairro'].unique()
bairro = st.selectbox('Bairro desejado:', bairros)
st.write('Bairro escolhido: ', bairro)


bairro2 = aptos[aptos['bairro']==bairro]

min_quarto = int(bairro2['quartos'].min())
max_quarto = int(bairro2['quartos'].max())
meio_quarto = (max_quarto+min_quarto)//2
quartos = st.slider('Número de quartos: ', min_quarto, max_quarto, meio_quarto)

min_area = int(bairro2['area'].min())
max_area = int(bairro2['area'].max())
meio_area = (max_area+min_area)//2

area = st.slider('Area: ', min_area, max_area, meio_area)


x = bairro2[['quartos','area']].values.reshape(-1,2)
y = bairro2['preco'].values.flatten()

rl = LinearRegression()

rl.fit(x,y)

x = [[quartos],[area]]#Valor para a variável independente
x_arr = np.array(x).reshape(-1,2) #prepara para o formato adequado
y_pred  = rl.predict(x_arr) #calcula a predição
st.write(f'Quartos : ( {quartos} )')
st.write(f'Area : ( {area} ) m²')
st.write('Preço : ', y_pred.flatten())