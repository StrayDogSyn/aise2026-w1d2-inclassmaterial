from typing import List, Dict, Set

def in_stock_names(cart: List[Dict]) -> List[str]:
    """
    Return the list of item names that are in stock and have qty > 0.
    Must use a single list comprehension.
    """
    return [item["name"] for item in cart if item["in_stock"] and item["qty"] > 0]

def totals_over(cart: List[Dict], min_total: float) -> List[str]:
    """
    Return the list of product names for in-stock items whose total value (price*qty) >= min_total.
    Must use a single list comprehension.
    """
    return [item["name"] for item in cart if item["in_stock"] and (item["price"] * item["qty"]) >= min_total]

if __name__ == "__main__":
    cart = [
        {"name": "Apples", "price": 1.50, "qty": 4, "in_stock": True,  "category": "grocery"},
        {"name": "USB Cable", "price": 7.99, "qty": 0, "in_stock": False, "category": "electronics"},
        {"name": "Coffee", "price": 12.00, "qty": 2, "in_stock": True,  "category": "grocery"},
        {"name": "Mug", "price": 8.50, "qty": 1, "in_stock": True,  "category": "home"},
    ]

    print(in_stock_names(cart))
    print(totals_over(cart, 10))
