class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f'유한체 {num} 는 0 보다 커야하고 {prime-1} 보다 작아야 합니다'
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f'FieldElement_{self.prime}_value: {self.num}'

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')

        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')

        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')

        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')

        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return self.__class__(num, self.prime)

    def __rmul__(self, coefficient):
        # 유한체 상에서 오른쪽 곱의 값이 객체인 경우 - ECC 를 구현하기 위해서 point, 유한체 에서 필요
        num = (self.num * coefficient) % self.prime
        return self.__class__(num=num, prime=self.prime)