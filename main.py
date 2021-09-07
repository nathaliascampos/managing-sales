import pandas as pd
import sys

def get_sales_dataframe(): 
    return pd.read_excel('./Sales.xlsx') 

def filter_sales_by_item(all_sales_df: pd.DataFrame, item_name: str):
    """ Filter data frame by item name 

    item_name (str): Sale Item Name
    """
    sales_item = all_sales_df[all_sales_df['Sale Item Name'] == item_name]

    return(sales_item)

def rank_sellers_by_item(item_name: str):
    all_sales_df = get_sales_dataframe()
    
    sales_item = filter_sales_by_item(all_sales_df, item_name)

    if(sales_item.empty): 
        print("Item name not found.")
        
        return "Item name not found."

    sellers_count = sales_item.groupby('Seller Name')['Seller Name'].count().reset_index(name = "Count")

    ranked = sellers_count.sort_values("Count", ascending = False)

    print(ranked)
    
    return ranked

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
