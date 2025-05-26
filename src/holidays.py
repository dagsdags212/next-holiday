from dataclasses import dataclass
from datetime import date

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
