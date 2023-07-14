init:
    $ mods["MI_MOD_ARSENA_1_DAY_1_IKARUS"]=u"Лагерь Совёнок: Время, Приключения и Потеря"

    $ ns = Character (u'Система', color="#ffeb38", what_color="FFB3B3")
    $ nl = Character (u'Система', color="#af38ff", what_color="FFB3B3")


    $ beg_night_les = "mods/LS:VPP/music/beg_night_les.mp3"

label MI_MOD_ARSENA_1_DAY_1_IKARUS:
    play music beg_night_les fadein 3
    pause(3)
    ns"Бежим!"
    ns"У нас мало времени!"
    nl"Ага!"
    pause(2)
    ns"Вот оно!{w}, осталось чуть-чуть."

    
        

    
    