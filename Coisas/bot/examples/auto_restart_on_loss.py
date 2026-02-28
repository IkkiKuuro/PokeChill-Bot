"""
Exemplo: Reiniciar automaticamente ao perder a batalha
"""

import sys
import os

# Adiciona o diretório pai ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pokechill_bot import create_bot
import time


def main():
    print("🎮 Exemplo: Auto-restart ao perder\n")
    
    # Cria o bot (você pode passar a URL do jogo online aqui)
    bot = create_bot()
    
    try:
        # Aguarda o jogo carregar
        print("⏳ Aguardando o jogo carregar...")
        time.sleep(5)
        
        print("\n" + "="*50)
        print("Bot configurado para:")
        print("  ✓ Reiniciar automaticamente ao perder")
        print("  ✗ Continuar ao vencer")
        print("="*50 + "\n")
        
        # Monitora e reinicia ao perder
        bot.monitor_battle(
            auto_restart_on_loss=True,  # Reinicia ao perder
            auto_restart_on_win=False   # Não reinicia ao vencer
        )
        
    except KeyboardInterrupt:
        print("\n👋 Encerrando...")
    finally:
        bot.stop()


if __name__ == "__main__":
    main()
