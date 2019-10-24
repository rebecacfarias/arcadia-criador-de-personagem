from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image

class Personagem(object):
  nome = ""
  sobrenome = ""
  genero = ""
  pele = ""
  especie = ""
  classe = ""
  arma = ""
  inimigos = ""
  aliados = ""
  origem = ""
  poderes_raciais = ""
  poderes_classe = "" #AJEITAR: FAZER SET E GET
  profissoes = []
  tipoArmadura = ""
  imagem_armadura = ""
  imagem_arma = ""
  imagem_personagem = ""
  animal = ""



  def set_nome(self,nome):
    self.nome = nome
  def set_sobrenome(self,sobrenome):
    self.sobrenome = sobrenome
  def set_genero(self,genero):
    self.genero = genero
  def set_pele(self,pele):
    self.pele = pele
  def set_especie(self,especie):
    self.especie = especie
  def set_classe(self,classe):
    self.classe = classe
  def set_arma(self):
    especie = self.get_especie()
    classe = self.get_classe()
    if especie == "vampir@":
      if classe == "assassino":
        self.arma = "adagas"
      elif classe == "cavaleiro sanguinario":
        self.arma = "foice sanguinária"
      elif classe == "caçador":
        self.arma = "pistolas"
    elif especie == "elf@":
      if classe == "sacerdote":
        self.arma = "cetro solar"
      elif classe == "paladino":
        self.arma = "martelo da justiça"
      elif classe == "arqueiro":
        self.arma = "arco místico"
    elif especie == "brux@":
      if classe == "alquimista":
        self.arma = "livro proibido"
      elif classe == "necromancer":
        self.arma = "varinha"
      elif classe == "ladrão de almas":
        self.arma = "varinha"
    elif especie == "lobisomem":
      if classe == "sentinela":
        self.arma = "espada lunar"
      elif classe == "caçador":
        self.arma = "besta"
      elif classe == "rastreador":
        self.arma = "garras de aço"

  def set_tipo_armadura(self):
    especie = self.get_especie()
    classe = self.get_classe()
    if especie == "vampir@":
      if classe == "assassino":
        self.tipoArmadura = "leve"
      elif classe == "cavaleiro sanguinario":
        self.tipoArmadura = "pesada"
      elif classe == "caçador":
        self.tipoArmadura = "leve"
    elif especie == "elf@":
      if classe == "sacerdote":
        self.tipoArmadura = "leve"
      elif classe == "paladino":
        self.tipoArmadura = "pesada"
      elif classe == "arqueiro":
        self.tipoArmadura = "leve"
    elif especie == "brux@":
      self.tipoArmadura = "leve"
    elif especie == "lobisomem":
      if classe == "sentinela":
        self.tipoArmadura = "pesada"
      elif classe == "caçador":
        self.tipoArmadura = "leve"
      elif classe == "rastreador":
        self.tipoArmadura = "leve"
  def set_origem(self):
    if self.especie == "vampir@":
      self.origem = "CLÃ TENEBRIS"
    elif self.especie == "elf@":
      self.origem = "REINO ARCANA"
    elif self.especie == "lobisomem":
      self.origem = "MONTE LYCAN"
    elif self.especie == "brux@":
      self.origem = "ESFERA MAGICAE"
  def set_aliancas(self): #AJEITAR: COLOCAR NO TEXTO
    if self.especie == "vampir@":
      self.aliados = "elfos"
      self.inimigos = "lobisomens e bruxos"
    elif self.especie == "elf@":
      self.aliados = "vampiros"
      self.inimigos = "bruxos e lobisomens"
    elif self.especie == "lobisomem":
      self.aliados = "bruxos"
      self.inimigos = "vampiros e elfos"
    elif self.especie == "brux@":
      self.aliados = "lobisomens"
      self.inimigos = "elfos e vampiros"
  def set_profissoes(self):
    if self.especie == "vampir@":
      self.profissoes = ["cavaleiro sanguinario","assassino","caçador"]
    elif self.especie == "elf@":
      self.profissoes = ["sacerdote","arqueiro","paladino"]
    elif self.especie == "lobisomem":
      self.profissoes = ["sentinela","caçador","rastreador"]
    elif self.especie == "brux@":
      self.profissoes = ["necromancer","ladrão de almas","alquimista"]
  def set_poderes_raciais(self):
    especie = self.get_especie()
    if especie == "vampir@":
      self.poderes_raciais = "+SUBTERFÚGIO +PRESAS DO DESTINO +FURTIVIDADE"
    elif especie == "elf@":
      self.poderes_raciais = "+LUZ ARCANA +TELETRANSPORTE +CANALIZAR LUZ SOLAR"
    elif especie == "brux@":
      self.poderes_raciais = "+POSSESSÃO +PETRIFICAR +TELECINESE"
    elif especie == "lobisomem":
      self.poderes_raciais = "+PELAGEM BLINDADA +FERRARIA +GARRAS-VENENO"

  def set_poderes_classe(self):
    especie = self.get_especie()
    classe = self.get_classe()
    if especie == "vampir@":
      if classe == "assassino":
        self.poderes_classe = "+LÂMINAS DA MORTE +ATORDOAR +NOCAUTEAR"
      elif classe == "cavaleiro sanguinario":
        self.poderes_classe = "+DECAPITAR +GOLPE MÚLTIPLO +CAVALARIA"
      elif classe == "caçador":
        self.poderes_classe = "+TIRO MÚLTIPLO +DESVENCILHAR +FUGA SÚBITA"
    elif especie == "elf@":
      if classe == "sacerdote":
        self.poderes_classe = "+CURA ARCANA +CANALIZAR CAMPO PROTETOR +FERIDA ARCANA"
      elif classe == "paladino":
        self.poderes_classe = "+TERREMOTO SÚBITO +MARTELO DA JUSTIÇA +ESCUDO MÍSTICO"
      elif classe == "arqueiro":
        self.poderes_classe = "+OLHOS DE ÁGUIA +INVOCAR FERAS +FLECHAS DE FOGO"
    elif especie == "brux@":
      if classe == "necromancer":
        self.poderes_classe ="+ATERRORIZAR +TOMAR CORPO +LANÇA-ALUCINAÇÃO"
      elif classe == "ladrão de almas":
        self.poderes_classe = "+SUGAR ALMA +INVADIR MENTE +TRANSFIGURAR"
      elif classe == "alquimista":
        self.poderes_classe = "+POÇÃO ARDENTE +POÇÃO SANGRIA +POÇÃO-MANIPULA"
    elif especie == "lobisomem":
      if classe == "sentinela":
        self.poderes_classe = "+RUGIDO DA MORTE +ABATE DE GUERRA +LOBO-PARCIAL"
      elif classe == "caçador":
        self.poderes_classe = "+ABOCANHAR +OLHO DO LOBO +ABATE CERTEIRO"
      elif classe == "rastreador":
        self.poderes_classe = "+DILACERAR +GARRA VENENOSA +FAREJAR INIMIGOS"
  def set_imagem_armadura(self,imagem_armadura):
    self.imagem_armadura = imagem_armadura
  def set_imagem_arma(self, imagem):
    self.imagem_arma = imagem
  def set_imagem_personagem(self):
    if self.get_especie() == "vampir@":
      if self.get_genero() == "feminino":
        if self.get_pele() == "clara":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\vampirabranca.png')
        elif self.get_pele() == "escura":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\vampira.png')
      elif self.get_genero() == "masculino":
        if self.get_pele() == "clara":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\vampirobranco.png')
        elif self.get_pele() == "escura":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\vampiro.png')
    elif self.get_especie()=="elf@":
      if self.get_genero() == "feminino":
        if self.get_pele() == "clara":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\elfabranca.jpeg')
        elif self.get_pele() == "escura":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\elfa.jpeg')
      elif self.get_genero() == "masculino":
        if self.get_pele() == "clara":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\elfobranco.jpeg')
        elif self.get_pele() == "escura":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\elfo.jpeg')
    elif self.get_especie() == "brux@":
      if self.get_genero() == "feminino":
        self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Bruxa.png')
      elif self.get_genero() == "masculino":
        self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\Bruxo.png')
    elif self.get_especie()=="lobisomem":
      if self.get_genero() == "feminino":
        self.animal = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\loba.png')
        if self.get_pele() == "clara":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\lobiwoman.png')
        elif self.get_pele() == "escura":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\lobiwomanNegra.png')
      elif self.get_genero() == "masculino":
        self.animal = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\lobisomem.jpeg')
        if self.get_pele() == "clara":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\lobobranco.jpeg')
        elif self.get_pele() == "escura":
          self.imagem_personagem = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\lobo.jpeg')

    #im1 = Image.open(r'C:\Users\Rebeca\PycharmProjects\arcadia\img\arcadian.png')
    #im1 = im1.resize((50, 50))
    #image1 = ImageTk.PhotoImage(im1)
    #Label(image=image1, text="SYMBOL", borderwidth=0).place(x='150', y='340')

  def get_lobo(self):
    return self.animal
  def get_imagem_personagem(self):
    return self.imagem_personagem

  def get_imagem_arma(self):
    return self.imagem_arma
  def get_profissoes(self):
    return self.profissoes
  def get_nome(self):
    return self.nome
  def get_nomeCompleto(self):
    return self.nome+' '+self.sobrenome
  def get_genero(self):
    return self.genero
  def get_pele(self):
    return self.pele
  def get_especie(self):
    return self.especie
  def get_classe(self):
    return self.classe
  def get_origem(self):
    return self.origem
  def get_inimigos(self):
    return self.inimigos
  def get_aliados(self):
    return self.aliados
  def get_arma(self):
    return self.arma.upper()
  def get_poderes_raciais(self):
    return self.poderes_raciais
  def get_color(self): #AJEITAR: SEPARAR EM SET
    if self.especie == "vampir@":
      color = '#8B0000'
    elif self.especie == "elf@":
      color = 'green'
    elif self.especie == "lobisomem":
      color = 'brown'
    elif self.especie == "brux@":
      color = 'purple'
    return color

 # def get_texto1(self):


  def get_especieBars(self,tela):
    color = self.get_color()
    if self.get_especie()=="vampir@":
      Label(tela, text="SEUS ATRIBUTOS:", bg="#000000", fg="yellow").pack(pady=7)
      Label(tela, text="SUPER-VELOCIDADE:", bg='#8B0000', fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="FORÇA FÍSICA:", bg='#8B0000', fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="AGILIDADE:", bg='#8B0000', fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="HABILIDADE ARCANA:", bg='#8B0000', fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 10
      progress.pack(pady=10)
    elif self.get_especie() == "elf@":
      Label(tela, text="SEUS ATRIBUTOS:", bg="#000000", fg="yellow").pack(pady=7)
      Label(tela, text="HABILIDADE ARCANA:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="FEITIÇARIA:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="SENSITIVIDADE:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="COMBATE CORPO A CORPO:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 10
      progress.pack(pady=10)
    elif self.get_especie() == "lobisomem":
      Label(tela, text="SEUS ATRIBUTOS:", bg="#000000", fg="yellow").pack(pady=7)
      Label(tela, text="FORÇA FÍSICA:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="PRECISÃO:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 80
      progress.pack(pady=10)
      Label(tela, text="GOLPES FATAIS:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 80
      progress.pack(pady=10)
      Label(tela, text="HABILIDADE ARCANA:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 10
      progress.pack(pady=10)
    elif self.get_especie() == "brux@":
      Label(tela, text="SEUS ATRIBUTOS:", bg="#000000", fg="yellow").pack(pady=7)
      Label(tela, text="HABILIDADE ARCANA:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="MAGIA DEMONÍACA:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.pack(pady=10)
      Label(tela, text="CANALIZAÇÃO:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 70
      progress.pack(pady=10)
      Label(tela, text="COMBATE CORPO A CORPO:", bg=color, fg="yellow").pack()
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 10
      progress.pack(pady=10)



  def get_tipo_armadura(self):
    return self.tipoArmadura
  def get_poderes_classe(self):
    return self.poderes_classe

  def classes_vampiras(self,tela):
    classe = self.get_classe()
    color = self.get_color()
    x = 70
    y = 430
    if classe == "assassino":

      Label(tela, text="PRECISÃO DE MOVIMENTOS:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 40
      progress.place(x=x,y=y+75)

    elif classe == "cavaleiro sanguinario":
      y = 450
      Label(tela, text="SUPER-BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="AGILIDADE:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 40
      progress.place(x=x,y=y+75)
    elif classe == "caçador":
      y = 450
      Label(tela, text="AGILIDADE:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 70
      progress.place(x=x,y=y+75)

  def classes_elfas(self,tela):
    classe = self.get_classe()
    color = self.get_color()
    x = 70
    y = 450
    if classe == "sacerdote":
      y = 470
      Label(tela, text="PRECISÃO DE MOVIMENTOS:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 40
      progress.place(x=x,y=y+75)

    elif classe == "paladino":

      Label(tela, text="SUPER-BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="AGILIDADE:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 40
      progress.place(x=x,y=y+75)
    elif classe == "arqueiro":

      Label(tela, text="AGILIDADE:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 70
      progress.place(x=x,y=y+75)
  def classes_lobas(self,tela):
    classe = self.get_classe()
    color = self.get_color()
    x = 70
    y = 430
    if classe == "caçador":
      y = 450
      Label(tela, text="PRECISÃO DE MOVIMENTOS:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 40
      progress.place(x=x,y=y+75)

    elif classe == "sentinela":
      y = 450
      Label(tela, text="SUPER-BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="AGILIDADE:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 40
      progress.place(x=x,y=y+75)
    elif classe == "rastreador":
      y = 470
      Label(tela, text="AGILIDADE:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 70
      progress.place(x=x,y=y+75)

  def classes_bruxas(self,tela):
    classe = self.get_classe()
    color = self.get_color()
    x = 70
    y = 430
    if classe == "necromancer":
      y = 470
      Label(tela, text="PRECISÃO DE MOVIMENTOS:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 40
      progress.place(x=x,y=y+75)

    elif classe == "ladrão de almas":
      y = 450
      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 70
      progress.place(x=x,y=y+25)

      Label(tela, text="AGILIDADE:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+75)
    elif classe == "alquimista":
      y = 470
      Label(tela, text="AGILIDADE:", bg=color, fg="yellow").place(x=x,y=y)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 90
      progress.place(x=x,y=y+25)

      Label(tela, text="BLINDAGEM:", bg=color, fg="yellow").place(x=x,y=y+50)
      progress = ttk.Progressbar(tela, orient=HORIZONTAL,
                                 length=100, mode='determinate')
      progress['value'] = 50
      progress.place(x=x,y=y+75)
  def get_textoEspecie(self,tela):
    if self.get_especie()=="elf@":
      txt = """
      Você escolheu o mundo da luz!
      Bem-vindo a floresta de ARCANA, jovem aprendiz. 
      Aqui você encontrará a inteligência que precisa para enfrentar seus inimigos.
      """
      Label(tela, text=txt.upper(), bg="#000000", fg="yellow", font = ("Verdana", "10", "italic", "bold")).pack(pady=10)
    elif self.get_especie()=="vampir@":
      txt = """
      Você escolheu o mundo das sombras!
      Bem-vindo ao Clã Tenebris, jovem vampiro. 
      Junte-se à noite e descubra o poder dos deuses das sombras!. 
      """
      Label(tela, text=txt.upper(), bg="#000000", fg="yellow",font = ("Verdana", "10", "italic", "bold")).pack(pady=10)

    elif self.get_especie()=="brux@":
      txt = """
      Você escolheu a magia sombria!
      Bem-vindo à Esfera Magicae, um reino sombrio, repleto de magia demoníaca e segredos místicos. 
      Elimine a sua bondade com as seguintes naturezas malignas:
 
      """
      Label(tela, text=txt.upper(), bg="#000000", fg="yellow",font = ("Verdana", "10", "italic", "bold")).pack(pady=10)

    elif self.get_especie() == "lobisomem":
      txt = """
      Você escolheu servir à lua!
      Bem-vindo ao Monte Lycan! A nossa força reflete nosso treinamento. 
      Não pense que será fácil, mas se juntar a nós é requisito para a conquista de arcádia. 


      """
      Label(tela, text=txt.upper(), bg="#000000", fg="yellow",font = ("Verdana", "10", "italic", "bold")).pack(pady = 10)



  def texto_vampiros(self,tela):
    txt = """"""
    if self.classe == "assassino":
      #ADICIONAR SETAGEM DE IMAGEM E EM BAIXO AS BARRAS DE PROGRESSO+ARMADURA+ARMA
      txt = """Você escolheu a profissão do assassinato!" 
            Os assassinos são extremamente ágeis em combate corpo a corpo, 
            lutam com suas adagas da morta e eliminam seus inimigos antes mesmo de serem vistos. 
            """
      msg = Label(tela, text=txt, bg="#000000", fg="yellow", font=("Verdana", "10", "italic", "bold"))
      msg.pack(pady=10)
    elif self.classe == "cavaleiro sanguinario":
      txt = """
      Você escolheu ser um guerreiro sanguinário!
      Os cavaleiros sanguinários podem perder agilidade, mas são 
      insanamente resistentes com sua armadura e empunhando uma foice mortífera!
      """
      msg = Label(tela, text=txt.upper(), bg="#000000", fg="yellow", font=("Verdana", "10", "italic", "bold"))
      msg.pack(pady=10)
    elif self.classe == "caçador":
      txt = """
      Você escolheu caçar seus inimigos!
      Os caçadores ão dotados de extrema destreza e precisão, 
      utilizam duas pistolas munidas de balas explosivas de prata e 
      conseguem eliminar inimigos à uma grande distância
      """
      msg = Label(tela, text=txt.upper(), bg="#000000", fg="yellow", font=("Verdana", "10", "italic", "bold"))
      msg.pack(pady=10)




  def get_txt(self):

    txt = """
    Você está pront@ para iniciar sua jornada no mundo de Arcadia!
    """+self.get_nomeCompleto()+", o mais novo membro do "+self.get_origem()+""", prepare-se para
     desenvolver sua reputação e talento como """+self.get_classe()+""" e enfrentar 
     seus inimigos!"""
    return txt.upper()

  def get_descricao(self): #AJEITAR: COLOCAR ALIADOS INIMIGOS E CLASSES
    txt = ("""
    Nome: %s
    Exército: %s
    Profissão: %s
    Poderes Raciais: 
    %s
    Poderes da Classe: 
    %s
    Tipo de Armadura: %s
    Arma: %s
    Aliados: %s
    Inimigos: %s
    """% (self.get_nomeCompleto(),self.get_origem(),self.get_classe(),self.get_poderes_raciais(),self.get_poderes_classe(),self.get_tipo_armadura(),self.get_arma(),self.get_aliados(),self.get_inimigos()))
    return txt.upper()
