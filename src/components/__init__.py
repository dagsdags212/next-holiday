from datetime import date, datetime
from fasthtml.common import *

def days_from_now(holiday):
    dfn = (datetime.strptime(holiday.date, '%Y-%m-%d').date() - date.today()).days
    return dfn if dfn > 0 else 0

def Badge(label, color, **cls):
    return Span(label, cls=f"bg-{color}-500 text-white text-{cls.get('font_size', 'xs')} px-{cls.get('px', 4)} py-{cls.get('py', 2)} mb-{cls.get('mb', 4)} rounded-md") 

def HolidayCard(holiday):
    match holiday.type:
        case "Regular Holiday":
            color = "green"
        case "Special Non-Working Day":
            color = "cyan"
        case "Special Working Day":
            color = "red"
        case "Common Local Holiday":
            color = "amber"
        case _:
            color = "slate"

    return Article(
        Div(
            Badge(holiday.type, color=color, px=2, py=1.5, mb=2),
            cls="flex flex-row gap-4"
        ),
        H3(holiday.name, cls="mt-0.5 text-2xl font-medium text-gray-900 mb-2"),
        Div(
            Time(holiday.date, cls="text-sm text-gray-500"),
            Span(f"{days_from_now(holiday)} days from now", cls="text-sm text-gray-500"),
            cls="flex flex-row justify-between gap-4"
        ),
        cls="rounded-lg border border-gray-200 bg-white px-8 py-6 my-4 min-w-5/6"
    )