class RentalPropertyCalculator:
    def __init__(self, purchase_price, loan_amount, annual_rental_income, operating_expenses, property_value_after_years):
        self.purchase_price = purchase_price
        self.loan_amount = loan_amount
        self.annual_rental_income = annual_rental_income
        self.operating_expenses = operating_expenses
        self.property_value_after_years = property_value_after_years

    def calculate_roi(self):
        down_payment = self.purchase_price - self.loan_amount
        net_cash_flow = self.annual_rental_income - self.operating_expenses
        total_cash_investment = down_payment + self.operating_expenses
        property_value_increase = self.property_value_after_years - self.purchase_price

        roi = (net_cash_flow + property_value_increase) / total_cash_investment * 100

        return roi

purchase_price = float(input("Enter the purchase price: "))
loan_amount = float(input("Enter the loan amount: "))
annual_rental_income = float(input("Enter the annual rental income: "))
operating_expenses = float(input("Enter the annual operating expenses: "))
property_value_after_years = float(input("Enter the property value after the specified number of years: "))

property_calculator = RentalPropertyCalculator(
    purchase_price, loan_amount, annual_rental_income, operating_expenses, property_value_after_years
)

roi = property_calculator.calculate_roi()

print(f"Return on Investment (ROI): {roi:.2f}%")
