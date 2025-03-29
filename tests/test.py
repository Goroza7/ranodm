import setup_path 
from guessing_game import main
import random

def test_guessing_game(monkeypatch, capsys):
    # Force the random number to always be 42.
    monkeypatch.setattr(random,
                        'randint', lambda a, b: 42)

    # Simulate two user inputs: first
    # guess '50' (too high) then '42' (correct).
    inputs = iter(["50", "42"])
    monkeypatch.setattr("builtins.input",
                        lambda prompt="": next(inputs))

    # Run the game.
    main()

    # Capture the output.
    captured = capsys.readouterr().out

    # Check for expected outputs.
    assert "Too high!" in captured
    assert "Congratulations! You guessed it" in captured
