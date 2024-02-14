import requests
from bs4 import BeautifulSoup

def scrape_webpage(person_id):
    url = f"https://www.justiz-dolmetscher.de/Recherche/en/Person/Details/{person_id}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        card_divs = soup.find_all('div', class_='card')[:4]  # Take only the first 4 "card" divs

        person_data_tuples = []
        for card_div in card_divs:
            form_group_divs = card_div.find_all('div', class_='form-group')
            for form_group_div in form_group_divs:
                label_element = form_group_div.find('label')
                span_element = form_group_div.find('span')

                if label_element and span_element:
                    label_content = label_element.get_text(strip=True)
                    span_content = span_element.get_text(strip=True)
                    person_data_tuples.append((label_content, span_content))
        return person_data_tuples
    else:
        print(f"Error: Unable to fetch data for PersonID {person_id}")
        return {}


def scrap_data_by_id(person_id):
    person_data_tuples = scrape_webpage(person_id)
    person = {}
    person["ID"] = person_id
    if person_data_tuples:
        person["State"] = person_data_tuples[0][1]
        person["Government_agency"] = person_data_tuples[1][1]
        person["File_number"] = person_data_tuples[2][1]
        person["Name"] = person_data_tuples[3][1]
        person["Address"] = person_data_tuples[4][1]
        person["Email"] = person_data_tuples[5][1]
        person["Internet_address"] = person_data_tuples[6][1]
        person["Mobile_phone"] = person_data_tuples[7][1]
        person["Phone"] = person_data_tuples[8][1]
        person["Fax"] = person_data_tuples[9][1]
        person["Home_country"] = person_data_tuples[10][1]
        person["Company"] = person_data_tuples[11][1]
        person["Company_address"] = person_data_tuples[12][1]
        person["Company_email"] = person_data_tuples[13][1]
        person["Company_mobile_phone"] = person_data_tuples[14][1]
        person["Company_phone"] = person_data_tuples[15][1]
        person["Company_fax"] = person_data_tuples[16][1]
        person["Job_description"] = person_data_tuples[17][1]
        person["Remarks"] = person_data_tuples[18][1]
        person["eBO_address"] = person_data_tuples[19][1]
        person["Service_hours"] = person_data_tuples[20][1]
        person["Industry"] = person_data_tuples[21][1]
    return person