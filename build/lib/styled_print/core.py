from termcolor import colored

def styled_print(string, options):
    color = options.get("color")
    styles = options.get("styles", [])
    bg_color = options.get("bg_color")
    uppercase = options.get("uppercase", False)
    lowercase = options.get("lowercase", False)
    align = options.get("align", "left") 
    padding = options.get("padding", 0)
    border = options.get("border", False) 

    if uppercase:
        string = string.upper()
    elif lowercase:
        string = string.lower()

    string = f"{' ' * padding}{string}{' ' * padding}"

    if align == "center":
        string = string.center(50) 
    elif align == "right":
        string = string.rjust(50)

    styled_text = colored(string, color, on_color=bg_color, attrs=styles)

    if border:
        border_line = "-" * (len(string) + 4)
        print(border_line)
        print(f"| {styled_text} |")
        print(border_line)
    else:
        print(styled_text)