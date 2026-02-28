"""
Configurações do Bot PokeChill
Edite este arquivo para personalizar o comportamento do bot
"""

# ============================================
# CONFIGURAÇÕES GERAIS
# ============================================

# URL do jogo
GAME_URL = "https://play-pokechill.github.io"

# Tempo de espera inicial para login manual (segundos)
INITIAL_WAIT = 5

# Tempo entre ações (segundos)
ACTION_DELAY = 0.5

# Tempo de espera após batalhas (segundos)
BATTLE_DELAY = 2


# ============================================
# TIMES PREDEFINIDOS
# ============================================
# O jogo tem 30 times predefinidos (preview1 a preview30)
# O bot pode escolher entre time 1 e time 30

# Para trocar de time, execute o bot e escolha o número
# OU edite a linha team_number no bot.py


# ============================================
# SELETORES DO JOGO (HTML)
# ============================================
# Ajuste conforme o HTML real do jogo
# Use o Test.py para descobrir os IDs corretos

# Botões de iniciar batalha (tenta todos na ordem)
START_BATTLE_SELECTORS = [
    ("id", "start-battle"),
    ("id", "battle-button"),
    ("xpath", "//button[contains(text(), 'Battle')]"),
    ("xpath", "//button[contains(text(), 'Start')]"),
    ("xpath", "//button[contains(text(), 'Fight')]"),
    ("class", "start-battle"),
]

# Indicadores de derrota
LOST_INDICATORS = [
    ("xpath", "//div[contains(text(), 'You lost')]"),
    ("xpath", "//div[contains(text(), 'Defeat')]"),
    ("xpath", "//button[contains(text(), 'Try Again')]"),
    ("xpath", "//button[contains(text(), 'Restart')]"),
    ("id", "defeat-screen"),
    ("class", "defeat"),
]

# Indicadores de vitória
WON_INDICATORS = [
    ("xpath", "//div[contains(text(), 'You won')]"),
    ("xpath", "//div[contains(text(), 'Victory')]"),
    ("xpath", "//button[contains(text(), 'Continue')]"),
    ("id", "victory-screen"),
    ("class", "victory"),
]

# Botões de ataque
ATTACK_SELECTORS = [
    ("class", "move-button"),
    ("class", "attack"),
    ("xpath", "//button[contains(@class, 'move')]"),
    ("id", "move1"),
    ("id", "attack1"),
]

# Botões de reiniciar
RESTART_SELECTORS = [
    ("xpath", "//button[contains(text(), 'Try Again')]"),
    ("xpath", "//button[contains(text(), 'Restart')]"),
    ("xpath", "//button[contains(text(), 'New Game')]"),
    ("id", "restart-button"),
    ("id", "try-again"),
    ("class", "restart"),
]

# Botões de continuar
CONTINUE_SELECTORS = [
    ("xpath", "//button[contains(text(), 'Continue')]"),
    ("xpath", "//button[contains(text(), 'Next')]"),
    ("id", "continue-button"),
    ("class", "continue"),
]


# ============================================
# CONFIGURAÇÕES DE ESTRATÉGIA
# ============================================

# Escolher ataques aleatoriamente ou sempre o primeiro?
RANDOM_ATTACKS = True

# Frequência de exibição de estatísticas (a cada X batalhas)
STATS_FREQUENCY = 10

# Ativar logs detalhados?
VERBOSE_LOGGING = True
