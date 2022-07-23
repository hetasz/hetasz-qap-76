from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_correctly(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 9, 3) == 6

    def test_adding_correctly(self):
        assert self.calc.adding(self, 3, 3) == 6
