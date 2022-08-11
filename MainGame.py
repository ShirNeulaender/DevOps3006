from Live import load_game, welcome
from GuessGame import play_guess
from MemoryGame import play_mem
from CurrencyRouletteGame import play

print(welcome("Guy"))
load_game()
play_guess()
play_mem()
play()
