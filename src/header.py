from fasthtml.common import Link, Script

custom_css = Link(rel="stylesheet", href="./main.css", type="text/css")
tailwind_css = Link(
    rel="stylesheet",
    href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
    type="text/css",
)
tailwind_js = Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4")
daisyui_css = Link(
    rel="stylesheet",
    href="https://cdn.jsdelivr.net/npm/daisyui@4.12.22/dist/full.min.css",
    type="text/css",
)

HEADERS = (
    tailwind_css,
    tailwind_js,
    #daisyui_css,
    custom_css,
)
