# creates parent class
class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


# creates child class senior patient
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.80   # gets 20% discount

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


# crates child class phil health patient
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85   # gets 15% discount

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


# creates objects
regular = Patient("Juan Dela Cruz", 15000)
senior = SeniorPatient("Maria Santos", 15000)
philhealth = PhilHealthPatient("Pedro Reyes", 15000)

# outputs
print("Hospital Billing System")
print("-----------------------")

print("Patient Name:", regular.name)
regular.display_patient_type()
print("Original Bill: ₱15,000.00")
print("Final Bill: ₱15,000.00")
print()

print("Patient Name:", senior.name)
senior.display_patient_type()
print("Original Bill: ₱15,000.00")
print("Final Bill: ₱12,000.00")
print()

print("Patient Name:", philhealth.name)
philhealth.display_patient_type()
print("Original Bill: ₱15,000.00")
print("Final Bill: ₱12,750.00")
