import pygame
import math
import re
import tkinter as tk
import threading
from tkinter import messagebox
from math import sqrt

from arrow import draw_arrow

cores_portugues_ingles = {
    "azul": "blue",
    "verde": "green",
    "vermelho": "red",
    "amarelo": "yellow",
    "roxo": "purple",
    "rosa": "pink",
    "laranja": "orange",
    "branco": "white",
    "preto": "black",
    "cinza": "gray",
    "marrom": "brown",
    "ciano": "cyan",
    "magenta": "magenta",
    "prata": "silver",
    "ouro": "gold",
    "bege": "beige",
    "turquesa": "turquoise",
    "lima": "lime",
    "salmão": "salmon",
    "índigo": "indigo",
    "vermelho escuro": "darkred",
    "verde escuro": "darkgreen",
    "azul escuro": "darkblue",
    "violeta escuro": "darkviolet",
    "amarelo escuro": "darkyellow",
    "marrom escuro": "darkbrown",
    "cinza escuro": "darkgray",
    "vermelho claro": "lightred",
    "verde claro": "lightgreen",
    "azul claro": "lightblue",
    "violeta claro": "lightviolet",
    "amarelo claro": "lightyellow",
    "marrom claro": "lightbrown",
    "cinza claro": "lightgray",
    "vermelho rosado": "rosybrown",
    "azul celeste": "skyblue",
    "verde marinho": "seagreen",
    "amarelo dourado": "goldenrod",
    "rosa claro": "lightpink",
    "azul marinho": "navy",
    "amarelo ouro": "golden",
    "azul aço": "steelblue",
    "verde oliva": "olive",
    "azul ardósia": "slateblue",
    "verde limão": "limegreen",
    "rosa profundo": "deeppink",
    "azul profundo": "deepskyblue",
    "verde floresta": "forestgreen",
    "azul marinho": "midnightblue",
    "rosa quente": "hotpink",
    "azul médio": "mediumblue",
    "verde médio": "mediumseagreen",
    "amarelo médio": "mediumyellow",
    "azul médio": "mediumblue",
    "verde musgo": "darkolivegreen",
    "azul ardósia": "slateblue",
    "turquesa pálida": "palegreen",
    "verde primavera": "springgreen",
    "azul aço claro": "lightsteelblue",
    "verde marinho claro": "lightseagreen",
    "azul ardósia claro": "lightslategray",
    "azul ardósia pálido": "lightblue",
    "verde primavera médio": "mediumspringgreen",
    "azul pálido": "paleblue",
    "azul ardósia pálido": "lightslateblue",
    "azul ardósia pálido": "lightskyblue",
    "azul ardósia pálido": "lightslateblue",
    "azul ardósia pálido": "lightskyblue",
    "azul ardósia pálido": "lightslateblue",
    "azul ardósia pálido": "lightskyblue",
    "azul ardósia pálido": "lightslateblue",
    "azul ardósia pálido": "lightskyblue",
    "azul ardósia pálido": "lightslateblue",
}




