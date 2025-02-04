import json
from sqlalchemy.orm import Session
from model import engine, Well

with open('output.json', 'r') as json_file:
    data = json.load(json_file)


def insert_data():
    with Session(engine) as session:
        session.query(Well).delete() #(found a bug used this for avoiding repeated insertion of same data)
        for record in data:
            well = Well(
                api_well_number=record.get('API WELL  NUMBER'),
                production_year=record.get('Production Year'),
                quarter=record.get('QUARTER 1,2,3,4'),
                owner_name=record.get('OWNER NAME'),
                county=record.get('COUNTY'),
                township=record.get('TOWNSHIP'),
                well_name=record.get('WELL NAME'),
                well_number=record.get('WELL NUMBER'),
                oil=record.get('OIL'),
                gas=record.get('GAS'),
                brine=record.get('BRINE'),
                days=record.get('DAYS')
            )
            session.add(well)
        session.commit()

if __name__ == "__main__":
    insert_data()
    print("Data has been inserted into the database.")
