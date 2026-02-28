# 🎮 PokeChill Bot

Bot automatizado para jogar PokeChill infinitamente sem abrir o navegador automaticamente.

## 📋 Instalação

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

### Método 1: Bot abre o navegador (Recomendado)
```bash
python bot.py
```
- Escolha o time (1 a 30) ou ENTER para time 1
- Escolha navegador: **1** = Chrome, **2** = Brave
- Bot abre automaticamente

### Método 2: Usar navegador já aberto (Chrome/Brave)
1. Feche todos os navegadores
2. Execute no cmd:
   - Chrome: `chrome.exe --remote-debugging-port=9222`
   - Brave: `"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222`
3. Abra o jogo: https://play-pokechill.github.io
4. Execute: `python bot.py`
5. Escolha o time (1 a 30)

> 💡 **Usando Brave?** Veja [USAR_COM_BRAVE.md](USAR_COM_BRAVE.md) para instruções detalhadas

## ⚙️ Configuração

O jogo tem 30 times predefinidos. Ao executar o bot, escolha de 1 a 30.

## 📊 Funcionalidades

- ✅ Loop infinito
- ✅ Auto-restart quando perde
- ✅ Seleção de times (1-30)
- ✅ Estatísticas de batalha
- ✅ Suporte a Chrome e Brave
- ✅ Conecta ao navegador já aberto

## 💡 Mais Informações

Veja [GUIA_RAPIDO.md](GUIA_RAPIDO.md) para detalhes completos.