class Body:
    def __init__(self, x, y, vx, vy, mass, color, radius,name):
        self.x = x
        self.y = y
        self.vy = vy
        self.vx = vx
        self.mass = mass
        self.color = color
        self.radius = radius
        self.name = name
        self.trace = []
        self.changed = False

    def print(self):
        print("\t------ {} ------".format(self.name))
        print("Velocidade x: {} m/s".format(self.vx))
        print("Velocidade y: {} m/s".format(self.vy))
        print("Massa : {} kg".format(self.mass))

    #Função que guarda as informações do corpo planetário
    def storage(self):
        info_planeta = {
            'Nome': self.name,
            'Velocidade X (m/s)': self.vx,
            'Velocidade Y (m/s)': self.vy,
            'Massa (kg)': self.mass
        }
        return info_planeta
    
    def aumentar_velocidade(self):
        # Aumenta a velocidade do corpo em uma certa porcentagem
        self.vx *= 1.1
        self.vy *= 1.1

    def draw(self, win, ZOOM, SCALE):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        if len(self.trace) > 2:
            traceLine = []
            for point in self.trace:
                x, y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                traceLine.append((x, y))
            pygame.draw.lines(win, self.color, False, traceLine, 2)

        # Desenhar o corpo celeste
        pygame.draw.circle(win, self.color, (x, y), self.radius / ZOOM)

    def attraction(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def changeVel(self,x2,y2,SCALE):

        if self.changed == False:
            x1 = self.x * SCALE + WIDTH/2
            y1 = self.y * SCALE + HEIGHT/2

            theta = math.atan2(y2 - y1, x2 - x1)
            mod = math.dist([x2,y2],[x1,y1])

            self.vx = math.cos(theta) * mod * 100
            self.vy = math.sin(theta) * mod * 100
            self.changed = True


    def updatePosition(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.vx += total_fx / self.mass * TIMESTEP
        self.vy += total_fy / self.mass * TIMESTEP

        self.x += self.vx * TIMESTEP
        self.y += self.vy * TIMESTEP

        self.trace.append((self.x, self.y))

        if len(self.trace) > 100:
            self.trace.pop(0)
        self.changed = False


class gVar:

    def __init__(self):
        self.ZOOM = 1
        self.SCALE = 250 / AU
        self.PAUSE = False

    def addZoom(self,where,bodies):
        if where:
            if(self.ZOOM < 2):
                self.ZOOM = self.ZOOM + 0.1
                self.SCALE = self.SCALE - self.SCALE * 0.1
        else:
            if(self.ZOOM > 0.5):
                self.ZOOM = self.ZOOM - 0.1
                self.SCALE = self.SCALE + self.SCALE * 0.1

        for bodie in bodies:
            bodie.trace = []

    def pause(self):
        self.PAUSE = not self.PAUSE


PI = 3.14159265358979323
# AU em metros
AU = 149.6e6 * 1000
G = 6.67428e-11
# Tick da simulação = 1 dia
TIMESTEP = 3600*24

WIDTH = 900
HEIGHT = 700


def bodiesInit(custom):
    
    # position = AU
    # vel = m/s
    # mass = kg
    bodies = []

    if custom:
        input = open("input.data","r")
        for line in input.readlines():
            x = re.search("x: [0-9e*,.-]+",line)
            x = x.group()
            x = x.split()[-1]
            x = eval(x)
            x = x*AU

            y = re.search("y: [0-9e*,.-]+",line)
            y = y.group()
            y = y.split()[-1]
            y = eval(y)
            y = y*AU

            vx = re.search("vx: [0-9e*,.-]+",line)
            vx = vx.group()
            vx = vx.split()[-1]
            vx = eval(vx)

            vy = re.search("vy: [0-9e*,.-]+",line)
            vy = vy.group()
            vy = vy.split()[-1]
            vy = eval(vy)

            massa = re.search("massa: [0-9e*,.-]+",line)
            massa = massa.group()
            massa = massa.split()[-1]
            massa = eval(massa)

            cor = re.search("cor: \w+",line)
            cor = cor.group()
            cor = cor.split()[-1]

            r = re.search("raio: [0-9e*,.-]+",line)
            r = r.group()
            r = r.split()[-1]
            r = eval(r)

            name = re.search("nome: \w+",line)
            name = name.group()
            name = name.split()[-1]

            newB = Body(x,y,vx,vy,massa,pygame.Color(cor),r,name)
            bodies.append(newB)

        input.close()
        return bodies

    else:

        sun = Body(0, 0,0,0,1.98892 * 10**30,
            pygame.Color("gold"),50,"Sol")

        earth = Body(-1 * AU, 0,0,29.783 * 1000,5.9742 * 10**24,
            pygame.Color("aquamarine2"),10,"Terra")
        mars = Body(-1.524 * AU, 0,0,24.077 * 1000, 6.39 * 10**23,
            pygame.Color("brown3"),10,"Marte")
        mercury = Body(0.387 * AU, 0,0,-47.4 * 1000,3.30 * 10**23,
            pygame.Color("darkgray"),10,"Mercúrio")
        venus = Body(0.723 * AU, 0,0,-35.02 * 1000,4.8685 * 10**24,
            pygame.Color("darkorange3"),10,"Vênus")
        saturn = Body(-1.61 * AU,0,0, 27.3886 * 1000 ,5.683 * 10**26, 
            pygame.Color("antiquewhite1"), 15,"Saturno") 

        return [sun, earth,mars,mercury,venus,saturn]


def checkCollision(x1,y1,r1,x2,y2,r2):
    if(math.dist([x1,y1],[x2,y2]) < r1 + r2):
        return True

def velArrow(win,const,arrow):
    start = pygame.Vector2(arrow[2],arrow[3])
    end = pygame.Vector2(arrow[0],arrow[1])
    draw_arrow(win,start,end,pygame.Color("red"),4/const.ZOOM,12/const.ZOOM,12/const.ZOOM)

def mostrar_opcao_simulacao_pronta():
    root = tk.Tk()
    root.title("Tela Inicial")
    root.configure(bg="#cfe8fc")  # Define uma cor de fundo azul pastel mais leve

    # Frame para o GIF à esquerda
    frame_gif = tk.Frame(root, bg="#cfe8fc")
    frame_gif.pack(side=tk.LEFT, padx=20, pady=20)

    # Frame para as informações à direita
    frame_info = tk.Frame(root, bg="#cfe8fc")
    frame_info.pack(side=tk.RIGHT, padx=20, pady=20)

    # Carrega o GIF animado
    gif_path = "figuras/Sistema-Solar.gif"  # Substitua pelo caminho do seu arquivo GIF
    gif = tk.PhotoImage(file=gif_path)

    # Exibe o GIF em um rótulo
    label_gif = tk.Label(root, image=gif, bg="#cfe8fc")
    label_gif.pack(pady=10)


    # Texto de boas-vindas e informações sobre os comandos do Pygame
    boas_vindas = "\nBem-vindo à Simulação de Corpos Celestes!\n\n"
    comandos_pygame = (
        "\nComandos Pygame:\n\n" \
        "Espaço: Pausar/Continuar\n" \
        "Scroll do Mouse: Zoom in e Zoom out\n" \
        "Botão esquerdo do mouse: Exibir informações do corpo celestial\n" \
        "Botão direito do mouse: Exibir as distâncias do corpo aos demais\n" \
        "J: Adicionar novo corpo celestial\n" \
        "I: Exibir informações dos corpos celestes\n" \
        "V: Aumenta a velocidade do corpo selecionado com o Botão Esquerdo\n" \
        "S: Encerrar o programa\n" \
        "ESC: Reiniciar a simulação\n" \
        "Para saber informações específicas, clique no planeta desejado\n" \
        "(aconselhamos a pausar a simulação quando essa operação for desejada)"
    )

    # Estilo de texto mais moderno e fonte
    fonte_boas_vindas = ("Arial", 16, "bold")
    fonte_comandos = ("Arial", 12)
    cor_texto = "#333333"  # Cor de texto mais escura para contraste

    # Rótulo de boas-vindas
    label_welcome = tk.Label(frame_info, text=boas_vindas + comandos_pygame, font=fonte_boas_vindas, fg=cor_texto, bg="#cfe8fc")
    label_welcome.pack(pady=20, padx=20, anchor="w")

    def start_custom_simulation():
        root.destroy()
        adicionar_corpo()
        main(custom=True)

    def start_default_simulation():
        root.destroy()
         # Mostrar uma mensagem de simulação pronta
        messagebox.showinfo("Simulação Pronta", "Essa é uma simulação do Sistema Solar, considerando os planetas de Mercúrio até Saturno.")
        main(custom=False)

    # Frame para a pergunta e os botões
    frame_pergunta_botoes = tk.Frame(frame_info, bg="#cfe8fc")
    frame_pergunta_botoes.pack(pady=(0, 10))

    # Rótulo da pergunta
    label_pergunta = tk.Label(frame_pergunta_botoes, text="Gostaria de utilizar uma simulação pronta?", font=("Arial", 14), fg=cor_texto, bg="#cfe8fc")
    label_pergunta.pack(pady=(0, 10), padx=20)

    # Botões dentro do frame de perguntas e botões
    btn_sim = tk.Button(frame_pergunta_botoes, text="Sim", font=("Helvetica", 12), command=start_default_simulation)
    btn_sim.pack()

    btn_nao = tk.Button(frame_pergunta_botoes, text="Não", font=("Helvetica", 12), command=start_custom_simulation)
    btn_nao.pack()

    root.mainloop()    

selected_body = None  # Inicializa selected_body

def main(custom=False):
    global selected_body
    pygame.init()
    const = gVar()

    clock = pygame.time.Clock()

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    background = (33, 33,33)
    pygame.display.set_caption("Simulador de Gravidade")

    bodies = bodiesInit(custom)

    mouseMotion = None
    dragged = False
    run = True
    arrows = []

    #Função para reiniciar o programa
    def reiniciar_programa():
        pygame.quit()  # Fecha o Pygame
        mostrar_opcao_simulacao_pronta()  # Mostra a opção de simulação novamente

    # Botão para reiniciar o programa
    btn_reiniciar = pygame.Rect(8, 8, 240, 40)  # Posição e tamanho do botão
    font = pygame.font.SysFont(None, 30)  # Fonte do texto do botão
    text = font.render("Reiniciar o Programa", True, (255, 255, 255))  # Texto do botão


    while run:
        # Roda 60 vezes por segundo
        clock.tick(60)
        # Background da janela
        win.fill(background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Lógica no loop principal para alternar a janela de informações
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    adicionar_corpo()
                # Pausa ao apertar espaço
                if event.key == pygame.K_i:
                        mostrar_informacoes_gui(bodies)  # Exibe a janela de informações
                if event.key == pygame.K_SPACE:
                    arrows = []
                    const.pause()
                # reseta ao apertar ESC
                if event.key == pygame.K_s:
                    pygame.quit()
                elif event.key == pygame.K_ESCAPE:
                    bodies = bodiesInit(custom)
                    const.SCALE = 250 / AU
                if event.key == pygame.K_v:  # Aumentar a velocidade do corpo selecionado
                    if selected_body is not None:
                        selected_body.aumentar_velocidade()  # Aqui você chama o método que aumenta a velocidade do corpo celeste selecionado


            elif event.type == pygame.MOUSEBUTTONUP:
                if const.PAUSE:
                    # Calcula a seta
                    if(dragged and mouseMotion[2].changed == False):
                        arrows.append((event.pos[0],event.pos[1],mouseMotion[0],mouseMotion[1],mouseMotion[2]))

                    mouseMotion = None
                    dragged = False
            
            elif event.type == pygame.MOUSEMOTION:
                # Drag da seta
                if mouseMotion != None:
                    if (math.fabs(event.pos[0] - mouseMotion[0]) > 10):
                        if(math.fabs(event.pos[1] - mouseMotion[1]) > 10):
                            dragged = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o botão de reiniciar foi clicado
                if btn_reiniciar.collidepoint(event.pos):
                    reiniciar_programa()
                if event.button == 5:
                    const.addZoom(1, bodies)
                elif event.button == 4:
                    const.addZoom(0, bodies)
                elif event.button == 1:  # Botão esquerdo do mouse
                    for body in bodies:
                        x = body.x * const.SCALE + WIDTH / 2
                        y = body.y * const.SCALE + HEIGHT / 2
                        if checkCollision(x, y, body.radius / const.ZOOM, event.pos[0], event.pos[1], 1):
                            mostrar_informacoes_planeta(body.name, body.storage())
                            # Se o corpo celeste foi clicado
                            selected_body = body
                elif event.button == 3:  # Botão direito do mouse
                    for body in bodies:
                        x = body.x * const.SCALE + WIDTH / 2
                        y = body.y * const.SCALE + HEIGHT / 2
                        if checkCollision(x, y, body.radius / const.ZOOM, event.pos[0], event.pos[1], 1):
                            # Encontra o corpo celeste clicado
                            clicked_body = body
                            # Calcula a distância entre o corpo clicado e os outros corpos celestes
                            distances = {other_body.name: calcular_distancia(clicked_body, other_body, const) for other_body in bodies if other_body != clicked_body}
                            # Mostra a distância em uma caixa de mensagem
                            message = "\n".join([f"{name}: {distance:.2f} AU" for name, distance in distances.items()])
                            messagebox.showinfo(title="Distâncias", message=message)

        pygame.draw.rect(win, (0, 255, 0), btn_reiniciar)  # Cor do botão
        win.blit(text, (btn_reiniciar.x + 25, btn_reiniciar.y + 10))  # Posição do texto do botão


        # Desenha as setas
        for arrow in arrows:
            velArrow(win,const,arrow) 

        # Desenha e atualiza os corpos
        for body in bodies:
            if not const.PAUSE:
                body.updatePosition(bodies)

            for arrow in arrows:
                if arrow[4].name == body.name:
                    body.changeVel(arrow[0],arrow[1],const.SCALE)

            body.draw(win,const.ZOOM,const.SCALE)

        # Update gráfico
        pygame.display.update()
    pygame.quit()


def calcular_distancia(body1, body2, const):
    distance_x = body2.x - body1.x
    distance_y = body2.y - body1.y
    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
    return distance / const.SCALE  # Converta para unidades astronômicas (AU)


#Coleta as informações no dicionário
def coletar_informacoes(bodies):
    todas_infos = []
    for body in bodies:
        info = body.storage()
        todas_infos.append(info)
    return todas_infos

def mostrar_informacoes_planeta(nome, info):
    # Formata as informações do planeta
    info_text = "\n".join([f"{key}: {value}" for key, value in info.items()])
    # Exibe as informações em uma messagebox sem botão "OK"
    messagebox.showinfo(title=nome, message=info_text, parent=None)


def mostrar_informacoes_gui(bodies):
    infos = coletar_informacoes(bodies)
    
    window = tk.Tk()
    window.title("Informações dos Planetas")
    
    # Definindo cores
    bg_color = "#f0f0f0"
    text_color = "#333333"
    
    # Criando frames para organizar os elementos
    header_frame = tk.Frame(window, bg=bg_color)
    header_frame.pack(pady=10)
    
    body_frame = tk.Frame(window, bg=bg_color)
    body_frame.pack(padx=10, pady=5)
    
    # Adicionando cabeçalho
    tk.Label(header_frame, text="Informações dos Planetas", font=("Helvetica", 16), fg="#007bff", bg=bg_color).pack()
    
    # Adicionando informações dos corpos celestes
    for info in infos:
        # Calcula a velocidade total
        velocidade_total = sqrt(info['Velocidade X (m/s)'] ** 2 + info['Velocidade Y (m/s)'] ** 2)
        info_text = f"Nome: {info['Nome']}, Velocidade Total: {velocidade_total:.2f} m/s, Massa: {info['Massa (kg)']}"
        tk.Label(body_frame, text=info_text, font=("Helvetica", 12), fg=text_color, bg=bg_color).pack(anchor="w", pady=3)
    # Adicionando informações sobre os comandos do Pygame
    pygame_info_text = "\nComandos Pygame:\n\n" \
                       "Espaço: Pausar/Continuar\n" \
                       "Scroll do Mouse: Zoom in e Zoom out\n" \
                       "Botão esquerdo do mouse: Exibir informações do corpo celestial\n" \
                       "Botão direito do mouse: Exibir as distâncias do corpo aos demais\n" \
                       "J: Adicionar novo corpo celestial\n" \
                       "I: Exibir informações dos corpos celestes\n" \
                       "V: Aumenta a velocidade do corpo selecionado com o Botão Esquerdo\n" \
                       "S: Encerrar o programa\n" \
                       "ESC: Reiniciar a simulação\n" \
                       "Para saber informações específicas, clique no planeta desejado (aconselhamos a pausar a simulação quando essa operação for desejada) "
    tk.Label(body_frame, text=pygame_info_text, font=("Helvetica", 12), fg=text_color, bg=bg_color).pack(anchor="center", pady=3)

    # Função para destruir a janela quando uma tecla é pressionada
    def destroy_window(event):
        window.destroy()
    
    # Vincula a função `destroy_window` ao evento de tecla pressionada
    window.bind("<KeyPress>", destroy_window)

    window.mainloop()
    return window



def adicionar_corpo():
    window = tk.Tk()  # Cria uma nova janela
    window.title("Adicionar Corpo Celeste")

    def on_entry_click(event, entry):
        if entry.cget("fg") == "gray":
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focusout(event, entry, default_text):
        if entry.get() == "":
            entry.insert(0, default_text)
            entry.config(fg="gray")

    def salvar_info():
        # Coleta as informações inseridas pelo usuário
        nome = nome_entry.get()
        x = x_entry.get()
        y = y_entry.get()
        massa = massa_entry.get()
        vx = vx_entry.get()
        vy = vy_entry.get()
        cor = cor_entry.get()
        raio = raio_entry.get()
        
        cor = cor_entry.get().lower()  # Converta para minúsculas para facilitar a comparação
        if cor in cores_portugues_ingles:
            cor = cores_portugues_ingles[cor]  # Use o equivalente em inglês


        # Formata as informações
        info_formatada = f"nome: {nome} x: {x} y: {y} massa: {massa} vx: {vx} vy: {vy} cor: {cor} raio: {raio}\n"

        # Salva as informações no arquivo input.data
        with open("input.data", "a") as arquivo:
            arquivo.write(info_formatada)

        # Limpa os campos de entrada após salvar
        nome_entry.delete(0, tk.END)
        x_entry.delete(0, tk.END)
        y_entry.delete(0, tk.END)
        massa_entry.delete(0, tk.END)
        vx_entry.delete(0, tk.END)
        vy_entry.delete(0, tk.END)
        cor_entry.delete(0, tk.END)
        raio_entry.delete(0, tk.END)

        # Mostra uma mensagem de confirmação
        messagebox.showinfo("Sucesso", "As informações foram salvas, reinicie o programa pressionando ESC para iniciar a simulação!")

    # Labels
    tk.Label(window, text="Nome do Corpo: ").grid(row=0, column=0)
    tk.Label(window, text="Posição em X: ").grid(row=1, column=0)
    tk.Label(window, text="Posição em Y: ").grid(row=2, column=0)
    tk.Label(window, text="Massa (kg): ").grid(row=3, column=0)
    tk.Label(window, text="Velocidade X (m/s): ").grid(row=4, column=0)
    tk.Label(window, text="Velocidade Y (m/s): ").grid(row=5, column=0)
    tk.Label(window, text="Cor: ").grid(row=6, column=0)
    tk.Label(window, text="Raio (m): ").grid(row=7, column=0)

    # Campos de entrada com sugestões visuais
    default_texts = [
        "Insira o nome do corpo celeste",
        "Insira a posição X",
        "Insira a posição Y",
        "1*E+x para 1*10^x",
        "Insira a velocidade X",
        "Insira a velocidade Y",
        "Em português",
        "Insira o raio"
    ]

    nome_entry = tk.Entry(window)
    nome_entry.grid(row=0, column=1)
    nome_entry.insert(tk.END, default_texts[0])
    nome_entry.config(fg="gray")
    nome_entry.bind("<FocusIn>", lambda event, entry=nome_entry: on_entry_click(event, entry))
    nome_entry.bind("<FocusOut>", lambda event, entry=nome_entry, default_text=default_texts[0]: on_focusout(event, entry, default_text))

    x_entry = tk.Entry(window)
    x_entry.grid(row=1, column=1)
    x_entry.insert(tk.END, default_texts[1])
    x_entry.config(fg="gray")
    x_entry.bind("<FocusIn>", lambda event, entry=x_entry: on_entry_click(event, entry))
    x_entry.bind("<FocusOut>", lambda event, entry=x_entry, default_text=default_texts[1]: on_focusout(event, entry, default_text))

    y_entry = tk.Entry(window)
    y_entry.grid(row=2, column=1)
    y_entry.insert(tk.END, default_texts[2])
    y_entry.config(fg="gray")
    y_entry.bind("<FocusIn>", lambda event, entry=y_entry: on_entry_click(event, entry))
    y_entry.bind("<FocusOut>", lambda event, entry=y_entry, default_text=default_texts[2]: on_focusout(event, entry, default_text))

    massa_entry = tk.Entry(window)
    massa_entry.grid(row=3, column=1)
    massa_entry.insert(tk.END, default_texts[3])
    massa_entry.config(fg="gray")
    massa_entry.bind("<FocusIn>", lambda event, entry=massa_entry: on_entry_click(event, entry))
    massa_entry.bind("<FocusOut>", lambda event, entry=massa_entry, default_text=default_texts[3]: on_focusout(event, entry, default_text))

    vx_entry = tk.Entry(window)
    vx_entry.grid(row=4, column=1)
    vx_entry.insert(tk.END, default_texts[4])
    vx_entry.config(fg="gray")
    vx_entry.bind("<FocusIn>", lambda event, entry=vx_entry: on_entry_click(event, entry))
    vx_entry.bind("<FocusOut>", lambda event, entry=vx_entry, default_text=default_texts[4]: on_focusout(event, entry, default_text))

    vy_entry = tk.Entry(window)
    vy_entry.grid(row=5, column=1)
    vy_entry.insert(tk.END, default_texts[5])
    vy_entry.config(fg="gray")
    vy_entry.bind("<FocusIn>", lambda event, entry=vy_entry: on_entry_click(event, entry))
    vy_entry.bind("<FocusOut>", lambda event, entry=vy_entry, default_text=default_texts[5]: on_focusout(event, entry, default_text))

    cor_entry = tk.Entry(window)
    cor_entry.grid(row=6, column=1)
    cor_entry.insert(tk.END, default_texts[6])
    cor_entry.config(fg="gray")
    cor_entry.bind("<FocusIn>", lambda event, entry=cor_entry: on_entry_click(event, entry))
    cor_entry.bind("<FocusOut>", lambda event, entry=cor_entry, default_text=default_texts[6]: on_focusout(event, entry, default_text))

    raio_entry = tk.Entry(window)
    raio_entry.grid(row=7, column=1)
    raio_entry.insert(tk.END, default_texts[7])
    raio_entry.config(fg="gray")
    raio_entry.bind("<FocusIn>", lambda event, entry=raio_entry: on_entry_click(event, entry))
    raio_entry.bind("<FocusOut>", lambda event, entry=raio_entry, default_text=default_texts[7]: on_focusout(event, entry, default_text))

    # Botão para salvar as informações
    botao_salvar = tk.Button(window, text="Salvar", command=salvar_info)
    botao_salvar.grid(row=8, column=0, columnspan=2, pady=10)

    def limpar_arquivo():
            # Confirmação do usuário
            resposta = messagebox.askquestion("Limpar Arquivo", "Tem certeza que deseja limpar o arquivo? Todas as informações serão perdidas.")

            if resposta == "yes":
                # Limpa o arquivo
                open('input.data', 'w').close()
                messagebox.showinfo("Limpar Arquivo", "Arquivo limpo com sucesso.")
            else:
                return
    # Botão para limpar o arquivo
    botao_limpar = tk.Button(window, text="Limpar Arquivo", command=limpar_arquivo)
    botao_limpar.grid(row=9, column=0, columnspan=2, pady=5)

    window.mainloop()  # Executa a janela





if __name__ == '__main__':
    mostrar_opcao_simulacao_pronta()
    