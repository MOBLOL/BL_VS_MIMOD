init:
    $ mods["MI_MOD_ARSENA_1_DAY_1_IKARUS"]=u"Лагерь Совёнок: Время, Приключения и Потеря"

    $ ns = Character (u'???', color="#ffeb38", what_color="FFFFFF")
    $ nl = Character (u'???', color="#af38ff", what_color="FFFFFF")
    $ bd = Character (u'Бездомный', color="#8d4b1f", what_color="FFFFFF")


    screen MyScreenModArsenaDay1:
        imagemap:
            auto "mods/BL_VS_MIMOD/img/maps1_%s.png"
            hotspot(190, 5, 93, 48) action Jump("ylica_Ikarus_Dvor_Mod_Arsena_Day_1")
            hotspot(2, 142, 75, 132) action Jump("ylica_Ikarus_avtobus_Mod_Arsena_Day_1")
            hotspot(185, 80, 110, 200) action Jump("MI_MOD_ARSENA_2_DAY_1_IKARUS")


    $ beg_night_les = "mods/BL_VS_MIMOD/music/beg_night_les.mp3"
    $ epic_music = "mods/BL_VS_MIMOD/music/Lindsey_Stirling_-_Take_Flight_48078070.mp3"
    $ budilnic = "mods/BL_VS_MIMOD/music/signal-elektronnogo-budilnika-33304.mp3"

    image magazin = "mods/BL_VS_MIMOD/img/magaz.jpg"
    image zdvor = "mods/BL_VS_MIMOD/img/dvorik.png"

    $ lekarstfo = 0
    $ predmet = 0
    $ fonarik = "false"
    $ Nozik = "false"
    $ dengi = "false"
    $ dosirak = "false"
    $ bumaga_and_ruchka = "false"
    $ vitamini = "false"
    $ konveti = "false"
    $ sumka_dla_vtoroi_obufi = "false"
    $ komp_perv_med_help = "false"
    $ nabor_arduino_min_disp = "false"
    $ book_territoria = "false"
    $ neilonvie_struni = "false"

    $ lekarstfo_ot_angin = "false"
    $ lekarstfo_ot_prostudi = "false"
    $ lekarstfo_perekis_vodoroda = "false"
    $ is_magaz = "false"


    $ pos1 = "false"
    $ inpos1 = ""
    $ pos2 = "false"
    $ inpos2 = ""
    $ pos3 = "false"
    $ inpos3 = ""
    $ pos4 = "true"
    $ inpos4 = ""

    $ is_dop_invent = "false"
    $ is_all_lekarstva = 0
    $ is_all_lekarstva_otvet = ""
    $ is_dvor_Arsen_day_1 = "false"

    $ Money = 0

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
    th"Ну ладно пионеры, даже  {b}Я{/b}!"
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
            jump Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1
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
            jump Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1
        else:
            $ dengi = "true"
            $ predmet += 1
            $ Money += 300
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
            jump Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1
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
            jump Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1
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
            jump Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1
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
            jump Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1
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
            jump Im_Yzu_Eto_Vzal_Mod_Arsena_Day_1
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
    th"Я это уже взял."
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
        th"Больше в корманы не влезает."
        th"Ммм... пожалуй [inpos1] и [inpos2] полезные [is_all_lekarstva_otvet]."
        th"Пора идти."
        "Я направился к выходу из дома."
        play sound sfx_open_door_clubs_2
    hide semen_room with dissolve
label Idu_Na_Ylicu_Mod_Arsena_Day_1:
    show blink
    pause(2)
    scene bus_stop
    hide blink
    show unblink
    play music music_list["eternal_longing"] fadein 3
    "..."
    th"Ну вот я уже у автобусной остановки где меня будет ждать неменуемая судьба."
    "Подошол к автобусной останоке."
    me"И ты тоже не меняешся..."
    "Сказал я с ухмылкой."
    th"Хотя если приглядется то есть небольшие отличая {w} например слегка расшатаная лавочка{w}, облезлая краска{w} и чуть скосившая крыша."
    th"Может в магазин заглянуть пока есть возможность?"
    "Я направился в сторону магазинчика."
    scene magazin with dissolve
    $ is_magaz = "true"
    th"Таак..."
    "я порылся в своих карманах"
    if inpos1 == "Деньги":
        th"У меня есть 150р и ещё 300р которые я взял дома."
        $ Money += 150
    elif inpos2 == "Деньги":
        th"У меня есть 150р и ещё 300р которые я взял дома."
        $ Money += 150
    else:
        th"У меня с собой только 100р."
        th"Что-же можно мне купить на них."
        $ Money = 100
    "Я огляделся."
    th"Людей с утра очень мало."
    th"Вернее{w} совсем нет."
    "Я рассмотрел товар."

label MI_MOD_ARSENA_2_DAY_1_IKARUS:
if is_magaz == "false":
    scene magazin with dissolve
