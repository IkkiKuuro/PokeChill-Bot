# 🦁 Usar Bot com Brave (seu navegador já aberto)

Como você já está com o Brave aberto no jogo, siga estas instruções:

## ✅ Método Mais Fácil (Recomendado)

1. **Execute o bot:**
   ```bash
   python bot.py
   ```

2. **Quando pedir para abrir o navegador:**
   - Aperte ENTER (o jogo já está aberto)

3. **Se perguntar qual navegador:**
   - Digite **2** (Brave)

4. **Pronto!** O bot vai abrir uma nova janela do Brave e começar

## 🔧 Método Avançado (Conectar ao Brave já aberto)

Se você quer que o bot use **exatamente a janela que você já tem aberta**:

### Passo 1: Fechar todos os Brave
```bash
# Feche TODAS as janelas do Brave
```

### Passo 2: Abrir Brave com debug
Abra o CMD ou PowerShell e execute:

```bash
"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222
```

**OU** se estiver em outro local:
```bash
"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222
```

### Passo 3: Navegar para o jogo
1. No Brave que abriu, vá para: https://play-pokechill.github.io
2. Faça login
3. Deixe aberto

### Passo 4: Executar o bot
```bash
python bot.py
```

Quando pedir, aperte ENTER. O bot detectará automaticamente o Brave!

## 💡 Dicas

- **Brave funciona igual ao Chrome** - usa o mesmo ChromeDriver
- **Não precisa instalar nada extra** - se o Selenium já funciona, o Brave também
- **Mantenha a janela visível** - assim você vê o que o bot está fazendo

## 🐛 Problemas?

### "Não encontrou o navegador"
- Verifique se o Brave está instalado em um dos caminhos padrão
- Se estiver em outro lugar, o bot vai pedir o caminho

### "ChromeDriver não compatível"
```bash
pip install --upgrade selenium
```

---

**Pode testar agora!** 🚀
