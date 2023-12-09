doctors = {}

while True:
    patient_name = input("Please enter your full name (or 'quit' to exit): ")
    if patient_name == "quit":
        break

    doctor_name = input("Which doctor will you be seeing? ")

    if doctor_name in doctors:
        doctors[doctor_name].append(patient_name)
    else:
        doctors[doctor_name] = [patient_name]

    position = len(doctors[doctor_name])
    print("You are number", position, "in the queue for", doctor_name)

    wait_time = position * 10
    print("The approximate wait time is", wait_time, "minutes")

    num_patients = len(doctors[doctor_name])
    print("There are", num_patients, "patients in the queue for", doctor_name)