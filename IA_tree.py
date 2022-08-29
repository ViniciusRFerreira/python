import streamlit as st
import pandas as pd
import graphviz
from sklearn import tree

dJogo = {
'Tempo'       : ['Chuvoso', 'Ensolarado', 'Ensolarado', 'Nublado', 'Chuvoso',
                 'Chuvoso', 'Nublado', 'Nublado', 'Ensolarado', 'Chuvoso',
                 'Nublado', 'Ensolarado',
                 'Ensolarado', 'Chuvoso'],
'Temperatura' : [22, 21, 27, 28, 21, 
                 18, 18, 22, 24, 20, 
                 27, 29, 22, 24],
'Umidade'     : [91,72,90,86,96,
                 70,65,90,70,80,
                 75,85,95,80],
'Vento'       : ['Sim','Não','Sim','Não','Não',
                 'Sim','Sim','Sim','Sim','Não',
                 'Não','Não','Não','Não'],
'Jogo'        : ['Não','Sim','Não','Sim','Sim',
                 'Não','Sim','Sim','Sim','Sim',
                 'Sim','Não','Não','Sim']
}
dfTenis = pd.DataFrame(dJogo)

st.title('Vai ter jogo ?') #Título para a página
tempo = st.selectbox("Tempo: ",['Chuvoso','Ensolarado','Nublado'])
vento = st.selectbox("Vento: ",['Sim',"Não"])
umidade = st.slider("Umidade: ",0,100,50)
temperatura = st.number_input("Temperatura: ",-50,50,20)
st.metric(label='Umidade', value=f'{umidade} %')
st.metric(label='Temperatura', value=f'{temperatura} °C')





alvo = 'Jogo' #variável alvo
quali = ['Tempo', 'Vento'] #Variáveis qualitativas
quant = ['Temperatura', 'Umidade'] #Variáveis quantitativas



target = dfTenis[alvo] #Separa a variável alvo
dfQualiDummies = pd.get_dummies(dfTenis[quali]) #Dataframe com qualitativas dummy
dfQuant = dfTenis[quant] #Dataframe com quantitativas
dfWork = pd.concat([dfQualiDummies, dfQuant], axis=1) #Dataframe com todas variáveis

arv = tree.DecisionTreeClassifier() #árvore de decisão
# arv = tree.DecisionTreeRegressor()  #árvore de regressão

# Gere a árvore
arv.fit(dfWork, target) #cria a árvore

# Visualize a árvore (passo não obrigatório)
dot_data = tree.export_graphviz(arv, 
feature_names=dfWork.columns,  #variáveis
class_names=arv.classes_,      #valores dos resultados
out_file=None,                 #Arquivo de saída
#configurações dos nós
filled=True, rounded=True,     
special_characters=True)  
graph = graphviz.Source(dot_data)  
graph