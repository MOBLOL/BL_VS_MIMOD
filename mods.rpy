init:
    $ mods["MI_MOD_ARSENA_1_DAY_1_IKARUS"]=u"Лагерь Совёнок: Время, Приключения и Потеря"

    $ ns = Character (u'???', color="#ffeb38", what_color="FFFFFF")
    $ nl = Character (u'???', color="#af38ff", what_color="FFFFFF")


    $ beg_night_les = "mods/BL_VS_MIMOD/music/beg_night_les.mp3"
    $ epic_music = "mods/BL_VS_MIMOD/music/Lindsey_Stirling_-_Take_Flight_48078070.mp3"
    $ budilnic = "mods/BL_VS_MIMOD/music/signal-elektronnogo-budilnika-33304.mp3"

    image magazin = "mods/BL_VS_MIMOD/img/magaz.jpg"

    $ lekarstfo = 0
    $ predmet = 0
    $ fonarik = "false"
    $ Nozik = "false"
    $ dengi = "false"
    $ dosirak = "false"
    $ bumaga_and_ruchka = "false"

    $ lekarstfo_ot_angin = "false"
    $ lekarstfo_ot_prostudi = "false"
    $ lekarstfo_perekis_vodoroda = "false"


    $ pos1 = "false"
    $ inpos1 = ""
    $ pos2 = "false"
    $ inpos2 = ""

    $ is_all_lekarstva = 0
    $ is_all_lekarstva_otvet = ""



label MI_MOD_ARSENA_1_DAY_1_IKARUS:
    play music beg_night_les fadein 3
    pause(3)
    ns"Бежим!"
    ns"У нас мало времени!"
    nl"Ага!"
    pause(2)
    ns"Вот оно!{w} осталось чуть-чуть."
    stop music fadeout 5
    pause(1)
    play music budilnic fadein 3
    pause(4)
    scene semen_room
    show unblink
    "Ууу-ааа...."
    th"Пора встовать."
    th"И выключить этот бесячий звук."
    stop music fadeout 3
    play music music_list["confession_oboe"] fadein 5
    th"Пора собираться в Школу в которую я уже хожу 5 лет в один и тот-же класс."
    th"Это потаму что каждый год когда я сажусь в \"Икарус\" с номером 410 {w}, я попадаю в лагерь \"Совёнок\"."
    th"После того как я попал в этот лагерь и вернулся назад"
    th"я начал избекать {w}Икарусов...{w} особенно с номерои 410!"
    th"Но если я не садился в Икарус то я попадал в лагерь когда засыпал."
    th"А самое главное в лагере нечего не меняется{w}, даже пионеры!"
    th"А я ведь хотел стать врачом..."
    th"Если сказать кому нибуть это, то восьмая бригада сразу выедит."
    th"И так{w} сегодня тот самый день"
    th"День когда я должен опять попасть в лагерь"
    th"Может взять какие нибуть вещи с собой?"
    "Я неспеша подошол к столу"
label menu_fibora_Day_1_Mod_Arsena:
scene semen_room


menu:
    "Фонарик":
        if fonarik == "true":
            jump Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1
        else:
            $ fonarik = "true"
            $ predmet += 1
            if pos1 == "false":
                $ inpos1 = "фонарика"
                $ pos1 = "true"
            elif pos2 == "false":
                $ inpos2 = "фонарика"
                $ pos2 = "true"
            jump Add_Predmet_Mod_Arsena_day_1
    "Ножик":
        if Nozik == "true":
            jump Im_Yzu_E_Vzal_Mod_Arsena_Day_1
        else:
            $ Nozik = "true"
            $ predmet += 1
            if pos1 == "false":
                $ inpos1 = "Ножик"
                $ pos1 = "true"
            elif pos2 == "false":
                $ inpos2 = "Ножик"
                $ pos2 = "true"
            jump Add_Predmet_Mod_Arsena_day_1
    "Деньги":
        if dengi == "true":
            jump Im_Yzu_E_Vzal_Mod_Arsena_Day_1
        else:
            $ dengi = "true"
            $ predmet += 1
            if pos1 == "false":
                $ inpos1 = "Деньги"
                $ pos1 = "true"
            elif pos2 == "false":
                $ inpos2 = "Деньги"
                $ pos2 = "true"
            jump Add_Predmet_Mod_Arsena_day_1
    "Лекарство":
        jump lekarstfo_Mod_Arsena_Day_1
    "Доширак":
        if dosirak == "true":
            jump Im_Yzu_E_Vzal_Mod_Arsena_Day_1
        else:
            $ dosirak = "true"
            $ predmet += 1
            if pos1 == "false":
                $ inpos1 = "Доширак"
                $ pos1 = "true"
            elif pos2 == "false":
                $ inpos2 = "Доширак"
                $ pos2 = "true"
            jump Add_Predmet_Mod_Arsena_day_1
    "Бумага и ручка":
        if bumaga_and_ruchka == "true":
            jump Im_Yzu_E_Vzal_Mod_Arsena_Day_1
        else:
            $ bumaga_and_ruchka = "true"
            $ predmet += 1
            if pos1 == "false":
                $ inpos1 = "Бумага и ручка"
                $ pos1 = "true"
            elif pos2 == "false":
                $ inpos2 = "Бумага и ручка"
                $ pos2 = "true"
            jump Add_Predmet_Mod_Arsena_day_1


