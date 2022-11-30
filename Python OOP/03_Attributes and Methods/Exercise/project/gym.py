from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    customers = List[Customer]
    trainers = List[Trainer]
    equipment = List[Equipment]
    plans = List[ExercisePlan]
    subscriptions = List[Subscription]

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

        self._customer_by_id = {}
        self._trainer_by_id = {}
        self._equipment_by_id = {}
        self._plan_by_id = {}
        self._subscription_by_id = {}

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
            self._customer_by_id[customer.id] = customer
        # – add the customer in the customer list, if the customer is not already in it

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
            self._trainer_by_id[trainer.id] = trainer
        # – add the trainer to the trainers list, if the trainer is not already in it

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
            self._equipment_by_id[equipment.id] = equipment
    # – add the equipment to the equipment list, if the equipment is not already in it

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)
            self._plan_by_id[plan.id] = plan
    # – add the plan to the plans list, if the plan is not already in it

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
            self._subscription_by_id[subscription.id] = subscription
    # – add the subscription in the subscriptions list, if the subscription is not already in it

    def subscription_info(self, subscription_id: int):
        sub = self._subscription_by_id[subscription_id]

        customer = self._customer_by_id[sub.customer_id]
        trainer = self._trainer_by_id[sub.trainer_id]
        exercise = self._plan_by_id[sub.exercise_id]

        equipment = self._equipment_by_id[plan.equipment_id]

        return "\n".join([
            repr(sub),
            repr(customer),
            repr(trainer),
            repr(equipment),
            repr(exercise),
        ])
    # – get the subscription, the customer and trainer to it, the plan to that trainer and the equipment to the plan. Then return their string representations each separated by a new line




# from project.customer import Customer
# from project.equipment import Equipment
# from project.exercise_plan import ExercisePlan
# from project.gym import Gym
# from project.subscription import Subscription
# from project.trainer import Trainer

# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
