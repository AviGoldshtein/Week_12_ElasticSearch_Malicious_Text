import os
import pandas as pd


class DataLoader:
    def __init__(self):
        self.data = None
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(base_path, "data", "tweets_injected.csv")
        self.path = path

    def load_data(self) -> pd.DataFrame:
        if not self.data:
            self.data = pd.read_csv(self.path)
        return self.data

    def get_black_list(self):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(base_path, "data", "weapons.txt")
        with open(path, mode="r", encoding="utf-8") as black_list:
            return black_list.read().lower().split()

d = DataLoader()
print(d.load_data().head().to_string())