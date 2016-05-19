# Seilwaith Adnabod Lleferydd

## Cyflwyniad
Mae'r project hwn yn darparu'r amgylchedd defnyddir gan Uned Technolegau Iaith Prifysgol Bangor i hyfforddi'r modelau iaith ac acwstig ar gyfer adnabod lleferydd Cymraeg.

Mae nifer o'r camau hyfforddi arferol wedi eu hwyluso er mwyn caniatáu i ddatblygwyr ac ymchwilwyr ei ddefnyddio hefyd. 

Mae'r amgylchedd yn darparu nodweddion i:

 - llwytho corpws lleferydd Paldaruo i lawr o wefan Porth Technolegau Iaith Cenedlaethol Cymru. 
 - asesu a dadansoddi pob cyfraniad o gorpws Paldaruo
 - hidlo'r recordiadau gorau ar gyfer hyfforddi
 - hyfforddi model acwstig ar sail un, casgliad neu bob cyfraniad yn y corpws.
 - ddulliau syml i brofi'r modelau acwstig
 - pecynnu'r modelau acwstig ar gyfer defnyddio o fewn Julius-cy

 - llwytho corpora testun yr Uned i lawr a'u defnyddio i hyfforddi modelau iaith
 - creu lecsicon ynganu o eirfa corpws.
 - pecynnu'r modelau iaith a lecsicon ynganu ar gyfer eu defnyddio o fewn defnydd arddweud o Julius-cy

## Sut mae cychwyn...
Bydd angen cyfrifiadur gyda system weithredu Linux fel Ubuntu neu RedHat ar gyfer y project. Bydd angen i chi gosod git,wget, make  a Docker cyn cychwyn arni. Cychwynwch o'ch cyfeiriadur cartref (h.y. $HOME)

```
~$ mkdir src
~$ cd src
~/src$ git clone https://github.com/techiaith/seilwaith.git
~/src$ cd seilwaith
```

Mae'r project yn defnyddio'r HTK i gynhyrchu modelau acwstig. Mae rhaid i chi gofrestru ar wefan http://htk.eng.cam.ac.uk, er mwyn derbyn enw defnyddiwr a chyfrinair er mwyn llwytho'r cod ffynhonnell i lawr. Mae modd llwytho'r cod i lawr fel hyn:

`$ wget --user <eich enw defnyddiwr HTK> --ask-password http://htk.eng.cam.ac.uk/ftp/software/HTK-3.4.1.tar.gz`

`$ wget --user <eich enw defnyddiwr HTK> --ask-password http://htk.eng.cam.ac.uk/ftp/software/HTK-samples-3.4.1.tar.gz`

Bydd yn gofyn am eich cyfrinair yn y man.

Bydd ddwy ffeil, HTK-3.4.1.tar.gz a HTK-samples-3.4.1.tar.gz yn bodoli o fewn y cyfeiriadur 'SpeechRecDevKit'. h.y.:

```
~/src/seilwaith $ ls
Dockerfile  HTK-3.4.1.tar.gz  HTK-samples-3.4.1.tar.gz  Makefile  README.md  srdk
```

Y cam nesaf yw teipio:

`~/src/seilwaith $ make`

Bydd hyn yn adeiladu rhannau craidd yr amgylchedd hyfforddi gan ddefnyddio'r ffeiliau HTK rydych wedi llwytho i lawr ar wahân. Pan mae wedi cwblhau, teipiwch i mewn 

`$ exit`
 
Y cam nesaf yw mynd i ffolder 'srdk

`~/src/seilwaith $ cd srdk`

a dilyn cyfarwyddiadau'r README yno [srdk/README](srdk/README.md)

