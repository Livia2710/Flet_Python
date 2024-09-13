import flet as ft  # Importa a biblioteca FLET para criar interfaces gráficas
import random  # Importa o módulo random para gerar valores aleatórios
import string  # Importa o módulo string para acessar os caracteres (letras, números e símbolos)

# Função principal do aplicativo, que define a interface e a lógica
def main(page: ft.Page):
    # Define o modo de tema com base no sistema operacional do dispositivo (claro ou escuro)
    page.theme_mode = ft.ThemeMode.SYSTEM
    # Define a largura da janela, simulando o tamanho de um celular
    page.window.width = 350
    # Define a altura da janela
    page.window.height = 600
    # Define o padding (espaçamento interno) ao redor da página
    page.padding = 20

    # Função que gera a senha com base nas preferências do usuário
    def gerar_senha(e):
        comprimento = int(slider.value)  # Obtém o valor do comprimento da senha a partir do slider
        caracteres = ""  # Inicializa a string de caracteres disponíveis para a senha

        # Verifica se o switch de letras maiúsculas está ativo, e se sim, adiciona ao conjunto de caracteres
        if upper_switch.value:
            caracteres += string.ascii_uppercase
        # Verifica se o switch de letras minúsculas está ativo, e se sim, adiciona ao conjunto de caracteres
        if lower_switch.value:
            caracteres += string.ascii_lowercase
        # Verifica se o switch de números está ativo, e se sim, adiciona ao conjunto de caracteres
        if numbers_switch.value:
            caracteres += string.digits
        # Verifica se o switch de símbolos está ativo, e se sim, adiciona ao conjunto de caracteres
        if symbols_switch.value:
            caracteres += string.punctuation

        # Verifica se ao menos um tipo de caractere foi selecionado
        if caracteres:
            # Gera a senha escolhendo caracteres aleatórios
            senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
            senha_output.value = senha  # Define a senha gerada como o valor do campo de saída
        else:
            # Caso nenhum tipo de caractere tenha sido selecionado, mostra uma mensagem de erro
            senha_output.value = "Selecione ao menos um tipo de caractere."
        page.update()  # Atualiza a interface da página para refletir as mudanças

    # Função para copiar a senha gerada para a área de transferência
    def copiar_senha(e):
        # Copia o valor da senha gerada para a área de transferência
        page.set_clipboard(senha_output.value)
        # Cria um snackbar (notificação) informando que a senha foi copiada
        snack = ft.SnackBar(ft.Text("Senha copiada para a área de transferência!"))
        page.overlay.append(snack)  # Adiciona o snackbar à sobreposição da página
        snack.open = True  # Abre o snackbar (faz ele aparecer)
        page.update()

    # Elemento de título da UI, com estilo e espaçamento no topo
    titulo = ft.Container(
        content=ft.Text("Gerador de Senhas", size=28, weight="bold"),
        padding=ft.padding.only(top=50)  # Espaçamento somente para o topo
    )

    # Campo de texto que mostra a senha gerada, com ícone de copiar e um fundo variante
    senha_output = ft.TextField(
        value="", 
        label="Senha gerada",
        read_only=True,  # Define que o campo é apenas leitura
        width=280,
        # Botão de ícone para copiar a senha, associando à função copiar_senha
        suffix=ft.IconButton(ft.icons.COPY, on_click=copiar_senha),
        # Define a cor de fundo do campo
        bgcolor=ft.colors.SURFACE_VARIANT
    )

    # Slider que permite escolher o comprimento da senha (De 8 a 20 caracteres)
    slider = ft.Slider(
        min=8,  # Comprimento mínimo da senha
        max=20,  # Máximo
        value=12,  # Comprimento padrão
        divisions=12,  # Número de divisões no slider
        label="CARACTERES: {value}"  # Rótulo dinâmico mostrando o valor atual do slider
    )

    # Switch para selecionar se letras maiúsculas devem ser incluídas na senha
    upper_switch = ft.Switch(label="Letras maiúsculas")
    # Switch para selecionar se letras minúsculas devem ser incluídas na senha (ativo por padrão)
    lower_switch = ft.Switch(label="Letras minúsculas", value=True)
    # Switch para selecionar se números devem ser incluídos na senha
    numbers_switch = ft.Switch(label="Incluir números")
    # Switch para selecionar se símbolos devem ser incluídos na senha
    symbols_switch = ft.Switch(label="Incluir símbolos")

    # Botão para gerar a senha, que chama a função gerar_senha ao ser clicado
    gerar_senha_btn = ft.ElevatedButton(
        text="GERAR SENHA",
        on_click=gerar_senha,  # Função a ser chamada quando o botão é clicado
        color=ft.colors.ON_PRIMARY,  # Cor do texto do botão
        bgcolor=ft.colors.PRIMARY  # Cor do fundo do botão
    )

    # Coluna para organizar os switches de forma centralizada
    seletores = ft.Column(
        [
            upper_switch,
            lower_switch,
            numbers_switch,
            symbols_switch
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Alinha os elementos verticalmente no centro
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha horizontalmente
        spacing=10  # Espaço entre elementos
    )

    # Adiciona todos os elementos à página em uma única coluna
    page.add(
        ft.Column(
            [
                titulo,
                senha_output,
                slider,
                ft.Text("PREFERÊNCIAS"),
                seletores,
                gerar_senha_btn,
            ],
            alignment=ft.MainAxisAlignment.START,  # Alinha no topo da coluna
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinha horizontalmente
            spacing=10  # Espaço entre elementos
        )
    )

# Executa o aplicativo, chamando a função main como ponto de entrada
ft.app(target=main)
