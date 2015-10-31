data = [
    'IMKTHEQUIBBLERNOCWDRAGONIMARAUDERSMAPW',
    'MUGGLEIMBEATERSLHLWORMTAILBPORTKEYEGDF',
    'EDAPDALBPONGPHILOSOPHERSSTONEWBEFOIFSL',
    'VBTHRLBEEIYBARTYCROUCHJUNIORDOIURWDAMO',
    'ILLOEBARMHGSNITCHABBROOMDTHIUSBNDEETRO',
    'KOOELUNALOVEGOODAUEMOANINGMYRTLEKLALAP',
    'TOBNPSSGTGOIWIZENGAMOTPEEVESMWHPAYTAHO',
    'ODEIADHERWNNTYTMGNUOKAZKABANSUCATOHDCW',
    'ROLXRUEKNAOWYTSEHOXDSADRACOTTIRNTGEYWD',
    'KAKSVMEAIRWWHOONDRBAHJAMESSIRIUSBLACKE',
    'RRCIABSCCTOPVEHTRBAEANIMAGUSAECSDYTOUR',
    'UOAPTLRCSSTMUNGOSETHNPADFOOTNWIUKEEPER',
    'MSHRIEKINGSHACKREROSKCAPERCYGAORRERTIS',
    'MMSOTDBOGGARTHESLTNGSPRONGSAVNEESTSOEL',
    'EENFROTHEKYETRVEOWSOALAVADAKEDAVRAHKOM',
    'PRBEURRNCNCRRUEXNHAHDIGGORYNDINETEWNNO',
    'ETBSNEOINDOBBYIFGODETOODPATRONUSIASSEB',
    'RAASKIWITMOLLYSIBMRHNAGINIGVEELAFOYLRI',
    'TIROMTGTEWASSONLOPOTNANARCISSAMALFOYDL',
    'RSCRIIFDPETERPETTIGREWCAENLICFAECESTLI',
    'IEELDELSFREDDRPCTNEWTSACMTLHEIRONLEHUC',
    'FHFUNOUOLETHIEEHOGHOOPNEUEYTNUHABILEAO',
    'ITWPVHEKUWEASLEYMWQEMINZSCWYTODUEXFRCR',
    'CQUILLRNCOMEAWGETIUYROUNNREAAMIARFFIYP',
    'UTCNHYSOILOUPORWILIPILLEBEEMUORRTEUNKU',
    'STROLLCZUFKTPHOALLDODNMRCRDERAGGYLNAAS',
    'THESTRALSMADEYEMOODYDUNICORNINANBISBER',
    'OABNIMBUSTEHREGLOWIOLCKFMADAMEHOOCHILE',
    'TFUDGEBTSMBRAESLRSTCEMLOCKHARTSETIAUEG',
    'AE-MINERVAKOTHBEARCRNARGLESYPOULTSTQHT',
    'LTHEBURROWCREFVEROHANGHORCRUXDELSTHSTE',
    'UFAWKESHALUULILYEVANSIFPHOENIXBASILISK',
    'SEEKERBLOOBALDPOTIONSCHORACESLUGHORNPR',
    'IFLUFFYALOHOMORANCPANSYKNOCKTURNALLEYE',
]

