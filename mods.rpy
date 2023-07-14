init:
    $ mods["MI_MOD_ARSENA_1_DAY_1_IKARUS"]=u"Лагерь Совёнок: Время, Приключения и Потеря"

    $ ns = Character (u'Система', color="#ffeb38", what_color="FFB3B3")
    $ nl = Character (u'Система', color="#af38ff", what_color="FFB3B3")


    $ beg_night_les = "mods/LS:VPP/music/beg_night_les.mp3"
    $ epic_music = "mods/LS:VPP/music/Lindsey_Stirling_-_Take_Flight_48078070.mp3"
    $ budilnic = "mods/LS:VPP/music/signal-elektronnogo-budilnika-33304.mp3"
    $ budilnic = "mods/LS:VPP/music/fent.mp3"


label MI_MOD_ARSENA_1_DAY_1_IKARUS:
    play music beg_night_les fadein 3
    pause(3)
    ns"Бежим!"
    ns"У нас мало времени!"
    nl"Ага!"
    pause(2)
    ns"Вот оно!{w}, осталось чуть-чуть."
    stop music fadeout 3
    play music fadein 4
    play sound fadein 4
    pause(5)
    scene semen_room
    show unblink
    "Ууу-ааа...."
    th"Пора встовать."
    th"И выключить этот бесячий звук."
    stop music
    th"Пора собираться в Школу в которую я уже хожу 5 лет в один и тот-же класс."
    th"Это потаму что каждый год когда я сажусь в \"Икарус\" с номером 410 {w} я попадаю в лагерь \"Совёнок\"."
    th"После того как я попал в этот лагерь и вернулся назад"
    th"я начал избекать{w}Икарусы...{w} особенно с номерои 410!"
    th"Но если я не садился в Икарус то я попадал в лагерь когда засыпал."
    th"А самое главное в лагере нечего не меняется{w}, даже пионеры!"
    th"А я ведь хотел стать врачом..."
    th"Если сказать кому нибуть это то восьмая бригада сразу выедит."
    



    
        

    
    