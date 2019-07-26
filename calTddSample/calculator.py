class Calculator:
    
    def plus(self, x, y):
        if y == 0:
            return x

        return self.plus(x + 1, y - 1)

    def minus(self, x, y):
        if y == 0:
            return x
        
        return self.minus(x - 1, y - 1)

    def mul(self, x, y):
        result = 0
        for i in range(y):
            result = self.plus(result, x)

        return result

    def divide(self, x, y):
        count = 0
        limit = x

        while True:
            limit = self.minus(limit, y)
            
            if limit <= 0:
                break

            count += 1

        return count