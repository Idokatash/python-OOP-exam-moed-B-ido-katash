class Show:
    used_ids = set()

    def __init__(self, show_id, show_name, show_date):
        if show_id in Show.used_ids:
            raise ValueError("Show ID already exists")

        self.show_id = show_id
        self.show_name = show_name
        self.show_date = show_date

        self.tickets = []
        self.food_vouchers = {}
        self.voucher_history = set()

        Show.used_ids.add(show_id)

    def add_ticket(self, ticket):
        if ticket.show_name != self.show_name:
            raise ValueError("Ticket belongs to another show")

        if ticket.show_date != self.show_date:
            raise ValueError("Ticket date does not match show")

        if ticket in self.tickets:
            raise ValueError("Ticket already added")

        self.tickets.append(ticket)

    def remove_ticket(self, ticket):
        self.tickets.remove(ticket)

    def calculate_revenue(self):
        total = 0

        for ticket in self.tickets:
            total += ticket.ticket_price

        return total

    def calculate_total_discount(self):
        total_discount = 0

        for ticket in self.tickets:
            total_discount += (
                ticket.original_price - ticket.ticket_price
            )

        return total_discount

    def give_food_voucher(self, customer, food_voucher):
        if customer.customer_id in self.voucher_history:
            raise ValueError(
                "Customer already received a voucher for this show"
            )

        if not callable(getattr(food_voucher, "eat", None)):
            raise TypeError("Voucher must have an eat() method")

        if not callable(getattr(food_voucher, "get_name", None)):
            raise TypeError("Voucher must have a get_name() method")

        if customer.voucher is not None:
            raise ValueError("Customer already has a voucher")

        customer.voucher = food_voucher

        self.food_vouchers[customer.customer_id] = (
            food_voucher.get_name()
        )

        self.voucher_history.add(customer.customer_id)

    def take_food_voucher(self, customer):
        if customer.customer_id not in self.food_vouchers:
            raise ValueError("Customer has no voucher for this show")

        customer.voucher = None
        del self.food_vouchers[customer.customer_id]
