# Проблем трговачког путника

Проблем трговачког путника спада у велику класу проблема који се називају комбинаторни проблеми оптимизације. Ово је један од највише проучаваних проблема оптимизације, а његова решења и примене ће бити описане у овом раду. Коришћене методе решавања су:

- Алгоритам планинаренја (Hill climbing algorithm) 
- Генетски алгоритам (Genetic algorithm)

## Алгоритам планинаренја (Hill climbing algorithm)

Овај метод хеуристичке претраге заснива се на методама исрпљујуће претраге и похлепне претраге. Име методе - планинарење, потиче од избора следећег чвора који ће се отворити. Темељен је на логици успона: алгоритам почиње од неког решења и уколико постоји сусед који боље оптимизује функцију, ново решење постаје 
тај сусед. Наиме, следећи чвор који се отвара има максималну вредност хеуристичке функције. Када се дође до решења онда то одговара врху. За неко међустање које може бити и почетно, генеришу се сва могућа стања применом свих оператора. Тиме се једноставно елиминише хеуристичка функција за операторе, пошто се примењују сви оператори на одабрани чвор Затим се испитује да ли је неко од тих нових стања можда решење. Ако јесте, то је крај претраге, а ако не, на основу хеуристичке функције бира се следећи чвор из скупа нових генерисаних чворова 
Описана процедура се даље понавља, све док се не дође до решења. Сама функција може бити недовољно адекватна, тако да вредност за дати чвор не мора увек бити меродавна, јер можда не узима у обзир баш све меродавне факторе за најперспективнији чвор. Може се десити да функција даје исту вредност за више различитих чворова, у ком случају седећи чвор који треба отворити није једнозначно одређен. Алгоритми  планинарења  немају начина да примете да се налазе у локалном максимуму. Чвор алгоритма за планинарења има две компоненте које су стање и вредност. Алгоритам планинарења углавном се користи када је на располагању добра хеуристика.

## Генетски алгоритам (Genetic algorithm)

Прве идеје о генетским алгоритмима изложене су у раду Холланд-а, 1975. и јавиле су се у оквиру тзв. теорије адаптивних система, која проучава моделе ефикасног адаптивног понашања неких биолошких, специјално генетских, система. Овакви алгоритми су првобитно креирани да симулирају процес генетске еволуције једне популације јединки под дејством окружења и генетских оператора. У овом процесу је свака јединка окарактерисана хромозомом који представља њен генетски код. Оне јединке које су у ведој мери прилагођене окружењу, међусобно се даље репродукују (применом генетских оператора на њихове хромозоме) и тако се ствара нова генерација јединки, прилагођенија од претходне. Овај процес се понавља, при чему се из генерације у генерацију просечна прилагођеност чланова популације повећава. 

### Принцип рада 

1. Одабрани родитељи добрих својстава имају шансу да дају потомке који це имати боља својства од сваког појединачног родитеља. 
2. Родитељи добрих својстава имају веду шансу да дају потомке и пренесу своја својства (гене) у идућу генерацију. 
3. Свака следећа генерација ће имати све боља својства  

## Закључак

Алгоритам планинарења дао је солидне резултате, за кратко време, међутим морамо узети у обзир да је тестиран на релативно малом проблему у смислу количине података које обрађује, јер мањи број улазних података олакшава прорачуне алгоритма. Да је тестиран на већем узорку ефикасност би била далеко мања, више времена би му било потребно јер претражује најбољу руту од тачке у којој се тренутно налази.  

На примеру проблема трговачког путника алгоритам планинарења показао је мању тачност, а већу брзину. 
 
Познато је да је за сваку врсту проблема потребно дизајнирати посебан генетски алгоритам или је потребно прилагодити проблем неком већ постојећем генетском алгоритму. Еволуцију решења коришћењем генетског алгоритма могуће је усмеравати подешавањем параметара које неки генетски алгоритам може 
имати. Од параметрима зависи колико ће се времена потрошити на еволуцију решења, којом ће се брзином алгоритам усмеравати према потенцијалном оптималном решењу, хоће ли претраживати већи или мањи део простора решења, итд... 

Скуп параметара који за један генетски алгоритам један проблем даје квалитетне резултате, за неки други проблем не мора дати једнако квалитетне резултате. Главни параметри су: 
 
-Величина популације – параметар који директно утиче на квалитет добијених решења, али исто тако и у зависности од селекције може имати велики утицај на дужину извођења генетског алгоритма. 
 
-Број генерација (итерација) – параметар који директно утиче и на квалитет добијених решења и на дужину извођења генетског алгоритма. Свакако да већи број генерација, даје веће време извршавања генетског алгоритму да пронађе оптималније решење задатог проблема. Међутим, код дизајнирања генетског алгоритма за теже проблеме, време се узима као један од важних фактора. Наравно да се увек покушава да се пронађе оптимално решење за проблем, али је некада цена за време које би требало генетском алгоритму једноставно превелика, па се зато покушава пронаћи задовољавајуће решење у што краћем времену извршавања. Задовољавајуће решење је оно решење које је довољно близу оптималном, а за које је потребно много мање времена како би се до њега дошло. 
 
-Вероватноћа мутације – један од најважнијих параметара код генетских алгоритама, јер директно утиче на то да ли це доћи код одређене јединке или код одреденог бита унутар јединке до мутације, а сама мутација, ради случајне скокове алгоритма по простору решења, што омогућује избегавање заглављивања алгоритма у локалним оптимумима и проширивање подручја претраге на још неистражене делове простора решења. Могуће је да се добијена решења бити лошија од оригиналних, али због тога та лошија решења имају мању вероватноћу уласка у даље репродукције, чиме се оставља простор за напредовање у правом смеру. Генетски алгоритам је доста осетљив на промене овог параметра, па је доста битно пажљиво одабрати његове вредности. 
 
На примеру проблема трговачког путника генетски алгоритам показао је већу тачност, а мању брзину. 
 
Закључак је да је генетски алгоритам далеко прецизнији и комплекснији од алгоритма планинарења и да резултати које даје су тачнији на мањем, а и на већем узорку.
