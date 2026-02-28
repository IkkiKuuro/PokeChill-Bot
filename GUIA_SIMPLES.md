# 🎮 PokeChill Bot - Automatização Simplificada

Bot para automatizar batalhas no jogo PokeChill usando o código fonte do jogo.

## ✨ O que o bot faz:

1. ✅ **Seleciona o time** que você escolher (1-30)
2. ✅ **Monitora batalhas** a cada 3 segundos
3. ✅ **Detecta quando a batalha termina** (vitória ou derrota)
4. ✅ **Clica automaticamente** em "Fight Again"
5. ✅ **Aguarda 60 segundos** antes de verificar novamente

## 🚀 Como usar:

### 1️⃣ **Preparar o navegador:**

**Feche TODOS os navegadores abertos**, depois:

#### Para Brave:
```cmd
"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222
```

#### Para Chrome:
```cmd
chrome.exe --remote-debugging-port=9222
```

### 2️⃣ **Abrir o jogo:**
1. No navegador que abriu, vá para: https://play-pokechill.github.io
2. Faça login
3. **IMPORTANTE**: Entre em uma área e comece uma batalha

### 3️⃣ **Rodar o bot:**
```cmd
python bot_simple.py
```

4. Escolha o time (1-30) ou aperte ENTER para usar o time 2
5. Deixe rodando!

## 📊 Recursos:

- **Monitoramento em tempo real**: Mostra status a cada 30 segundos
- **Contador de batalhas**: Acompanhe quantas batalhas foram feitas
- **Estatísticas**: Mostra stats a cada 5 batalhas
- **Ctrl+C para parar**: Para o bot com segurança

## 🔧 Como funciona:

O bot usa o **código fonte do jogo** para detectar:
- `explore-combat` - Div que aparece durante batalhas
- `area-rejoin` - Botão "Fight Again" após batalha
- `team-slot-selector` - Dropdown para selecionar times

Muito mais simples e confiável que a versão anterior!

## ⚠️ Problemas comuns:

### "Não conseguiu conectar ao navegador"
→ Certifique-se de abrir o navegador com `--remote-debugging-port=9222`

### "Não encontrou botão Fight Again"
→ Você precisa estar em uma área de batalha no jogo antes de rodar o bot

### Bot não faz nada
→ Verifique se você **começou uma batalha** antes de iniciar o bot

## 📝 Exemplo de uso:

```
🎮 POKECHILL BOT - Versão Simplificada
============================================================
🎯 Escolha o time (1-30) ou ENTER para time 2: 5

✅ Time 5 selecionado!

🌐 COMO USAR:
============================================================
1. Abra o jogo no navegador (Chrome ou Brave)
2. Faça login se necessário
3. ENTRE EM UMA ÁREA/BATALHA no jogo
4. Deixe o jogo rodando
============================================================

✅ Depois que entrar na batalha, APERTE ENTER aqui...

[14:30:00] 🤖 Bot iniciado!
[14:30:00] 🎯 Usando time: 5
[14:30:00] 💡 Pressione Ctrl+C para parar

[14:30:30] 🎮 Status: EM BATALHA | Batalhas: 0

==================================================
[14:32:15] 💀 Batalha terminou!
[14:32:15] ⏳ Aguardando 2 segundos...
[14:32:17] ✅ Clicou em 'Fight Again'
[14:32:17] ⏳ Aguardando 60 segundos para nova batalha...
```

---

Feito com ❤️ usando o código fonte do PokeChill
