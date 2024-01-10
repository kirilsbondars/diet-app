# Ievads
| Grupas dalībnieks     	| Izdarītie darbi                                                         	|
|-----------------------	|-------------------------------------------------------------------------	|
| Elizabete Citskovska  	| Testa datu izveide, datu importēšanas funkcijas rakstīšana, mājaslapas veidošana (sign up, profile). Dokumentācijas rakstīšana (novērtēšana, secinājumi u.c.) un informācijas atlasīšana plakātam.                                                                        	|
| Kirils Bondars        	| Grupas vadītājs, izveidoja projekta struktūru, datubāzi un mājaslapas skici. Veidoja mājaslapu (create menu, blacklist logs, ēdienu pievienošana un attēlu pievienošana ēdieniem u.c.), uzrakstīja algoritmu ēdienkartei, veica pārējo grupas dalībnieku kodu revīziju un labošanu. Rakstīja dokumentāciju, pievienoja instrukcijas tam, kā var instalēt risinājumu, izveidoja tehnoloģiju stekus.  	|
| Dmitrijs Sizovs       	| Veidoja mājaslapu (history logs, admin panelis, uzturvielu pievienošana profilam).                                                                        	|
| Artūrs Zvirgzdiņš     	| Veidoja mājaslapu (admin panelis, profile un login problēmu labošana, navbar).                                                                         	|
| Miks Šics             	| Veidoja mājaslapu (login logs, create menu dizains), dokumentāciju (algoritma blokshēmas veidošana, programmatūras apraksts u.c.) un atlasīja informāciju plakātam.                                                                      	|
| Katrīna Kate Mālniece 	| Testa datu izveide, kaloriju un uzturvielu ģenerēšanas funkcijas rakstīšana, dokumentācijas veidošana (ievads, secinājumi) un plakāta izveide.                                                                      	|

## Problēmas nostādne
Veselīgs un sabalansēts uzturs ir svarīgs labai veselībai, tomēr sekot līdzi uzņemto kaloriju, olbaltumvielu, ogļhidrātu un tauku daudzumam var būt sarežģīti. Katra cilvēka ķermeņa īpašības un dzīvesveids ir atšķirīgi, kā arī neviens negribētu ēst vienus un tos pašus ēdienus katru dienu, tāpēc nav iespējams atrast kādu universālu ēdienu, ko cilvēks varētu ēst katru dienu.
## Darba un novērtēšanas mērķis
Darba mērķis ir izstrādāt web risinājumu, kas ļauj lietotājam vieglā un ērtā veidā izveidot personalizētu ēdienkarti katrai dienai. Šis risinājums atvieglotu lietotāju ikdienu - vairs nebūtu jāplāno katra ēdienreize un jāseko līdzi tam, vai ir uzņemts atbilstošs daudzums kaloriju un uzturvielu. Darba novērtēšana ļaus saprast to, cik ātri tiek izveidota un parādīta ēdienkarte, atkarībā no ēdienu skaita datubāzē.
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
| 1.    | Lietotājs vēlas ielogoties, jo grib tik klāt saviem datiem                                                        | S            |
| 2.    | Lietotājs vēlas reģistrēties, jo grib, lai viņa dati saglabājas                                                   | S            |
| 3.    | Lietotājs vēlas izvelēties uzturvielu daudzumu savā ēdienkartē, jo pielāgot ēdienkarti savām vajadzībām           | S            |
| 4.    | Lietotājs vēlas jaunu ēdienu piedāvājumus, jo negrib ēst vienu un to pašu                                         | C            |
| 5.    | Lietotājs vēlas iegūt optimālo ēdienkarti, jo grib minimizēt ēdiena izmaksas                                      | M            |
| 6.    | Lietotājs vēlas iespēju izvēlēties produktu preferences, jo lietotājam var būt alerģijas vai uztura ierobežojumi  | S            |
| 7.    | Lietotājs vēlas ievadīt datus par sevi, jo grib iegūt personalizēto kaloriju un uzturvielu daudzumu                | S            |
| 8.    | Lietotājs vēlas, lai ēdieniem būtu bildes, jo tā ir vieglāk uztvert                                                | C            |
| 9.    | Lietotājs vēlas, lai būtu nevēlamo ēdienu melnais saraksts, jo ir ēdieni, kas viņam negaršo                                          | C            |
| 10.   | Administrators vēlas pievienot jaunus ēdienus, jo grib, lai lietotājiem būtu vairāk ēdienu no kuriem izvēlēties   | M            |
| 11.   | Administrators vēlas apskatīt informāciju par lietotājiem, jo grib, zināt informāciju par lietotājiem sistēma     | C            |
## Algoritms
![Algoritms](/images/Algoritms.png)