menu:
    "[Money]р"
    "Витомины - 50р":
        if Money - 50 > 0:
            if vitamini == "false":
                if pos3 == "false":
                    th"Ели как уместил их в корманы."
                    th"Заболеть мне ещё непомешало!"
                    th"Лучше уш плавать на речке{w} чем жариться в постеле."
                    $ inpos3 = "витомины"
                    $ pos3 = "true"
                    $ Money -= 50
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                elif pos4 == "false":
                    th"Ели как уместил их в корманы."
                    th"Заболеть мне ещё непомешало!"
                    th"Лучше уш плавать на речке{w} чем жариться в постеле."
                    $ inpos3 = "витомины"
                    $ pos3 = "true"
                    $ Money -= 50
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                else:
                    th"у меня карманы забиты битком."
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
            else:
                th"Я это уже взял."
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
        else:
            th"Мне не хватает денег."
            jump MI_MOD_ARSENA_2_DAY_1_IKARUS
    "Конфеты - 100р":
        if Money - 100 > 0:
            if konveti == "false":
                if pos3 == "false":
                    th"Ели как уместил их в корманы."
                    th"Надеюсь конфеты хоть както скрасят моё пробывание в лагере."
                    $ inpos3 = "Конфеты"
                    $ pos3 = "true"
                    $ Money -= 100
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                elif pos4 == "false":
                    th"Ели как уместил их в корманы."
                    th"Надеюсь конфеты хоть както скрасят моё пробывание в лагере."
                    $ inpos3 = "Конфеты"
                    $ pos3 = "true"
                    $ Money -= 100
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                else:
                    th"у меня карманы забиты битком."
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
            else:
                th"Я это уже взял."
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
        else:
            th"Мне не хватает денег."
            jump MI_MOD_ARSENA_2_DAY_1_IKARUS
    "Сумка для второй обуви - 200р":
        if Money - 200 > 0:
            if sumka_dla_vtoroi_obufi == "false":
                th"Теперь у меня больше места."
                $ inpos3 = "Сумока для второй обуви"
                $ pos3 = "true"
                $ Money -= 200
                $ pos4 = "false"
                $ is_dop_invent = "true"
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
            else:
                th"У меня уже есть сумка."
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
        else:
            th"Мне не хватает денег."
            jump MI_MOD_ARSENA_2_DAY_1_IKARUS
    "Комплект первой мед помощи - 200р":
        if Money - 200 > 0:
            if komp_perv_med_help == "false":
                if pos3 == "false":
                    th"Лишнем точно не будет!"
                    th"Придётся в руках нести."
                    $ inpos3 = "Конфеты"
                    $ pos3 = "true"
                    $ Money -=200
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                elif pos4 == "false":
                    th"Лишнем точно не будет!"
                    th"Придётся в руках нести."
                    $ inpos3 = "Конфеты"
                    $ pos3 = "true"
                    $ Money -=200
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                else:
                    th"у меня карманы забиты битком."
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
            else:
                th"Я это уже взял."
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
        else:
            th"Мне не хватает денег."
            jump MI_MOD_ARSENA_2_DAY_1_IKARUS
    "Набор Arduino с миниатюр. дисплеем - 400р":
        if Money - 50 > 0:
            if nabor_arduino_min_disp == "false":
                if pos3 == "false":
                    th"Придётся в руках нести."
                    th"Может вкоем то веке запишусь в кружок электроники."
                    $ inpos3 = "Набор Arduino с миниатюр. дисплеем"
                    $ pos3 = "true"
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                elif pos4 == "false":
                    th"Придётся в руках нести."
                    th"Может вкоем то веке запишусь в кружок электроники."
                    $ inpos3 = "Набор Arduino с миниатюр. дисплеем"
                    $ pos3 = "true"
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                else:
                    th"у меня карманы забиты битком."
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
            else:
                th"Я это уже взял."
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
        else:
                th"Мне не хватает денег."
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
    "Книга \"Территория\" - 200р":
        if Money - 200 > 0:
            if book_territoria == "false":
                if pos3 == "false":
                    th"Придётся в руках нести."
                    th"Можно хоть книгу почитать."
                    $ inpos3 = "Книга \"Территория\""
                    $ pos3 = "true"
                    $ Money -= 200
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                elif pos4 == "false":
                    th"Придётся в руках нести."
                    th"Можно хоть книгу почитать."
                    $ inpos3 = "Книга \"Территория\""
                    $ pos3 = "true"
                    $ Money -= 200
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                else:
                    th"у меня карманы забиты битком."
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
            else:
                th"Я это уже взял."
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
        else:
            th"Мне не хватает денег."
            jump MI_MOD_ARSENA_2_DAY_1_IKARUS
    "нейлоновые струны - 200р":
        if Money - 200 > 0:
            if book_territoria == "false":
                if pos3 == "false":
                    th"Струны от которых мазолей на пальцах не будут."
                    th"Может я там и играть научусь?"
                    th"Ели как уместил их в корманы."
                    $ inpos3 = "нейлоновые струны"
                    $ pos3 = "true"
                    $ Money -= 200
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                elif pos4 == "false":
                    th"Ели как уместил их в корманы."
                    $ inpos3 = "нейлоновые струны"
                    $ pos3 = "true"
                    $ Money -= 200
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
                else:
                    th"у меня карманы забиты битком."
                    jump MI_MOD_ARSENA_2_DAY_1_IKARUS
            else:
                th"Я это уже взял."
                jump MI_MOD_ARSENA_2_DAY_1_IKARUS
        else:
            th"Мне не хватает денег."
            jump MI_MOD_ARSENA_2_DAY_1_IKARUS

    "Водка - 200р":
        th"Мне нет 18-ти"
        th"Но душевно мне уже больше 18-ти лет"
        jump MI_MOD_ARSENA_2_DAY_1_IKARUS
    "Выйти из магазина":
        jump ylica_Ikarus_magazin_Mod_Arsena_Day_1


