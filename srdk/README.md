# Yr Offer Datblygu Adnabod Lleferydd Cymraeg 
(*[click here](README_en.md) for the English version of this file*)

O fewn y ffolder hon teipiwch :

`$ make clean`

`$ make`

Mae 'rhith-beiriant' Docker gyda'r 'srdk' yn cychwyn yn syth.


## Hyfforddi Modelau Acwstig

### Datblygu gyda Corpws Paldaruo
I llwytho corpws Paldaruo i lawr er mwyn ei ddefnyddio i greu modelau acwstig:

`root@4fb715613e82:/usr/local/srdk# cd /usr/local/srdk/cy/paldaruo`

`root@4fb715613e82:/usr/local/srdk/cy/paldaruo# ./fetch.sh`

`root@4fb715613e82:/usr/local/srdk/cy/paldaruo# ./init.sh`

(__D.S. mae hwn yn llwytho cannodd a'r filoedd o ffeiliau WAV i lawr. Felly mae beryg iddo cymryd hyd at 24 awr os yn llwytho dros band llydan__)

Gweler `/srdk_projects/cy/paldaruo/corpus/wav` i weld cyfeiriadau yn cynnwys wavs cyfrannwr ac wedi eu henwi gyda'r uid

Mae na dri modd i hyfforddi a chreu modelau acwstig

 1. hyfforddi gyda nifer o gyfranadiau gyda'i gilydd (unai pawb neu is-set o uids)
 2. hyfforddi a phrofi fesul cyfraniad (unia jyst un ar ben ei hun, is-set, neu pawb)
 
### Hyfforddi Fesul Cyfrannwr

`root@4fb715613e82:/usr/local/srdk/cy/paldaruo# cd /srdk_projects/cy/paldaruo`

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_0_PrepareAudio.py -n paldaruo`

Mae hyn yn creu ffolder /srdk_project/cy/paldaruo/audio/wav sy'n cynnwys symbolic links at y data go iawn

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_EvaluateEachUser.py`

Ar ddiwedd y prosesu, mae'r ffolder results yn cynnwys is-ffolderi ar gyfer pob API sydd yn eu tro yn cynnwys ffeil `recout.mlf'. Mae `recout.mlf' yn cynnwys canlyniadau profi mewn un man cyfleus.

Rhedwch y script yma nesaf:

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_HResults.py`

sydd yn diweddaru'r ffeil `/srdk_projects/cy/paldaruo/paldaruo-metadata.db` gyda tabl sy'n cynnwys y canlyniadau mewn un le. Mae modd canfod 

Mae modd ysgrifennu select er mwyn canfod yr API keys sydd a chanlyniadau prawf gwell:

```
sqlite> .tables
metadata      user_results
sqlite> .schema user_results
CREATE TABLE user_results (uid PRIMARY KEY NOT NULL, word_accuracy NUMERIC NOT NULL);
sqlite> .mode csv
sqlite> .output apikeys_gorau.csv
sqlite> select uid from user_results where word_accuracy > 70;
sqlite> .output stdout
```

i gael rhagor o ystadegau ar maint y data gorau ar gyfer hyfforddi. Gellir defnyddio:

```
sqlite> select count(*) from ( select u.uid, u.word_accuracy, w.filename, w.duration from user_results as u, wavfiles as w where u.uid=w.uid and u.word_accuracy>70 );
2349
sqlite> select count(DISTINCT uid) from ( select u.uid, u.word_accuracy, w.filename, w.duration from user_results as u, wavfiles as w where u.uid=w.uid and u.word_accuracy>70 );
96
sqlite> select sum(duration) from ( select u.uid, u.word_accuracy, w.filename, w.duration from user_results as u, wavfiles as w where u.uid=w.uid and u.word_accuracy>70 );
23093.7175208333
sqlite> select sum(duration)/60/60 from ( select u.uid, u.word_accuracy, w.filename, w.duration from user_results as u, wavfiles as w where u.uid=w.uid and u.word_accuracy>70 );
6.41492153356481
```


### Hyfforddi Gyda Is-set o Cyfraniadau

Mae'n bosib hyfforddi gyda cyfraniadau nifer o defnyddwyr ar y cyd, yn enwedig y rhai sydd uchod sydd â canlyniadau da yn y profion. Mae modd paratoi'r corpws hyfforddi gyda'r ffeil CSV cynhyrchwyd uchod.

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_0_PrepareAudio.py -f apikeys_gorau.csv -n paldaruo`

ac yna

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_Train.py`

 
### Hyffordii mesul cam â llaw.....
 
Os mae'r corpws Paldaruo wedi ei lwytho eisoes, yna:

`$ cd /srdk_projects/cy/paldaruo`

`$/srdk_projects/cy/paldaruo $ SRDK_2_PronunciationDictionary`

`$/srdk_projects/cy/paldaruo $ SRDK_4_Transcriptions`

A dyna fo ar gyfer paratoi'r adnoddau geirfaol/ynganu.


### Hyfforddi Gyda Recordiadau

Mae angen rhedeg y scriptiau canlynol o ffolder y project srdk:

`/srdk_projects/cy/paldaruo $ SRDK_5_CodingAudioData`

`/srdk_projects/cy/paldaruo $ SRDK_6_FlatStart`

`/srdk_projects/cy/paldaruo $ SRDK_7_SilenceModels`

`/srdk_projects/cy/paldaruo $ SRDK_8_Realign`

`/srdk_projects/cy/paldaruo $ SRDK_9_Triphones`

`/srdk_projects/cy/paldaruo $ SRDK_10_TiedStateTriphones`

Ac mae'r modelau yn hmm15. Defnyddiwch y canlynol i'w brofi:

`/srdk_projects/cy/paldaruo $ SRDK_11_TestModels`


## Hyfforddi Modelau Iaith

Mae angen corpws. Yn ffodus, mae'r porth technolegau iaith yn cynnwys rhai eisoes, fel CofnodYCynulliad. Mae modd ei estyn drwy:

`/usr/local/srdk/cy/lang_tools $ ./fetch_cofnod_corpus.sh`

I gychwyn hyfforddi gyda'r testun, ewch i'r ffolder hyfforddi, ac, os oes angen, creu ffolder 'lm':

`/srdk_projects/cy/paldaruo $ mkdir lm`

Rhaid mynd i fewn i'r ffolder 'lm' er mwyn defnyddio'r scgriptiau canlynol. Mae angen defnyddio ym mhob orchymyn enw'r corpws, a maint yr eirfa ar gyfer eich model. e.e. CofnodYCynulliad a 5000

`/srdk_projects/cy/paldaruo/lm $ SRDK_LM_Make CofnodYCynulliad`

Mae modd profi'r model newydd i cael perplexity score :

```
root@a75269e08333:/srdk_projects/cy/paldaruo/lm# SRDK_LM_PerplexityTest CofnodYCynulliad
inpfile: CofnodYCynulliad/lm.irstlm.arpa
outfile: lm.irstlm.arpa.blm
evalfile: /srdk_projects/cy/corpus/text/CofnodYCynulliad/test/test.txt
loading up to the LM level 1000 (if any)
dub: 10000000
Language Model Type of CofnodYCynulliad/lm.irstlm.arpa is 1
Language Model Type is 1
OOV code is 43154
OOV code is 43154
Start Eval
OOV code: 43154
%% Nw=13159 PP=162.65 PPwp=41.12 Nbo=5617 Noov=238 OOV=1.81%
```

