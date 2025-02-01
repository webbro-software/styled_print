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