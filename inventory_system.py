"""
Inventory Management System
Performs add, remove, load, save, and reporting of stock items.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a specified quantity of an item to the stock."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for item or quantity")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specified quantity of an item from stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning("Item '%s' not found in stock_data", item)


def get_qty(item):
    """Return the current quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.warning("Error loading inventory data from file '%s'", file)


def save_data(file="inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print all inventory items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items that are below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function demonstrating inventory system operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types handled safely
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("eval used")  # removed unsafe eval


if __name__ == "__main__":
    main()