# 🌍🔭 Gravitação e Simulação de Órbitas com Tkinter e Pygame

Este repositório contém uma simulação de gravitação e órbitas planetárias utilizando o **Pygame** para visualização e o **Tkinter** para a criação de interfaces gráficas interativas. A simulação é inspirada no projeto original de [Getulio Mendes](https://github.com/Getulio-Mendes/gravity-simulation), e adicionamos uma interface gráfica que permite ao usuário manipular os parâmetros de simulação com facilidade.

## 🎯 Objetivo

Este trabalho tem como objetivo implementar, dentro de um código funcional que simula comportamentos planetários, uma interação mais eficiente e otimizada entre o usuário e o simulador. Para isso, buscamos preservar o funcionamento original da simulação, ao mesmo tempo em que inserimos interfaces que facilitam o uso do software, incluindo novos recursos que expandem suas possibilidades. Utilizaremos a linguagem original do simulador, Python, e manipularemos a biblioteca **Tkinter** para o desenvolvimento dessas otimizações.

## 🌍 Fundamentos Teóricos

Neste trabalho, utilizamos a lei básica que governa a interação gravitacional. De acordo com o livro de física "Fundamentos de Oscilações, Fluídos e Termodinâmica" de Young & Freedman (2015), essa lei é universal: a gravidade atua do mesmo modo fundamental entre a Terra e o corpo do leitor deste arquivo, entre o Sol e um planeta, e entre um planeta e uma de suas luas.

Estudando o movimento da Lua e dos planetas, Isaac Newton descobriu uma lei da gravitação que oferece o caráter fundamental da atração gravitacional entre dois corpos de qualquer natureza. Com as três leis do movimento, Newton publicou a lei da gravitação em 1687. Ela pode ser enunciada do seguinte modo, em linguagem moderna:

> *Cada partícula do universo atrai qualquer outra partícula com uma força diretamente proporcional ao produto das respectivas massas e inversamente proporcional ao quadrado da distância entre as partículas.*

Para chegar a essa conclusão, Newton utilizou suas três leis do movimento:

1. **Primeira Lei de Newton** (Lei da Inércia): Um corpo em repouso permanece em repouso e um corpo em movimento continua em movimento retilíneo uniforme, a menos que seja atuado por uma força externa.
   
   $$ \vec{F} = \vec{0} \implies \vec{v} = \text{constante} $$
   
3. **Segunda Lei de Newton**: Relaciona a força atuante sobre um corpo, sua massa e sua aceleração.

   A fórmula é: `F = m * a`

4. **Terceira Lei de Newton** (Lei de Ação e Reação): Para toda ação há uma reação igual e oposta.

   A fórmula é: `F_12 = -F_21`

As forças gravitacionais sempre atuam ao longo da linha que une as duas partículas e têm módulos iguais, independentemente das massas. A força gravitacional \( F_g \) entre dois corpos de massas \( m_1 \) e \( m_2 \) separados por uma distância \( r \) é dada pela fórmula:

$$ F_g = G \frac{m_1 m_2}{r^2} $$

A força gravitacional entre duas partículas diminui com o aumento da distância \(r\). O valor da constante gravitacional \(G\) foi determinado por Henry Cavendish em 1798, e seu valor atualmente aceito (em unidades SI) é:

$$ G = 6.67384(80) \cdot 10^{-11} \, \text{N} \cdot \text{m}^2 / \text{kg}^{-2} $$

### 🛰️ Simulador de Gravidade

O simulador de gravidade foi projetado para demonstrar a aplicação prática da Lei da Gravitação Universal. A implementação do código Python segue os princípios teóricos da seguinte forma:

- **Cálculo da Força Gravitacional:** A fórmula da gravitação universal é implementada para calcular a força de atração entre dois corpos celestes. A função `calcular_forca_gravitacional` recebe as massas e a distância entre os corpos e retorna a força gravitacional.
  
- **Atualização das Posições:** A força gravitacional calculada é utilizada para atualizar as posições dos corpos. As equações do movimento consideram a força de atração gravitacional, permitindo que os corpos interajam de acordo com as leis de Newton.

- **Interface Gráfica:** A interface gráfica, desenvolvida com **Pygame**, permite visualizar as interações gravitacionais em tempo real. O usuário pode ajustar as massas e a distância entre os corpos e observar as mudanças nas órbitas e nas forças de atração.

A aplicação desses fundamentos teóricos no projeto oferece uma visualização interativa dos conceitos de gravitação universal, permitindo ao usuário explorar as variações de massa e distância entre corpos celestes.


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
git clone https://github.com/Jottynha/SIMULADOR_GRAVIDADE.git
cd seu-repositorio
```

### 2. Instalar dependências

O projeto requer Python 3.9+ e algumas bibliotecas específicas. Você pode instalar as dependências com:

```bash
Instalar (Python, Pygame e Tkinter):
sudo apt-get install python3.9
sudo apt-get install python3-pip
sudo apt-get install python3-tk
pip install pygame
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
