'''
3. Mastering Tuple Packing and Unpacking in Python

Task 1: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Write a function to iterate over the list of orders. Unpack each tuple in the list and format the details for display.

'''

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]


for order in orders:
    customer, item, quantity = order
    print(f"Customer name: {customer}, Item Ordered: {item}, Quantity: {quantity}")

