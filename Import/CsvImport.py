import csv
import requests
from decimal import Decimal
from flask import json

from Webservice.DbModels import Coating


def import_csv(filename, webservice_url):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            if reader.line_num == 1:
                continue  # This row contains field names -> do nothing
            else:
                coating = Coating(name=row[0], text_short=row[1], article_id=row[2], order_id=row[3], supplier=row[4],
                                  photo=row[5], sweight=parse_sweight(row[6]))
                data = coating.to_dict()
                response = requests.post(url=webservice_url, json=data,
                                         headers={'Content-Type': 'application/json'})
                print(response.status_code)


def parse_sweight(sweight_field):
    """Parses the sweigt csv field into a json serialized decimal. If the field contains an empty string it'll be 0"""
    if sweight_field == '':
        sweight_field = '0'
    parseable_string = sweight_field.replace(',', '.')
    return json.dumps(Decimal(parseable_string))


import_csv('coatings.CSV', 'http://127.0.0.1:5000/api/v1/coating')
