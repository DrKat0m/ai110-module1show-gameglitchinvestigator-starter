from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "🎉" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_score_penalty():
    # Guessing wrong should subtract 2 points
    initial_score = 100
    new_score = update_score(initial_score, "Too High", 1, "Normal")
    assert new_score == 98

def test_parse_invalid_input():
    # Non-numeric input should be caught
    from logic_utils import parse_guess
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert val is None
    assert "not a valid number" in err

def test_parse_empty_input():
    # Empty input should be caught
    from logic_utils import parse_guess
    ok, val, err = parse_guess("")
    assert ok is False
    assert "Enter a guess" in err
