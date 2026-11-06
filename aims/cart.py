MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)
    
    def total_cost_with_discount(self, discount_percent):
        """
        Tính tổng tiền sau khi áp dụng phần trăm giảm giá.
        discount_percent: Số nguyên hoặc số thực từ 0 đến 100.
        """
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        
        total = self.total_cost()
        return total * (1 - discount_percent / 100.0)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("***********************CART***********************")
        print("Ordered Items:")
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. DVD - {item.title} - {item.category} - {item.director} - {item.length}: {item.cost}$")
        print(f"Total cost: {self.total_cost():.2f}$")
        print("***************************************************")