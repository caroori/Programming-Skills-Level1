import time
import sys
import os


user_ = "admin"
pwd_ = "123"

counter = 0
login_attempts = 0

#option = 0

##################################     F U N C T I O N S            ######################
#dictiorany
doctors = {
   "juan": {"speciality": ["general medicine", "emergency care", "clinical analysis", "cardiology", "neurology", "nutrition", "physiotherapy", "traumatology", "internal medicine"],
             "morning": ["09:00", "10:00", "11:00"],
             "afternoon": ["17:00", "18:00", "19:00"]},
    "pablo": {"speciality": ["general medicine", "emergency care", "clinical analysis", "cardiology", "neurology", "nutrition", "physiotherapy", "traumatology", "internal medicine"],
              "morning": ["09:00", "10:00", "11:00"],
              "afternoon": ["17:00", "18:00", "19:00"]},
    "pedro": {"speciality": ["general medicine", "emergency care", "clinical analysis", "cardiology", "neurology", "nutrition", "physiotherapy", "traumatology", "internal medicine"],
              "morning": ["09:00", "10:00", "11:00"],
              "afternoon": ["17:00", "18:00", "19:00"]}
}

appointments = []


#login
def login():
    global login_attempts
    user = input("User: ")                 
    pwd = input("Password: ") 
    #check
    clean_console()
    if user == user_ and pwd == pwd_: 
        print("WELCOME - VALECIA HOSPITAL")
        login_attempts = 0
        return True
    else:
        print("Invalid user o password")
        login_attempts += 1
        if login_attempts >= 3:
            print("Too many failed login attempts")
            exit()
        return login()      ##while

def menu():
    print(" M E N U ")
    print("1. Medical shift")
    print("2. Log out")
    option = int(input("Select an option: "))
    clean_console()
    if option == 1:
        submenu()
    elif option == 2:
        login()
    else: 
        print("Invalid option")

def submenu():
    specialist = input("Please, enter the specialist (General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine): ").lower()
    doctor = input("Enter the doctor (Juan, Pablo, Pedro): ").lower()
    if error(specialist, doctor):
        shift = input("Enter your preferred time slot (morning or afternoon): ").lower()
        if shift == "morning":
            for slot in doctors[doctor]['morning']:
                print(slot)
            time_slot_m = input("Choose the time slot: ")
            if time_slot_m in doctors[doctor]['morning']:
                doctors[doctor]['morning'].remove(time_slot_m)
                appointments.append((doctor, specialist, time_slot_m))
                clean_console()
                print(f"Appointment with Dr. {doctor} at {time_slot_m}")
                print(" ")
            else:
                print("schedule not available") 
                print(" ")
        elif shift == "afternoon":
            for slot in doctors[doctor]['afternoon']:
                print(slot)
            time_slot_a = print("Choose the time slot: ")
            if time_slot_a in doctors[doctor]['afternoon']:
                doctors[doctor]['afternoon'].remove(time_slot_a)
                clean_console()
                print(f"Appointment with Dr. {doctor} at {time_slot_a}")
                print(" ")
            else:
                print("schedule not available") 
                print(" ")
    else:
        clean_console()
        print("Error (doctor or speciality)")

def error(specialist, doctor):
    if doctor not in doctors.keys():
        print("Avilable doctor")
        time.sleep(1.5)
        clean_console()
        return False
    elif specialist not in doctors[doctor]['speciality']:
        print("Available specialists")
        time.sleep(1.5)
        clean_console()
        return False
    return True




##Console
def clean_console():
    operative_sistems = os.name
    if operative_sistems == 'posix':  # Linux y macOS
        os.system('clear')
    elif operative_sistems == 'nt':   # Windows
        os.system('cls')
         
def main():
    if not login():
        return
    else:
        while True:
            menu()

##################################     E N D - - F U N C T I O N S  ######################
            

main()   
   
       