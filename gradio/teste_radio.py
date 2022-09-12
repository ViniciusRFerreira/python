import gradio as gr
import numpy as np

# ----------------------------------------------------
# 1º Código - Entrada e saída de nome

# def oi(nome):
#     frase = f'Olá {nome}.'
#     return frase

# with gr.Blocks() as app:
#     nome = gr.Textbox(label='Nome')
#     saida = gr.Textbox(label='Saida')
#     botao = gr.Button('Oi')

#     botao.click(fn=oi, inputs=nome, outputs=saida)

# app.launch()
#----------------------------------------------------

# ----------------------------------------------------
# 2º Código - Entrada e saída de nome

# def sepia(input_img):
#     sepia_filter = np.array([
#         [0.393, 0.769, 0.189], 
#         [0.349, 0.686, 0.168], 
#         [0.272, 0.534, 0.131]
#     ])
#     sepia_img = input_img.dot(sepia_filter.T)
#     sepia_img /= sepia_img.max()
#     return sepia_img

# demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
# demo.launch()
#----------------------------------------------------

def sketch():
    pass

with gr.Blocks() as app:
    saida = gr.Textbox()
    inter = gr.Interface(fn=sketch, 
             inputs="sketchpad",
             outputs=saida,
             live=True)

app.launch()