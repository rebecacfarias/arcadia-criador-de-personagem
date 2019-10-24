from tkinter import *
import functools
import Personagem
from Personagem import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import time

#TELAS
class Tela(Frame):
  def __init__(self,parent,nome):
    Frame.__init__(self,parent)
    self.current_frame = self
    self.parent = parent
    self.nome = nome
    self.tela = classes_vampiros

  def muda_tela(self, qual):
    self.current_frame.pack_forget()
    qual.pack(fill = BOTH, expand=1, anchor = CENTER)
    self.current_frame = qual

#COMANDO DO BOTÃO PARA SELECIONAR CLASSE
  def gettinClasse(self,profissao):
    #pega lista de classes
    profissoes = personagem.get_profissoes()
    #pega resultado do dropdown
    global classe
    classe = str(profissao.get())
    print(classe) #checar se pegou

    #teste se digitou valor da lista de classes
    if classe not in profissoes:
      erroX = Label(self,bg='#000000', fg='red', font=('Arial', '11'), text='')
      erroX['text'] = 'Selecione uma profissão válida!'
      erroX.pack()
    else:
      #se digitou, criar o próximo frame de acordo com a raça
      personagem.set_classe(classe)
      if personagem.get_especie() == "vampir@":
        self.tela = classes_vampiros(root)
      elif personagem.get_especie() == "elf@":
        self.tela = classes_elfos(root)
      elif personagem.get_especie() == "lobisomem":
        self.tela = classes_lobos(root)
      elif personagem.get_especie() == "brux@":
        self.tela = classes_bruxos(root)
      self.tela.telas(personagem.get_classe())
      self.tela.config(bg=personagem.get_color(), pady=30, padx=40)
      print(personagem.get_classe())
      #ir para o proximo frame
      self.current_frame.pack_forget()
      self.tela.pack(fill=BOTH, expand=1, anchor = CENTER)
      self.current_frame = self.tela

  def telas(self,nome):

    color = personagem.get_color()
    if nome == "Criar Personagem":
      profissoes = personagem.get_profissoes()
      personagem.get_textoEspecie(self)
      personagem.get_especieBars(self)
      self.msg = Label(image=logoarcadia, text="SYMBOL", borderwidth=0)
      self.msg["font"] = ("Verdana", "15", "italic", "bold")
      self.msg.place(x='360', y='5')
      self.msg3 = Label(self, text="""
              VOCÊ PRECISA DE UMA PROFISSÃO PARA SEGUIR EM FRENTE!
      """,bg = color)
      self.msg3["font"] = ("Verdana", "10", "italic", "bold")
      self.msg3.pack()
      Info4 = Label(self,font=('Arial', '11', 'bold'), fg='yellow', bg='#000000', text='ESCOLHA UMA PROFISSÃO:')
      Info4.pack(pady=10)
      classevar = StringVar()
      getClasse = ttk.Combobox(self,textvariable=classevar, values=profissoes)
      getClasse.pack(pady=10)
      Button(self, text="SEGUIR EM FRENTE", width=14,
                bg="black", fg="white", command=functools.partial(self.gettinClasse,getClasse)).pack(pady=10)
    elif nome == "Galeria":
      personagem.set_arma()
      personagem.set_tipo_armadura()
      personagem.set_poderes_classe()
      creditos = Tela(root, 'Creditos')
      creditos.config(bg=personagem.get_color(), pady=30, padx=40)
      creditos.telas("Créditos")
      about = Tela(root,'Sobre Arcadia')
      about.config(bg=personagem.get_color(), pady=30, padx=40)
      about.telas("Sobre Arcadia")
      subtelas = [about,creditos]
      #YOU
      self.msg = Label(image=logoarcadia, text="SYMBOL", borderwidth=0)
      self.msg["font"] = ("Verdana", "15", "italic", "bold")
      self.msg.place(x='360', y='5')
      self.msg2 = Label(self, text="VOCÊ ESTÁ PRONTO!",bg="black",fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.place(x=285,y=30)

      x = 60
      y = 120
      #PERSONAGEM
      self.imagem = Label(self,image=you,text = "SYMBOL",borderwidth=0)
      self.imagem.place(x=x,y=y)
      self.imagens = self.get_imagem_armadura()
      self.botao_armadura = Button(self, text="ARMADURA", width=15,
                               bg="black", fg="white", command=functools.partial(self.muda_foto, self.imagens[0])).place(x=130, y=397)
      self.botao_armadura = Button(self, text="ARMA", width=15,
                                   bg="black", fg="white",
                                   command=functools.partial(self.muda_foto, self.imagens[1])).place(x=130, y=422)
      if personagem.get_especie() == "lobisomem":
        self.botao_voce = Button(self, text="TRANSFORMAR", width=15,
               bg="black", fg="white", command=functools.partial(self.show_lobo,"VOLTAR")).place(x = 130,y=372)
      else:
        self.botao_voce = Button(self, text="VOCÊ", width=15,
                                 bg="black", fg="white", command=functools.partial(self.muda_foto, you)).place(x=130,
                                                                                                               y=372)



      #TEXTOS
      self.msg3 = Label(self, text = personagem.get_txt(),bg="black",fg="yellow")
      self.msg3["font"] = ("Verdana", "10", "italic", "bold")
      self.msg3.place(x=70,y=500)

      self.msg4 = Label(self, text=personagem.get_descricao(), borderwidth=0,justify = LEFT,bg = "black",fg="yellow")
      self.msg4["font"] = ("Verdana", "10", "italic", "bold")
      self.msg4.place(x=320,y=y)
      x= 170

      #botoes de subtelas
      for subtela in subtelas:

        Button(subtela, text='Voltar',
               bg="black", fg="white",width=15,  command=functools.partial(self.muda_tela, self)).pack(side=BOTTOM,pady="10")
        Button(self, text=subtela.nome, width=15,
               bg="black", fg="white", command=functools.partial(self.muda_tela, subtela)).place(x = x,y=650)
        x+=110

      self.sair = Button(self,bg="black",fg="white")
      self.sair["text"] = "Sair"
      self.sair["width"] = 15
      self.sair["command"] = self.quit
      self.sair.place(x=x,y=650)
    elif nome == "Créditos":
      self.msg2 = Label(self, text="CREDITOS:",bg="black", fg="#BDB76B")
      self.msg2["font"] = ("Verdana", "15", "italic", "bold")
      self.msg2.place(x=310,y=30)
      grupo = ["REBECA FARIAS","KELVE NUNES","LARA YASMIN","ROBERTA FÉLIX"]
      y = 80
      x = 240
      for nomes in grupo:
        Label(self, text=nomes, font=("Verdana", "15", "italic", "bold"), bg="black", fg="#BDB76B",width=20).place(x=x,y=y)
        y+=50


    elif nome == "Sobre Arcadia":
      self.msg2 = Label(self, text="HISTÓRIA",bg="black",fg="#BDB76B")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.place(x=330,y=30)
      y = 80
      x = 83
      Label(self, image=arcana, text="SYMBOL", borderwidth=0).place(x=x+100, y=y)
      Label(self, image=tenebris, text="SYMBOL", borderwidth=0).place(x=x+200, y=y)
      Label(self, image=magicae, text="SYMBOL", borderwidth=0).place(x=x+300, y=y)
      Label(self, image=lycan, text="SYMBOL", borderwidth=0).place(x=x+400, y=y)
      y = 180
      x = 83
      Label(self, text="REINO ARCANA", borderwidth=0,bg="black",fg="#BDB76B",width=15,justify=CENTER).place(x=x + 100, y=y)
      Label(self, text="CLÃ TENEBRIS", borderwidth=0,bg="black",fg="#BDB76B",width =15,justify=CENTER).place(x=x + 200, y=y)
      Label(self, text="ESFERA MAGICAE", borderwidth=0,bg="black",fg="#BDB76B",width=15,justify=CENTER).place(x=x + 300, y=y)
      Label(self, text="MONTE LYCAN", borderwidth=0,bg="black",fg="#BDB76B",width=14,justify=CENTER).place(x=x + 400, y=y)
      texto = """
Boas-vindas aventureiro, este é o universo de Arcadia.
A história de arcadia começa vários anos atrás quando a raça humana, sedenta por poder, 
começou a mexer com a magia estridente que paira sobre o mundo. 
Alguns foram para as florestas adquirindo conhecimento e protegendo a magia para que não 
seja usada de forma perigosa, esses são os elfos, que usam luz arcana para protegerem as 
florestas e as criaturas vivas. Os elfos são os fundadores do Reino Arcana.
Por outro lado essa magia corrompeu aqueles de coração fraco, surgindo assim os bruxos, 
criaturas que usam a magia para bem próprio, originando a mais antiga guerra ancestral. 
Os bruxos fundaram a Esfera Magicae, onde desenvolvem sua magia demoníaca.
Em meio ao caos da guerra das duas raças surgem os lobisomens das montanhas, fruto do 
desequilíbrio natural.
Os lobos são criaturas de força bruta e uma sede por sangue incontrolável que foram 
conquistados pelos interesses dos bruxos e formam uma aliança para pôr um fim em todas as 
ameaças aos seus interesses naturais. O Monte Lycan é o lar dos lobisomens.
Os elfos, temendo a ascensão das trevas, vão até as profundezas de arcadia, indo em busca 
de equilíbrio com os seres da noite, que a muito foram esquecidos, são eles, os vampiros, 
seres imortais protetores da noite e devotos dos deuses da noite. Esses seres, ainda mais 
que os lobos, sentem sede de sangue a todo momento, mas sua imortalidade os ensinou a buscarem
 o equilíbrio entre as raças. Seu clã é o Tenebris.
Hoje, as 4 raças, entre alianças e inimizades, vivem o ápice da guerra eterna,
e você agora faz parte dessa história. Lute pelo seu exército! 

      """
      historia = Label(self,text =texto,font =("Verdana", "10", "italic", "bold"),bg = "black",fg="#BDB76B").place(x=15,y=210)

  def muda_foto(self,foto):
    self.imagem = Label(self, image=foto, text="SYMBOL", borderwidth=0)
    self.imagem.place(x=60, y=120)
  def show_lobo(self,txt):
      self.imagem = Label(self, image=lobo, text="SYMBOL", borderwidth=0)
      self.imagem.place(x=60, y=120)
      self.lobutton = Button(self, text="TRANSFORMAR", width=15,
                           bg="black", fg="white", command=functools.partial(self.show_human, "VOLTAR")).place(x = 130,y=372)

  def show_human(self, txt):
    self.imagem = Label(self, image=you, text="SYMBOL", borderwidth=0)
    self.imagem.place(x=60, y=120)
    self.lobutton = Button(self, text="TRANSFORMAR", width=15,
                           bg="black", fg="white", command=functools.partial(self.show_lobo, "VOLTAR")).place(x = 130,y=372)

  def get_imagem_armadura(self):
    imagens = ["",""]
    if personagem.get_especie() == "vampir@":
      if personagem.get_classe() == "assassino":
        imagens[1] = adagas
        if personagem.get_genero() == "feminino":
          imagens[0] = assassina
        elif personagem.get_genero()=="masculino":
          imagens[0] = assassino
      elif personagem.get_classe() == "cavaleiro sanguinario":
        imagens[1] = foice
        if personagem.get_genero() == "feminino":
          imagens[0] = cavaleira_sanguinaria
        elif personagem.get_genero() == "masculino":
          imagens[0] = cavaleiro_sanguinario
      elif personagem.get_classe() == "caçador":
        imagens[1] = pistola
        if personagem.get_genero() == "feminino":
          imagens[0] = cacadora_vampira
        elif personagem.get_genero() == "masculino":
          imagens[0] = cacador_vampiro
    elif personagem.get_especie() == "elf@":
      if personagem.get_classe() == "arqueiro":
        imagens[1] = arco
        if personagem.get_genero() == "feminino":
          imagens[0] = arqueira
        elif personagem.get_genero()=="masculino":
          imagens[0] = arqueiro
      elif personagem.get_classe() == "sacerdote":
        imagens[1] = cetro
        if personagem.get_genero() == "feminino":
          imagens[0] = sacerdotisa
        elif personagem.get_genero() == "masculino":
          imagens[0] = sacerdote
      elif personagem.get_classe() == "paladino":
        imagens[1] = martelo
        if personagem.get_genero() == "feminino":
          imagens[0] = paladina
        elif personagem.get_genero() == "masculino":
          imagens[0] = paladino
    elif personagem.get_especie() == "brux@":
      if personagem.get_classe() == "necromancer":
        imagens[1] = varinha
        imagens[0] = necromancer
      elif personagem.get_classe() == "ladrão de almas":
        imagens[1] = varinha
        imagens[0] = ladrao
      elif personagem.get_classe() == "alquimista":
        imagens[1] = livro
        imagens[0] = alquimista
    elif personagem.get_especie() == "lobisomem":
      if personagem.get_classe() == "rastreador":
        imagens[1] = garras
        imagens[0] = rastreador
      elif personagem.get_classe() == "caçador":
        imagens[1] = besta
        imagens[0] = cacador
      elif personagem.get_classe() == "sentinela":
        imagens[1] = espada
        imagens[0] = sentinela
    return imagens





class classes_vampiros(Frame):
  def __init__(self,parent):
    Frame.__init__(self,parent)
    self.current_frame = self
    self.parent = parent
    self.msg = Label(self, text="", bg=personagem.get_color())
    self.msg["font"] = ("Verdana", "15", "italic", "bold")
    self.msg.pack()

  def telas(self,nome):
    tela_final = Tela(root,"Galeria")
    tela_final.telas("Galeria")
    tela_final.config(bg=personagem.get_color(), pady=30, padx=40)
    if nome == "assassino":
      y = 170
      image2 = adagas
      self.msg2 = Label(self, text="""ASSASSINO""",bg='#000000',fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()

      if personagem.get_genero() == "feminino":
        image1 = assassina
      elif personagem.get_genero()=="masculino":
        image1 = assassino

    elif nome == "cavaleiro sanguinario":
      y = 200
      image2 = foice
      self.msg2 = Label(self,text="""CAVALEIRO SANGUINÁRIO""",bg='#000000',fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      if personagem.get_genero() == "feminino":
        image1 = cavaleira_sanguinaria
      elif personagem.get_genero()=="masculino":
        image1 = cavaleiro_sanguinario

    elif nome == "caçador":
      y = 200
      image2 = pistola
      self.msg2 = Label(self,text="""CAÇADOR""",bg='#000000',fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      if personagem.get_genero() == "feminino":
        image1 = cacadora_vampira
      elif personagem.get_genero()=="masculino":
        image1 = cacador_vampiro

    Label(self, text="""ARMADURA:""",bg='#000000',fg="yellow").place(x=70,y=y-30)
    img_armadura = Label(self, image=image1, text="SYMBOL", borderwidth=0)
    img_armadura.place(x=70,y=y)
    Label(self, text="""ARMA:""", bg='#000000', fg="yellow").place(x=400, y=y - 30)
    img_arma = Label(self,image=image2,text = "SYMBOL",borderwidth=0)
    img_arma.place(x=400,y=y)
    arma = Label(self, text=personagem.get_arma(), bg='#000000', fg="yellow")
    arma["font"] = ("Verdana", "13", "italic", "bold")
    arma.place(x=400, y=y + 270)
    personagem.texto_vampiros(self) #texto
    personagem.classes_vampiras(self) #progress bar

    #AJEITAR personagem.set_poderes_classe(poderes)
    personagem.set_imagem_armadura(image1)
    personagem.set_imagem_arma(image2)

    Button(self, text="SALVAR", width=15,
               bg = "black",fg = "white",command=functools.partial(self.muda_tela,tela_final)).place(x=300,y=600)


  def muda_tela(self, qual):
    qual.pack(fill = BOTH, expand=1, anchor = CENTER)
    self.current_frame.pack_forget()
    self.current_frame = qual


class classes_elfos(Frame):
  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.current_frame = self
    self.parent = parent
    self.msg = Label(self, text="", bg=personagem.get_color())
    self.msg["font"] = ("Verdana", "15", "italic", "bold")
    self.msg.pack()

  def telas(self,nome):
    tela_final = Tela(root, "Galeria")
    tela_final.telas("Galeria")
    tela_final.config(bg=personagem.get_color(), pady=30, padx=40)

    if nome == "sacerdote":
      y = 210
      image2 = cetro
      self.msg2 = Label(self, text="""SACERDOTE""",bg = "black",fg ="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """
      Você escolheu ser um místico da natureza!
      Os sacerdotes utilizam um cetro místico que canaliza energia 
      da floresta e da luz solar,ganhando poderes de cura e magias de suporte.

      """
      if personagem.get_genero() == "feminino":
        image1 = sacerdotisa
      elif personagem.get_genero()=="masculino":
        image1 = sacerdote

    elif nome == "paladino":
      y=210
      image2 = martelo
      self.msg2 = Label(self, text="""PALADINO""",bg = "black",fg ="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """
      Você escolheu ser um guerreiro celestial!
      Os paladinos empunham de um martelo robusto e brilhante, 
      carregado das energias de magias ancestrais que aumentam suas defesas
      e lhes dão habilidades de extrema resistência em combate.

      """
      if personagem.get_genero() == "feminino":
        image1 = paladina
      elif personagem.get_genero()=="masculino":
        image1 = paladino


    elif nome == "arqueiro":
      y = 190
      image2 = arco
      self.msg2 = Label(self, text="""ARQUEIRO""",bg = "black",fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """
      Você escolheu ser um mestre das flechas eternas!
      Portadores de poderosos arcos encantados com a magia dos deuses antigos,
      adquirindo um poderoso olhar que os permitem alcançar inimigos à longa distância.
      """
      if personagem.get_genero() == "feminino":
        image1 = arqueira
      elif personagem.get_genero()=="masculino":
        image1 = arqueiro


    personagem.set_imagem_armadura(image1)
    personagem.set_imagem_arma(image2)
    Label(self, text="""ARMADURA:""", bg='#000000', fg="yellow").place(x=70, y=y - 30)
    img_armadura = Label(self, image=image1, text="SYMBOL", borderwidth=0)
    img_armadura.place(x=70, y=y)
    Label(self, text="""ARMA:""", bg='#000000', fg="yellow").place(x=400, y=y - 30)
    img_arma = Label(self, image=image2, text="SYMBOL", borderwidth=0)
    img_arma.place(x=400, y=y)
    arma = Label(self, text=personagem.get_arma(), bg='#000000', fg="yellow")
    arma["font"] = ("Verdana", "13", "italic", "bold")
    arma.place(x=400, y=y + 270)
    Label(self, text=txt.upper(), bg="#000000", fg="yellow", font=("Verdana", "10", "italic", "bold")).pack(pady=10)
    personagem.classes_elfas(self)
    Button(self, text="SALVAR", width=15,
           bg = "black",fg = "white",command=functools.partial(self.muda_tela, tela_final)).place(x=300,y=600)
  def muda_tela(self, qual):
    self.current_frame.pack_forget()
    qual.pack(fill = BOTH, expand=1, anchor = CENTER)
    self.current_frame = qual

class classes_lobos(Frame):
  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.current_frame = self
    self.parent = parent
    self.msg = Label(self, text="", bg=personagem.get_color())
    self.msg["font"] = ("Verdana", "15", "italic", "bold")
    self.msg.pack()

  def telas(self, nome):
    tela_final = Tela(root, "Galeria")
    tela_final.telas("Galeria")
    tela_final.config(bg=personagem.get_color(), pady=30, padx=40)
    txt = ""
    color = personagem.get_color()
    #AJEITAR IMAGEM LOBO
    if nome == "caçador":
      y = 200
      image2 = besta
      image1 = cacador
      self.msg2 = Label(self, text="""CAÇADOR""",bg='#000000',fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """Você escolheu caçar seus inimigos!" 
            Com a capacidade dos lobisomens de se locomoverem em terrenos 
            de difícil acesso, os caçadores carregam bestas de disparo múltiplo
            e se escondem sob os altos picos das montanhas, sempre alerta para caçar 
            o inimigo antes que este o caçe. 
            """

    elif nome == "sentinela":
      y=190

      image1 = sentinela
      image2 = espada
      self.msg2 = Label(self, text="""SENTINELA""",bg='#000000',fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """
      Você escolheu ser um sentinela e proteger seus aliados!
      Um poderoso lobisomem criado apenas para a batalha com espada, 
      sua força o faz cortar seus inimigos com apenas um golpe.
      """
    elif nome == "rastreador":
      y=210
      image1 = rastreador
      image2 = garras
      self.msg2 = Label(self, text="""RASTREADOR""",bg='#000000',fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """
      Você escolheu rastrear seus inimigos!
      O seu faro, desenvolvido nas cavernas das montanhas, permitem esses seres localizar seus inimigos 
      em quase toda a Arcadia.
      Silenciosos, eles rapidamente rasgam a entranhas de seus inimigos com suas garras.
       """

    personagem.set_imagem_arma(image2)
    personagem.set_imagem_armadura(image1)

    Label(self, text="""ARMADURA:""", bg='#000000', fg="yellow").place(x=70, y=y - 30)
    img_armadura = Label(self, image=image1, text="SYMBOL", borderwidth=0)
    img_armadura.place(x=70, y=y)
    Label(self, text="""ARMA:""", bg='#000000', fg="yellow").place(x=400, y=y - 30)
    img_arma = Label(self, image=image2, text="SYMBOL", borderwidth=0)
    img_arma.place(x=400, y=y)
    arma = Label(self, text=personagem.get_arma(), bg='#000000', fg="yellow")
    arma["font"] = ("Verdana", "13", "italic", "bold")
    arma.place(x=400, y=y + 270)

    Label(self, text=txt.upper(), bg="#000000", fg="yellow", font=("Verdana", "10", "italic", "bold")).pack(pady=10)
    personagem.classes_lobas(self)
    Button(self, text="SALVAR", width=15,
           bg = "black",fg = "white",command=functools.partial(self.muda_tela, tela_final)).place(x=300,y=600)
  def muda_tela(self, qual):
    self.current_frame.pack_forget()
    qual.pack(fill = BOTH, expand=1, anchor = CENTER)
    self.current_frame = qual

class classes_bruxos(Frame):
  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.current_frame = self
    self.parent = parent
    self.msg = Label(self, text="", bg=personagem.get_color())
    self.msg["font"] = ("Verdana", "15", "italic", "bold")
    self.msg.pack()

  def telas(self,nome):
    tela_final = Tela(root, "Galeria")
    tela_final.telas("Galeria")
    tela_final.config(bg=personagem.get_color(), pady=30, padx=40)
    txt = ""
    if nome == "necromancer":
      y = 210
      image1 = necromancer
      image2 = varinha
      self.msg2 = Label(self, text="""NECROMANCER""", bg="black",fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """
            Você escolheu aterrorizar seus inimigos!
            A morte é a melhor amiga desses reanimadores de cadáveres que usam 
            seus inimigos contra eles mesmos, aterrorizando-os com a visão da morte.

            """

    elif nome == "ladrão de almas":
      y = 190
      image1 = ladrao
      image2 = varinha
      self.msg2 = Label(self, text="""LADRÃO DE ALMAS""", bg="black",fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """
      Você escolheu sugar a alma de seus inimigos!
      Os ladrões de almas usam a fraqueza mental de sus inimigos para absorverem
      suas almas e ficarem mais fortes e insanos em qualquer batalha que se engajarem.
      """
    elif nome == "alquimista":
      y = 210
      image1 = alquimista
      image2 = livro
      self.msg2 = Label(self, text="""ALQUIMISTA""", bg="black",fg="yellow")
      self.msg2["font"] = ("Verdana", "10", "italic", "bold")
      self.msg2.pack()
      txt = """
      Você escolheu a feitiçaria e as poções!
      Os alquimistas possuem o poder de decifrar o livro dos feitiços proibidos 
      que desafiam as leis da natureza e o equilíbrio natural. 
      Suas poções são geralmente explosivas e possuem talento como piromancers! 
       """
    personagem.set_imagem_armadura(image1)
    personagem.set_imagem_arma(image2)
    Label(self, text="""ARMADURA:""", bg='#000000', fg="yellow").place(x=70, y=y - 30)
    img_armadura = Label(self, image=image1, text="SYMBOL", borderwidth=0)
    img_armadura.place(x=70, y=y)
    Label(self, text="""ARMA:""", bg='#000000', fg="yellow").place(x=400, y=y - 30)
    img_arma = Label(self, image=image2, text="SYMBOL", borderwidth=0)
    img_arma.place(x=400, y=y)
    arma = Label(self, text=personagem.get_arma(), bg='#000000', fg="yellow")
    arma["font"] = ("Verdana", "13", "italic", "bold")
    arma.place(x=400, y=y + 270)
    Label(self, text=txt.upper(), bg="#000000", fg="yellow", font=("Verdana", "10", "italic", "bold")).pack(pady=10)
    personagem.classes_bruxas(self)

    Button(self, text="SALVAR", width=15,
           bg = "black",fg = "white",command=functools.partial(self.muda_tela,tela_final)).place(x=300,y=600)
  def muda_tela(self, qual):
    self.current_frame.pack_forget()
    qual.pack(fill = BOTH, expand=1, anchor = CENTER)
    self.current_frame = qual


if __name__ == '__main__':

  janela = Tk()
  def __init__():
    pass




  def ok():

    nick = str(CaixaDeEntrada1.get())
    sobrenome = str(CaixaDeEntrada2.get())
    genero = str(getGenero.get())
    pele = str(getPele.get())
    especie = str(getEspecie.get())
    Linha_Entry_1 = nick
    Linha_Entry_2 = sobrenome
    Linha_Entry_3 = genero
    Linha_Entry_4 = pele
    Linha_Entry_5 = especie
    print(Linha_Entry_1)
    print(Linha_Entry_2)
    print(Linha_Entry_3)
    print(Linha_Entry_4)
    print(Linha_Entry_5)

    if nick in ' ':
      CaixaDeEntrada1['bg'] = 'pink'
      erro['text'] = 'Preencha todos os campos!'
    else:
      CaixaDeEntrada1['bg'] = 'white'
    if sobrenome in ' ':
      CaixaDeEntrada2['bg'] = 'pink'
      erro['text'] = 'Preencha todos os campos!'
    else:
      CaixaDeEntrada2['bg'] = 'white'
    if genero in ' ':
      erro['text'] = 'Preencha todos os campos!'
    elif genero!="feminino" and genero!="masculino":
      erro2['text'] = 'Selecione feminino ou masculino!'
    if pele in ' ':
      erro['text'] = 'Preencha todos os campos!'
    elif pele != 'clara' and pele != 'escura':
      erro3['text'] = 'Selecione tom de pele!'
    if especie in ' ':
      erro['text'] = 'Preencha todos os campos!'
    elif especie != 'vampir@' and especie != 'brux@' and especie != "lobisomem" and especie != "elf@":
      erro4['text'] = 'Selecione uma espécie válida!'



    if nick != '' and sobrenome != '' and genero != '' and (genero =='feminino' or genero=='masculino') and(pele=='clara' or pele=='escura') and(especie=='vampir@' or especie=='elf@' or especie =="lobisomem" or especie == 'brux@'):
      janela.destroy()
      #DESTRÓI JANELA INICIAL E CRIA A PRÓXIMA
      global root
      root = Tk()  # geometry
      root.geometry('850x730+350+2')
      root.resizable(width=False, height=False)
      #SETANDO AS INFORMAÇOES QUE JÁ ESTAO DISPONIVELS DO PERSONAGEM
      logo = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\logo.jpeg')
      logo = logo.resize((100, 30))
      global logoarcadia
      logoarcadia = ImageTk.PhotoImage(logo)


      global personagem
      personagem = Personagem()
      personagem.set_nome(nick.upper())
      personagem.set_genero(genero)
      personagem.set_sobrenome(sobrenome.upper())
      personagem.set_pele(pele)
      personagem.set_especie(especie)
      personagem.set_aliancas()
      personagem.set_profissoes()
      personagem.set_origem()
      personagem.set_poderes_raciais()

      # SETANDO A APARÊNCIA DO PERSONAGEM
      personagem.set_imagem_personagem()
      vc = personagem.get_imagem_personagem()
      vc = vc.resize((250, 250))
      global you
      you = ImageTk.PhotoImage(vc)
      global pb #TIMESLEEP NAS COISAS DA PROPRIA TELA
      pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")

      #IMPORTANDO A IMAGEM DO LOBO

            #COLOCAR LOBO NA GALERIA
      if personagem.get_especie() == "lobisomem":
        animal = personagem.get_lobo()
        animal = animal.resize((250,250))
        global lobo
        lobo = ImageTk.PhotoImage(animal)

      #TELA INICIAL
      t1 = Tela(root, 'Criar Personagem')
      t1.telas("Criar Personagem")
      color = personagem.get_color()
      root.configure(bg=color)
      t1.configure(bg=color,pady=30)
      t1.pack(fill=BOTH, expand=1, anchor = CENTER)
      x = 250
      y = 250

      #VAMPIROS
      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Assassina.png')
      im1 = im1.resize((x, y))
      global assassina
      assassina = ImageTk.PhotoImage(im1)

      im2 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Assassino.png')
      im2 = im2.resize((x, y))
      global assassino
      assassino = ImageTk.PhotoImage(im2)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\CavaleiraSanguinária.png')
      im1 = im1.resize((x, y))
      global cavaleira_sanguinaria
      cavaleira_sanguinaria = ImageTk.PhotoImage(im1)

      im2 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\CavaleiroSanguinário.png')
      im2 = im2.resize((x, y))
      global cavaleiro_sanguinario
      cavaleiro_sanguinario = ImageTk.PhotoImage(im2)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\CaçadoraDaNoite.png')
      im1 = im1.resize((x, y))
      global cacadora_vampira
      cacadora_vampira = ImageTk.PhotoImage(im1)

      im2 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\CaçadorDaNoite.png')
      im2 = im2.resize((x, y))
      global cacador_vampiro
      cacador_vampiro = ImageTk.PhotoImage(im2)

      #ELFOS

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Sacerdotisa.png')
      im1 = im1.resize((x, y))
      global sacerdotisa
      sacerdotisa = ImageTk.PhotoImage(im1)

      im2 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Sacerdote.png')
      im2 = im2.resize((x, y))
      global sacerdote
      sacerdote = ImageTk.PhotoImage(im2)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\paladina.png')
      im1 = im1.resize((x, y))
      global paladina
      paladina = ImageTk.PhotoImage(im1)

      im2 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Paladino.png')
      im2 = im2.resize((x, y))
      global paladino
      paladino = ImageTk.PhotoImage(im2)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Arqueira.png')
      im1 = im1.resize((x, y))
      global arqueira
      arqueira = ImageTk.PhotoImage(im1)

      im2 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Arqueiro.png')
      im2 = im2.resize((x, y))
      global arqueiro
      arqueiro = ImageTk.PhotoImage(im2)

      #LOBOS

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Sentinela.png')
      im1 = im1.resize((x, y))
      global sentinela
      sentinela = ImageTk.PhotoImage(im1)

      im2 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Rastreador.png')
      im2 = im2.resize((x, y))
      global rastreador
      rastreador = ImageTk.PhotoImage(im2)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Caçador.png')
      im1 = im1.resize((x, y))
      global cacador
      cacador = ImageTk.PhotoImage(im1)

     #BRUXAS

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Alquimista.png')
      im1 = im1.resize((x, y))
      global alquimista
      alquimista = ImageTk.PhotoImage(im1)

      im2 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Necromanço.png')
      im2 = im2.resize((x, y))
      global necromancer
      necromancer = ImageTk.PhotoImage(im2)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\LadrãoDeAlmas.png')
      im1 = im1.resize((x, y))
      global ladrao
      ladrao = ImageTk.PhotoImage(im1)
     #ARMAS
      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Assassinoarma.png')
      im1 = im1.resize((x, y))
      global adagas
      adagas = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\CaçadorDaNoitearma.png')
      im1 = im1.resize((x, y))
      global pistola
      pistola = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\CavaleiroSanguinárioarma.png')
      im1 = im1.resize((x, y))
      global foice
      foice = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\armasacerdote.png')
      im1 = im1.resize((x, y))
      global cetro
      cetro = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\arqueiroarma.png')
      im1 = im1.resize((x, y))
      global arco
      arco = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\paladinoarma.png')
      im1 = im1.resize((x, y))
      global martelo
      martelo = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Necromançoarma.png')
      im1 = im1.resize((x, y))
      global varinha
      varinha = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\alquimistaarma.png')
      im1 = im1.resize((x, y))
      global livro
      livro = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Perseguidorarma.png')
      im1 = im1.resize((x, y))
      global besta
      besta = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Rastreadorarma.png')
      im1 = im1.resize((x, y))
      global garras
      garras = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Sentinelaarma.png')
      im1 = im1.resize((x, y))
      global espada
      espada = ImageTk.PhotoImage(im1)

      #SÍMBOLOS DOS EXÉRCITOS
      x = 100
      y = 100
      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\arcana.png')
      im1 = im1.resize((x, y))
      global arcana
      arcana = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\tenebris.png')
      im1 = im1.resize((x, y))
      global tenebris
      tenebris = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\magicae.png')
      im1 = im1.resize((x, y))
      global magicae
      magicae = ImageTk.PhotoImage(im1)

      im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\lycan.png')
      im1 = im1.resize((x, y))
      global lycan
      lycan = ImageTk.PhotoImage(im1)

      root.mainloop()

  # ==========================================Janela Inicial:



  logo = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\logo.jpeg')
  logo = logo.resize((100, 30))

  logoarcadia = ImageTk.PhotoImage(logo)
  Label(image=logoarcadia, text="SYMBOL", borderwidth=0).place(x='130', y='10')
  titulo2 = Label(bg='#000000', font=('Arial', '8', 'bold'), fg='#BDB76B', text='PREENCHA OS CAMPOS PARA INICIALIZAR SEU PERSONAGEM!')
  titulo2.place(x='13', y='50')

  im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\arcadian.png')
  im1 = im1.resize((50,50))
  image1 = ImageTk.PhotoImage(im1)
  Label(image = image1,text="SYMBOL",borderwidth=0).place(x='150',y='340')

  CaixaDeEntrada1 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
  CaixaDeEntrada1.place(x=130, y=75)
  Info1 = Label(font=('Arial', '11', 'bold'), fg='#BDB76B', bg='#000000', text='NOME:')
  Info1.place(x=10, y=75)

  CaixaDeEntrada2 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
  CaixaDeEntrada2.place(x=130, y=100)
  Info2 = Label(font=('Arial', '11', 'bold'), fg='#BDB76B', bg='#000000', text='SOBRENOME:')
  Info2.place(x=10, y=100)

  generovar = StringVar()
  getGenero = ttk.Combobox(textvariable=generovar,values = ['feminino','masculino'])
  getGenero.place(x=130, y=125)
 # CaixaDeEntrada3 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
  #CaixaDeEntrada3.place(x=130, y=125)
  Info3 = Label(font=('Arial', '11', 'bold'), fg='#BDB76B', bg='#000000', text='GENERO:     ')
  Info3.place(x=10, y=125)

  pelevar = StringVar()
  getPele = ttk.Combobox(textvariable=pelevar,values = ['clara','escura'])
  getPele.place(x=130, y=150)

  Info4 = Label(font=('Arial', '11', 'bold'), fg='#BDB76B', bg='#000000', text='COR DA PELE:')
  Info4.place(x=10, y=150)

  especievar = StringVar()
  getEspecie = ttk.Combobox(textvariable=especievar,values = ['elf@','vampir@','lobisomem','brux@'])
  getEspecie.place(x=130, y=175)

  Info5 = Label(font=('Arial', '11', 'bold'), fg='#BDB76B', bg='#000000', text='ESPÉCIE:')
  Info5.place(x=10, y=175)

  erro = Label(bg='#000000', fg='red', font=('Arial', '11'), text='')
  erro.place(x=130, y=200)

  erro2 = Label(bg='#000000', fg='red', font=('Arial', '11'), text='')
  erro2.place(x=130, y=220)

  erro3 = Label(bg='#000000', fg='red', font=('Arial', '11'), text='')
  erro3.place(x=130, y=240)

  erro4 = Label(bg='#000000', fg='red', font=('Arial', '11'), text='')
  erro4.place(x=130, y=260)

  proximo = Button(width='39', text='Próximo', font=('Arial', '10',"bold"),bg='#BDB76B',fg="black", command=ok)
  proximo.place(x=15, y=400)

# Propriedades da janela:
  janela.resizable(width=False, height=False)
  janela.configure(bg='#000000')
  janela.title('ARCADIA BETA')
  janela.geometry('353x450+450+100')
  janela.mainloop()
  Linha_Entry_1 = 'Salve a primeira entry nessa variavel'
  Linha_Entry_2 = 'Salve a segunda entry nessa variavel'
  Linha_Entry_3 = 'Salve a terceira entry nessa variavel'
