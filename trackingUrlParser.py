# Write your code here :-)
import re
ibmLinks = ['https://www.ibm.com/thought-leadership/covid19/?utm_medium=OSocial&utm_source=Twitter&utm_content=000033TP&cm_mmc=OSocial_Twitter-_-IBM+Master+Brand_Communications-_-WW_WW&cm_mmca1=000033TP&social_post=3254840228&linkId=86027323','https://www.globalcitizen.org/en/connect/togetherathome/?utm_source=social_platform&utm_medium=platformglobal_partner&utm_campaign=oneworld_launch&utm_content=signup&linkId=86771603', 'https://newsroom.ibm.com/ibmfellows2020?social_post=3260351378&linkId=86180469']
vcpiRegex = re.compile(r'social_post=\d{10}')

for link in ibmLinks:
    socialIDs = vcpiRegex.findall(link)
    if socialIDs is None:
        print('Not Tagged')
    else:
        print(socialIDs)

