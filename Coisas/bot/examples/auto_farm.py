"""
Exemplo: Farmar automaticamente (reinicia sempre que a batalha termina)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pokechill_bot import create_bot
import time


def main():
    print("🎮 Exemplo: Auto-farm (reinicia sempre)\n")
    
    # Cria o bot
    bot = create_bot()
    
    try:
        print("⏳ Aguardando o jogo carregar...")
        time.sleep(5)
        
        print("\n" + "="*50)
        print("Bot configurado para:")
        print("  ✓ Reiniciar automaticamente ao perder")
        print("  ✓ Reiniciar automaticamente ao vencer")
        print("  → Farm infinito ativado!")
        print("="*50 + "\n")
        
        # Monitora e reinicia sempre (farm infinito)
        bot.monitor_battle(
            auto_restart_on_loss=True,  # Reinicia ao perder
            auto_restart_on_win=True    # Reinicia ao vencer
        )
        
    except KeyboardInterrupt:
        print("\n👋 Encerrando farm...")
    finally:
        bot.stop()


if __name__ == "__main__":
    main()
