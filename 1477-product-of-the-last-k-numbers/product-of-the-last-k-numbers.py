class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = [1]
        self.last_zero_idx = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]
            self.last_zero_idx = len(self.prefix_product) - 1
        else:
            self.prefix_product.append(num * self.prefix_product[-1])

    def getProduct(self, k: int) -> int:
        size = len(self.prefix_product)
        if size - k - 1 < self.last_zero_idx:
            return 0
        return self.prefix_product[-1] // self.prefix_product[size - k - 1]