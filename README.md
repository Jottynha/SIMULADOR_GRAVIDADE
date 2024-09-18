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
   
   $$\vec{F} = \vec{0} \implies \vec{v} = \text{constante}$$
   
3. **Segunda Lei de Newton**: Relaciona a força atuante sobre um corpo, sua massa e sua aceleração.

   $$\vec{F} = m \cdot \vec{a}$$
   
5. **Terceira Lei de Newton** (Lei de Ação e Reação): Para toda ação há uma reação igual e oposta.

   $$\vec{F_{12}} = -\vec{F_{21}}$$

As forças gravitacionais sempre atuam ao longo da linha que une as duas partículas e têm módulos iguais, independentemente das massas. A força gravitacional \( F_g \) entre dois corpos de massas \( m_1 \) e \( m_2 \) separados por uma distância \( r \) é dada pela fórmula:

$$F_g = G \frac{m_1 m_2}{r^2}$$

A força gravitacional entre duas partículas diminui com o aumento da distância \(r\). O valor da constante gravitacional \(G\) foi determinado por Henry Cavendish em 1798, e seu valor atualmente aceito (em unidades SI) é:

$$G = 6.67384(80) \cdot 10^{-11} \, \text{N} \cdot \text{m}^2 / \text{kg}^{-2}$$

## Desenvolvimento da Interface

Para o desenvolvimento deste trabalho, adotou-se uma abordagem orientada ao design da interface do usuário e à manipulação interativa do programa. A metodologia utilizada focou na criação de uma interface gráfica intuitiva e funcional, empregando a biblioteca Tkinter em Python. A seguir, descreve-se a abordagem detalhada adotada para implementar as funcionalidades do Front-End do programa.

A interface gráfica do simulador foi desenvolvida utilizando a biblioteca Tkinter, que permite a criação de interfaces ricas e interativas em Python. Tkinter foi escolhido devido à sua simplicidade e integração direta com o Python, facilitando o desenvolvimento e a manutenção do código.

### Visualização e Atualização da Simulação

A visualização da simulação é atualizada em tempo real em uma área dedicada da interface. Esta área mostra a movimentação dos corpos e os efeitos da gravitação, permitindo ao usuário acompanhar a simulação de forma dinâmica. O programa utiliza um loop de eventos para atualizar continuamente a visualização da simulação. Cada iteração do loop recalcula as posições dos corpos com base nas forças gravitacionais e atualiza a exibição gráfica. Além disso, um arquivo de texto é utilizado como base de dados, onde as interfaces que adicionam corpos celestes em simulações personalizadas manipulam diretamente este mesmo arquivo.

### Componentes da Interface

A interface foi projetada para permitir ao usuário interagir com a simulação de forma intuitiva. O layout inclui elementos visuais como botões, campos de entrada e áreas de visualização, dispostos de forma a maximizar a usabilidade e a clareza das informações apresentadas.

- **Botões e Controles:** Foram implementados botões para iniciar, pausar e reiniciar a simulação. Controles adicionais permitem a configuração dos parâmetros da simulação, como a massa dos corpos e a distância entre eles. Clicando com o mouse sobre cada corpo, é possível visualizar a distância em AU dos demais corpos ou as informações simplificadas do corpo selecionado.

- **Campos de Entrada:** O usuário pode inserir valores diretamente nos campos de entrada para ajustar os parâmetros da simulação. Isso inclui a definição das características dos corpos em simulação, como suas massas, posições iniciais, cores e velocidades iniciais.

- **Legendas Intuitivas:** A interface inclui legendas que auxiliam o usuário a utilizar o programa, demonstrando como a simulação pode ser manipulada e como cada campo influencia na simulação.

- **Manipulação dos Dados:** Os dados colocados dentro do arquivo de dados podem ser limpos a qualquer instante, proporcionando maior liberdade e facilidade para o usuário nas simulações desejadas.

### Interatividade e Feedback

Para garantir uma experiência de usuário fluida e interativa, foram implementadas técnicas de manipulação dinâmica e atualização em tempo real dos elementos da interface. A seguir, detalha-se como essas manipulações são realizadas:

- **Interatividade:** A interface permite ao usuário interagir diretamente com a simulação através de controles e ajustes. As entradas do usuário são processadas em tempo real, ajustando os parâmetros da simulação conforme necessário.

- **Feedback Imediato:** A resposta da interface às ações do usuário é imediata, proporcionando um feedback visual claro. Isso inclui a atualização das informações exibidas e a adaptação da simulação de acordo com as mudanças nos parâmetros.

Essa abordagem permite uma interação eficiente e intuitiva com o simulador de gravidade, facilitando o uso e compreensão dos resultados obtidos na simulação.

## Proposta de Atividade

### Lei da Gravitação Universal

A partir da lei da gravitação universal de Newton, a força que o Sol exerce sobre a Terra é dada por:
 
$$F = \frac{G \cdot M_{\text{Sol}} \cdot M_{\text{Terra}}}{r^2}$$

onde \( G \) é a constante gravitacional, \( M_Sol \) e \( M_Terra \) são as massas do Sol e da Terra, respectivamente, e \( r \) é a distância entre os centros de massa da Terra e do Sol.