targets = [
    ['DUMBLEDORE', 'FIRENZE', 'VIKTORKRUMM', 'HEDWIG',
        'LUNALOVEGOOD', 'SNUFFLES', 'MADEYEMOODY', 'CROOKSHANKS',
        'CHARMS', 'MARAUDERSMAP', 'NARCISSA', 'PROFESSOR',
        'SQUIB', 'PETERPETTIGREW', 'MALFOY', 'LUPIN',
        'ALBUS', 'PRONGS', 'FELIXFELICIS', 'HERMIONE',
        'UMBERAGE', 'DOBBY', 'HALFBLOOD', 'MUGGLE',
        'PIG', 'FAWKES', 'PRINCE', 'MUDBLOOD',
        'WAND', 'FLOOPOWDER', 'AVADAKEDAVRA', 'UNICORN',
        'TRUNK', 'BASILISK', 'HORCRUX', 'LILYEVANS',
        'JAMES', 'OLIVER', 'PENSIEVE', 'PHILOSOPHERS',
        'DEMENTORS', 'AUROR', 'HORACE', 'STONE',
        'WIZENGAMOT', 'GHOST', 'SLUGHORN', 'GALLION',
        'BOGGART', 'VEELA', 'POTIONS', 'BERTYBOTTS'],
    ['CENTAUR', 'SEVERUSSNAPE', 'OCCLUMENCY', 'SLYTHERIN',
        'CRUCIO', 'KNOCKTURN', 'DISAPPERATE', 'GRYFFINDOR',
        'THEQUIBBLER', 'ALLEY', 'WORMTAIL', 'AZKABAN',
        'HOWLER', 'PHOENIX', 'DIGGORY', 'VOLDEMORT',
        'NORBERT', 'PADFOOT', 'NEWTS', 'RON',
        'PEEVES', 'TROLL', 'OWLS', 'SEEKER',
        'MADAMEHOOCH', 'ZONKOS', 'ALOHOMORA', 'DRAGON',
        'CHOCHANG', 'FLEUR', 'LONGBOTTOM', 'GINNY',
        'FILTCH', 'FLITWICK', 'MOBILICORPUS', 'DRACO',
        'WINKY', 'FUDGE', 'PATRONUS', 'LUCIUS',
        'PERCY', 'NAGINI', 'SHRIEKING', 'HOGWARTS',
        'CRABB', 'WHOMPING', 'SHACK', 'THEHOGSHEAD',
        'GOYLE', 'WILLOW', 'NARGLES', 'THELEAKY'],
    ['PANSY', 'ARAGOG', 'STMUNGOS', 'CAULDREN',
        'ACCIO', 'TOMRIDDLE', 'THESTRALS', 'BANSHEE',
        'GRAWP', 'MOANINGMYRTLE', 'BROOM', 'GEORGE',
        'SIRIUSBLACK', 'DURMSTRANG', 'PERTRIFICUS', 'FRED',
        'QUILL', 'GILLYWEED', 'TOTALUS', 'PARVATI',
        'BUCKBEAK', 'BEAUXBATONS', 'NIMBUS', 'ROSMERTA',
        'WEREWOLF', 'DEATHEATERS', 'WEASLEY', 'SNITCH',
        'MOONY', 'PORTKEY', 'BEATERS', 'SHACKLEBOLT',
        'RUBEUSHAGRID', 'QUIDDITCH', 'KEEPER', 'FATLADY',
        'ANIMAGUS', 'THEBURROW', 'DOBBY', 'LOCKHART',
        'PHOENIX', 'BARTYCROUCH', 'CREATURE',
        'MAGIC', 'JUNIOR', 'SCABBERS',
        'MINERVA', 'REMUS', 'FLUFFY'],
    # ['SQUIB', 'PORTKEY', 'RUBEUSHAGRID', 'WEASLEY'],
    # ['GALLION', 'GRYFFINDOR', 'OWLS', 'FLEUR'],
]

max_error = 0

print_data = None
print_mode = None


def find_pos(word, i, j, di, dj, err):
    if i not in range(0, len(data)):
        return False
    if j not in range(0, len(data[i])):
        return False
    if data[i][j] != word[0]:
        err -= 1
        if err < 0:
            return False

    if len(word) == 1:
        return True
    else:
        return find_pos(word[1:], i + di, j + dj, di, dj, err)


def find_pos_d(word, i, j):
    result = []

    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            if find_pos(word, i, j, di, dj, max_error):
                result.append((di, dj))

    return result


def find(word):
    result = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            for item in find_pos_d(word, i, j):
                result.append(((i, j), item))

    return result


def go(word):
    found = find(word)

    for item in found:
        ((i, j), (di, dj)) = item

        cmap = [
            ['1;31', '1;32', '1;33', '1;36'],
            ['42', '43', '44', '45', '46'],
            ['4', '9'],
        ]

        # randomize
        ic = i + di * len(word) * 0.5
        jc = j + dj * len(word) * 0.5
        index1 = int(abs(round(
            ic * dj
            + jc * di
        )))
        index2 = int(round(
            ic * 11
            + jc * 13
        ))

        # mode
        modes = {0, 1, 2} if di == 0 else {0, 1}
        for k in range(len(word)):
            modes.difference_update(print_mode[i + k * di][j + k * dj])
        for k in range(len(cmap)):
            mode = (k + index1) % len(cmap)
            if mode in modes:
                break
        else:
            print 'warning: output mode conflict'
        for k in range(len(word)):
            print_mode[i + k * di][j + k * dj].add(mode)

        # print
        for k in range(len(word)):
            print_data[i + k * di][j + k * dj] = (
                '\x1b[' + cmap[mode][index2 % len(cmap[mode])] + 'm'
                + print_data[i + k * di][j + k * dj]
                + '\x1b[0m'
            )

    return found


def print_result():
    for line in print_data:
        print ''.join([
            char if len(char) > 2 else '\x1b[2m' + char + '\x1b[0m'
            for char in line
        ])

for group in targets:
    print_data = [
        [
            ' ' + char for char in line
        ] for line in data
    ]
    print_mode = [
        [
            set() for char in line
        ] for line in data
    ]

    for i in range(len(group)):
        if go(group[i]):
            print i,
        else:
            print group[i],

    print
    print
    print_result()
    print
