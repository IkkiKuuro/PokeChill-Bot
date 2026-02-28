# 🎮 GUIA RÁPIDO - POKECHILL BOT

## 📦 INSTALAÇÃO (Primeira vez)

Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 COMO USAR

### Opção 1: Deixar o bot abrir o navegador (MAIS FÁCIL)
1. Execute: `python bot.py`
2. Escolha o time (1 a 30) ou ENTER para time 1
3. Quando perguntar, escolha:
   - **1** para Chrome
   - **2** para Brave
4. Faça login se necessário
5. Aperte ENTER
6. Pronto! O bot começará automaticamente

### Opção 2: Usar navegador já aberto (Chrome ou Brave)
1. Feche TODOS os navegadores
2. Abra o cmd/terminal
3. Execute:
   - **Chrome:** `chrome.exe --remote-debugging-port=9222`
   - **Brave:** `"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222`
4. Navegue para: https://play-pokechill.github.io
5. Faça login
6. Execute: `python bot.py`
7. Escolha o time (1 a 30)
8. Aperte ENTER quando solicitado

## 🎯 TIMES DISPONÍVEIS

O jogo tem **30 times predefinidos**:
- Time 1 a Time 30
- Escolha o número do seu time ao executar o bot
- Cada time tem 6 slots de Pokémon configurados

## 🔍 DESCOBRIR SLOTS E BOTÕES

Use o Test.py (se tiver) ou adicione prints no bot para ver os elementos disponíveis.

## ⌨️ CONTROLES

- **Ctrl + C**: Para o bot e mostra estatísticas

## 📊 ESTATÍSTICAS

O bot rastreia automaticamente:
- Total de batalhas
- Vitórias e derrotas
- Taxa de vitória

## 🐛 PROBLEMAS COMUNS

### "selenium não encontrado"
```bash
pip install selenium
```

### "ChromeDriver não encontrado"
- O Selenium geralmente instala automaticamente
- Ou baixe em: https://chromedriver.chromium.org/

### "Bot não encontra os botões"
- Atualize os seletores em **config.py**
- Use ferramentas de inspeção do Chrome (F12)

## 📝 ESTRUTURA DOS ARQUIVOS

```
📁 PokeChill-Bot/
│
├── 🤖 bot.py              # Bot principal - EXECUTE ESTE
├── ⚙️ config.py           # Configurações dos times
├── 📄 GUIA_RAPIDO.md      # Este arquivo
├── 📦 requirements.txt    # Dependências
└── 💾 save.json           # Save do jogo
```

## 💡 DICAS

1. **Mantenha a janela visível**: Para ver o que o bot está fazendo
2. **Comece com default**: Teste primeiro com o time padrão
3. **Monitore as estatísticas**: Aparecem a cada 10 batalhas

---

**Bom jogo! 🎮🚀**
