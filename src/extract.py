import pandas as pd


def extract(filepath: str) -> pd.DataFrame:
    """
    Läser in CSV-filen och returnerar en pandas DataFrame.
    Skriver ut en förhandsgranskning av datan.
    """
    print("=" * 50)
    print("[EXTRACT] Läser in data från:", filepath)
    print("=" * 50)

    df = pd.read_csv(filepath)

    print(f"  Antal rader    : {len(df)}")
    print(f"  Antal kolumner : {len(df.columns)}")
    print(f"  Kolumner       : {list(df.columns)}")
    print()
    print(df.head())
    print()

    return df


if __name__ == "__main__":
    df = extract("data/products_100.csv")