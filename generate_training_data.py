#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator tréninkových dat pro spamový klasifikátor
Generuje 300 e-mailů v češtině (200 HAM, 100 SPAM)
"""

import random

def generate_ham_emails():
    """Generuje 200 HAM e-mailů"""
    ham_emails = []
    
    # 70 newsletterů / promo pro stávající zákazníky
    newsletters = [
        "Vážený zákazníku, máme pro vás speciální nabídku na nové produkty se slevou 20%. Navštivte náš e-shop.",
        "Dobrý den, jako člen našeho věrnostního programu máte nárok na exkluzivní slevy. Podívejte se na naší nabídku.",
        "Ahoj, rádi bychom vás pozvali na akci výprodeje letní kolekce. Přijďte si vybrat své oblíbené kousky.",
        "Dobry den, tento tyden mame specialni akci na elektroniku. Nakupujte online s dopravou zdarma.",
        "Vážená paní, děkujeme za vaši věrnost. Připravili jsme pro vás dárkový poukaz v hodnotě 500 Kč.",
        "Milý zákazníku, nová kolekce podzimní módy je tady. Prohlédněte si novinky na našich webových stránkách.",
        "Dobrý večer, zaregistrovali jsme vaši objednávku. Těšíme se na vaši návštěvu v našem obchodě.",
        "Ahoj, máme pro tebe zajímavou nabídku na fitness produkty. Slevy až 30% na vybrané položky.",
        "Vazeny zakazniku, dekujeme za nakup u nas. Urcite si prohlednete nase novinky v sekci doplnky.",
        "Dobrý den, jako člen našeho klubu dostáváte měsíční newsletter s tipy a radami. Přejeme příjemné čtení.",
        "Milá zákaznice, právě jsme přidali nové produkty do naší nabídky. Podívejte se, co pro vás máme.",
        "Ahoj, těšíme se na vaši další návštěvu. Nezapomeňte na své bonusové body z minulé objednávky.",
        "Dobrý den, poslední dny našeho letního výprodeje. Nakupujte ještě dnes a využijte slevy.",
        "Vážená zákaznice, rádi bychom vás informovali o nových službách, které jsme připravili.",
        "Dobry vecer, muzete se tesit na nasi jarni kolekci. Registrujte se a ziskejte pristup jako prvni.",
        "Ahoj, díky za tvou registraci do našeho programu. Brzy ti pošleme více informací.",
        "Dobrý den, právě jsme spustili nový e-shop. Přijďte se podívat na naši aktuální nabídku.",
        "Milý zákazníku, máme pro vás speciální nabídku na vánoční dárky. Nakupujte s jistotou.",
        "Vážený pane, jako stálému zákazníkovi vám nabízíme prioritní přístup k našim akcím.",
        "Ahoj, tento měsíc si můžeš užít slevy na vybrané knihy v našem obchodě. Zastavte se.",
        "Dobrý den, připravili jsme pro vás průvodce výběrem správných produktů. Stáhněte si ho zdarma.",
        "Vazena zakaznice, dnes startuje nase black friday akce. Pripravte se na nejlepsi slevy roku.",
        "Milá paní, děkujeme za vaši zpětnou vazbu. Vaše připomínky jsou pro nás důležité.",
        "Ahoj, právě jsme přidali nové funkce do naší aplikace. Aktualizujte si ji a vyzkoušejte novinky.",
        "Dobrý večer, máme novou kolekci sportovního oblečení. Prohlédněte si novinky na webu.",
        "Vážený zákazníku, nabízíme vám prodloužení záruky na vámi zakoupené zboží. Více informací na našich stránkách.",
        "Dobry den, nase zimni kolekce prave dorazila do skladu. Objednavejte online s dopravou zdarma.",
        "Ahoj, chceš být informován o našich akcích jako první? Aktivuj si notifikace v aplikaci.",
        "Dobrý den, poslední šance získat slevu 25% na vybrané produkty. Akce končí o půlnoci.",
        "Milý zákazníku, těšíme se na vaši příští návštěvu v našem obchodě. Přejeme hezký den.",
        "Vážená zákaznice, právě jsme přidali nové barvy do naší kolekce. Podívejte se na web.",
        "Ahoj, dekujeme za tvuj nakup. Tvoje balicek bude dorucen do 3 pracovnich dnu.",
        "Dobrý den, rádi bychom vás pozvali na prezentaci našich nových služeb příští týden.",
        "Vazeny zakazniku, muzete se tesit na nasi vanoce akci. Sledujte nase stranky pro vice informaci.",
        "Ahoj, máme pro tebe speciální nabídku na kosmetiku. Využij slevu 15% s kódem BEAUTY15.",
        "Dobrý večer, právě jsme otevřeli novou pobočku ve vašem městě. Přijďte nás navštívit.",
        "Milá zákaznice, připravili jsme pro vás průvodce naší nabídkou. Stáhněte si ho z našeho webu.",
        "Vážený pane, váš věrnostní program byl úspěšně aktivován. Začněte sbírat body už dnes.",
        "Ahoj, nova kolekce tricek je uz dostupna. Objednej si sve oblibene kusy jeste dnes.",
        "Dobrý den, děkujeme za vaši objednávku. Budeme vás informovat o průběhu expedice.",
        "Vážená zákaznice, jako náš stálý zákazník získáváte bonus 100 Kč na další nákup.",
        "Dobry den, tento vikend mame akci na domaci spotrebice. Navstivte nas v prodejne.",
        "Ahoj, právě jsme přidali nové recepty do naší sekce inspirace. Zkus je vyzkoušet.",
        "Dobrý večer, máme pro vás speciální nabídku na elektronické knihy. Nakupujte se slevou.",
        "Milý zákazníku, těšíme se, že využijete naše služby. Přejeme vám příjemný den.",
        "Vážený pane, právě jsme spustili nový věrnostní program. Zaregistrujte se ještě dnes.",
        "Ahoj, dekujeme za registraci. Tvuj ucet byl uspesne vytvoren a muzesh zacit nakupovat.",
        "Dobrý den, máme pro vás speciální balíček služeb za zvýhodněnou cenu. Více na webu.",
        "Vazena zakaznice, nase podzimni akce prave zacina. Objednavejte s dopravou zdarma.",
        "Ahoj, chceš získat slevu 10%? Doporuč nás svým přátelům a získej bonus.",
        "Dobrý večer, právě jsme přidali nové produkty do kategorie domácnost. Mrkněte na ně.",
        "Milá paní, připravili jsme pro vás jarní kolekci. Prohlédněte si novinky na našich stránkách.",
        "Vážený zákazníku, máme pro vás speciální nabídku na auto-moto produkty se slevou 20%.",
        "Dobry den, muzete se tesit na nasi novou kolekci kabelek. Prave dorazila do skladu.",
        "Ahoj, tento týden máme akci na vybrané hry a hračky. Nakupuj online a ušetři.",
        "Dobrý den, rádi bychom vás informovali o změnách v našem sortimentu. Více na webu.",
        "Vážená zákaznice, jako členka našeho klubu máte nárok na bezplatnou dopravu.",
        "Ahoj, dekujeme za tvuj nakup u nas. Doufame, ze jsi spokojena s vybranym zbozim.",
        "Dobrý večer, právě jsme spustili nový blog s tipy a radami. Přijďte si přečíst články.",
        "Milý zákazníku, máme pro vás speciální nabídku na zimní oblečení. Slevy až 40%.",
        "Vážený pane, váš nákup byl úspěšně zpracován. Děkujeme za vaši objednávku.",
        "Dobry den, nase letni akce prave zacina. Vyuzte slevy na vybranou elektroniku.",
        "Ahoj, právě jsme přidali nové barvy do naší kolekce bot. Podívej se na web.",
        "Dobrý den, připravili jsme pro vás katalog nové kolekce. Můžete si ho stáhnout online.",
        "Vážená zákaznice, těšíme se na vaši další návštěvu. Přejeme příjemný víkend.",
        "Ahoj, muzete se tesit na nasi valentynskou akci. Pripravte se na nejlepsi darky.",
        "Dobrý večer, máme pro vás speciální nabídku na dětské oblečení. Nakupujte se slevou.",
        "Milá paní, právě jsme spustili nový program odměn. Zaregistrujte se a začněte sbírat body.",
        "Vážený zákazníku, děkujeme za vaši věrnost. Nabízíme vám exkluzivní přístup k novinkám.",
        "Dobry den, tento mesic mame akci na zahradni nabytek. Objednavejte s dopravou zdarma."
    ]
    
    # 70 systémových e-mailů (faktura, změna hesla, potvrzení objednávky)
    system_emails = [
        "Vaše objednávka č. 12345 byla úspěšně přijata. Očekávaný termín doručení je 3-5 pracovních dnů.",
        "Dobrý den, vaše heslo bylo úspěšně změněno. Pokud jste tuto změnu neprovedli vy, kontaktujte nás.",
        "Faktura č. 2024001 za služby v březnu je připravena ke stažení ve vašem účtu.",
        "Potvrzujeme platbu částky 1250 Kč za objednávku č. 67890. Děkujeme za váš nákup.",
        "Vase objednavka byla expedovana. Sledovaci cislo: CZ123456789. Ocekavane doruceni do 2 dnu.",
        "Dobrý den, váš účet byl úspěšně vytvořen. Přihlašovací údaje najdete v tomto e-mailu.",
        "Upozorňujeme vás, že platnost vašeho předplatného vyprší za 7 dní. Prodlužte si ho online.",
        "Vaše zásilka byla doručena na výdejní místo. Můžete si ji vyzvednout během 7 dnů.",
        "Dobrý den, vaše platba byla zpracována. Účtenku si můžete stáhnout ve vašem profilu.",
        "Potvrzujeme rezervaci na datum 15. května 2024. Těšíme se na vaši návštěvu.",
        "Vase heslo bylo obnoveno. Pokud jste o obnovu nezadali, kontaktujte nasi podporu okamzite.",
        "Faktura za elektřinu za období leden-březen je k dispozici v zákaznickém portálu.",
        "Dobrý den, vaše objednávka č. 54321 byla úspěšně zrušena. Peníze budou vráceny do 5 dnů.",
        "Potvrzujeme přijetí vaší reklamace č. R-2024-789. Vyřízení do 30 dnů.",
        "Váš účet byl dočasně uzamčen z bezpečnostních důvodů. Pro odemčení navštivte náš web.",
        "Dobrý večer, vaše zásilka byla předána kurýrovi. Očekávejte doručení do 24 hodin.",
        "Faktura c. 2024055 za mobilni sluzby je pripravena. Castka k uhrade: 450 Kc. Splatnost: 14 dni.",
        "Potvrzujeme změnu vašich kontaktních údajů. Data byla úspěšně aktualizována.",
        "Vaše objednávka č. 11223 je připravena k vyzvednutí na naší pobočce. Přijďte kdykoliv.",
        "Dobrý den, váš tarif byl úspěšně změněn. Nové podmínky platí od prvního dne příštího měsíce.",
        "Upozorňujeme vás, že váš kredit vyprší za 14 dní. Dobijte si ho přes náš portál.",
        "Vase platba byla zamítnuta. Zkontrolujte prosím údaje karty a zkuste to znovu.",
        "Faktura za připojení k internetu je připravena. Stáhněte si ji ve vašem zákaznickém účtu.",
        "Dobrý den, vaše zásilka byla vrácena odesílateli. Kontaktujte nás pro více informací.",
        "Potvrzujeme změnu vašeho e-mailu. Od této chvíle používejte novou adresu pro přihlášení.",
        "Váš úkol byl úspěšně odeslán. Odpověď obdržíte do 48 hodin.",
        "Dobry den, vase objednavka c. 99887 byla uspesne dodana. Muzete ji hodnotit ve vasem uctu.",
        "Upozorňujeme, že jste dosáhli limitu pro stažení dat. Navyšte si ho ve vašem profilu.",
        "Vaše zpráva byla odeslána. Odpovíme vám co nejdříve.",
        "Dobrý večer, vaše smlouva byla úspěšně prodloužena. Děkujeme za vaši důvěru.",
        "Faktura č. 2024078 za webhosting je k dispozici. Částka: 299 Kč. Zaplaťte do 10 dnů.",
        "Potvrzujeme přijetí vaší platby. Služby budou aktivovány do 24 hodin.",
        "Váš účet byl ověřen. Můžete začít používat všechny naše služby bez omezení.",
        "Dobry den, vase sluzby byly obnoveny. Dekujeme za uhrazeni faktury.",
        "Upozorňujeme, že váš balíček čeká na poště. Vyzvedněte si ho do 15 dnů.",
        "Vaše objednávka č. 44556 byla stornována na základě vašeho požadavku. Peníze vrátíme do týdne.",
        "Dobrý den, vaše zpětná vazba byla zaznamenána. Děkujeme za váš čas.",
        "Faktura za plyn za období duben-červen je připravena ke stažení. Splatnost: 21 dnů.",
        "Potvrzujeme změnu vašeho dodacího místa. Příští zásilky budou doručeny na novou adresu.",
        "Váš certifikát byl úspěšně vydán. Můžete si ho stáhnout ve vašem profilu.",
        "Dobry vecer, vase rezervace byla potvrzena. Tešime se na vasi navstevu 20. kvetna.",
        "Upozorňujeme, že platba nebyla připsána. Zkontrolujte prosím údaje a zkuste znovu.",
        "Vaše smlouva vyprší za 30 dní. Prodlužte si ji online a využijte naši akci.",
        "Dobrý den, vaše registrace byla dokončena. Přihlašte se pomocí vašeho e-mailu a hesla.",
        "Faktura č. 2024099 za telefonní služby je k dispozici. Částka: 550 Kč. Uhraďte do 14 dnů.",
        "Potvrzujeme vrácení zboží. Peníze budou připsány na váš účet do 10 pracovních dnů.",
        "Váš profil byl úspěšně aktualizován. Nové údaje jsou již platné.",
        "Dobrý večer, vaše předplatné bylo zrušeno. Děkujeme za využívání našich služeb.",
        "Upozorneni: Vase sluzby budou pozastaveny za 5 dnu kvuli neuhrazene fakture.",
        "Vaše zásilka je na cestě. Sledujte ji pomocí čísla CS987654321 na našem webu.",
        "Dobrý den, váš požadavek byl zpracován. Výsledek najdete ve vašem zákaznickém účtu.",
        "Faktura za služby pojištění je připravena. Stáhněte si ji a uhraďte do 30 dnů.",
        "Potvrzujeme přijetí vaší žádosti. Vyřízení do 14 pracovních dnů.",
        "Váš účet byl úspěšně smazán. Všechna vaše data byla odstraněna dle GDPR.",
        "Dobry den, vase objednavka c. 33445 je pripravena k vyzvednuti. Prijdte behem 7 dnu.",
        "Upozorňujeme, že vaše karta vyprší koncem tohoto měsíce. Objednejte si novou online.",
        "Vaše zásilka nemohla být doručena. Kontaktujte nás pro další pokus o doručení.",
        "Dobrý večer, vaše transakce byla zamítnuta z bezpečnostních důvodů. Kontaktujte banku.",
        "Faktura c. 2024111 za cloudove sluzby je k dispozici. Castka: 899 Kc. Splatnost: 7 dnu.",
        "Potvrzujeme změnu vašeho telefonního čísla. Nové číslo je již aktivní.",
        "Váš kupón byl úspěšně uplatněn. Sleva 15% bude automaticky odečtena při objednávce.",
        "Dobrý den, vaše doména byla úspěšně prodloužena na další rok. Děkujeme.",
        "Upozorňujeme, že váš certifikát SSL vyprší za 14 dní. Obnovte ho na našem portálu.",
        "Vaše žádost o výplatu byla schválena. Peníze budou převedeny do 3 pracovních dnů.",
        "Dobry vecer, vase sluzby byly upgradovany. Nove funkce jsou uz dostupne ve vasem uctu.",
        "Potvrzujeme přijetí vaší stížnosti. Vyřízení do 30 dnů dle reklamačního řádu.",
        "Váš newsletter byl úspěšně odhlášen. Již nebudete dostávat naše e-maily.",
        "Dobrý den, vaše licence byla prodloužena. Platnost do 31. prosince 2025.",
        "Faktura za parkovací služby je připravena. Uhraďte prosím 200 Kč do 5 dnů.",
        "Potvrzujeme zrušení vaší služby. Přístup bude ukončen koncem tohoto měsíce."
    ]
    
    # 40 osobních nebo pracovních komunikací
    personal_work = [
        "Ahoj Petro, zítra máme schůzku ve tři odpoledne. Nezapomeň si vzít materiály k projektu.",
        "Dobrý den, posílám vám zprávu o dokončení úkolu. Reporty jsou připraveny ke kontrole.",
        "Ahoj, chces jit vecer na pivo? Mohl bych se bavit o tom vikendu na chate.",
        "Vazeny pane, rad bych vam posknul vice informaci o nasem projektu. Muzeme se sejit zitra?",
        "Ahoj, díky za tvůj e-mail. Odpovím ti na tvoje otázky do konce týdne.",
        "Dobrý den, chtěl jsem vás informovat, že schůzka byla přesunuta na příští úterý.",
        "Ahoj Marto, mohl bys mi poslat ten dokument, o kterém jsme mluvili? Díky moc.",
        "Vážená paní, rád bych se zeptal na termín naší spolupráce. Můžeme si zavolat?",
        "Ahoj, posílám ti fotky z dovolené. Doufám, že se ti budou líbit.",
        "Dobry den, mohl byste mi poslat prezentaci z minule porady? Dekuji.",
        "Ahoj Jano, nezapomen na rodinnou oslavu v sobotu. Těšíme se na tebe.",
        "Dobrý večer, chtěl jsem se zeptat, jestli můžete pomoct s tím projektem.",
        "Ahoj, dnes budu pozde. Muzem se sejit az zitra rano?",
        "Vážený pane, posílám vám návrh smlouvy ke kontrole. Dejte mi prosím vědět.",
        "Ahoj Pavle, mohl bys mi poradit s tím problémem? Nevím, jak ho vyřešit.",
        "Dobrý den, rád bych s vámi prodiskutoval termíny nového projektu. Kdy máte čas?",
        "Ahoj, díky za pozvánku. Bohužel tam nebudu moct, mám již jiný program.",
        "Dobry vecer, potreboval bych od vas potvrzeni do pátku. Je to mozne?",
        "Ahoj Kláro, nesla bys mi půjčit tu knihu? Velmi bych ji potřeboval.",
        "Dobrý den, posílám vám výsledky z minulého týdne. Všechno je v přiložených souborech.",
        "Ahoj, pojd s námi zítra na večeři. Budeme na tom novém místě v centru.",
        "Vážená paní, děkuji za váš e-mail. Odpovím vám co nejdříve.",
        "Ahoj Tome, mohl bys mi zavolat? Potreboval bych s tebou neco probrat.",
        "Dobrý den, chtěl jsem se zeptat na váš názor k té věci, o které jsme mluvili.",
        "Ahoj, zitra mam dovolenou. Muzeme to prehodit na pristi tyden?",
        "Vážený pane, posílám vám aktualizovaný harmonogram. Zkontrolujte ho prosím.",
        "Ahoj Lenko, díky za pomoc s tím projektem. Opravdu si toho vážím.",
        "Dobrý večer, mohl byste mi poslat kontakt na toho dodavatele? Dekuji.",
        "Ahoj, uz jsi dorazil? Cekam na tebe u vchodu.",
        "Dobrý den, rád bych vás pozval na pracovní oběd příští týden. Máte čas?",
        "Ahoj Míšo, nezapomeň na to, co jsme si slíbili. Díky za spolupráci.",
        "Vážená paní, děkuji za váš čas a trpělivost. Vážím si toho.",
        "Ahoj, pošli mi prosím tu adresu. Zapomněl jsem si ji poznamenat.",
        "Dobry den, muzete mi poslat ten rozpocet? Potrebuji ho do zitrejsi porady.",
        "Ahoj Dane, šel bys dnes odpoledne na kávu? Chtěl bych si s tebou popovídat.",
        "Dobrý večer, posílám vám návrh na schůzku. Dejte mi prosím vědět, jestli vám to vyhovuje.",
        "Ahoj, uz si ty materialy pripravil? Budeme je potrebovat v pondeli.",
        "Vážený pane, rád bych s vámi probral detaily smlouvy. Můžeme si zavolat zítra?",
        "Ahoj Jirko, jak se ti daří? Dlouho jsme se neviděli. Dáme si někdy pivo?",
        "Dobrý den, chtěl jsem vás informovat o změně termínu schůzky. Vyhovuje vám středa?"
    ]
    
    # 20 neutrálních oznámení
    neutral = [
        "Upozorňujeme, že zítra bude v budově odstávka elektřiny od 8:00 do 12:00.",
        "Dobrý den, informujeme vás o změně provozních hodin. Nová doba: Po-Pá 9-17.",
        "V sobotu 15. března proběhne údržba systému. Služby budou nedostupné 2-4 hodiny.",
        "Vazeni zakaznisi, tento tyden mame v provozu zkracenou pracovni dobu kvuli svatku.",
        "Upozorňujeme, že parkování bude dočasně omezeno kvůli stavebním pracím.",
        "Dobrý den, informujeme vás o aktualizaci našich obchodních podmínek. Platí od 1.4.",
        "V období letních prázdnin budeme zavřeni od 1. do 15. srpna. Děkujeme za pochopení.",
        "Upozorňujeme na změnu kontaktních údajů. Nové telefonní číslo: 224 567 890.",
        "Dobry den, tento mesic probiha inventura. Muze dojit k prodlevam pri vyrizovani objednavek.",
        "Informujeme vás o plánované údržbě webu. Proběhne v noci z pátku na sobotu.",
        "V pondělí 10. května je státní svátek. Kanceláře budou uzavřeny.",
        "Upozorňujeme, že některé služby budou dočasně nedostupné kvůli upgradu systému.",
        "Dobrý den, informujeme o změně bankovního účtu pro platby. Nové číslo v příloze.",
        "V období vánočních svátků bude provoz omezen. Otevřeno opět od 2. ledna.",
        "Upozorneni: Dnes probiha skoleni zamestnancu. Odpovedi na dotazy budou zpozdene.",
        "Dobrý večer, informujeme vás o změně adresy naší pobočky. Nová adresa v e-mailu.",
        "V pátek bude naše kancelář uzavřena kvůli firemní akci. Omlouvame se za komplikace.",
        "Upozorňujeme na změnu dodacích podmínek. Nové podmínky platí od příštího měsíce.",
        "Dobry den, informujeme vas o presunu nasi pobocky do novych prostor. Adresa v priloze.",
        "Dnes večer mezi 20:00 a 22:00 proběhne plánovaná údržba databází. Děkujeme za trpělivost."
    ]
    
    ham_emails.extend(newsletters)
    ham_emails.extend(system_emails)
    ham_emails.extend(personal_work)
    ham_emails.extend(neutral)
    
    return ham_emails

def generate_spam_emails():
    """Generuje 100 SPAM e-mailů"""
    spam_emails = []
    
    # 40 realistických phishingů (ověření účtu, bezpečnost)
    phishing = [
        "Vážený kliente, váš účet vyžaduje okamžité ověření. Pokračujte na csob-overeni-2024.cz do 48 hodin.",
        "Dobrý den, detekovali jsme podezřelou aktivitu na vašem účtu. Ověřte své údaje zde: kb-bezpecnost.cz",
        "Váš účet byl dočasně zablokován. Pro odemčení navštivte: ceska-sporitelna-overeni.cz",
        "Vazeny zakazniku, prosim potvrdte sve osobni udaje do 24 hodin na: csob-verifikace.cz",
        "Dobrý den, váš e-mail vyžaduje aktualizaci bezpečnostních nastavení. Klikněte zde: email-bezpecnost.cz",
        "Upozornění: Váš účet bude smazán za 48 hodin. Ověřte identitu na: ucet-overeni.cz",
        "Vaše heslo vyprší za 24 hodin. Aktualizujte ho na: bezpecne-heslo-update.cz",
        "Dobrý den, váš účet potřebuje revalidaci. Pokračujte na: banka-revalidace.cz do konce týdne.",
        "Detekovali jsme neautorizovaný přístup k vašemu účtu. Změňte heslo zde: prihlaseni-bezpecnost.cz",
        "Vazeny klient, vas ucet bude pozastaven. Overste se na: banka-aktivace-2024.cz ihned.",
        "Dobrý večer, váš profil vyžaduje potvrzení. Klikněte na: profil-potvrzeni.cz do 12 hodin.",
        "Váš účet byl nahlášen jako podezřelý. Ověřte totožnost: banka-totožnost.cz dnes.",
        "Upozorňujeme na neobvyklou aktivitu. Zkontrolujte svůj účet: kontrola-uctu.cz okamžitě.",
        "Dobrý den, vaše data jsou neúplná. Doplňte informace na: doplneni-udaju.cz do zítra.",
        "Váš bezpečnostní certifikát vypršel. Obnovte ho zde: certifikat-obnova.cz bez prodlení.",
        "Vazeny uzivatel, vas ucet potrebuje verifikaci. Postupujte na: verifikace-uctu.cz ted.",
        "Dobrý den, zjistili jsme porušení bezpečnosti. Změňte údaje: zmena-udaju.cz ihned.",
        "Váš účet bude uzavřen za 24 hodin. Zabráníte tomu na: ucet-zachrana.cz dnes.",
        "Upozornění: Váš přístup bude omezen. Ověřte se na: overeni-pristupu.cz do půlnoci.",
        "Dobrý večer, váš účet vyžaduje okamžitou akci. Pokračujte: akce-ucet.cz bez odkladu.",
        "Váš email bude deaktivován. Předejte na: email-aktivace.cz do 48 hodin.",
        "Vazeny zakazniku, detekovali jsme pokus o prihlaseni. Overste na: pokus-prihlaseni.cz.",
        "Dobrý den, vaše platební údaje jsou zastaralé. Aktualizujte: platba-update.cz dnes.",
        "Váš profil byl napadnut. Zabezpečte ho zde: zabezpeceni-profilu.cz okamžitě.",
        "Upozorňujeme na expiraci účtu. Prodlužte ho na: prodlouzeni-uctu.cz do zítra.",
        "Dobrý den, váš účet vyžaduje autentizaci. Pokračujte: autentizace.cz bez prodlení.",
        "Váš přístup byl omezen kvůli bezpečnosti. Obnovte: obnova-pristupu.cz ihned.",
        "Vazeny klient, vas ucet je pozastaven. Reaktivujte na: reaktivace-uctu.cz dnes.",
        "Dobrý večer, potřebujeme ověřit vaši totožnost. Navštivte: totožnost-overeni.cz ted.",
        "Váš účet má nedokončenou verifikaci. Dokončete: dokonceni-verifikace.cz do 24 hodin.",
        "Upozornění: Váš profil bude smazán. Zabráníte na: profil-zruseni.cz okamžitě.",
        "Dobrý den, zjistili jsme podezřelou transakci. Ověřte: transakce-overeni.cz dnes.",
        "Váš účet potřebuje bezpečnostní upgrade. Pokračujte: bezpecnost-upgrade.cz ihned.",
        "Vazeny uzivatel, detekovali jsme riziko. Chraňte se na: ochrana-uctu.cz ted.",
        "Dobrý den, vaše údaje jsou v ohrožení. Aktualizujte: udaje-aktualizace.cz dnes.",
        "Váš email vyžaduje potvrzení. Potvrďte na: email-potvrzeni.cz do půlnoci.",
        "Upozorňujeme na pokus o hacknutí. Zabezpečte se: hacknutí-prevence.cz okamžitě.",
        "Dobrý večer, váš účet byl kompromitován. Změňte údaje: kompromis-udaje.cz ihned.",
        "Váš přístup bude zablokován. Předejděte na: blokovani-prevence.cz do 12 hodin.",
        "Vazeny klient, vase heslo je slabe. Zmente ho na: heslo-posílení.cz dnes."
    ]
    
    # 30 problémů s platbou nebo doručením
    payment_delivery = [
        "Dobrý den, vaše zásilka nemůže být doručena. Uhraďte poplatek 49 Kč na: doruceni-poplatek.cz",
        "Vaše balík čeká na celnici. Zaplaťte clo 120 Kč zde: celni-poplatek.cz do zítřka.",
        "Upozornění: Vaše platba selhala. Aktualizujte údaje karty na: platba-oprava.cz ihned.",
        "Dobry den, vase zasilka byla zadrzena. Uhrdte 80 Kc na: zasilka-uvolneni.cz dnes.",
        "Váš balík má problém s adresou. Potvrďte doručení na: adresa-potvrzeni.cz do večera.",
        "Dobrý večer, vaše transakce byla zamítnuta. Zopakujte platbu: transakce-oprava.cz ted.",
        "Vaše zásilka potřebuje potvrzení. Potvrďte na: potvrzeni-doruceni.cz do 24 hodin.",
        "Upozorňujeme na neúspěšnou platbu. Uhraďte na: neuspesna-platba.cz okamžitě.",
        "Dobrý den, váš balík vyžaduje dodatečný poplatek. Zaplaťte: dodatecny-poplatek.cz dnes.",
        "Váš převod selhal. Zkuste znovu na: prevod-opakovat.cz bez prodlení.",
        "Vazena zakaznice, vase doruceni je pozastaveno. Pokracujte: doruceni-pokracovani.cz.",
        "Dobrý den, vaše faktura je po splatnosti. Uhraďte: faktura-uhrada.cz do zítřka.",
        "Váš balík nemá správnou cenu. Doplaťte 65 Kč: cena-doplatok.cz ihned.",
        "Upozornění: Vaše platební údaje jsou neplatné. Opravte: udaje-oprava.cz dnes.",
        "Dobrý večer, váš účet má dluh 250 Kč. Uhraďte: dluh-uhrada.cz do půlnoci.",
        "Vaše zásilka je blokována. Uvolněte ji na: zasilka-odblokovani.cz okamžitě.",
        "Dobry den, vase karta byla zamitnuta. Zkuste jinou: karta-oprava.cz ted.",
        "Váš balík má poškozené štítky. Potvrďte údaje: stitky-oprava.cz do 12 hodin.",
        "Upozorňujeme na problém s doručením. Vyřešte: problem-doruceni.cz dnes.",
        "Dobrý den, vaše platba čeká na potvrzení. Potvrďte: platba-potvrzeni.cz ihned.",
        "Váš účet má neuhrazenou částku. Zaplaťte: castka-uhrada.cz do zítřka.",
        "Vazeny zakazniku, vase zasilka vyzaduje overeni. Overste: zasilka-overeni.cz.",
        "Dobrý večer, vaše transakce je pozastavena. Obnovte: transakce-obnova.cz dnes.",
        "Váš balík nemůže být zpracován. Pokračujte: zpracovani-baliku.cz okamžitě.",
        "Upozornění: Váš převod vyžaduje autorizaci. Autorizujte: prevod-autorizace.cz ted.",
        "Dobrý den, vaše faktura má nesrovnalost. Zkontrolujte: faktura-kontrola.cz ihned.",
        "Váš účet je v mínusu. Doplňte kredit: kredit-doplneni.cz do půlnoci.",
        "Dobry den, vase doruceni ma problem s celnicí. Vyrezte: celnice-vyrizeni.cz.",
        "Váš balík vyžaduje potvrzení příjemce. Potvrďte: prijemce-potvrzeni.cz dnes.",
        "Upozorňujeme na chybějící údaje k platbě. Doplňte: udaje-doplneni.cz okamžitě."
    ]
    
    # 30 investičních / finančních podvodů psaných nenápadně
    investment_scams = [
        "Dobrý den, máme pro vás investiční příležitost s garantovaným výnosem 15% ročně. Více info na investice-garantovane.cz",
        "Vážený investore, náš fond dosáhl výnosu 25% za poslední rok. Přidejte se k nám: fond-vynos.cz",
        "Ahoj, znáš někoho, kdo by chtěl investovat do kryptoměn? Mám osvědčenou strategii s vysokými zisky.",
        "Dobry den, nabizime investice do nemovitosti s vynosem 20% rocne. Bezpecne a overene.",
        "Dobrý večer, máte zájem o pasivní příjem? Naše investice přináší stabilní výnosy. Kontakt na finalni-prijem.cz",
        "Vážený klient, dostali jste pozvánku do exkluzivního investičního klubu. Registrace na klub-investory.cz",
        "Ahoj, investoval jsem 50 tisíc a za měsíc mám 75 tisíc. Chceš se přidat? Napiš mi.",
        "Dobrý den, nabízíme investice do solárních elektráren s návratností 3 roky. Více na solarni-investice.cz",
        "Vazeny zajem, nase spolecnost garantuje zhodnoceni vasich uspor o 18% za rok.",
        "Dobrý večer, máte volné prostředky? Investujte je s námi a získejte až 22% ročně.",
        "Ahoj, hledám investory do startupů. Již máme 3 úspěšné projekty. Zajímá tě to?",
        "Dobrý den, nabízíme investice do zlata s minimálním rizikem. Výnosy až 12% ročně.",
        "Vážený pane, máme pro vás speciální nabídku na investice do kryptoměn s pojištěním.",
        "Ahoj, znam zpusob jak vydelat na forexu. Ukazal bych ti strategii, ktera funguje.",
        "Dobrý den, investice do našich projektů jsou zajištěné státní zárukou. Info na statni-investice.cz",
        "Vážený investore, připojte se k tisícům spokojených klientů. Průměrný výnos 16% ročně.",
        "Ahoj, mám tip na investici do bioplynu. Garantovaný výnos a ekologické. Zajímá tě to?",
        "Dobrý večer, nabízíme investice s garantovanou návratností. Žádné skryté poplatky.",
        "Dobry den, nase investicni portfolio prinasi stabilni zisky. Minimalni vklad 20 tisic Kc.",
        "Vážený klient, máte možnost investovat do luxusních nemovitostí v zahraničí. Výnosy až 20%.",
        "Ahoj, znáš kryptoměnu která právě startuje? Můžeš být mezi prvními investory.",
        "Dobrý den, nabízíme investice do umění s vysokým potenciálem růstu hodnoty.",
        "Vazeny zajem, nase investice jsou overene a bezpecne. Prumerny vynos 14% rocne.",
        "Dobrý večer, máte zájem o investice do renewable energy? Výnosy až 17% ročně.",
        "Ahoj, investuješ někam? Mám skvělou příležitost s minimálním rizikem a vysokým výnosem.",
        "Dobrý den, nabízíme portfolio diverzifikovaných investic. Garantovaný růst vašich úspor.",
        "Vážený investore, přidejte se k našemu programu a vydělávejte i ve spánku.",
        "Ahoj, mám kontakt na investiční skupinu s úspěšností 95%. Chceš víc informací?",
        "Dobry den, investice do nasich projektu jsou pojistene proti ztrátě. Stabilni vynosy.",
        "Dobrý večer, máme limitovanou nabídku na investice s bonusem 5% navíc. Rychle rozhodnout."
    ]
    
    spam_emails.extend(phishing)
    spam_emails.extend(payment_delivery)
    spam_emails.extend(investment_scams)
    
    return spam_emails

def main():
    """Hlavní funkce generující tréninkový soubor"""
    print("Generuji tréninková data...")
    
    # Generuj e-maily
    ham_emails = generate_ham_emails()
    spam_emails = generate_spam_emails()
    
    # Zkontroluj počty
    assert len(ham_emails) == 200, f"HAM: očekáváno 200, získáno {len(ham_emails)}"
    assert len(spam_emails) == 100, f"SPAM: očekáváno 100, získáno {len(spam_emails)}"
    
    # Vytvoř seznam všech e-mailů s labely
    all_emails = []
    for email in ham_emails:
        all_emails.append(f"0,{email}")
    for email in spam_emails:
        all_emails.append(f"1,{email}")
    
    # Zamíchej e-maily
    random.shuffle(all_emails)
    
    # Ulož do souboru
    output_file = "training_data.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for email in all_emails:
            f.write(email + '\n')
    
    print(f"Hotovo! Vygenerováno {len(all_emails)} e-mailů do souboru {output_file}")
    print(f"  - HAM: 200 e-mailů (label 0)")
    print(f"  - SPAM: 100 e-mailů (label 1)")
    print(f"\nFormát: <label>,<text_emailu>")
    print(f"  0 = HAM (legitimní e-mail)")
    print(f"  1 = SPAM (phishing/podvod)")

if __name__ == "__main__":
    main()
