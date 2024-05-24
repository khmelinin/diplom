import datetime
from models import Client, Event, Service
from data_base2 import db_manager



def analyze_first_event_by_age():
    age = Client.tmpClient.get_age()

    if(age < 2):
        firstEvent = Event.Event()
        firstEvent.doctor_id = 1
        firstEvent.service_id = 1
        d = datetime.date.today() + datetime.timedelta(days=14)
        firstEvent.date_plan = d.strftime("%Y-%m-%d")

        patient_id = db_manager.find_patient_id(Client.tmpClient.name, Client.tmpClient.birthday)[0][0]
        db_manager.insert_event(firstEvent.doctor_id, patient_id, firstEvent.service_id, firstEvent.date_plan, '', -1)