import json
import colour

def write_color_json():
    article_info = {
        "EMPTY" : colour.Color("white").hex_l,
        "NONEMPTY" : colour.Color("black").hex_l,
        "INTEGER" : colour.Color("lightpink").hex_l,
        "FLOAT" : colour.Color("mediumvioletred").hex_l,
        "TIME" : colour.Color("mediumorchid").hex_l,
        "DATE" : colour.Color("mediumpurple").hex_l,
        "STRING_UPPER" : colour.Color("lime").hex_l,
        "STRING_LOWER" : colour.Color("limegreen").hex_l,
        "STRING_TITLE" : colour.Color("springgreen").hex_l,
        "STRING_GENERIC" : colour.Color("lightgreen").hex_l,

        "differentiate_alle_upper_case": "False",
        "differentiate_all_lowercase": "False",
        "differentiate_all_titles": "False"
    }

    # color_settings = {
    #     "differentiate_alle_upper_case": False,
    #     "differentiate_all_lowercase": False,
    #     "differentiate_all_titles": False
    # }

    with open("colors.json", "w") as jsonfile:
        json.dump(article_info, jsonfile)
        #json.dump(color_settings, jsonfile)