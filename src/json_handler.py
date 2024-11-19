import pandas as pd

def handle(path: str):
    df = pd.read_csv(path, index_col='key', usecols=["key","en", "fr", "de", "sw", "ar"])
    translations_object = {}
    for key, row in df.iterrows():
        translations_object = build_translations_object(key, row['en'], translations_object)
        
    print(translations_object)    
    
def build_translations_object(aggregate_key: str, value: str, translations_object: dict) -> dict:
    keys = aggregate_key.split('.')
    print(keys)  
    for index, key in enumerate(reversed(keys)):
        print(key)
          
    return translations_object