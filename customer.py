class Customer:
    used_ids = set()

    def __init__(self, customer_id, first_name, last_name,
                 email, delivery_address, customer_type,
                 customer_discount=None):

        if customer_id in Customer.used_ids:
            raise ValueError("Customer ID already exists")

        if customer_type not in ("REGULAR", "VIP"):
            raise ValueError("Invalid customer type")

        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.voucher = None

        Customer.used_ids.add(customer_id)

    def eat_food(self, show):
        if self.voucher is None:
            raise ValueError("Customer has no food voucher")

        if self.customer_id not in show.food_vouchers:
            raise ValueError("No voucher for this show")

        self.voucher.eat()
        show.take_food_voucher(self)


