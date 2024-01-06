# Ievads
## Problēmas nostādne
## Darba un novērtēšanas mērķis
# Līdzīgo risinājumu pārskats
| Risinājums | Pozitīvās īpašības | Trūkumi |
| --- | --- | --- |
| [Diet problem solver](https://www.zweigmedia.com/RealWorld/dietProblem/diet.html) | <ul><li>Var norādīt nepieciešamo uzturvielu, kaloriju daudzumu</li><li>Var izvēlēties kādus ēdienus iekļaut aprēķinā</li><li>Var norādīt maksimālo porciju daudzumu katram ēdienam</li></ul> | <ul><li>Ēdiena saraksts ir neliels</li><li>Ēdiena porcijām tiek izmantotas imperiālās mērvienības, cenas norādītas dolāros</li></ul> |
| [Eat this much](https://www.eatthismuch.com/) | <ul><li>Lietotājs norada cik kilokaloriju jābūt viņa ēdienkartei un tiek ģenerēti iespējami ēdieni. Ja lietotājam nepatīk saģenerētais ēdiens viņš var viņu, samainīt uz citu.</li><li>Var izvelēties cik ēdienus vajag saģenerēt</li><li>Ir uzturu un cenu informācija par ēdienu</li><li>Var izvēlēties ēdienkartes tipu (vegāns, veģetārs, u.c)</li></ul> | <ul><li>Nevar izvelēties cik tavā ēdienkartē būs olbaltumvielu, ogļhidrātu un tauku</li><li>Piedāvā dārgus ēdienus</li></ul> |
| [Strongr Fastr](https://www.strongrfastr.com/macro-meal-planner) | <ul><li>Var izvēlēties dzimumu, vecumu, augumu, svaru, aktivitātes līmeni, diētas tipu, aptuvenu budžetu, utt., vai arī var manuāli ievadīt kaloriju, olbaltumvielu un ogļhidrātu daudzumu un alerģijas.</li><li>Var izvēlēties receptes, ko grib iekļaut, un pārējais plāns tiek sastādīts automātiski.</li><li>Rezultātā piedāvā gatavu ēdienkarti nedēļai, ar detalizētu apskatu par kalorijām, ogļhidrātiem, olbaltumvielām un taukiem.</li><li>Ēdienkartē var mainīt ēdienus.</li></ul> | <ul><li>Par ieprikumu sarakstu ir jāmaksā.</li><li>Nav informācijas par reālajām produktu cenām.</li></ul> 
| [MyFitnessPal](https://www.myfitnesspal.com/) |	<ul><li>Pieejamas jau gatavas receptes</li><li>Lietotāji var pielāgot sava uztura mērķus, piemēram, makroelementu (ogļhidrāti, olbaltumvielas, tauki) daudzumus, atbilstoši savām personīgajām vajadzībām un mērķiem.</li><li>Iespēja sekot sava svara un citu veselības mērķu progresam ar vizuālām diagrammām un pārskatiem.</li><li>Integrācija ar fitnesa lietotnēm un ierīcēm</li><li>Lietotne ietver ērtu barcode skeneri, kas ātri identificē produktus un to uzturvērtību, atvieglojot diētas uzskaiti.</li></ul>	| <ul><li>Pilnas funkcionalitātes izmantošana prasa abonēšanu</li><li>Nepieciešams laiks, lai iemācītos izmantot ļoti lielu daudzumu funkciju</li><li>Manuāla mērķu pielāgošana, kas prasa pašmācību</li></ul>
| [Meta Nutrition - Meal Planner](https://www.metnu.com/) |	<ul><li>Ērti lietojams UI</li><li>Iebūvētas receptes</li><li>Plaša datubāze ar produktiem / to uzturvielu informāciju</li><li>Iespēja izmantot personalizētus diētas plānus</li><li>Iebūvēta statistikas funkcionalitāte</li></ul>	| <ul><li>Vairāk pielāgota tieši optimālu recepšu atrašanai nevis optimālu produktu kombināciju.</li><li>Daļa funkcionalitātes pieejama tikai maksas versijā</li></ul>
# Tehniskais risinājums
## Prasības
| Nr. 	 | Lietotāju stāsts 	                                                                                                | Prioritāte 	 |
|-------|-------------------------------------------------------------------------------------------------------------------|--------------|
| 1.    | Lietotājs vēlas ielogoties, jo grib tik klat saviem datiem                                                        | S            |
| 2.    | Lietotājs vēlas reģistrēties, jo grib, lai viņa dati saglabājas                                                   | S            |
| 3.    | Lietotājs vēlas izveidot ēdienkarti, jo grib saplānot savas ēdienreizes                                           | M            |
| 4.    | Lietotājs vēlas, lai tiek piedāvāti jauni ēdieni, jo negrib ēst vienu un to pašu                                  | C            |
| 5.    | Lietotājs vēlas iegūt optimālo ēdienkarti, jo grib minimizēt ēdiena izmaksas                                      | M            |
| 6.    | Lietotājs vēlas iespēju izvēlēties produktu preferences, jo lietotājam var būt alerģijas vai dietāri ierobežojumi | S            |
| 7.    | Lietotājs grib ievadīt datus par sevi, jo grib iegūt personalizēto kaloriju un uzturvielu daudzumu                | S            |
| 8.    | Lietotājs grib, lai ēdieniem būtu bildes, jo tā ir vieglāk uztvert                                                | C            |
| 9.    | Lietotājs grib, lai būtu edienu melnraksts, jo viņam nepatik dāži edieni                                          | C            |
| 10.   | Administrators vēlas pievienot jaunus ēdienus, jo grib, lai lietotājiem būtu vairāk ēdienu no kuriem izvēlēties   | M            |
| 11.   | Administrators vēlas apskatīt informāciju par lietotājiem, jo grib, zināt informāciju par lietotājiem sistēma     | C            |
## Algoritms
## Konceptu modelis
![Konceptu modelis](/images/konceptu_modelis.png)
## Tehnoloģiju steks
![Tehnoloģiju steks - servera puse](/images/tehnologiju_steks_servera_puse.png)
![Tehnoloģiju steks - klienta puse](/images/tehnologiju_steks_klienta_puse.png)
## Programmatūras apraksts
# Novērtējums
## Novērtēšanas plāns
## Novērtēšanas rezultāti un to analīze
# Secinājumi
