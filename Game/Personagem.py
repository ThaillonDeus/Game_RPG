from Criatura import Criatura

class Personagem(Criatura):
    def __init__(self):
        #Atribuições genericos
        #id = Numero de identificação || name = Nome do Personagem || xp = Experiencia do Personagem
        self.id = ""
        self.name = "Thaillon"
        self.xp = 0
        #Atributos Basicos
        #int = Inteligencia || str = Força || dex = Agilidade || con = Constituição
        #hp = Pontos de Vida || hp_r = Regeneração de Vida || mana = Energia para Magias || mana_r = Regeneração de mana
        self.int = 0
        self.str = 0
        self.dex = 0
        self.con = 0
        self.hp = 0
        self.hp_r = 0
        self.mana = 0
        self.mana_r = 0
        #Atributos Magicos
        #dano_m = Dano Magico || pen_m = Penetração Magica || vamp_m = Roubo de Vida Magico || cast_s = Velocidade de Conjuração
        self.dano_m = 0
        self.pen_m = 0
        self.vamp_m = 0
        self.cast_s = 0
        #Atributos Fisicos
        #dano_f = Dano Fisico || pen_f = Penetração Fisica || life_s = Roubo de Vida || atk_s = Velocidade de Ataque
        self.dano_f = 0
        self.pen_f = 0
        self.life_s = 0
        self.atk_s = 0
        #Atributos Especiais
        #chan_c = Chance de Critico || dano_c = Dano Critico || dano_fogo = Dano tipo Fogo || dano_gelo = Dano tipo Gelo ||
        #dano_elet = Dano tipo Eletrico || dano_sagr = Dano tipo Sagrado || dano_trev = Dano tipo Trevas || dano_vene = Dano tipo Veneno ||
        self.chan_c = 0
        self.dano_c = 0
        self.dano_fogo = 0
        self.dano_gelo = 0
        self.dano_elet = 0
        self.dano_sagr = 0
        self.dano_trev = 0
        self.dano_vene = 0
        #Atributos Defensivos
        #block = Chance de bloqueio || dodge = Chance de esquiva
        #def_f = Defesa Fisica || def_m = Defesa Magica || def_fogo = Defesa para Fogo || def_gelo = Defesa para Gelo ||
        # def_elet = Defesa para Eletrico || def_sagr = Defesa para Sagrado || def_trev = Defesa para Trevas || def_vene = Defesa para Veneno ||
        self.block = 0
        self.dodge = 0
        self.def_m = 0
        self.def_f = 0
        self.def_fogo = 0
        self.def_gelo = 0
        self.def_elet = 0
        self.def_sagr = 0
        self.def_trev = 0
        self.def_vene = 0



