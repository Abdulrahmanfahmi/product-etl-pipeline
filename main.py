 
import sys
sys.path.insert(0, ".")
 
from src.extract import extract
from src.transform import transform
from src.load import load
 
 
def main():
    print()
    print("ETL PIPELINE - Produktdata")
    print()
 
    
    df_raw = extract("data/products_100.csv")
 
    
    df_clean, stats = transform(df_raw)
 
    
    load(df_clean, stats)
 
    print("PIPELINE KLAR")
    print()
 
 
if __name__ == "__main__":
    main()