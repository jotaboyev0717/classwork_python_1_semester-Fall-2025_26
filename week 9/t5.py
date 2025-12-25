def parse_markdown(text):
    result = ""
    i = 0
    bold_open = False
    italic_open = False

    while i < len(text):
        if i + 1 < len(text) and text[i] == "*" and text[i+1] == "*":
            if not bold_open:
                result += "<b>"
            else:
                result += "</b>"
            bold_open = not bold_open
            i += 2
            continue


        if text[i] == "_":
            if not italic_open:
                result += "<i>"
            else:
                result += "</i>"
            italic_open = not italic_open
            i += 1
            continue


        result += text[i]
        i += 1

    return result



print(parse_markdown("This is **bold** text."))             
print(parse_markdown("Hello _world_."))                    
print(parse_markdown("Make **this** bold and _this_ italic."))  
print(parse_markdown("No formatting here."))               
print(parse_markdown("**Bold** at start."))                
