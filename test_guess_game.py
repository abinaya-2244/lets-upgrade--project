from guess_game import check_guess


def test_low():
    assert check_guess(50, 30) == "Too Low"


def test_high():
    assert check_guess(50, 70) == "Too High"


def test_correct():
    assert check_guess(50, 50) == "Correct"
