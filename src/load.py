import time
import pandas as pd


def load(df: pd.DataFrame, stats: dict, output_path: str = "data/results.csv") -> None:
    """
    Tar emot bearbetad data och statistik.
    1. Strömmar topp 5 dyraste produkter en i taget (simulerad Kafka-ström)
    2. Sparar rensad data till en ny CSV-fil
    """

    
    print("=" * 50)
    print("[LOAD] Startar ström – topp 5 dyraste produkter")
    print("=" * 50)
    print()

    products = stats["top5_expensive"]

    for rank, product in enumerate(products, start=1):
        print(f"  [{rank}/5] Skickar: {product['name']}")
        print(f"         Kategori : {product['category']}")
        print(f"         Pris     : {product['price']} kr")
        print(f"         Antal    : {product['quantity']} st")
        print()
        time.sleep(1.0)  

    print("  Ström klar – alla 5 produkter skickade.")
    print()

    
    print("=" * 50)
    print(f"[LOAD] Sparar resultat till: {output_path}")
    print("=" * 50)

    df.to_csv(output_path, index=False)
    print(f"  {len(df)} rader sparade till '{output_path}'")
    print()



if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    from src.extract import extract
    from src.transform import transform

    df_raw = extract("data/products_100.csv")
    df_clean, stats = transform(df_raw)
    load(df_clean, stats)