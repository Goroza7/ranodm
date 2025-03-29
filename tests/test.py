# tests/test_game.py
import random
import sys
import os

# Add the directory containing guessing_game.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from guessing_game import main

# Add the repository root directory to sys.path
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


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
