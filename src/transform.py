import pandas as pd


def transform(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Tar emot en DataFrame, städar den och beräknar statistik.

    Returnerar:
        df_clean  – bearbetad DataFrame
        stats     – dict med statistiska resultat
    """
    print("=" * 50)
    print("[TRANSFORM] Bearbetar data...")
    print("=" * 50)

    
    antal_innan = len(df)
    df = df.dropna()                      
    df = df[df["price"] > 0]              
    df = df[df["quantity"] >= 0]          
    df["name"] = df["name"].str.strip()   
    df["category"] = df["category"].str.strip()
    antal_efter = len(df)

    print(f"  Rader innan städning : {antal_innan}")
    print(f"  Rader efter städning : {antal_efter}")
    print(f"  Borttagna rader      : {antal_innan - antal_efter}")
    print()

    
    df["total_value"] = df["price"] * df["quantity"]  

  
    stats = {
        "total_products": len(df),
        "avg_price": round(df["price"].mean(), 2),
        "max_price": round(df["price"].max(), 2),
        "min_price": round(df["price"].min(), 2),
        "total_inventory_value": round(df["total_value"].sum(), 2),
        "top5_expensive": (
            df.nlargest(5, "price")[["id", "name", "category", "price", "quantity"]]
            .to_dict(orient="records")
        ),
        "category_summary": (
            df.groupby("category")
            .agg(
                antal_produkter=("id", "count"),
                snitt_pris=("price", lambda x: round(x.mean(), 2)),
                totalt_lagervarde=("total_value", lambda x: round(x.sum(), 2)),
            )
            .reset_index()
            .to_dict(orient="records")
        ),
    }

    print(f"  Snittpris            : {stats['avg_price']} kr")
    print(f"  Dyraste produkt      : {stats['max_price']} kr")
    print(f"  Billigaste produkt   : {stats['min_price']} kr")
    print(f"  Totalt lagervärde    : {stats['total_inventory_value']} kr")
    print()
    print("  Kategoriöversikt:")
    for row in stats["category_summary"]:
        print(
            f"    {row['category']:<15}"
            f"  {row['antal_produkter']} produkter"
            f"  |  snitt {row['snitt_pris']} kr"
        )
    print()

    return df, stats


if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    from src.extract import extract

    df_raw = extract("data/products_100.csv")
    df_clean, stats = transform(df_raw)