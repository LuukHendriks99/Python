def lang_genoeg(lengte):
    if lengte <= 120:
        print("Je bent te klein")

    else:
        print("Je bent lang genoeg voor de attractie!")

lengte= eval(input("Vul je lengte in:"))
lang_genoeg(lengte)