from logic_utils import check_guess


# --- check_guess: basic outcomes ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- check_guess: messages ---

def test_win_message():
    outcome, message = check_guess(7, 7)
    assert "Correct" in message or "🎉" in message

def test_too_high_message():
    outcome, message = check_guess(99, 1)
    assert "LOWER" in message or "lower" in message.lower()

def test_too_low_message():
    outcome, message = check_guess(1, 99)
    assert "HIGHER" in message or "higher" in message.lower()


# --- check_guess: boundary values ---

def test_guess_equals_secret_at_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_guess_equals_secret_at_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"

def test_guess_one_below_secret():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"

def test_guess_one_above_secret():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"


# --- check_guess: string secret (the even-attempt bug in app.py) ---

def test_win_when_secret_is_string():
    # Reproduces the app.py bug: secret cast to str on even attempts
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

def test_too_high_when_secret_is_string():
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"

def test_too_low_when_secret_is_string():
    outcome, _ = check_guess(40, "50")
    assert outcome == "Too Low"
