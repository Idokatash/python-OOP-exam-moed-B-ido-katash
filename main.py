from customer import Customer
from show import Show
from regular_ticket import RegularTicket
from vip_ticket import VIPTicket
from food_voucher import PizzaVoucher, SushiVoucher


def check_error(description, func, *args):
    try:
        func(*args)
        print(description, "- FAILED")
    except ValueError as error:
        print(description, "- PASSED:", error)


def main():
    regular = Customer(1, "Dan", "Cohen", "dan@gmail.com",
                       "Tel Aviv", "REGULAR")
    vip = Customer(2, "Noa", "Levi", "noa@gmail.com",
                   "Haifa", "VIP", 20)

    show = Show(1, "Omer Adam", "2026-12-20")

    t1 = RegularTicket(101, "Omer Adam", "2026-12-20",
                       5, 10, regular, 200)
    t2 = VIPTicket(102, "Omer Adam", "2026-12-20",
                   1, 2, vip, 300)


    show.add_ticket(t1)
    show.add_ticket(t2)

    print("Revenue:", show.calculate_revenue())
    print("Discount:", show.calculate_total_discount())

    show.give_food_voucher(regular, PizzaVoucher())
    show.give_food_voucher(vip, SushiVoucher())
    print("Vouchers:", show.food_vouchers)

    regular.eat_food(show)
    print("After eating:", show.food_vouchers)

    # Error scenarios
    check_error("Duplicate customer", Customer, 1, "Test", "User",
                "test@gmail.com", "Tel Aviv", "REGULAR")

    check_error("Duplicate ticket", RegularTicket, 101,
                "Omer Adam", "2026-12-20", 3, 5, regular, 200)

    check_error("Regular buying VIP", VIPTicket, 103,
                "Omer Adam", "2026-12-20", 1, 3, regular, 300)

    check_error("Second voucher", show.give_food_voucher,
                regular, PizzaVoucher())

    check_error("Duplicate show", Show, 1, "Other", "2026-12-21")

    wrong = RegularTicket(104, "Other", "2026-12-21",
                          3, 4, regular, 150)
    check_error("Wrong show", show.add_ticket, wrong)

    # Remove ticket
    show.remove_ticket(t1)
    print("Revenue after removal:", show.calculate_revenue())

    # Return voucher
    show.take_food_voucher(vip)
    print("Vouchers after return:", show.food_vouchers)

    check_error("Second voucher after return",
                show.give_food_voucher, vip, SushiVoucher())

    # VIP without discount
    vip2 = Customer(3, "Avi", "Levi", "avi@gmail.com",
                    "Jerusalem", "VIP")
    t3 = VIPTicket(105, "Omer Adam", "2026-12-20",
                   2, 5, vip2, 300)
    print("VIP without discount:", t3.ticket_price)

    check_error("Eat without voucher", vip2.eat_food, show)

    # Custom voucher (duck typing)
    class BurgerVoucher:
        def eat(self):
            print("Here is your food, enjoy!")

        def get_name(self):
            return "Burger Voucher"

    show.give_food_voucher(vip2, BurgerVoucher())
    vip2.eat_food(show)
    print("Vouchers after custom voucher:", show.food_vouchers)


if __name__ == "__main__":
    main()
