import requests
import pandas as pd

response = requests.get('https://data.police.uk/api/stops-force?force=avon-and-somerset')

police_data = response.json()

ageRange = [data['age_range'] for data in police_data]


outcome = [data['outcome'] for data in police_data]

involved_person = [data['involved_person'] for data in police_data]

selfDefinedEthnicity = [data['self_defined_ethnicity'] for data in police_data]

gender = [data['gender'] for data in police_data]

legislation = [data['legislation'] for data in police_data]

outcome_of_search = [data['outcome_linked_to_object_of_search'] for data in police_data]

date_of_stop = [data['datetime'] for data in police_data]

removal_of_inner_clothing = [data['removal_of_more_than_outer_clothing'] for data in police_data]

outcomObject = [data['outcome_object'] for data in police_data]
outcomeObjectID = [newData['id'] for newData in outcomObject]
newOutcomeName = [newData['name'] for newData in outcomObject]

OfficerDefinedEthnicity = [data['officer_defined_ethnicity'] for data in police_data]


type = [data['type'] for data in police_data]

object_of_search = [data['object_of_search'] for data in police_data]


# convert the lists into dictionary

policeReports = {
    'Outcome' : outcome,
    'Involve Person' : involved_person,
    'Self Defined Ethnicity' : selfDefinedEthnicity,
    'Gender' : gender,
    'Legislation' : legislation,
    'Outcome of Search' : outcome_of_search,
    'Date of Stop' : date_of_stop,
    'Removal of More than outer clothing' : removal_of_inner_clothing,
    'Outcome Object ID': outcomeObjectID,
    'Outcome Object Name': newOutcomeName,
    'Officer Defined Ethnicity' : OfficerDefinedEthnicity,
    'Type' : type,
    'Object of Search' : object_of_search
}


myPoliceReport = pd.DataFrame(policeReports)

print(myPoliceReport.head(10))

myPoliceReport.to_csv('police_stop_search', header=False, index=False)