Algoritms uzsāk savu darbību, kad lietotājs izvēlas uzsākt ēdienkartes ģenerēšanu. Pirms ģenerēšanas, lietotājam ir iespēja vai nu manuāli ievadīt datus par nepieciešamajām uzturvielām, vai arī pēc noklusējuma par tām iegūt datus no profila, un algoritms attiecīgi pārbauda, kurš no abiem datu avotiem ir izvēlēts. Kad ir saņemtas nepieciešamo uzturvielu vērtības, tiek izgūti visi pieejamie ēdieni, lietotāja preferences (kā arī ēdieni, ko lietotājs ir ielicis melnajā sarakstā) kā arī informācija par iepriekšējo dienu ēdienkaršu ēdieniem.

Kad visa informācija ir iegūta, algoritms pārbauda vai eksistē ēdieni, kas atbilstu uzstādītajām prasībām (iekļautos preferencēs / nebūtu melnajā sarakstā u.tml). Ja atbilstoši ēdieni netiek atrasti, tiek izvadīts kļūdas paziņojums. Ja tie tiek atrasti, tiek veikta optimālas ēdienkartes ģenerēšana. Lai to īstenotu, tika izmantots lineārās programmēšanas minimizācijas modelis / algoritms, kas atrasts vietnē "neos Guide" https://neos-guide.org/case-studies/om/the-diet-problem/ (minimizācijas izpilde tika īstenota ar Python PuLP bibliotēkas palīdzību)

Attiecīgā LP modeļa / algoritma matemātiskais noformulējums:

![LP Algoritma matemātiskais noformulējums](/images/Algoritms-mat.png)

Fmin = 0, Fmax = 5 visiem ēdieniem
Uzturvielu daudzums Aij un cena ci ir uz/par 100g ēdiena
Porciju daudzums Xi ir skaitlis no 0 līdz 5, kas attiecīgi apzīmē 0g - 500g

Pēc algoritma izpildes vēl tiek veikta beidzamā pārbaude, kas nosaka, vai nav pieļauta kāda kļūda un uzturvielu daudzumi patiešām iekļaujas nepieciešamajos intervālos. Ja kāds no daudzumiem tomēr neiekļaujas, tiek izvadīts kļūdas paziņojums. Ja ar uzturvielu daudzumiem viss ir kārtībā, ģenerētā ēdienkarte tiek izvadīta lietotājam.

## Konceptu modelis
![Konceptu modelis](/images/konceptu_modelis.png)
## Tehnoloģiju steks
![Tehnoloģiju steks - servera puse](/images/tehnologiju_steks_servera_puse.png)
![Tehnoloģiju steks - klienta puse](/images/tehnologiju_steks_klienta_puse.png)
## Programmatūras apraksts
Programmatūras pirmkots ir atrodams GitHub: https://github.com/kirilsbondars/diet-app.git

Instalācijas instrukcija pa soļiem pieejama failā README.md. Papildus arī risinājumu iespējams izmēģināt / apskatīt bez instalācijas, izmantojot uzstādīto mājaslapu https://www.diet.id.lv/ (testa lietotājam var piekļūt ar attiecīgo login informāciju: email: test@test.test, password: 123)

# Novērtējums
## Novērtēšanas plāns
Mērķis ir novērtēt ēdienkartes izveides un parādīšanas laiku lietotājam atkarībā no tā, cik daudz ēdienu ir datubāzē.

Ieejas mainīgie:
- Ēdienu skaits datubāzē (N)
  - 100, 200, 300, 400 ēdieni
- Testēšanas vide - Azure Standard B2s (2 vcpus, 4 GiB memory), Ubuntu serveris 22.04 LTS
- Uzturvielu un kaloriju daudzums (testa lietotāja dati)

