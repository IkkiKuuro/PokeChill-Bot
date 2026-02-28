"""
Exemplo: Ações customizadas baseadas em eventos
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pokechill_bot import create_bot
import time


def custom_monitor(bot):
    """Monitor customizado com lógica própria"""
    print("👀 Monitor customizado iniciado...")
    
    battles_won = 0
    battles_lost = 0
    
    try:
        while True:
            # Obtém estado do jogo
            state = bot.get_game_state()
            
            # Verifica se venceu
            if bot.is_battle_won():
                battles_won += 1
                print(f"🏆 Vitória #{battles_won}!")
                
                # Salva o jogo a cada 5 vitórias
                if battles_won % 5 == 0:
                    bot.save_game()
                    print("💾 Jogo salvo automaticamente!")
                
                time.sleep(2)
                bot.restart_battle()
                time.sleep(2)
            
            # Verifica se perdeu
            elif bot.is_battle_lost():
                battles_lost += 1
                print(f"💀 Derrota #{battles_lost}")
                
                # Se perder 3 vezes seguidas, para o bot
                if battles_lost >= 3:
                    print("⚠️ 3 derrotas consecutivas. Parando bot...")
                    break
                
                time.sleep(2)
                bot.restart_battle()
                time.sleep(2)
            
            # Exibe estatísticas a cada 10 segundos
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\n⏹️ Monitor interrompido")
    
    print(f"\n📊 Estatísticas finais:")
    print(f"  Vitórias: {battles_won}")
    print(f"  Derrotas: {battles_lost}")


def main():
    print("🎮 Exemplo: Ações customizadas\n")
    
    bot = create_bot()
    
    try:
        print("⏳ Aguardando o jogo carregar...")
        time.sleep(5)
        
        print("\n" + "="*50)
        print("Bot com ações customizadas:")
        print("  ✓ Salva a cada 5 vitórias")
        print("  ✓ Para após 3 derrotas consecutivas")
        print("  ✓ Mostra estatísticas")
        print("="*50 + "\n")
        
        # Usa o monitor customizado
        custom_monitor(bot)
        
    except KeyboardInterrupt:
        print("\n👋 Encerrando...")
    finally:
        bot.stop()


if __name__ == "__main__":
    main()
