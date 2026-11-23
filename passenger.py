class PassengerAccount:
    def __init__(self, name: str):
        self.name = name
        self.__wallet_balance: float = 0.0

@property
def wallet_balance(self) -> float:
    return self.__wallet_balance

def top_up_wallet(self, amount: float) -> None:
    if amount < 0:
        raise ValueError("Top-up amount cannot be negative. ")
    self.__wallet_balance += amount

def pay_for_ride(self, fare_amount: float) -> None:
    if fare_amount < 0:
        raise ValueError("Fare amount cannot be negative. ")
    if self.__wallet_balance < fare_amount:
        raise ValueError("Insufficient funds! Please top up. ")
    self.__wallet_balance -= fare_amount
    print(f"Remaining balance: {self.__wallet_balance}")
