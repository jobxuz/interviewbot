from fuzzywuzzy import fuzz

def suniyintelekt(text,data):
    max = []
    for date in data:
        javob = fuzz.ratio(text.lower(), date.lower())
        max.append(javob)
    return sorted(max)[-1]



def helpbot():
    text = f"👨🏻‍💻 Assalomu alaykum\n"
    text += f"🤖 Botdan kerakli bo'limni tanlang va bot sizga interview savollarini beradi.\n"
    text += f"❗️Savollarga javobni text ko'rinishida yuboring."

    return text



