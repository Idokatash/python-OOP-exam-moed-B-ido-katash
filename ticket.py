from abc import ABC, abstractmethod


class Ticket(ABC):
    used_ids = set()

    def __init__(self, ticket_id, show_name, show_date,
                 row_number, seat_number, customer, ticket_price):

        if ticket_id in Ticket.used_ids:
            raise ValueError("Ticket ID already exists")

        self.ticket_id = ticket_id
        self.show_name = show_name
        self.show_date = show_date
        self.row_number = row_number
        self.seat_number = seat_number
        self.customer = customer
        self.original_price = ticket_price

        self.ticket_price = self.calculate_price()

        Ticket.used_ids.add(ticket_id)

    @abstractmethod
    def calculate_price(self):
        pass

