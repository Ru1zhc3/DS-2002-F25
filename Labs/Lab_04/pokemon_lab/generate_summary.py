import os
import pandas as pd
import sys

def generate_summary(portfolio_file):
    if not os.path.exists(portfolio_file):
        print(f"Error: Portfolio file '{portfolio_file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)

    if df.empty:
        print("The portfolio is empty.")
        return
    
    total_value = df['card_market_value'].sum()

    index = df['card_market_value'].idxmax()
    most_valuable_card = df.loc[index]
    print("Portfolio Summary Report:")
    print(f"Total Portfolio Value: ${total_value:,.2f}")
    print(f"Most Valuable Card:")
    print(f"   - Name: {most_valuable_card['card_name']}")
    print(f"   - ID: {most_valuable_card['set_id']}-{most_valuable_card['card_number']}")
    print(f"   - Market Value: ${most_valuable_card['card_market_value']:,.2f}")
    print("-" * 40)

def main():
    generate_summary(portfolio_file="card_portfolio.csv")

def test():
    generate_summary(portfolio_file="card_portfolio_test.csv")

if __name__ == "__main__":
    test