import re

text = """
Октябрь уж наступил — уж роща отряхает
Последние листы с нагих своих ветвей;
Дохнул осенний хлад — дорога промерзает.
Журча еще бежит за мельницу ручей,
Но пруд уже застыл; сосед мой поспешает
В отъезжие поля с охотою своей,
И страждут озими от бешеной забавы,
И будит лай собак уснувшие дубравы.

II
Теперь моя пора: я не люблю весны;
Скучна мне оттепель; вонь, грязь — весной я болен;
Кровь бродит; чувства, ум тоскою стеснены.
Суровою зимой я более доволен,
Люблю ее снега; в присутствии луны
Как легкий бег саней с подругой быстр и волен,
Когда под соболем, согрета и свежа,
Она вам руку жмет, пылая и дрожа!

III
Как весело, обув железом острым ноги,
Скользить по зеркалу стоячих, ровных рек!
А зимних праздников блестящие тревоги?..
Но надо знать и честь; полгода снег да снег,
Ведь это наконец и жителю берлоги,
Медведю, надоест. Нельзя же целый век
Кататься нам в санях с Армидами младыми
Иль киснуть у печей за стеклами двойными.

IV
Ох, лето красное! любил бы я тебя,
Когда б не зной, да пыль, да комары, да мухи.
Ты, все душевные способности губя,
Нас мучишь; как поля, мы страждем от засухи;
Лишь как бы напоить, да освежить себя —
Иной в нас мысли нет, и жаль зимы старухи,
И, проводив ее блинами и вином,
Поминки ей творим мороженым и льдом.

V
Дни поздней осени бранят обыкновенно,
Но мне она мила, читатель дорогой,
Красою тихою, блистающей смиренно.
Так нелюбимое дитя в семье родной
К себе меня влечет. Сказать вам откровенно,
Из годовых времен я рад лишь ей одной,
В ней много доброго; любовник не тщеславный,
Я нечто в ней нашел мечтою своенравной.

VI
Как это объяснить? Мне нравится она,
Как, вероятно, вам чахоточная дева
Порою нравится. На смерть осуждена,
Бедняжка клонится без ропота, без гнева.
Улыбка на устах увянувших видна;
Могильной пропасти она не слышит зева;
Играет на лице еще багровый цвет.
Она жива еще сегодня, завтра нет.

VII
Унылая пора! очей очарованье!
Приятна мне твоя прощальная краса —
Люблю я пышное природы увяданье,
В багрец и в золото одетые леса,
В их сенях ветра шум и свежее дыханье,
И мглой волнистою покрыты небеса,
И редкий солнца луч, и первые морозы,
И отдаленные седой зимы угрозы.

VIII
И с каждой осенью я расцветаю вновь;
Здоровью моему полезен русской холод;
К привычкам бытия вновь чувствую любовь:
Чредой слетает сон, чредой находит голод;
Легко и радостно играет в сердце кровь,
Желания кипят — я снова счастлив, молод,
Я снова жизни полн — таков мой организм
(Извольте мне простить ненужный прозаизм).

IX
Ведут ко мне коня; в раздолии открытом,
Махая гривою, он всадника несет,
И звонко под его блистающим копытом
Звенит промерзлый дол и трескается лед.
Но гаснет краткий день, и в камельке забытом
Огонь опять горит — то яркий свет лиет,
То тлеет медленно — а я пред ним читаю
Иль думы долгие в душе моей питаю.

X
И забываю мир — и в сладкой тишине
Я сладко усыплен моим воображеньем,
И пробуждается поэзия во мне:
Душа стесняется лирическим волненьем,
Трепещет и звучит, и ищет, как во сне,
Излиться наконец свободным проявленьем —
И тут ко мне идет незримый рой гостей,
Знакомцы давние, плоды мечты моей.

XI
И мысли в голове волнуются в отваге,
И рифмы легкие навстречу им бегут,
И пальцы просятся к перу, перо к бумаге,
Минута — и стихи свободно потекут.
Так дремлет недвижим корабль в недвижной влаге,
Но чу! — матросы вдруг кидаются, ползут
Вверх, вниз — и паруса надулись, ветра полны;
Громада двинулась и рассекает волны.

XII
Плывет. Куда ж нам плыть?
. . . . . . . . . . . . 
"""

x = re.findall("[а-я]", text)

print(x)