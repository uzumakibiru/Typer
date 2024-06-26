from random import choice

lst=["why of call different did if left head so white carry follow again fall land my sound both until if live \n"
     "river man say live state below mean black go important took sea last eye want in there above earth form \n"
     "carry for these great together around could should water should would there eye three really if right two\n"
    "light story our together new between animal side letter once some she last his want state not mile young began\n"
      "fall air set really very second always talk this once almost such river people good animal city same never \n"
      "turn about why open live boy even earth under place second country for why will been can follow even another keep\n"
      " start time had through to up give upon grow very go are once her fall best every different set again right without\n"
        "its them no open again be large sun under man came fire line year for was long enough and song its sea life open\n" 
        "will group home leave right leave begin time study two through read is saw still\n"
        "they their if than he eye here girl miss where life did turn part through with have could \n"
          "not food family sound end a house answer cut by second large made large let after see if\n" 
          "them sometimes enough made which right been follow over red his its with soon add place came away \n"
          "be each open story thought know upon what other came want letter even eye as give sun river near \n"
          "these left this would show live when in my keep man began hear went some by list"]

text = '\n'.join(lst)
into_list=list(set(text.split()))

# Make the 40 word sentence 
def make_challenge():
    challenge_list=[]
    for _ in range(45):
        word=choice(into_list)
        challenge_list.append(word)
    challenge_sentence=" ".join(challenge_list)
    return challenge_sentence


 