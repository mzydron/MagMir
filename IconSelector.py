# Possible weatherstates : clear sky | few clouds | scattered clouds | broken clouds |  shower rain
# rain | thunderstorm | snow | mist
#
# Put proper icon name in below dictionary
iconDic = {"clear sky": "cs.gif", "few clouds": "fc.gif", "scattered clouds": "sc.gif", "broken clouds": "bc.gif",
           "shower rain": "sr.gif", "rain": "r.gif", "thunderstorm": "t.gif", "snow": 's.gif', "mist": "m.gif"}


def returnIconName(iconCode):
    try:
        return iconDic[iconCode]
    except IndexError as e:
        return "No proper icon" + str(e)
