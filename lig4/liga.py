import tkinter as tk
from tkinter import messagebox

class TelaInicial:
    def __init__(self, mestre, callback):
        self.mestre = mestre
        self.callback = callback
        self.criar_interface()

    def criar_interface(self):
        self.frame = tk.Frame(self.mestre, padx=20, pady=20)
        self.frame.pack()

        self.label_nome_jogador1 = tk.Label(self.frame, text="Nome do Jogador 1:")
        self.label_nome_jogador1.grid(row=0, column=0, pady=(0, 5))

        self.entry_nome_jogador1 = tk.Entry(self.frame)
        self.entry_nome_jogador1.grid(row=0, column=1, pady=(0, 5))

        self.label_nome_jogador2 = tk.Label(self.frame, text="Nome do Jogador 2:")
        self.label_nome_jogador2.grid(row=1, column=0, pady=(0, 5))

        self.entry_nome_jogador2 = tk.Entry(self.frame)
        self.entry_nome_jogador2.grid(row=1, column=1, pady=(0, 5))

        self.botao_iniciar = tk.Button(self.frame, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.botao_iniciar.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    def iniciar_jogo(self):
        nome_jogador1 = self.entry_nome_jogador1.get() or "Jogador 1"
        nome_jogador2 = self.entry_nome_jogador2.get() or "Jogador 2"
        self.callback(nome_jogador1, nome_jogador2)

class BotaoRedondo(tk.Canvas):
    def __init__(self, mestre, raio, cor_fundo, comando=None, *args, **kwargs):
        super().__init__(mestre, width=2*raio, height=2*raio, bd=0, highlightthickness=0, relief='ridge', *args, **kwargs)
        self.raio = raio
        self.comando = comando

        self.imagem_fundo = tk.PhotoImage(width=2*raio, height=2*raio)
        self.create_image(raio, raio, image=self.imagem_fundo)

        self.bind("<Button-1>", self._ao_clicar)

        self.atualizar_cor_fundo(cor_fundo)

    def _ao_clicar(self, evento):
        if self.comando:
            self.comando()

    def atualizar_cor_fundo(self, cor):
        self.create_oval(0, 0, 2*self.raio, 2*self.raio, fill=cor, outline=cor)
        self.itemconfig(self.imagem_fundo, image=self.imagem_fundo)

class Lig4:
    def __init__(self):
        self.nome_jogador1 = ""
        self.nome_jogador2 = ""
        self.jogador_atual = ""
        self.tabuleiro = [['' for _ in range(7)] for _ in range(6)]

    def iniciar(self):
        self.root = tk.Tk()
        self.root.title('Lig4')
        self.criar_tela_inicial()
        self.root.mainloop()

    def criar_tela_inicial(self):
        self.tela_inicial = TelaInicial(self.root, self.iniciar_jogo)

    def iniciar_jogo(self, nome_jogador1, nome_jogador2):
        self.nome_jogador1 = nome_jogador1
        self.nome_jogador2 = nome_jogador2
        self.jogador_atual = 'blue'
        self.tela_inicial.frame.destroy()
        self.criar_interface_jogo()

    def criar_interface_jogo(self):
        self.botoes = []
        for i in range(6):
            linha = []
            for j in range(7):
                botao = BotaoRedondo(self.root, 30, 'white', comando=lambda coluna=j: self.jogar(coluna))
                botao.grid(row=i, column=j, padx=5, pady=5)
                linha.append(botao)
            self.botoes.append(linha)

    def jogar(self, coluna):
        for i in range(5, -1, -1):
            if self.tabuleiro[i][coluna] == '':
                self.tabuleiro[i][coluna] = self.jogador_atual
                self.botoes[i][coluna].atualizar_cor_fundo(self.jogador_atual)
                if self.verificar_vitoria(i, coluna):
                    self.mostrar_vencedor()
                elif self.verificar_empate():
                    self.mostrar_empate()
                else:
                    self.jogador_atual = 'yellow' if self.jogador_atual == 'blue' else 'blue'
                break

    def verificar_vitoria(self, linha, coluna):
        if self.contar_pecas_na_linha(linha, coluna, 0, 1) >= 4:
            return True
        if self.contar_pecas_na_linha(linha, coluna, 1, 0) >= 4:
            return True
        if self.contar_pecas_na_linha(linha, coluna, 1, 1) >= 4:
            return True
        if self.contar_pecas_na_linha(linha, coluna, -1, 1) >= 4:
            return True
        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if '' in linha:
                return False  # Ainda há espaços vazios, o jogo não está empatado
        return True  # Não há mais espaços vazios, o jogo está empatado

    def contar_pecas_na_linha(self, linha, coluna, incremento_linha, incremento_coluna):
        jogador_atual = self.jogador_atual
        contador = 1
        i, j = linha + incremento_linha, coluna + incremento_coluna
        while 0 <= i < 6 and 0 <= j < 7 and self.tabuleiro[i][j] == jogador_atual:
            contador += 1
            i += incremento_linha
            j += incremento_coluna
        i, j = linha - incremento_linha, coluna - incremento_coluna
        while 0 <= i < 6 and 0 <= j < 7 and self.tabuleiro[i][j] == jogador_atual:
            contador += 1
            i -= incremento_linha
            j -= incremento_coluna
        return contador

    def mostrar_vencedor(self):
        mensagem = f'O jogador {self.jogador_atual.capitalize()} venceu!'
        self.mostrar_mensagem_final(mensagem)

    def mostrar_empate(self):
        mensagem = 'O jogo terminou em empate!'
        self.mostrar_mensagem_final(mensagem)

    def mostrar_mensagem_final(self, mensagem):
        resposta = messagebox.askquestion('Lig4', f'{mensagem}\nDeseja jogar outra partida?')
        if resposta == 'yes':
            self.reiniciar_jogo()
        else:
            self.root.destroy()

    def reiniciar_jogo(self):
        self.tabuleiro = [['' for _ in range(7)] for _ in range(6)]
        for linha in self.botoes:
            for botao in linha:
                botao.atualizar_cor_fundo('white')
        self.jogador_atual = 'blue'

# Criar e iniciar o jogo
jogo = Lig4()
jogo.iniciar()
