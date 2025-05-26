from fasthtml.common import *

def Badge(label, color):
    return Div(label, cls=f"bg-{color}-500 text-white px-4 py-2 mb-4 rounded-full") 