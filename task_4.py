class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None and self.rest_days is not None:
            return (7 - self.rest_days) * 8
        return self.hours

    def get_email(self):
        if self.email is None:
            return f"{self.name}@email.com"
        return self.email

    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        hours = self.get_hours()
        if hours is None:
            return None
        return hours * self.hourly_payment