No vácuo espacial, onde não há atrito significativo, a única força relevante atuando sobre a Terra em sua órbita ao redor do Sol é a força gravitacional \( F \). De acordo com a segunda lei de Newton, temos:

$$\vec{F_r} = M_{\text{Terra}} \cdot \vec{a}_c$$

onde \( a_c \) é a aceleração centrípeta da Terra. A aceleração centrípeta, que aponta em direção ao centro do Sol, é dada por:

$$\vec{a}_c = \frac{v^2}{r}\hat{r}$$

onde \( v \) é a velocidade da Terra em sua órbita. Como a força gravitacional é a única força agindo na direção radial, temos que:

$$\frac{G \cdot M_{\text{Sol}} \cdot M_{\text{Terra}}}{r^2} = M_{\text{Terra}} \cdot \frac{v^2}{r}$$

Podemos simplificar a equação cancelando a massa da Terra \( M_{\text{Terra}} \):

$$\frac{G \cdot M_{\text{Sol}}}{r^2} = \frac{v^2}{r}$$

Multiplicando ambos os lados da equação por \( r \), obtemos:

$$v^2 = \frac{G \cdot M_{\text{Sol}}}{r}$$

Por fim, a velocidade orbital da Terra \( v \) é dada por:

$$v = \sqrt{\frac{G \cdot M_{\text{Sol}}}{r}}$$

Essa equação demonstra que a velocidade necessária para que a Terra orbite o Sol depende apenas da constante gravitacional \( G \), da massa do Sol \( M_Sol \) e da distância \( r \) entre a Terra e o Sol. A ausência de atrito no espaço significa que essa velocidade permanece constante, permitindo que a Terra mantenha sua órbita estável em torno do Sol.

### Dados e Cálculo

Buscando os dados na literatura, observamos que:

- $$G = 6{,}674 \cdot 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$$ é a constante gravitacional,
- $$M_{\text{Sol}} = 1{,}989 \cdot 10^{30} \, \text{kg}$$ é a massa do Sol,
- $$r = 1{,}496 \cdot 10^{11} \, \text{m}$$ é a distância média entre a Terra e o Sol.

Substituindo esses valores na equação:

$$v \approx 2{,}978 \cdot 10^4 \, \text{m/s}$$

Portanto, a velocidade orbital média da Terra ao redor do Sol é aproximadamente $v \approx 29{,}78 \cdot 10^3 \, \text{m/s}$.
### Unidade Astronômica (AU)

Antes de executar a simulação, é importante entender a conceituação de AU. Uma Unidade Astronômica (AU) é uma medida de distância utilizada principalmente para descrever as distâncias dentro do Sistema Solar. Ela é definida como a distância média entre a Terra e o Sol, que é aproximadamente \( 149.597.870,7 \) km. Essa unidade é especialmente útil em astronomia para simplificar a comunicação de grandes distâncias, como a distância entre planetas ou entre um planeta e o Sol. Por exemplo, a Terra está a 1 AU do Sol, enquanto Júpiter está a cerca de 5,2 AU.

### Passos para Executar a Simulação

Para executar a simulação no simulador de gravitação, siga os passos abaixo:

1. **Execução do Simulador:**
   - Abra o executável do simulador de gravitação. Isso pode ser feito clicando duas vezes no arquivo executável ou, se preferir, pelo terminal, utilizando o comando apropriado para o seu sistema operacional para executar o arquivo em Python.

2. **Escolha de Simulação Personalizada:**
   - No menu inicial do simulador, selecione a opção de "Não" para simulação pronta. Isso permitirá que você configure manualmente as condições iniciais do sistema que deseja simular.

3. **Adicionando o Sol:**
   - Coloque o Sol na origem do sistema de coordenadas, ou seja, na posição \((0,0)\) em unidades astronômicas (AU).
   - Defina a velocidade do Sol como $v_x = 0 \, \text{m/s}$ e $v_y = 0 \, \text{m/s}$.

4. **Adicionando a Terra:**
   - Adicione a Terra na posição \((1,0)\) em AU, que representa uma distância média de 1 unidade astronômica do Sol.
   - Defina a velocidade da Terra com $v_x = 0 \, \text{m/s}$ e $v_y = 29780 \, \text{m/s}$.

5. **Iniciando a Simulação:**
   - Após configurar o Sol e a Terra, inicie a simulação. O simulador calculará a trajetória da Terra ao redor do Sol com base nas condições iniciais fornecidas, mostrando uma órbita estável se os parâmetros estiverem corretos.

### Importância da Órbita da Terra

Segundo Graham, "[...] se a órbita da Terra tivesse sido um pouco mais longe dentro ou fora de onde está, a vida provavelmente nunca teria surgido e o planeta seria um deserto frio como Marte ou uma fornalha turva como Vênus". A órbita quase circular da Terra ao redor do Sol é um fator essencial para a manutenção da vida em nosso planeta. A estabilidade orbital resulta em uma distribuição relativamente uniforme da radiação solar ao longo do ano, evitando variações extremas de temperatura que tornariam a Terra inóspita. Essa regularidade garante a existência de estações do ano, ciclos climáticos estáveis e, em conjunto com a atmosfera, permite a formação e manutenção de ecossistemas. A constância da velocidade orbital e da distância média entre a Terra e o Sol também assegura que as condições para a presença de água líquida — elemento vital para a vida — permaneçam adequadas.


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
