# custom checks and strategies go here
# note that it is highly recommended to put reusable checks and strategies in a separate app
from xchk_core.strats import *
from xchk_regex_strategies.strats import *
from xchk_multiple_choice_strategies.strats import *

voordelen_data = [('"Relationele integriteit" betekent hetzelfde als "integriteit"',
                   ('Ja',False,'Relationele integriteit is specifieker. Het houdt in dat de verwijzingen tussen stukjes data kloppen, maar niet dat andere aspecten van de data kloppen.'),
                   ('Nee',True,None)),
                  ('Alle gebruikers van een database kunnen alle data in de database bewerken.',
                   ('Ja',False,'Je krijgt van ons toegang tot een gemeenschappelijke database voor alle studenten. Zouden we dat doen als je per ongeluk het werk van je collega\'s kon aanpassen?'),
                   ('Nee',True,None))]
xchk_ap_db_intro_content_voordelen_van_een_database_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),
                                                  MultipleChoiceFormatCheck(),
                                                  MultipleChoiceAnswerCheck(None,voordelen_data)])),
        accepting_check=TrueCheck())

subtalen_data = [('Waarvoor staat "DML"?',
                  ('Data Modification Language',False,'Je kan inderdaad data aanpassen met deze taal, maar de term is anders. Doorzoek de tekst.'),
                  ('Data Manipulation Language',True,None),
                  ('Data Making Language',False,'Je kan inderdaad data aanmaken met deze taal, maar de term is anders. Doorzoek de tekst.')),
                 ('Waarvoor staat "DDL"?',
                  ('Data Definition Language',True,None),
                  ('Data Development Language',False,'Je gebruikt deze deeltaal wel om de structuur van je database te ontwikkelen, maar de term is anders. Doorzoek de tekst.'),
                  ('Data Directive Language',False,'Er zijn nog andere delen van SQL die "directives" ("instructies") bevatten, dus dat zou geen geschikte naam zijn. Doorzoek de tekst.')),
                 ('Met welke deeltaal zou je een nieuw boek toevoegen aan een tabel met boeken?',
                     ('DDL',False,'Je doet geen structurele wijziging. Dan is het niet logisch de DDL te gebruiken. Je past <em>de data zelf</em> aan, niet hun structuur.'),
                  ('DML',True,None)),
                 ('Met welke deeltaal zou je de tabel met boeken verwijderen?',
                  ('DDL',True,None),
                  ('DML',False,'Dit voorbeeld komt niet voor in de tekst, maar er staat dat je een <em>tabel</em> zou verwijderen. Dat is een structurele aanpassing.')),
                 ('Met welke deeltaal zou je een nieuwe kolom toevoegen aan de tabel met boeken?',
                  ('DDL',True,None),
                  ('DML',False,'Dit voorbeeld komt niet voor in de tekst, maar er staat dat je een <em>tabel</em> zou wijzigen. Dat is een structurele aanpassing.')),
                 ('Met welke deeltaal zou je de titel van een bepaald boek veranderen?',
                  ('DDL',False,'Het gaat hier over een specifiek boek. Je zou niets wijzigen aan <em>het soort</em> data dat je bijhoudt, wel aan <em>de data zelf</em>. Bekijk het zo: een krantenwinkel verkoopt een bepaald soort product: kranten. Maar hij verkoopt elke dag <em>andere</em> kranten.'),
                  ('DML',True,None))]
xchk_ap_db_intro_content_subtalen_van_my_sql_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),
                                                  MultipleChoiceFormatCheck(),
                                                  MultipleChoiceAnswerCheck(None,subtalen_data)])),
        accepting_check=TrueCheck())

wat_is_een_db_data = [('Wat betekent "DBMS"?',
                         ('Database Moderation Structure',False,'Lees de tekst nog eens grondig. De afkorting staat er in.'),
                         ('Database Moderation System',False,'Lees de tekst nog eens grondig. De afkorting staat er in.'),
                         ('Database Management Structure',False,'Lees de tekst nog eens grondig. De afkorting staat er in.'),
                         ('Database Management System',True,None)),
                        ('Wat is de "syntax" van een taal?',
                         ('Het programma dat de code van die taal omzet naar machinecode',False,'Dit staat niet in de tekst, maar de term voor een dergelijk programma is "compiler", niet "syntax"'),
                         ('De regels om een stuk code in die taal te ontleden',True,None),
                         ('De betekenis van een stuk code in die taal',False,'Syntax gaat alleen over de juiste vorm. Een stuk code kan uitvoerbaar maar onzinnig zijn zo lang het de syntax naleeft.'))]
xchk_ap_db_intro_content_wat_is_een_databank_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),
                                                  MultipleChoiceFormatCheck(),
                                                  MultipleChoiceAnswerCheck(None,wat_is_een_db_data)])),
        accepting_check=TrueCheck())

