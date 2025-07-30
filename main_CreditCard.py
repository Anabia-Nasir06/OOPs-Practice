from CreditCard import CreditCard

card = CreditCard('John Doe', 'Bank of Python', '1234 5678 9012 3456', 5000)
card.charge(100)
card.make_payment(50)
print(card.get_balance())