Novērtēšanas mēri:
- Izpildes un parādīšanas laiks sekundēs (t)
## Novērtēšanas rezultāti un to analīze
Katrs mērījums tika atkārtots piecas reizes un tika aprēķināta vidējā vērtība. 
### Visi mērījumi
| Nr. 	| N   	| t, s        	|
|-----	|-----	|-------------	|
| 1.  | 100 | 0.033261061 |
| 2.  | 100 | 0.035756826 |
| 3.  | 100 | 0.036137581 |
| 4.  | 100 | 0.032201529 |
| 5.  | 100 | 0.036095619 |
| 6.  | 200 | 0.05114603  |
| 7.  | 200 | 0.047989845 |
| 8.  | 200 | 0.048549175 |
| 9.  | 200 | 0.054720163 |
| 10. | 200 | 0.051140547 |
| 11. | 300 | 0.059136868 |
| 12. | 300 | 0.064473629 |
| 13. | 300 | 0.060349703 |
| 14. | 300 | 0.062695265 |
| 15. | 300 | 0.067826509 |
| 16. | 400 | 0.074854851 |
| 17. | 400 | 0.074888229 |
| 18. | 400 | 0.075597286 |
| 19. | 400 | 0.072670937 |
| 20. | 400 | 0.077696085 |

### Rezultāti
| Nr. 	| N   	| Vidējais laiks, s        	|
|-----	|-----	|-------------	|
| 1. | 100 | 0.034339249 |
| 2. | 200 | 0.047700167 |
| 3. | 300 | 0.059559202 |
| 4. | 400 | 0.073167562 |

<br>

![Grafiks](/images/grafiks.png)

Redzams, ka palielinoties ēdienu skaitam datubāzē, pieaug ēdienkartes izveides un parādīšanas laiks lietotājam. Toties visi šie izmērītie laiki ir nelieli, tāpēc lietotājs tos īsti nevar pamanīt vai precīzi noteikt, kurš brīdis ir bijis ilgāks.  

Kopumā algoritms izmērītajiem ēdienu daudzumiem darbojas ļoti labi, jo spēj ātri (lietotājam gandrīz nemanāmi) izveidot ēdienkarti.            

# Secinājumi
Projekta laikā tika izstrādāts risinājums, kurā tika veiksmīgi īstenoti visi iepriekš definētie lietotāju stāsti. Risinājums nodrošina visas būtiskākās pamata vajadzības / funkcionalitāti, kā arī labu bāzi lietotāja saskarnei. 

Veicot risinājuma novērtēšanu tika konstatēts, ka arī izvēlētais ģenerēšanas algoritms strādā samērā efektīvi, un veiksmīgi nodrošina vienu no svarīgākajām pamatfunkcionalitātes darbībām (kā arī nodrošina šīs funkcionalitātes ātrdarbību). 

Papildus veiksmīgai risinājuma izstrādei, projekta laikā ievērojami tika attīstītas arī visu dalībnieku prasmes, gan produktu / pakalpojumu izveidē / plānošanā, gan pašā izstrādes procesā ar Python Flask satvaru, gan arī komandas sadarbībā un GitHub  pareizā pielietošanā. Kopumā projekts bija labs ievads šāda veida risinājumu veidošanā un palīdzēja savienot dažādas studiju laikā apskatītās (kā arī pilnībā jaunas) prakses. Projekta laikā arī nācās samērā regulāri praktizēt pielāgošanās prasmes un veikt nepieciešamos labojumus, kad izstrādes laikā tika konstatēta to nepieciešamība. 

Ja risinājumu attīstītu tālāk, varētu uzlabot saskarnes dizainu un kopējo risinājuma prezentāciju. Kā arī būtu iespējams papildināt risinājumu ar vēl citām alternatīvām preferencēm un uzstādāmiem ierobežojumiem ēdienkartes ģenerēšanai. Papildus varētu uzlabot ēdienu savstarpējo sinerģiju, ģenerējot ēdienkarti, kā arī kompleksākiem ēdieniem pievienot iespēju apskatīt to receptes. Labi būtu arī ģenerēt ēdienus specifiskām ēdienreizēm, nevis visus vienā lielā ēdienkartē. 
