"""
Configurações do bot Pokechill
"""

# ===== CONFIGURAÇÕES DO JOGO =====

# URL do jogo (deixe None para detectar automaticamente o index.html local)
GAME_URL = None

# Se quer executar o navegador sem interface gráfica (headless)
HEADLESS = False

# ===== CONFIGURAÇÕES DE MONITORAMENTO =====

# Intervalo de checagem em segundos (quanto menor, mais CPU usa)
CHECK_INTERVAL = 0.5

# Tempo de espera após carregar o jogo (segundos)
LOAD_WAIT_TIME = 5

# ===== CONFIGURAÇÕES DE AUTO-RESTART =====

# Reiniciar automaticamente ao perder
AUTO_RESTART_ON_LOSS = True

# Reiniciar automaticamente ao vencer
AUTO_RESTART_ON_WIN = False

# Tempo de espera antes de reiniciar (segundos)
RESTART_DELAY = 1

# ===== CONFIGURAÇÕES DE SALVAMENTO =====

# Salvar automaticamente
AUTO_SAVE = False

# Intervalo de salvamento automático (em número de vitórias)
# Ex: 5 = salva a cada 5 vitórias
SAVE_INTERVAL = 5

# ===== CONFIGURAÇÕES AVANÇADAS =====

# Máximo de derrotas consecutivas antes de parar o bot
# 0 = nunca para
MAX_CONSECUTIVE_LOSSES = 0

# Ativar logs detalhados
VERBOSE_LOGGING = True

# Timeout para aguardar elementos aparecerem (segundos)
ELEMENT_TIMEOUT = 10

# ===== CONFIGURAÇÕES DO NAVEGADOR =====

# Argumentos adicionais para o Chrome
CHROME_OPTIONS = [
    '--disable-gpu',
    '--no-sandbox',
    # Adicione mais opções se necessário
    # '--window-size=1920,1080',
    # '--disable-notifications',
]
