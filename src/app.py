from dataclasses import dataclass
from fasthtml.common import *
from header import HEADERS
from components import Badge
from util import *

app, rt = fast_app(live=True, pico=False, hdrs=HEADERS)

@rt('/seed')
def get():
    seed_db()
    return RedirectResponse(url="/")

    
@rt
def index():
    holiday = get_next_nearest_holiday()
    holiday_name = holiday.get('name')
    holiday_date = str2date(holiday.get('date'))
    holiday_type = holiday.get('type')
    days_until_holiday = (holiday_date - date.today()).days
    days_until_holiday_str = f"{days_until_holiday} days from now" if days_until_holiday > 0 else "today"

    return Div(
        P("The next holiday is", cls="text-2xl"),
        H1(holiday_name, cls="text-6xl font-strech-condensed mt-6 mb-4"),
        Badge(holiday_type, color="slate"),
        P(f"{holiday_date.strftime('%B %d, %Y')} ({holiday_date.strftime('%A')})", cls="text-3xl mt-4"),
        P(days_until_holiday_str),
        cls="flex flex-col items-center justify-center pl-12 h-screen bg-slate-50",
    ) 

serve()
