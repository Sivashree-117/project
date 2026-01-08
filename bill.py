def calculate_bill(units):
    # Initialize charges
    first_charge = second_charge = remaining_charge = 0

    # First 100 units → ₹2/unit
    if units > 0:
        first_units = min(units, 100)
        first_charge = first_units * 2