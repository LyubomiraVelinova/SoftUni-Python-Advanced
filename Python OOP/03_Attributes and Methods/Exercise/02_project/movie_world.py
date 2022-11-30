from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    name: str
    customer: List[Customer]
    dvds: List[DVD]

    # _DVD_CAPACITY = 15
    # _CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []
        self.customer_ids = {}
        self.dvd_ids = {}

    @staticmethod
    def dvd_capacity():
        dvd_capacity = 15
        return dvd_capacity

    @staticmethod
    def customer_capacity():
        customer_capacity = 10
        return customer_capacity

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
            self.customer_ids[customer.id] = customer

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
            self.dvd_ids[dvd.id] = dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = self.dvd_ids.get(dvd_id)
        customer = self.customer_ids.get(customer_id)

        if customer.has_dvd(dvd):
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.rent()
        customer.add_dvd(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = self.dvd_ids.get(dvd_id)
        customer = self.customer_ids.get(customer_id)
        if customer.has_dvd(dvd):
            customer.remove_dvd(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers = list(map(str, self.customers))
        dvds = list(map(str, self.dvds))

        return "\n".join(customers + dvds)
