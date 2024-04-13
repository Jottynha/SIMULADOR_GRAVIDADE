import pygame
import math
import re
import tkinter as tk
from threading import Thread
from tkinter import messagebox

from arrow import draw_arrow


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
        print("Velocidade y: {} ms/s".format(self.vy))
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
    


    def draw(self, win,ZOOM,SCALE):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        if len(self.trace) > 2:
            traceLine = []
            for point in self.trace:
                x,y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                traceLine.append((x,y))
            pygame.draw.lines(win, self.color, False, traceLine, 2)

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
    root.title("Opção de Simulação")
    
    label = tk.Label(root, text="Gostaria de utilizar uma simulação pronta?", font=("Helvetica", 14))
    label.pack(pady=20)

    def start_custom_simulation():
        root.destroy()
        main(custom=True)

    def start_default_simulation():
        root.destroy()
        main(custom=False)

    btn_custom = tk.Button(root, text="Sim", font=("Helvetica", 12), command=start_default_simulation)
    btn_custom.pack(pady=10)

    btn_default = tk.Button(root, text="Não", font=("Helvetica", 12), command=start_custom_simulation)
    btn_default.pack(pady=10)

    root.mainloop()    

def main(custom=False):

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
                # Pausa ao apertar espaço
                if event.key == pygame.K_i:
                        mostrar_informacoes_gui(bodies)  # Exibe a janela de informações
                        adicionar_corpo()
                if event.key == pygame.K_SPACE:
                    arrows = []
                    const.pause()
                # reseta ao apertar ESC
                elif event.key == pygame.K_ESCAPE:
                    bodies = bodiesInit(custom)
                    const.SCALE = 250 / AU

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
                # Zoom in
                if event.button == 5:
                    const.addZoom(1,bodies)

                # Zoom out
                elif event.button == 4:
                    const.addZoom(0,bodies)

                # printa as informação quando o corpo é cliclado
                elif event.button == 1:
                    for body in bodies:
                        x = body.x * const.SCALE + WIDTH /2
                        y = body.y * const.SCALE + HEIGHT /2
                        if(checkCollision(x,y,body.radius/const.ZOOM,event.pos[0],event.pos[1],1)):
                            body.print()
                            # Seleciona o corpo cliclado
                            mouseMotion = [x,y,body]

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


#Coleta as informações no dicionário
def coletar_informacoes(bodies):
    todas_infos = []
    for body in bodies:
        info = body.storage()
        todas_infos.append(info)
    return todas_infos

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
        info_text = f"Nome: {info['Nome']}, Velocidade X: {info['Velocidade X (m/s)']}, Velocidade Y: {info['Velocidade Y (m/s)']}, Massa: {info['Massa (kg)']}"
        tk.Label(body_frame, text=info_text, font=("Helvetica", 12), fg=text_color, bg=bg_color).pack(anchor="w", pady=3)
    # Função para destruir a janela quando uma tecla é pressionada
    def destroy_window(event):
            window.destroy()
    # Vincula a função `destroy_window` ao evento de tecla pressionada
    window.bind("<KeyPress>", destroy_window)

    window.mainloop()
    return window
def limpar_arquivo():
    # Confirmação do usuário
    resposta = messagebox.askquestion("Limpar Arquivo", "Tem certeza que deseja limpar o arquivo? Todas as informações serão perdidas.")

    if resposta == "yes":
        # Limpa o arquivo
        open('input.data', 'w').close()
        messagebox.showinfo("Limpar Arquivo", "Arquivo limpo com sucesso.")
    else:
        return

def adicionar_corpo():
    janela_adicao = tk.Toplevel()
    janela_adicao.title("Adicionar Corpo Celeste")

    # Labels
    tk.Label(janela_adicao, text="Nome: ").grid(row=0, column=0)
    tk.Label(janela_adicao, text="X: ").grid(row=1, column=0)
    tk.Label(janela_adicao, text="Y: ").grid(row=2, column=0)
    tk.Label(janela_adicao, text="Massa: ").grid(row=3, column=0)
    tk.Label(janela_adicao, text="Velocidade X: ").grid(row=4, column=0)
    tk.Label(janela_adicao, text="Velocidade Y: ").grid(row=5, column=0)
    tk.Label(janela_adicao, text="Cor: ").grid(row=6, column=0)
    tk.Label(janela_adicao, text="Raio: ").grid(row=7, column=0)

    # Campos de entrada
    nome_entry = tk.Entry(janela_adicao)
    nome_entry.grid(row=0, column=1)
    x_entry = tk.Entry(janela_adicao)
    x_entry.grid(row=1, column=1)
    y_entry = tk.Entry(janela_adicao)
    y_entry.grid(row=2, column=1)
    massa_entry = tk.Entry(janela_adicao)
    massa_entry.grid(row=3, column=1)
    vx_entry = tk.Entry(janela_adicao)
    vx_entry.grid(row=4, column=1)
    vy_entry = tk.Entry(janela_adicao)
    vy_entry.grid(row=5, column=1)
    cor_entry = tk.Entry(janela_adicao)
    cor_entry.grid(row=6, column=1)
    raio_entry = tk.Entry(janela_adicao)
    raio_entry.grid(row=7, column=1)


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





# Cria a janela principal
janela = tk.Tk()
janela.title("Inserir Informações dos Corpos Celestes")

# Cria os rótulos e campos de entrada para as informações
tk.Label(janela, text="Nome:").grid(row=0, column=0)
nome_entry = tk.Entry(janela)
nome_entry.grid(row=0, column=1)

tk.Label(janela, text="X:").grid(row=1, column=0)
x_entry = tk.Entry(janela)
x_entry.grid(row=1, column=1)

tk.Label(janela, text="Y:").grid(row=2, column=0)
y_entry = tk.Entry(janela)
y_entry.grid(row=2, column=1)

tk.Label(janela, text="Massa:").grid(row=3, column=0)
massa_entry = tk.Entry(janela)
massa_entry.grid(row=3, column=1)

tk.Label(janela, text="Velocidade X:").grid(row=4, column=0)
vx_entry = tk.Entry(janela)
vx_entry.grid(row=4, column=1)

tk.Label(janela, text="Velocidade Y:").grid(row=5, column=0)
vy_entry = tk.Entry(janela)
vy_entry.grid(row=5, column=1)

tk.Label(janela, text="Cor:").grid(row=6, column=0)
cor_entry = tk.Entry(janela)
cor_entry.grid(row=6, column=1)

tk.Label(janela, text="Raio:").grid(row=7, column=0)
raio_entry = tk.Entry(janela)
raio_entry.grid(row=7, column=1)

# Botão para salvar as informações
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_info)
botao_salvar.grid(row=8, column=0, columnspan=2, pady=10)

# Botão para limpar o arquivo
botao_limpar = tk.Button(janela, text="Limpar Arquivo", command=limpar_arquivo)
botao_limpar.grid(row=9, column=0, columnspan=2, pady=5)

janela.mainloop()


if __name__ == '__main__':
    mostrar_opcao_simulacao_pronta()
