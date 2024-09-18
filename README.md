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
```

Essa estrutura básica foi expandida no projeto para incluir controle total sobre os corpos celestes.

## 🚀 Como Executar o Projeto

Siga as instruções abaixo para executar o projeto localmente em sua máquina:

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar dependências

O projeto requer Python 3.9+ e algumas bibliotecas específicas. Você pode instalar as dependências com:

```bash
pip install -r requirements.txt
```

### 3. Executar a simulação

Após instalar as dependências, basta executar o seguinte comando para rodar o simulador:

```bash
python main.py
```

### 4. Criar o executável com **cx_Freeze**

Criamos um executável para facilitar o uso do programa sem a necessidade de rodar diretamente o script. Para gerar o executável localmente, basta rodar o comando:

```bash
python setup.py build
```

Isso criará um diretório `build` contendo o executável do programa.

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
- **Pygame** – Para a simulação visual dos corpos celestes.
- **Tkinter** – Para a interface gráfica do usuário (GUI).
- **cx_Freeze** – Para criar um executável da aplicação.

## 👨‍💻 Créditos

Este projeto é baseado no simulador original de [Getulio Mendes](https://github.com/Getulio-Mendes/gravity-simulation). Fizemos modificações e melhorias para incluir uma interface gráfica com o **Tkinter** e algumas otimizações no desempenho.


Esse é o código Markdown completo para o README que pode ser copiado diretamente para o arquivo `README.md` do seu repositório.
