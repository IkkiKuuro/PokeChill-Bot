# 🤖 Pokechill Bot

Bot em Python para automatizar ações no jogo Pokechill usando Selenium.

## 📋 Funcionalidades

- ✅ Monitorar estado do jogo em tempo real
- ✅ Detectar vitórias e derrotas automaticamente
- ✅ Reiniciar batalhas automaticamente
- ✅ Executar JavaScript customizado no contexto do jogo
- ✅ Salvar/carregar jogo automaticamente
- ✅ Suporte para ações customizadas baseadas em eventos
- ✅ Estatísticas de batalhas (vitórias, derrotas, taxa de sucesso)
- ✅ Auto-save configurável
- ✅ Limite de derrotas consecutivas
- ✅ Menu interativo para testes

## 🚀 Instalação

### Método 1: Instalação Rápida (Windows)

1. **Execute o instalador:**
```bash
install.bat
```

2. **Inicie o bot:**
```bash
start.bat
```

### Método 2: Instalação Manual

1. **Instale o Python 3.8+** (se ainda não tiver)

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Instale o ChromeDriver:**
   - O bot usa o Chrome/Chromium
   - O `webdriver-manager` baixa automaticamente o driver correto

## 📖 Uso Básico

### Exemplo 1: Reiniciar ao perder

```python
from pokechill_bot import create_bot

# Cria e inicia o bot
bot = create_bot()

# Monitora e reinicia ao perder
bot.monitor_battle(
    auto_restart_on_loss=True,  # Reinicia ao perder
    auto_restart_on_win=False   # Não reinicia ao vencer
)

# Quando terminar
bot.stop()
```

### Exemplo 2: Farm infinito

```python
from pokechill_bot import create_bot

bot = create_bot()

# Reinicia tanto ao perder quanto ao vencer
bot.monitor_battle(
    auto_restart_on_loss=True,
    auto_restart_on_win=True
)

bot.stop()
```

### Exemplo 3: Ações customizadas

```python
from pokechill_bot import create_bot
import time

bot = create_bot()

# Lógica customizada
while True:
    state = bot.get_game_state()
    
    if bot.is_battle_won():
        print("Venci!")
        bot.save_game()  # Salva ao vencer
        bot.restart_battle()
    
    elif bot.is_battle_lost():
        print("Perdi!")
        bot.restart_battle()
    
    time.sleep(1)

bot.stop()
```

## 🎯 Exemplos Prontos

### Início Rápido (Windows)
```bash
start.bat
```

### Executar exemplos individualmente:

```bash
# Auto-restart ao perder (recomendado para iniciantes)
python examples/auto_restart_on_loss.py

# Farm infinito (reinicia sempre)
python examples/auto_farm.py

# Ações customizadas (salva a cada 5 vitórias, para após 3 derrotas)
python examples/custom_actions.py

# Bot avançado (usa config.py para configurações)
python examples/advanced_bot.py

# Menu interativo (testes e personalização)
python demo.py
```

## 🔧 API Principal

### `PokechillBot`

#### Métodos principais:

- **`start()`**: Inicia o navegador e abre o jogo
- **`stop()`**: Fecha o navegador
- **`get_game_state()`**: Obtém informações atuais do jogo
- **`is_in_combat()`**: Verifica se está em combate
- **`is_battle_lost()`**: Verifica se perdeu a batalha
- **`is_battle_won()`**: Verifica se venceu a batalha
- **`restart_battle()`**: Reinicia a batalha atual
- **`save_game()`**: Salva o jogo
- **`load_game()`**: Carrega o save
- **`execute_js(script)`**: Executa JavaScript no jogo
- **`monitor_battle(auto_restart_on_loss, auto_restart_on_win)`**: Monitora e age automaticamente

#### Exemplo completo:

```python
from pokechill_bot import PokechillBot
import time

# Cria o bot (pode passar URL custom)
bot = PokechillBot(game_url="file:///caminho/para/index.html")
bot.start()

# Aguarda carregar
time.sleep(5)

# Obtém estado
state = bot.get_game_state()
print(f"Área atual: {state['currentArea']}")
print(f"Em combate: {state['inCombat']}")

# Executa código JavaScript customizado
result = bot.execute_js("return saved.currentArea")
print(f"Resultado JS: {result}")

# Ativa auto-refight do próprio jogo
bot.enable_auto_refight()

# Monitora batalhas
bot.monitor_battle(auto_restart_on_loss=True)

bot.stop()
```

## 🎮 Configurações

### Usar com o jogo local:

```python
bot = create_bot()  # Detecta automaticamente o index.html
```

### Usar com URL online:

```python
bot = create_bot(game_url="https://seu-servidor.com/pokechill")
```

### Modo headless (sem janela do navegador):

```python
bot = create_bot(headless=True)
```

## 🐛 Troubleshooting

### Erro: ChromeDriver não encontrado
- E⚙️ Arquivo de Configuração

Edite o arquivo `config.py` para personalizar o comportamento do bot:

```python
# URL do jogo
GAME_URL = None  # None = detecta automaticamente

# Modo headless (sem janela)
HEADLESS = False

# Reiniciar automaticamente
AUTO_RESTART_ON_LOSS = True
AUTO_RESTART_ON_WIN = False

# Auto-save
AUTO_SAVE = False
SAVE_INTERVAL = 5  # Salvar a cada 5 vitórias

# Limite de derrotas consecutivas (0 = sem limite)
MAX_CONSECUTIVE_LOSSES = 0

# Logs detalhados
VERBOSE_LOGGING = True
```

## 📁 Estrutura do Projeto

```
bot/
├── pokechill_bot.py          # Classe principal do bot
├── config.py                 # Arquivo de configuração
├── requirements.txt          # Dependências Python
├── install.bat              # Instalador (Windows)
├── start.bat                # Launcher rápido (Windows)
├── demo.py                  # Menu interativo
├── README.md                # Este arquivo
└── examples/
    ├── auto_restart_on_loss.py   # Reinicia ao perder
    ├── auto_farm.py              # Farm infinito
    ├── custom_actions.py         # Ações personalizadas
    └── advanced_bot.py           # Bot com todas features
```

## 📝 Notas

- O bot interage com o jogo através do JavaScript, então todas as funções do jogo podem ser acessadas
- Você pode criar lógicas complexas usando `bot.execute_js()` para executar qualquer código no contexto do jogo
- Use `bot.get_game_state()` para monitorar variáveis do jogo como `saved.currentArea`, `wildPkmnHp`, etc.
- O bot funciona tanto com o jogo local (index.html) quanto hospedado online

## 💡 Dicas

- Use o **menu interativo** (`demo.py`) para entender como o bot funciona
- Configure o **bot avançado** (`advanced_bot.py`) para ter estatísticas e auto-save
- Edite `config.py` uma vez e use sempre o bot avançado
- Use **modo headless** (`HEADLESS = True`) para economizar recursos
- Confira se a estrutura do HTML não mudou

### JavaScript não executa
- Certifique-se de que o jogo está totalmente carregado
- Use `bot.execute_js()` apenas após o carregamento completo

## 📝 Notas

- O bot interage com o jogo através do JavaScript, então todas as funções do jogo podem ser acessadas
- Você pode criar lógicas complexas usando `bot.execute_js()` para executar qualquer código no contexto do jogo
- Use `bot.get_game_state()` para monitorar variáveis do jogo como `saved.currentArea`, `wildPkmnHp`, etc.

## 🔐 Segurança

- Este bot é para uso pessoal/educacional
- Não compartilhe credenciais ou dados sensíveis
- Use com responsabilidade

## 📄 Licença

Este bot é fornecido "como está" para uso educacional e pessoal.