basisstructuren_data = [('Wat voor iets is "Persoon"?',
                         ('Een entiteittype',True,None),
                         ('Een entiteit',False,'Een specifieke persoon is een entiteit. Maar "Persoon" als geheel is iets anders.'),
                         ('Een relatie',False,'Een relatie is een pijl in de verzamelingennotatie...'),
                         ('Een relatietype',False,'Een relatietype is een groep pijlen die hetzelfde verband uitdrukken in de verzamelingennotatie...')),
                        ('Wat is, in de tekst, "William, Shakespeare, 1564"?',
                         ('Een tabel',False,'Een tabel kan meerdere stukken data bevatten. Dit is één stukje data dat één persoon voorstelt. De data over <em>alle</em> personen staat wel in een tabel.'),
                         ('Een record',True,None),
                         ('Een veld',False,'Een veld stemt overeen met een kolom in een tabel. Dus "Voornaam" of "Geboortejaar" is een veld.'))]
xchk_ap_db_intro_content_basisstructuren_van_een_relationele_database_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),
                                                  MultipleChoiceFormatCheck(),
                                                  MultipleChoiceAnswerCheck(None,basisstructuren_data)])),
        accepting_check=TrueCheck())

create_regex = r'''
\s*
[cC][rR][eE][aA][tT][eE]
\s+
[tT][aA][bB][lL][eE]
\s+
Boeken\(
\s*
Titel
\ 
[vV][aA][rR][cC][hH][aA][rR]\(50\)
\s*
,
\s*
JaarUitgave
\ 
[iI][nN][tT]
\s*
\)
;?
\s*
'''
xchk_ap_db_intro_content_create_statement_regex_check = RegexCheck(regex.compile(create_regex,flags=regex.VERBOSE))
xchk_ap_db_intro_content_create_statement_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),xchk_ap_db_intro_content_create_statement_regex_check])),
        accepting_check=TrueCheck())

diagramnotatie_data = [('Welke figuur levert informatie die we via de DML in het systeem zullen plaatsen?',
    ('De verzamelingennotatie',True,None),
    ('Het ERD',False,'Het ERD vertelt hoe onze tabellen er uitzien, maar tabellen aanmaken doen we met DDL-instructies')),
    ('Welke figuur levert informatie die we via de DDL in het systeem zullen plaatsen?',
    ('De verzamelingennotatie',False,'De verzamelingennotatie vertelt welke data we hebben, maar niet wat de structuur van die data is. De DDL wordt gebruikt om structuur vast te leggen.'),
    ('Het ERD',True,None))]
xchk_ap_db_intro_content_diagramnotatie_tabel_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),MultipleChoiceFormatCheck(),MultipleChoiceAnswerCheck(None,diagramnotatie_data)])),
        accepting_check=TrueCheck())

simpele_tekst_regex = r'''
\s*
[vV][aA][rR][cC][hH][aA][rR]\(\s*200\s*\)
\s*
[cC][hH][aA][rR]\(\s*7\s*\)
\s*
'''
simpele_tekst_regex_compiled = regex.compile(simpele_tekst_regex, flags=regex.VERBOSE)
xchk_ap_db_intro_content_datatypes_simpele_tekst_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),RegexCheck(simpele_tekst_regex_compiled)])),
        accepting_check=TrueCheck())

relationele_databank_data = [('Wat stellen we voor met tabellen?',
    ('Alleen "interessante gehelen"',False,'We stellen onder andere deze "interessante gehelen" voor, maar kijk in de tekst naar andere voorbeelden van tabellen...'),
    ('Alleen verbanden',False,'We stellen onder andere verbanden voor, maar kijk in de tekst naar andere voorbeelden van tabellen...'),
    ('"interessante gehelen" en verbanden daar tussen',True,None)),
    ('Waarvoor staat "SQL"?',
        ('Systematic Question Language',False,'Zoek opnieuw in de tekst'),
        ('Systematic Query Language',False,'Zoek opnieuw in de tekst'),
        ('Structured Question Language',False,'Zoek opnieuw in de tekst'),
        ('Structured Query Language',True,None)),
    ('Kan je SQL-code geschreven voor relationeel DBMS A ook gebruiken in relationeel DBMS?',
        ('Ja, sowieso',False,'SQL is een algemene afspraak, maar elk DBMS heeft een eigen dialect.'),
        ('Nee, (bijna) nooit',False,'Verschillende relationele databanken gebruiken verschillende dialecten van SQL, maar er is nog altijd een gemeenschappelijke basis'),
        ('Soms wel, soms niet',True,None))]
xchk_ap_db_intro_content_wat_is_een_relationele_database_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),
                                                  MultipleChoiceFormatCheck(),
                                                  MultipleChoiceAnswerCheck(None,relationele_databank_data)])),
        accepting_check=TrueCheck())

