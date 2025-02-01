from styled_print import styled_print


styled_print("hello", {
    "color": "red",
    "styles": ["bold"],
    "bg_color": "on_white",
    "uppercase": True,
    "align": "center",
    "padding": 2,
    "border": False
})
styled_print("hello", {
    "color": "red",
    "styles": ["bold"],
    "bg_color": "on_red",
    "uppercase": True,
    "align": "center",
    "padding": 2,
    "border": True
})
styled_print("hello", {
    "color": "red",
    "styles": ["bold"],
    "uppercase": True,
    "align": "left",
    "padding": 2,
    "border": False
})
styled_print("hello", {
    "color": "yellow",
    "styles": ["underline"],
    "uppercase": True,
    "align": "left",
    "border": False
})
