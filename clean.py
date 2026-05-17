def clean_my_list(some_list):

    clean_list = []

    for element in some_list:
        clean_element = element.strip()
        clean_list.append(clean_element)

    return clean_list