getallen_data = [
('Welk gegevenstype zou je gebruiken voor de hoeveelheid van een ingrediënt in een recept om thuis te bereiden, uitgedrukt in gram zonder cijfers na de komma?',
    ('TINYINT',False,'Met een <code>TINYINT</code> kan je hoeveelheden tussen -128 en 127 gram voorstellen. Negatieve waarden hebben geen zin in een recept en maximum 127 gram is erg weinig.'),
    ('TINYINT UNSIGNED',False,'Met een <code>TINYINT UNSIGNED</code> kan je hoeveelheden tussen 0 en 255 gram voorstellen. Vaak heb je meer dan 255 gram van iets nodig.'),
    ('SMALLINT',False,'Met een <code>SMALLINT</code> kan je hoeveelheden tussen -32768 en 32767 gram voorstellen. Negatieve waarden hebben geen zin.'),
    ('SMALLINT UNSIGNED',True,None),
    ('MEDIUMINT',False,'Met een <code>MEDIUMINT</code> kan je hoeveelheden tussen -8388608 en 8388607 gram voorstellen. Negatieve waarden hebben geen zin en dit bereik lijkt wat te groot, waardoor je misschien bytes verspilt.'),
    ('MEDIUMINT UNSIGNED',False,'Met een <code>MEDIUMINT UNSIGNED</code> kan je hoeveelheden tussen 0 en 16777215 gram voorstellen. Dat laatste getal is bijna 17 ton. Dit lijkt wat te veel voor een gewoon recept, waardoor je misschien bytes verspilt.'),
    ('INT',False,'Met een <code>INT</code> kan je hoeveelheden tussen -2147483648 en 2147483647 gram voorstellen. Negatieve waarden hebben geen zin en dit bereik lijkt te groot, waardoor je bytes verspilt.'),
    ('INT UNSIGNED',False,'Met een <code>INT UNSIGNED</code> kan je hoeveelheden tussen 0 en 4294967295 gram voorstellen. Dit bereik lijkt te groot, waardoor je bytes verspilt.'),
    ('BIGINT',False,'Met een <code>BIGINT</code> kan je hoeveelheden tussen -2^63 en 2^63 gram voorstellen. Negatieve waarden hebben geen zin en dit bereik lijkt te groot, waardoor je bytes verspilt.'),
    ('BIGINT UNSIGNED',False,'Met een <code>BIGINT UNSIGNED</code> kan je hoeveelheden tussen 0 en 2^64-1 gram voorstellen. Dit bereik lijkt te groot, waardoor je bytes verspilt.'),
    ),
('Welk gegevenstype zou je gebruiken voor de hoogte ten opzichte van de zeespiegel, uitgedrukt in m zonder cijfers na de komma?',
    ('TINYINT',False,'Met een <code>TINYINT</code> kan je hoeveelheden tussen -128 en 127 meter voorstellen. Negatieve waarden hebben geen zin in een recept en maximum 127 meter is erg weinig.'),
    ('TINYINT UNSIGNED',False,'Met een <code>TINYINT UNSIGNED</code> kan je hoeveelheden tussen 0 en 255 meter voorstellen. Je hebt negatieve waarden nodig en er zijn plaatsen veel hoger dan 255 m.'),
    ('SMALLINT',True,None),
    ('SMALLINT UNSIGNED',False,'Met een <code>UNSIGNED</code> datatype kan je geen diepte onder de zeespiegel voorstellen.'),
    ('MEDIUMINT',False,'Met een <code>MEDIUMINT</code> kan je hoeveelheden tussen -8388608 en 8388607 meter voorstellen. Dit bereik lijkt wat te groot, waardoor je misschien bytes verspilt.'),
    ('MEDIUMINT UNSIGNED',False,'Met een <code>MEDIUMINT UNSIGNED</code> kan je hoeveelheden tussen 0 en 16777215 meter voorstellen. Je hebt negatieve waarden nodig Dat laatste getal is bijna 17000 kilometer. Het hoogste punt ter wereld ligt op ongeveer 9km en het diepste ligt op ongeveer -11km, waardoor je misschien bytes verspilt.'),
    ('INT',False,'Met een <code>INT</code> kan je hoeveelheden tussen -2147483648 en 2147483647 meter voorstellen. Dit bereik lijkt te groot, waardoor je bytes verspilt.'),
    ('INT UNSIGNED',False,'Met een <code>INT UNSIGNED</code> kan je hoeveelheden tussen 0 en 4294967295 meter voorstellen. Je hebt negatieve waarden nodig om diepte onder de zee voor te stellen.'),
    ('BIGINT UNSIGNED',False,'Met een <code>BIGINT UNSIGNED</code> kan je hoeveelheden tussen 0 en 2^64-1 meter voorstellen. Je hebt negatieve waarden nodig om diepte onder de zee voor te stellen.'),
    )]

xchk_ap_db_intro_content_datatypes_gehele_getallen_strat = Strategy(
        refusing_check=Negation(ConjunctiveCheck([FileExistsCheck(),
                                                  MultipleChoiceFormatCheck(),
                                                  MultipleChoiceAnswerCheck(None,getallen_data)])),
        accepting_check=TrueCheck())