label lekarstfo_Mod_Arsena_Day_1:

menu:
    "Лекарство от \"ангины\"":
        if lekarstfo_ot_angin == "true":
            jump Im_Yzu_E_Vzal_Mod_Arsena_Day_1
        else:
            $ lekarstfo_ot_angin = "true"
            $ predmet += 1
            $ is_all_lekarstva += 1
            if pos1 == "false":
                $ inpos1 = "Лекарство от ангины"
                $ pos1 = "true"
            elif pos2 == "false":
                $ inpos2 = "Лекарство от ангины"
                $ pos2 = "true"
            jump Add_Predmet_Mod_Arsena_day_1
    "Лекарство от \"Простуды\"":
        if lekarstfo_ot_prostudi == "true":
            jump Im_Yzu_E_Vzal_Mod_Arsena_Day_1
        else:
            $ lekarstfo_ot_prostudi = "true"
            $ predmet += 1
            $ is_all_lekarstva += 1
            if pos1 == "false":
                $ inpos1 = "Лекарство от Простуды"
                $ pos1 = "true"
            if pos2 == "false":
                $ inpos2 = "Лекарство от Простуды"
                $ pos2 = "true"
            jump Add_Predmet_Mod_Arsena_day_1
    "Перикись водорода":
        if lekarstfo_perekis_vodoroda == "true":
            jump Im_Yzu_E_Vzal_Mod_Arsena_Day_1
        else:
            $ lekarstfo_perekis_vodoroda = "true"
            $ predmet += 1
            $ is_all_lekarstva += 1
            if pos1 == "false":
                $ inpos1 = "Перикись водорода"
                $ pos1 = "true"
            if pos2 == "false":
                $ inpos2 = "Перикись водорода"
                $ pos2 = "true"
            jump Add_Predmet_Mod_Arsena_day_1
    "Назад":
        jump menu_fibora_Day_1_Mod_Arsena
    


label Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1:
    scene semen_room
    th"я это уже взял"
    jump menu_fibora_Day_1_Mod_Arsena


label Add_Predmet_Mod_Arsena_day_1:
    scene semen_room
    if is_all_lekarstva == 2:
        $ is_all_lekarstva_otvet = "лекарства"
    else:
        $ is_all_lekarstva_otvet = "вещи"
    if predmet != 2:
        th"Ммм... {w} может ещё что-то взять?"
        jump menu_fibora_Day_1_Mod_Arsena
    else: 
        th"Больше в корманы не влезает"
        th"Ммм... пожалуй [inpos1] и [inpos2] полезные [is_all_lekarstva_otvet]"
        th"пора идти"
        "Я направился к выходу из дома."
        play sound sfx_open_door_clubs_2
    hide semen_room with dissolve
label Idu_Na_Ylicu_Mod_Arsena_Day_1:
    show blink
    scene bus_stop
    pause(2)
    hide blink
    show unblink
    play music music_list["eternal_longing"] fadein 3
    th"..."
    th"Ну вот я уже у автобусной остановки где меня будет ждать неменуемая судьба."
    "Подошол к автобусной останоке"
    me"И ты тоже не меняешся..."
    "сказал я с ухмылкой"
    th"Хотя если приглядется то есть небольшие отличая {w} например слегка расшатаная лавочка{w}, облезлая краска{w} и чуть скосившая крыша."
    th"Может в магазин заглянуть пока есть возможность?"
    "Я направился в сторону магазинчика"
    hide bus_stop
    stop fadeout 2

    

    



    
        

    