label ylica_Ikarus_magazin_Mod_Arsena_Day_1:
    th"Думаю я там закончил."
    th"Куда-же мне теперь пойти?"
    show screen MyScreenModArsenaDay1
    $ renpy.pause(hard=true)

label ylica_Ikarus_Dvor_Mod_Arsena_Day_1:
    if is_dvor_Arsen_day_1 == "true":
        th"мне там делать нечего"
        jump ylica_Ikarus_magazin_Mod_Arsena_Day_1
    else:
        th"Ну делать мне всё равно нечего."
    th"Пойду прогуляюсь"
    scene zdvor with dissolve
    pause(1)
    th"Рядом с мусоркой на картонке волялся бездомный."
    bd"Парень пожалуйста дай денег сколько не жалко."
menu:
    "Дать денег":
        if Money >= 50:
            me"Хорошо я дам тебе денег."
            if Money >= 250:
                if pos1 == "false":
                    me"Но просто так я тебе их не дам."
                    me"Если пойдёш и купиш \"Водку\" то я тебе дам 50р."
                    bd"5 секунд."
                    th"Там от скуки и помереть охота."
                    th"С этим мне точно скучно не будет."
                    bd"Вот держи"
                    me"Спасибо"
                    "Я торопливо покинул двор."
                    $ pos1 = "true"
                    $ inpos1 = "водка"
                    jump ylica_Ikarus_MagazDvor_Mod_Arsena_Day_1
                elif pos2 == "false":
                    me"Но просто так я тебе их не дам."
                    me"Если пойдёш и купиш \"Водку\" то я тебе дам 50р."
                    bd"5 секунд."
                    th"Там от скуки и помереть охота."
                    th"С этим мне точно скучно не будет."
                    bd"Вот держи"
                    me"Спасибо"
                    "Я торопливо покинул двор."
                    $ pos2 = "true"
                    $ inpos2 = "водка"
                    jump ylica_Ikarus_MagazDvor_Mod_Arsena_Day_1
                elif pos3 == "false":
                    me"Но просто так я тебе их не дам."
                    me"Если пойдёш и купиш \"Водку\" то я тебе дам 50р."
                    bd"5 секунд."
                    th"Там от скуки и помереть охота."
                    th"С этим мне точно скучно не будет."
                    bd"Вот держи"
                    me"Спасибо"
                    "Я торопливо покинул двор."
                    $ pos3 = "true"
                    $ inpos3 = "водка"
                    jump ylica_Ikarus_MagazDvor_Mod_Arsena_Day_1
                elif pos4 == "false":
                    me"Но просто так я тебе их не дам."
                    me"Если пойдёш и купиш \"Водку\" то я тебе дам 50р."
                    bd"5 секунд."
                    th"Там от скуки и помереть охота."
                    th"С этим мне точно скучно не будет."
                    bd"Вот держи"
                    me"Спасибо"
                    "Я торопливо покинул двор."
                    $ pos4 = "true"
                    $ inpos4 = "водка"
                    jump ylica_Ikarus_MagazDvor_Mod_Arsena_Day_1
        else:
            me"Прости но у меня нет денег."
            "Я неторопливо покинул двор."
            jump ylica_Ikarus_MagazDvor_Mod_Arsena_Day_1
    "Недовать денег":
        me"Ещё чего! Возьми и заработай."
        "Я торопливо покинул двор."

label ylica_Ikarus_MagazDvor_Mod_Arsena_Day_1:
    hide MyScreenModArsenaDay1 with dissolve
    th"И так..."
    th"У меня ещё есть время."
    th"Может к остановки уже пойти?"
    $ renpy.pause(hard=true)

label ylica_Ikarus_avtobus_Mod_Arsena_Day_1:
    th"Пойду я пожалуй на остановку."
    th"Делать всёравно нечего."
    scene bus_stop with dissolve