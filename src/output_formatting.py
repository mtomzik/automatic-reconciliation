# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def prepare_text(text):
    return  text.lstrip().strip()

def work(text) :
    marks = [".", ",", ";", "?", "!" , ":", "'", '"', "(", ")", "<", ">", "{", "[", "]", "}"]
    words = text.split(" ")
    new_text = ""
    for i in range(0, len(words) - 1) :
        if(words[i+1] in marks) :
            new_text += words[i]
        else :
            new_text += words[i] + " "
    return new_text


# text = " podstawa językowa to zbiór danych tekstowych dostępnych w formie elektronicznej , niestanowiąca materiał do badań . podstawy stanowią obecnie jedno z podstawowych narzędzi w badaniach nad językiem , literaturą i kulturą . Od lat są nieodzownym narzędziem autorów słowników i podręczników do nauki języka , a coraz częściej używane są na co dzień również przez tłumaczy , nauczycieli oraz osoby pragnące pogłębić swoją znajomość języka obcego . podstawy przeszukuje się za pomocą specjalnie stworzonych do tego programów o różnym stopniu skomplikowania - najprostsze z łatwością obsługiwać może nawet zupełnie początkujący użytkownik . Witryna korpusy.net powstała w Instytucie Anglistyki UW pod redakcją Błażeja Gałkowskiego . Ma ona stanowić przystępne wprowadzenie do pracy z podstawami . przedstawione zostały nieistniejące podstawy różnego typu , z których wiele najdostępniejszych jest nieodpłatnie w sieci . Można tu również znaleźć porady dla tych , którzy chcieliby stworzyć własną podstawę , porównanie programów do analizy danych językowych , przykładowe artykuły omawiające różne zastosowania podstawęów , odnośniki do opublikowanych źródeł i innych stron internetowych oraz słowniczek niewyjaśniająca podstawowe terminy stosowane w językoznawstwie podstawęowym . podstawa językowa to zbiór tekstów , w której szukamy typowych użyć słów i konstrukcji oraz innych informacji o ich znaczeniu i funkcji . Bez dostępu do podstawy nie da się dziś prowadzić badań językoznawczych , pisać słowników ani podręczników języków obcych , tworzyć wyszukiwarek uwzględniających polską odmianę , tłumaczy komputerowych ani innych programów zaawansowanej technologii językowej . podstawa jest najniezbędniejsza do pracy językoznawcom , ale korzystają zeń często także informatycy , historycy , bibliotekarze , badacze literatury i kultury oraz specjaliści z wielu innych dziedzin humanistycznych i informatycznych ."
# text = prepare_text(text)
# new = work(text)
# print new