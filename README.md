# 🌍🔭 Gravitação e Simulação de Órbitas com Tkinter e Pygame

Este repositório contém uma simulação de gravitação e órbitas planetárias utilizando o **Pygame** para visualização e o **Tkinter** para a criação de interfaces gráficas interativas. A simulação é inspirada no projeto original de [Getulio Mendes](https://github.com/Getulio-Mendes/gravity-simulation), e adicionamos uma interface gráfica que permite ao usuário manipular os parâmetros de simulação com facilidade.

## 📋 Funcionalidades

- Visualização em tempo real de órbitas planetárias e sistemas gravitacionais.
- Interface gráfica para controle e manipulação dos corpos celestes (como massa, posição, velocidade, etc.) através do **Tkinter**.
- Simulação eficiente e fluida com **Pygame**.
- Criação de um executável para fácil uso, utilizando **cx_Freeze**.

## 🎮 Demonstração da Interface

A interface gráfica foi projetada para ser simples e intuitiva, usando o **Tkinter**. Abaixo, mostramos um exemplo de código básico da estrutura de uma janela criada com o Tkinter para o projeto:

```python
import tkinter as tk

def iniciar_simulacao():
    print("Simulação Iniciada!")
    # Aqui você chama a função do Pygame que inicializa a simulação.

# Criando a janela principal
janela = tk.Tk()
janela.title("Simulação de Gravidade")

# Criando os elementos da interface
label = tk.Label(janela, text="Bem-vindo à Simulação de Gravidade")
label.pack()

botao_iniciar = tk.Button(janela, text="Iniciar Simulação", command=iniciar_simulacao)
botao_iniciar.pack()

# Rodando a interface gráfica
janela.mainloop()
