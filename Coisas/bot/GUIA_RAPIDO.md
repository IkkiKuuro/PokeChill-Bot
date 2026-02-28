# 🎮 Guia Rápido - Pokechill Bot

## 🚀 Começando em 3 Passos

### 1️⃣ Instalação
```bash
# Execute o instalador (Windows)
install.bat

# OU instale manualmente
pip install -r requirements.txt
```

### 2️⃣ Escolha um Modo

#### Modo 1: Usar o Launcher (Mais Fácil) 🌟
```bash
start.bat
```
Escolha uma das opções no menu!

#### Modo 2: Executar Diretamente
```bash
# Reinicia ao perder (seu caso de uso!)
python examples\auto_restart_on_loss.py
```

### 3️⃣ Pronto! 🎉
O bot vai abrir o Chrome e começar a monitorar o jogo!

---

## 🎯 Casos de Uso Comuns

### 🔄 Caso 1: Reiniciar ao Perder (Seu Pedido!)
**Situação:** Quando perco a batalha, quero que o bot recomece automaticamente

```bash
python examples\auto_restart_on_loss.py
```

**O que faz:**
- ✅ Detecta quando você perde
- ✅ Reinicia a batalha automaticamente
- ✅ Continua jogando até você parar (Ctrl+C)

---

### ⚡ Caso 2: Farm Infinito
**Situação:** Quero farmar itens/experiência sem parar

```bash
python examples\auto_farm.py
```

**O que faz:**
- ✅ Reinicia ao perder
- ✅ Reinicia ao vencer
- ✅ Loop infinito de batalhas

---

### 📊 Caso 3: Bot Avançado com Estatísticas
**Situação:** Quero ver quantas batalhas ganhei/perdi e auto-salvar

```bash
python examples\advanced_bot.py
```

**Configure antes em `config.py`:**
```python
AUTO_SAVE = True          # Ativa auto-save
SAVE_INTERVAL = 5         # Salva a cada 5 vitórias
MAX_CONSECUTIVE_LOSSES = 3  # Para após 3 derrotas seguidas
```

**O que faz:**
- ✅ Mostra estatísticas (vitórias, derrotas, tempo)
- ✅ Auto-save configurável
- ✅ Para após X derrotas consecutivas

---

### 🛠️ Caso 4: Ações Personalizadas
**Situação:** Quero fazer algo específico em certas situações

**Edite:** `examples\custom_actions.py`

**Exemplos do que pode fazer:**
```python
# Detectar vitória
if bot.is_battle_won():
    print("Ganhei!")
    bot.save_game()  # Salva
    # Seu código aqui

# Detectar derrota
if bot.is_battle_lost():
    print("Perdi!")
    bot.restart_battle()  # Restart
    # Seu código aqui

# Obter informações do jogo
state = bot.get_game_state()
print(f"Área atual: {state['currentArea']}")

# Executar JavaScript customizado
bot.execute_js("saved.autoRefight = true")
```

---

## 🧪 Testar o Bot (Menu Interativo)

```bash
python demo.py
```

**Menu com opções:**
1. Ver estado do jogo
2. Verificar se está em combate
3. Verificar vitória/derrota
4. Reiniciar batalha manualmente
5. Ativar/desativar auto-refight
6. Executar JavaScript customizado
E mais...

---

## ⚙️ Configurações Principais (config.py)

```python
# === BÁSICO ===
HEADLESS = False  # True = sem janela do navegador
AUTO_RESTART_ON_LOSS = True  # Reinicia ao perder
AUTO_RESTART_ON_WIN = False  # Reinicia ao vencer

# === AUTO-SAVE ===
AUTO_SAVE = True
SAVE_INTERVAL = 5  # Salva a cada X vitórias

# === SEGURANÇA ===
MAX_CONSECUTIVE_LOSSES = 0  # 0 = sem limite, 3 = para após 3 derrotas seguidas

# === PERFORMANCE ===
CHECK_INTERVAL = 0.5  # Checa a cada 0.5s
```

---

## 🆘 Problemas Comuns

### ❌ "ChromeDriver not found"
**Solução:**
```bash
pip install webdriver-manager
```

### ❌ Bot não detecta vitórias/derrotas
**Solução:**
- Aumente `LOAD_WAIT_TIME` em `config.py`
- Certifique-se que o jogo carregou completamente

### ❌ "Module not found"
**Solução:**
```bash
pip install -r requirements.txt
```

### ❌ Navegador não abre
**Solução:**
- Instale o Google Chrome
- Ou use outro navegador editando `pokechill_bot.py`

---

## 💡 Dicas Pro

1. **Use o modo headless** para economizar recursos:
   ```python
   # Em config.py
   HEADLESS = True
   ```

2. **Combine com auto-save** para nunca perder progresso:
   ```python
   AUTO_SAVE = True
   SAVE_INTERVAL = 3  # Salva a cada 3 vitórias
   ```

3. **Limite derrotas** para não ficar preso em batalhas difíceis:
   ```python
   MAX_CONSECUTIVE_LOSSES = 5
   ```

4. **Execute em segundo plano** e faça outras coisas!

---

## 📞 Precisa de Ajuda?

1. **Menu Interativo:** Execute `python demo.py` para testar funções
2. **README Completo:** Veja `README.md` para documentação detalhada
3. **Exemplos:** Todos em `examples/` estão comentados

---

## ✨ Exemplo Completo - Seu Caso de Uso

```python
# arquivo: meu_bot.py
from pokechill_bot import create_bot
import time

# Cria o bot
bot = create_bot()

# Aguarda carregar
print("Aguardando jogo carregar...")
time.sleep(5)

print("🎮 Bot iniciado!")
print("📌 Detectará derrotas e reiniciará automaticamente")
print("⏹️  Pressione Ctrl+C para parar\n")

try:
    while True:
        # Verifica se perdeu
        if bot.is_battle_lost():
            print("💀 PERDEU! Reiniciando em 2 segundos...")
            time.sleep(2)
            bot.restart_battle()
            print("✅ Batalha reiniciada!\n")
        
        time.sleep(0.5)  # Checa a cada 0.5s

except KeyboardInterrupt:
    print("\n👋 Parando bot...")

finally:
    bot.stop()
    print("✅ Encerrado!")
```

**Execute:**
```bash
python meu_bot.py
```

---

## 🎉 Pronto!

Agora você tem um bot completo para automatizar o Pokechill!

**Comece com:**
```bash
start.bat
```

E escolha a opção que melhor se adequa ao que você quer fazer! 🚀
