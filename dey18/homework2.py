jgufi=['nika qatamadze''alexandre Katsarava','dato Jachvadze','dato Mgeladze','davit Janashia','gabriel Gogadze','gabrieli Molodini','giorgi Gelashvili','ilia Wiklauri','muhammedali Mamedov','nini Nozadze','sandro Bochorishvili','sandro Oqropiridze','vano Motiashvili','erekle gochitashvili','lasha wamalaidze','nika chochia']

i_count = 0
supersia = []


for element in jgufi:
    i_count = 0
    for char in element:
        if char == "i":
            i_count += 1

    if i_count > 2:
        supersia.append(element.capitalize())


print(supersia)