# 🚀 COMO USAR O BOT - ATUALIZADO

## ✅ Mudanças Recentes

1. **Delay de 1 minuto** - Após clicar em "Batalhar", o bot espera 1 minuto antes de começar a verificar o estado da batalha
2. **Verificações mais espaçadas** - Agora verifica a cada 3 segundos ao invés de 1 segundo (menos sobrecarga)
3. **Melhor detecção** - Mais seletores para detectar vitória/derrota
4. **Suporte a Brave** - Funciona com Chrome e Brave
5. **Logs melhores** - Mostra progresso da batalha

## 🎮 Uso Básico

```bash
python bot.py
```

1. Escolha o time (1-30) ou ENTER para time 1
2. Escolha navegador (Chrome ou Brave) ou use o já aberto
3. O bot vai:
   - Selecionar o time
   - Clicar em "Batalhar"
   - **Esperar 1 minuto** ⏳
   - Começar a monitorar a cada 3 segundos
   - Atacar a cada 6 segundos
   - Detectar vitória/derrota
   - Recomeçar automaticamente

## ⚙️ Configurações

### Tempos Importantes:
- **Delay inicial**: 60 segundos (1 minuto) após clicar em batalhar
- **Verificação**: A cada 3 segundos
- **Ataque**: A cada 6 segundos (2 verificações)
- **Log**: A cada 30 segundos mostra tempo decorrido

### Estatísticas:
- Mostra a cada **5 batalhas** (antes eram 10)

## 🔍 Descobrir Seletores Corretos

Se o bot não estiver funcionando, use:

```bash
python Test.py
```

Isso vai mostrar:
- Todos os botões disponíveis
- IDs dos times (preview1 a preview30)
- Botões de batalha
- E muito mais

Anote os IDs e atualize o `config.py`

## 🐛 Resolução de Problemas

### Bot não clica em "Batalhar"
1. Execute `python Test.py`
2. Vá para a tela do jogo onde tem o botão "Batalhar"
3. Veja qual o ID do botão
4. Adicione em `bot.py` na função `start_battle()`

### Bot não detecta vitória/derrota
1. Execute `python Test.py`
2. Entre em uma batalha
3. Espere terminar (ganhar ou perder)
4. Veja quais elementos aparecem na tela
5. Adicione em `bot.py` nas funções `check_won()` e `check_lost()`

### Bot não seleciona o time
1. Execute `python Test.py`
2. Vá para a tela de seleção de times
3. Veja o ID dos botões de time (ex: preview1, preview2, etc)
4. Ajuste em `bot.py` na função `select_team()`

## 💡 Dicas

1. **Mantenha visível** - Deixe a janela do navegador visível para monitorar
2. **Use Test.py** - Sempre que algo não funcionar, use o Test.py primeiro
3. **Aguarde o delay** - O bot espera 1 minuto após iniciar batalha propositalmente
4. **Veja os logs** - O bot mostra tudo que está fazendo

## 📊 Exemplo de Log

```
🎯 Selecionando time 2...
✅ Time 2 selecionado!
⚔️ Iniciando batalha...
✅ Batalha iniciada!
⏳ Aguardando 1 minuto para a batalha começar...
🎮 Começando monitoramento da batalha...
🎮 Em batalha...
💥 Atacou!
⏱️ Monitorando... (30 segundos)
💥 Atacou!
⏱️ Monitorando... (60 segundos)
✅ Ganhou a batalha!

🎉 Processando vitória...
```

---

**Boa sorte! 🎮**
