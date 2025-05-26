from dataclasses import dataclass
from datetime import datetime, date
from fasthtml.common import database

@dataclass
class Holiday:
    name: str
    date: date
    type: str

HOLIDAYS = [
    Holiday(name="Eid al-Adha (Day 1)", date=date(2025, 6, 7), type="Regular Holiday"),
    Holiday(name="Eid al-Adha (Day 2)", date=date(2025, 6, 8), type="Common Local Holiday"),
    Holiday(name="Independence Day", date=date(2025, 6, 12), type="Regular Holiday"),
    Holiday(name="Amun Jadid", date=date(2025, 6, 27), type="Common Local Holiday"),
    Holiday(name="Ninoy Aquino Day", date=date(2025, 8, 21), type="Special Non-Working Holiday"),
    Holiday(name="National Heroes Day", date=date(2025, 8, 25), type="Regular Holiday"),
    Holiday(name="Yamashita Surrender Day", date=date(2025, 9, 3), type="Special Working Holiday"),
    Holiday(name="Maulid un-Nabi", date=date(2025, 9, 5), type="Common Local Holiday"),
    Holiday(name="Feast of the Nativity of Mary", date=date(2025, 9, 8), type="Special Working Holiday"),
    Holiday(name="Halloween", date=date(2025, 10, 31), type="Special Non-working Holiday"),
    Holiday(name="All Saints' Day", date=date(2025, 11, 1), type="Special Non-working Holiday"),
    Holiday(name="All Souls Day", date=date(2025, 11, 2), type="Observance"),
    Holiday(name="Bonifacio Day", date=date(2025, 11, 30), type="Regular Holiday"),
    Holiday(name="Feast of the Immaculate Conception", date=date(2025, 12, 8), type="Special Non-working Holiday"),
    Holiday(name="Christmas Eve", date=date(2025, 12, 24), type="Special Non-working Holiday"),
    Holiday(name="Christmas Day", date=date(2025, 12, 25), type="Regular Holiday"),
    Holiday(name="Rizal Day", date=date(2025, 12, 30), type="Regular Holiday"),
    Holiday(name="New Year's Eve", date=date(2025, 12, 31), type="Special Non-working Holiday"),
    Holiday(name="New Year's Day", date=date(2026, 1, 1), type="Regular Holiday"),
]



def seed_db() -> None:
    db = database('sqlite:///holidays.db')
    holidays_tbl = db.create(Holiday, pk='name')

    for holiday in HOLIDAYS:
        try:
            holidays_tbl.insert(holiday)
        except Exception as e:
            print(f"Error: {e}")
            continue

def get_holidays():
    db = database('sqlite:///holidays.db')
    assert "holiday" in db.t, "table `holiday` does not exist"
    return db.query("SELECT * FROM holiday")

def str2date(dt):
    return datetime.strptime(dt, '%Y-%m-%d').date()

def get_next_nearest_holiday():
    query = """
    SELECT * FROM holiday
    WHERE date > date()
    ORDER BY date
    LIMIT 1
    """
    db = database("sqlite:///holidays.db")
    return list(db.query(query))[0]
