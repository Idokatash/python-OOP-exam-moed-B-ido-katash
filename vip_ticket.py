from ticket import Ticket

class VIPTicket(Ticket):
    def calculate_price(self):
        if self.customer.customer_type != "VIP":
            raise ValueError("Customer must be VIP")

        discount = self.customer.customer_discount

        if discount is None:
            discount = 0

        return self.original_price - discount
