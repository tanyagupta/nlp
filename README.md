# nlp
NLP test code
This is some test code related to NLP and more

## Book
The correct reference (book) for the exercises is:
https://www.nltk.org/book/

## Pipenv
1. IMPORTANT: be sure you are in the right directory
2. pipenv shell to install shell
3. pip install nlp (or other packages)

## Import and download packages
*>>> import nltk* in python shell
*>>> nltk.download('wordnet')* in python shell
*nltk.download('opinion_lexicon')*
*nltk.download('punkt')* etc.

## Gitpod error handling
For error *ERROR: Can not perform a '--user' install. User site-packages are not visible in this virtualenv*, try:
export PIP_USER=no
(reference https://github.com/gitpod-io/gitpod/issues/479)

## Getting Started
1. Go to the correct directory
2. Check if pip file is there
3. Open shell *pipenv shell*
4. Open python by typing *python*, this starts the python shell (you will see three arrows like so >>>)


## Useful info
1. Use exit() to exit python shell and exit to exit terminal
1. 4. You have to be in the python shell to run the code
1. Run python code from pipenv shell. You know you are in pipenv shell when you see () around the location
1. Run python shell from pipenv shell. You know you are in python shell when you see >>>
1. Run python code by *python name_of_file.py*
1. If the file is in a different location you can still run it from pipenv shell using the correct location. For instance if the file is one level above the current location use *python ../test.py*
1. Note pipenv shell has nothing to do with directories. You can always cd to change the directory within the pipenv shell. In the above example you can cd .., pwd to check you are one level up and then directly run *python test.py* without the *../*


## List of parts of speech
### CC: conjunction, coordinating
`& 'n and both but either et for less minus neither nor or plus so therefore times v. versus vs. whether yet`
### CD: numeral, cardinal
`mid-1890 nine-thirty forty-two one-tenth ten million 0.5 one forty- seven 1987 twenty '79 zero two 78-degrees eighty-four IX '60s .025 fifteen 271,124 dozen quintillion DM2,000 …`
### DT: determiner
`all an another any both del each either every half la many much nary neither no some such that the them these this those`
### EX: existential there`
`there
### IN: preposition or conjunction, subordinating
`astride among uppon whether out inside pro despite on by throughout below within for towards near behind atop around if like until below next into if beside ...`
### JJ: adjective or numeral, ordinal
`third ill-mannered pre-war regrettable oiled calamitous first separable ectoplasmic battery-powered participatory fourth still-to-be-named multilingual multi-disciplinary ...`
### JJR: adjective, comparative
`bleaker braver breezier briefer brighter brisker broader bumper busier calmer cheaper choosier cleaner clearer closer colder commoner costlier cozier creamier crunchier cuter ...`
### JJS: adjective, superlative
`calmest cheapest choicest classiest cleanest clearest closest commonest corniest costliest crassest creepiest crudest cutest darkest deadliest dearest deepest densest dinkiest ...`
### LS: list item marker
`A A. B B. C C. D E F First G H I J K One SP-44001 SP-44002 SP-44005 SP-44007 Second Third Three Two * a b c d first five four one six three two`
### MD: modal auxiliary
`can cannot could couldn't dare may might must need ought shall should shouldn't will would`
### NN: noun, common, singular or mass
`common-carrier cabbage knuckle-duster Casino afghan shed thermostat investment slide humour falloff slick wind hyena override subhumanity machinist ...`
### NNP: noun, proper, singular
`Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA Shannon A.K.C. Meltex Liverpool ...`
### NNS: noun, common, plural
`undergraduates scotches bric-a-brac products bodyguards facets coasts divestitures storehouses designs clubs fragrances averages subjectivists apprehensions muses factory-jobs ...`
### PDT: pre-determiner
`all both half many quite such sure this`
### POS: genitive marker
' 's`
### PRP: pronoun, personal
`hers herself him himself hisself it itself me myself one oneself ours ourselves ownself self she thee theirs them themselves they thou thy us`
### PRP$: pronoun, possessive
`her his mine my our ours their thy your`
### RB: adverb
`occasionally unabatingly maddeningly adventurously professedly stirringly prominently technologically magisterially predominately swiftly fiscally pitilessly ...`
### RBR: adverb, comparative
`further gloomier grander graver greater grimmer harder harsher healthier heavier higher however larger later leaner lengthier less- perfectly lesser lonelier longer louder lower more ...`
### RBS: adverb, superlative
`best biggest bluntest earliest farthest first furthest hardest heartiest highest largest least less most nearest second tightest worst`
### RP: particle
`aboard about across along apart around aside at away back before behind by crop down ever fast for forth from go high i.e. in into just later low more off on open out over per pie raising start teeth that through under unto up up-pp upon whole with you
### TO: "to" as preposition or infinitive marker
`to`
### UH: interjection
`Goodbye Goody Gosh Wow Jeepers Jee-sus Hubba Hey Kee-reist Oops amen huh howdy uh dammit whammo shucks heck anyways whodunnit honey golly man baby diddle hush sonuvabitch ...`
### VB: verb, base form
`ask assemble assess assign assume atone attention avoid bake balkanize bank begin behold believe bend benefit bevel beware bless boil bomb boost brace break bring broil brush build ...`
### VBD: verb, past tense
`dipped pleaded swiped regummed soaked tidied convened halted registered cushioned exacted snubbed strode aimed adopted belied figgered speculated wore appreciated contemplated ...`
### VBG: verb, present participle or gerund
`telegraphing stirring focusing angering judging stalling lactating hankerin' alleging veering capping approaching traveling besieging encrypting interrupting erasing wincing ...
### VBN: verb, past participle
`multihulled dilapidated aerosolized chaired languished panelized used experimented flourished imitated reunifed factored condensed sheared unsettled primed dubbed desired ...`
### VBP: verb, present tense, not 3rd person singular
`predominate wrap resort sue twist spill cure lengthen brush terminate appear tend stray glisten obtain comprise detest tease attract emphasize mold postpone sever return wag ...`
### VBZ: verb, present tense, 3rd person singular
`bases reconstructs marks mixes displeases seals carps weaves snatches slumps stretches authorizes smolders pictures emerges stockpiles seduces fizzes uses bolsters slaps speaks pleads ...`
### WDT: WH-determiner
`that what whatever which whichever`
### WP: WH-pronoun
`that what whatever whatsoever which who whom whosoever`
### WRB: Wh-adverb
`how however whence whenever where whereby whereever wherein whereof why`
