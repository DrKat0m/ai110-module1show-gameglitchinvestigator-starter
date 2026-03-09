"""
Logic utilities for the Number Guessing Game.
# FIX: Moved core logic from app.py to logic_utils.py using Copilot Agent mode.
"""

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 250
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        # Handle cases where someone might enter "5.0"
        value = int(float(raw))
        return True, value, None
    except (ValueError, TypeError):
        return False, None, "That is not a valid number."


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int, difficulty: str):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # Bonus for fewer attempts
        points = 100 - (attempt_number * 10)
        return current_score + max(points, 20)

    if outcome in ["Too High", "Too Low"]:
        return current_score - 2
    
    return current_score
