from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from model import SessionLocal, Well

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/wells/{api_well_number}")
def read_wells(api_well_number: str, db: Session = Depends(get_db)):
    wells = db.query(Well).filter(Well.api_well_number == api_well_number).all()
    print("wells" ,list(wells))
    if not wells:
        raise HTTPException(status_code=404, detail="Wells not found")
    for well in wells:
        print(list(well.oil for well in wells))
        print(list(well.gas for well in wells))
        print(list(well.brine for well in wells))
    total_oil = sum(well.oil for well in wells)
    total_gas = sum(well.gas for well in wells)
    total_brine = sum(well.brine for well in wells)

    return {
        "api_well_number": api_well_number,
        "total_oil": total_oil,
        "total_gas": total_gas,
        "total_brine": total_brine
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
