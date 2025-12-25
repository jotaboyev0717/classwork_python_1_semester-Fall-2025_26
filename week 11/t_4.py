def withdraw_funds(account, amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Invalid amount")

    current_balance = account['balance']
    new_balance = current_balance - amount
    limit = account['limit']

    if new_balance < limit:
        raise ValueError("Overdraft limit exceeded")

    account['balance'] = new_balance

    if new_balance < 0:
        raise UserWarning("Overdraft used")


my_account = {'balance': 50.0, 'limit': -100.0}
attempts = [40, 60, 200]

for amount in attempts:
    print(f"\nAttempting to withdraw ${amount}...")
    try:
        withdraw_funds(my_account, amount)
    except UserWarning as w:
        print(f"Alert: {w} Balance is {my_account['balance']}")
        print("Transaction completed with warning.")
    except ValueError as e:
        print(f"Transaction Failed: {e}")
    else:
        print("Transaction successful.")
    finally:
        print(f"Current Balance: {my_account['balance']}")
