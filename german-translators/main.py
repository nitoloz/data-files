import requests
from request_contants import data, headers, states, url
from bs_scrapper import scrap_data_by_id
from export import export_to_csv
import pandas as pd
from multiprocessing import Pool


all_translators_list = []
result = []
persons = []

def get_translators(state_code, display_start, display_length):
    data['Bundesland'] = state_code
    data['iDisplayStart'] = display_start
    data['iDisplayLength'] = display_length
    data[
        'mFormValsJson'] = f'{{"Sprache1":"","Sprache2":"","Bundesland":"{state_code}","Plz":"","Ort":"","IstDolmetscher":"false","IstUebersetzer":"false","Nachname":"","Behoerde":"0"}}'
    return requests.post(url, headers=headers, data=data).json()


def get_state_translators(state_code):
    print(f"Start: {state_code}")

    state_translators = []
    display_start = 0
    display_length = 1000
    response = get_translators(state_code, display_start, display_length)

    state_translators.extend(response["aaData"])
    while display_start + display_length < response["iTotalRecords"]:
        display_start += display_length
        response = get_translators(state_code, display_start, display_length)
        state_translators.extend(response["aaData"])

    print(f"Completed: {state_code} with {len(state_translators)} translators")
    return state_translators

def get_person_details(person):
    person_id = person['PersonId']
    print(f"Processing: {person_id}")
    return scrap_data_by_id(person_id)

if __name__ == "__main__":
    with Pool(16) as pool:
        responses = pool.map(get_state_translators, states)
    for response in responses:
        all_translators_list.extend(response)

if __name__ == "__main__":
    with Pool(16) as pool:
        persons = pool.map(get_person_details, all_translators_list)

    export_to_csv(persons, "full_output.csv")
