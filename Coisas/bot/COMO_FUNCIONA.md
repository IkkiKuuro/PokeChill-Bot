# 🤖 Pokechill Bot - Como Funciona

## 📚 Visão Geral

Este bot funciona interagindo com o jogo Pokechill através do navegador, usando Selenium para controle e JavaScript para acessar o estado interno do jogo.

## 🔧 Arquitetura

```
┌─────────────────────────────────────────────────┐
│                  Seu Script                     │
│  (ex: auto_restart_on_loss.py)                  │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│           PokechillBot (pokechill_bot.py)       │
│  • Gerencia navegador                           │
│  • Executa JavaScript                           │
│  • Detecta eventos                              │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│               Selenium WebDriver                │
│  • Controla o Chrome                            │
│  • Interage com DOM                             │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│         Navegador Chrome                        │
│  ┌───────────────────────────────────────────┐  │
│  │        Jogo Pokechill (index.html)        │  │
│  │  • Estado do jogo (saved, team, etc)      │  │
│  │  • Funções (leaveCombat, setWildPkmn)     │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

## 🎯 Como o Bot Detecta Eventos

### 1. Detecção de Estado

O bot executa JavaScript no contexto do jogo para ler variáveis:

```javascript
// Exemplo de código que o bot executa
return {
    currentArea: saved.currentArea,
    inCombat: document.getElementById('explore-combat')?.style.display !== 'none',
    wildPkmnHp: wildPkmnHp,
    wildPkmnHpMax: wildPkmnHpMax
};
```

### 2. Detecção de Vitória

```python
def is_battle_won(self):
    state = self.get_game_state()
    
    # Verifica se HP do Pokémon selvagem chegou a 0
    if state.get('wildPkmnHp') is not None:
        return state['wildPkmnHp'] <= 0
```

### 3. Detecção de Derrota

```python
def is_battle_lost(self):
    # Verifica se todos Pokémon do time foram derrotados
    script = """
    let allDefeated = true;
    for (let i = 1; i <= 6; i++) {
        const slot = team['slot' + i];
        if (slot && slot.pkmn && slot.pkmn.currentHp > 0) {
            allDefeated = false;
            break;
        }
    }
    return allDefeated;
    """
    return self.execute_js(script)
```

## 🔄 Fluxo de Execução

### Monitoramento Básico

```
Início
  ↓
[Inicia Navegador] ← pokechill_bot.start()
  ↓
[Carrega Jogo] ← driver.get(game_url)
  ↓
[Loop Infinito] ← while True:
  ↓
[Obtém Estado] ← get_game_state()
  ↓
[Verifica Vitória?] ← is_battle_won()
  │
  ├─ SIM → [Ação ao Vencer] → [Reinicia?]
  │                              ↓
  └─ NÃO → [Verifica Derrota?] ← is_battle_lost()
            │
            ├─ SIM → [Ação ao Perder] → [Reinicia?]
            │                              ↓
            └─ NÃO → [Aguarda 0.5s] → [Volta ao Loop]
```

### Reinício de Batalha

```python
def restart_battle(self):
    # 1. Sai do combate atual
    self.execute_js("if (typeof leaveCombat === 'function') leaveCombat();")
    
    # 2. Inicia nova batalha
    self.execute_js("if (typeof setWildPkmn === 'function') setWildPkmn();")
```

## 🧩 Componentes Principais

### 1. PokechillBot (Classe Principal)

```python
class PokechillBot:
    def __init__(self, game_url, headless)
    def start()              # Inicia navegador
    def stop()               # Fecha navegador
    def execute_js(script)   # Executa JavaScript
    def get_game_state()     # Obtém estado do jogo
    def is_battle_won()      # Verifica vitória
    def is_battle_lost()     # Verifica derrota
    def restart_battle()     # Reinicia batalha
    def monitor_battle()     # Loop de monitoramento
```

### 2. Selenium WebDriver

Controla o navegador programaticamente:
- Abre URLs
- Executa JavaScript
- Encontra elementos
- Simula cliques

### 3. JavaScript Injection

O bot "conversa" com o jogo através de JavaScript:

```python
# Python (Bot)
result = bot.execute_js("return saved.currentArea")

# JavaScript (Executado no jogo)
# return saved.currentArea → retorna área atual
```

## 🎮 Interação com o Jogo

### Variáveis Acessíveis

O bot pode ler/modificar variáveis globais do jogo:

```javascript
// Exemplos de variáveis acessíveis
saved.currentArea          // Área atual
saved.autoRefight          // Auto-refight ativado
team.slot1.pkmn           // Pokémon no slot 1
wildPkmnHp                // HP do Pokémon selvagem
currentTrainerSlot        // Slot do treinador atual
```

### Funções Chamáveis

O bot pode executar funções do jogo:

```javascript
leaveCombat()             // Sai do combate
setWildPkmn()             // Inicia novo Pokémon selvagem
saveGame()                // Salva o jogo
loadGame()                // Carrega o jogo
```

## 💡 Exemplos de Customização

### Exemplo 1: Trocar de Área Automaticamente

```python
def change_area(bot, area_id):
    bot.execute_js(f"saved.currentArea = areas.{area_id}.id")
    bot.execute_js("setWildPkmn()")
```

### Exemplo 2: Verificar Itens

```python
def get_item_count(bot, item_id):
    script = f"return item.{item_id}.got"
    return bot.execute_js(script)

# Uso
potions = get_item_count(bot, "potion")
print(f"Poções: {potions}")
```

### Exemplo 3: Auto-Evoluir Pokémon

```python
def auto_evolve(bot):
    script = """
    // Percorre todos Pokémon
    for (let pkmnId in pkmn) {
        if (pkmn[pkmnId].caught > 0 && pkmn[pkmnId].canEvolve) {
            // Código de evolução aqui
        }
    }
    """
    bot.execute_js(script)
```

## 🔍 Debug e Testes

### Menu Interativo (demo.py)

O `demo.py` oferece um menu para testar funções:

```
1. Ver estado do jogo
   → Mostra todas variáveis (área, HP, etc)

2. Verificar combate
   → True/False se está em combate

3. Executar JavaScript
   → Digite código JS e veja o resultado
```

### Logs Detalhados

Configure em `config.py`:

```python
VERBOSE_LOGGING = True  # Mostra cada ação
```

Saída:
```
🏆 Vitória #5!
💾 Jogo salvo automaticamente!
🔄 Reiniciando batalha...
✅ Batalha reiniciada
```

## 🚀 Performance

### Otimização de Checagens

```python
# config.py
CHECK_INTERVAL = 0.5  # Checa a cada 0.5s

# Mais rápido (usa mais CPU)
CHECK_INTERVAL = 0.1

# Mais lento (economiza CPU)
CHECK_INTERVAL = 1.0
```

### Modo Headless

```python
# config.py
HEADLESS = True  # Sem janela = menos recursos
```

Economiza ~30-40% de CPU/RAM!

## 🛡️ Tratamento de Erros

O bot trata erros comuns:

```python
try:
    element = driver.find_element(By.ID, "element-id")
except NoSuchElementException:
    print("Elemento não encontrado")
    
try:
    WebDriverWait(driver, 10).until(...)
except TimeoutException:
    print("Timeout ao aguardar elemento")
```

## 🎓 Conclusão

O bot é basicamente um **controle remoto** para o jogo que:

1. ✅ **Vê** o estado através de JavaScript
2. ✅ **Age** executando funções do jogo
3. ✅ **Decide** baseado em condições (if/else)
4. ✅ **Repete** em loop infinito

Você pode criar qualquer automação combinando essas capacidades! 🚀
