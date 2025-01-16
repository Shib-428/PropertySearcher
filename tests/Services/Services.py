class Services:
    def __init__(self, data: any) -> None:
        self.data = data

    def save(self) -> None:
        print(f"Saving data: {self.data}")

    def validate(self) -> bool:
        return True