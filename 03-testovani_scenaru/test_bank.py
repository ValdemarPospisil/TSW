def test_initial_balance(account):
    expected = 0
    outcome = account.get_balance()
    assert outcome == expected


def test_deposit(account):
    deposit_amount, expected_balance = 100, 100
    account.deposit(deposit_amount)
    outcome = account.get_balance()
    assert outcome == expected_balance


def test_withdraw_success(account):
    deposit_amount = 200
    withdraw_amount = 100
    expected_balance = 100
    expected_state = True

    account.deposit(deposit_amount)
    outcome_state = account.withdraw(withdraw_amount)
    outcome_balance = account.get_balance()

    assert outcome_state == expected_state
    assert outcome_balance == expected_balance


def test_withdraw_fail(account):
    withdraw_amount = 50
    expected_state = False
    expected_balance = 0

    outcome_state = account.withdraw(withdraw_amount)
    outcome_balance = account.get_balance()

    assert outcome_state == expected_state
    assert outcome_balance == expected_balance
