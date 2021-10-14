import time,copy,sys
from dataclasses import dataclass
from browser import document, html, timer, window

import  dragdrop, engmonarchs
from dragdrop import px,order
import random



@dataclass
class Oscar(dragdrop.Content):
    wiki: str
    name: str
    date: str
    film: str
    role: str
    description: str
    width: str
    height: str
    source: str


deck=\
[Oscar(wiki='/wiki/Emil_Jannings', name='Emil Jannings', date='1927', film='The Last Command', role='Grand Duke Sergius AlexanderAugust Schilling', description='German actor', width=224, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Emil_Jannings_-_no_watermark.jpg/224px-Emil_Jannings_-_no_watermark.jpg'),
Oscar(wiki='/wiki/Warner_Baxter', name='Warner Baxter', date='1928', film='In Old Arizona', role='The Cisco Kid', description='American actor (1889–1951)', width=256, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Warner_Baxter_promo.jpg/256px-Warner_Baxter_promo.jpg'),
Oscar(wiki='/wiki/George_Arliss', name='George Arliss', date='1929', film='Disraeli', role='Benjamin Disraeli', description='English actor, author, playwright, and filmmaker', width=225, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/George_Arliss_cph.3b31151.jpg/225px-George_Arliss_cph.3b31151.jpg'),
Oscar(wiki='/wiki/Lionel_Barrymore', name='Lionel Barrymore', date='1930', film='A Free Soul', role='Stephen Ashe', description='American actor, director, screenwriter', width=230, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Lionel_Barrymore_2.jpg/230px-Lionel_Barrymore_2.jpg'),
Oscar(wiki='/wiki/Wallace_Beery', name='Wallace Beery', date='1931', film='The Champ', role='Andy "Champ" Purcell', description='American actor', width=262, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Wallace_Beery-publicity.JPG/262px-Wallace_Beery-publicity.JPG'),
Oscar(wiki='/wiki/Fredric_March', name='Fredric March', date='ERROR', film='Dr. Jekyll and Mr. Hyde', role='Dr. Henry Jekyll / Mr. Edward Hyde', description='American actor', width=232, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Fredric_March_face.jpg/232px-Fredric_March_face.jpg'),
Oscar(wiki='/wiki/Charles_Laughton', name='Charles Laughton', date='1932', film='The Private Life of Henry VIII', role='King Henry VIII', description='English-born American stage and film actor and director', width=262, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Charles_Laughton-publicity2.JPG/262px-Charles_Laughton-publicity2.JPG'),
Oscar(wiki='/wiki/Clark_Gable', name='Clark Gable', date='1934', film='It Happened One Night', role='Peter Warne', description='American actor (1901–1960)', width=251, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Clark_Gable_-_publicity.JPG/251px-Clark_Gable_-_publicity.JPG'),
Oscar(wiki='/wiki/Victor_McLaglen', name='Victor McLaglen', date='1935', film='The Informer', role='Gypo Nolan', description='British-American actor', width=320, height=239, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Victor_McLaglen_in_Sea_Devils_trailer.jpg/320px-Victor_McLaglen_in_Sea_Devils_trailer.jpg'),
Oscar(wiki='/wiki/Paul_Muni', name='Paul Muni', date='1936', film='The Story of Louis Pasteur', role='Louis Pasteur', description='Austrian-born American stage and film actor', width=257, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Paul_Muni_-_Zola_-_1936.jpg/257px-Paul_Muni_-_Zola_-_1936.jpg'),
Oscar(wiki='/wiki/Spencer_Tracy', name='Spencer Tracy', date='1937', film='Captains Courageous', role='Manuel Fidello', description='American actor', width=254, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Spencer_Tracy_Judgment_at_Nuremberg_Still.jpg/254px-Spencer_Tracy_Judgment_at_Nuremberg_Still.jpg'),
Oscar(wiki='/wiki/Robert_Donat', name='Robert Donat', date='1939', film='Goodbye, Mr. Chips', role='Charles Edward Chipping', description='English actor', width=320, height=240, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/GoodbyeMrChipsTrailer1.jpg/320px-GoodbyeMrChipsTrailer1.jpg'),
Oscar(wiki='/wiki/James_Stewart', name='James Stewart', date='1940', film='The Philadelphia Story', role='Macaulay "Mike" Connor', description='American actor', width=253, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Annex_-_Stewart%2C_James_%28Call_Northside_777%29_01.jpg/253px-Annex_-_Stewart%2C_James_%28Call_Northside_777%29_01.jpg'),
Oscar(wiki='/wiki/Gary_Cooper', name='Gary Cooper', date='1941', film='Sergeant York', role='Sgt. Alvin York', description='American actor (1901–1961)', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Gary_Cooper_%281952%29.jpg/240px-Gary_Cooper_%281952%29.jpg'),
Oscar(wiki='/wiki/James_Cagney', name='James Cagney', date='1942', film='Yankee Doodle Dandy', role='George M. Cohan', description='American actor and dancer', width=216, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/James_cagney_promo_photo_%28cropped%2C_centered%29.jpg/216px-James_cagney_promo_photo_%28cropped%2C_centered%29.jpg'),
Oscar(wiki='/wiki/Paul_Lukas', name='Paul Lukas', date='1943', film='Watch on the Rhine', role='Kurt Muller', description='Hungarian-American actor', width=247, height=320, source='https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Paul_Lukas_-_1950.jpg/247px-Paul_Lukas_-_1950.jpg'),
Oscar(wiki='/wiki/Bing_Crosby', name='Bing Crosby', date='1944', film='Going My Way', role="Father Chuck O'Malley", description='American singer and actor (1903–1977)', width=252, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Bing_Crosby_1951.jpg/252px-Bing_Crosby_1951.jpg'),
Oscar(wiki='/wiki/Ray_Milland', name='Ray Milland', date='1945', film='The Lost Weekend', role='Don Birnam', description='Welsh-American actor and film director', width=254, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Ray_Milland_Markham_1959.JPG/254px-Ray_Milland_Markham_1959.JPG'),
Oscar(wiki='/wiki/Ronald_Colman', name='Ronald Colman', date='1947', film='A Double Life', role='Anthony John', description='British actor (1891–1958)', width=267, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Ronald_Colman_-_publicity.jpg/267px-Ronald_Colman_-_publicity.jpg'),
Oscar(wiki='/wiki/Laurence_Olivier', name='Laurence Olivier', date='1948', film='Hamlet', role='Hamlet, Prince of Denmark', description='English actor and director (1907–1989)', width=221, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Lord_Olivier_6_Allan_Warren.jpg/221px-Lord_Olivier_6_Allan_Warren.jpg'),
Oscar(wiki='/wiki/Broderick_Crawford', name='Broderick Crawford', date='1949', film="All the King's Men", role='Willie Stark', description='American actor (1911–1986)', width=250, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Broderick_Crawford_1970.JPG/250px-Broderick_Crawford_1970.JPG'),
Oscar(wiki='/wiki/Jos%C3%A9_Ferrer', name='José Ferrer', date='1950', film='Cyrano de Bergerac', role='Cyrano de Bergerac', description='Puerto Rican actor and director', width=239, height=320, source='https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Jose_Ferrer_-_1952.jpg/239px-Jose_Ferrer_-_1952.jpg'),
Oscar(wiki='/wiki/Humphrey_Bogart', name='Humphrey Bogart', date='1951', film='The African Queen', role='Charlie Allnut', description='American actor (1899–1957)', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Humphrey_Bogart_1940.jpg/226px-Humphrey_Bogart_1940.jpg'),
Oscar(wiki='/wiki/Gary_Cooper', name='Gary Cooper', date='1952', film='High Noon', role='Marshal Will Kane', description='American actor (1901–1961)', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Gary_Cooper_%281952%29.jpg/240px-Gary_Cooper_%281952%29.jpg'),
Oscar(wiki='/wiki/William_Holden', name='William Holden', date='1953', film='Stalag 17', role='Sgt. J.J. Sefton', description='American actor', width=256, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/WILLIAMHolden.jpg/256px-WILLIAMHolden.jpg'),
Oscar(wiki='/wiki/Marlon_Brando', name='Marlon Brando', date='1954', film='On the Waterfront', role='Terry Malloy', description='American actor (1924–2004)', width=249, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Marlon_Brando_publicity_for_One-Eyed_Jacks.png/249px-Marlon_Brando_publicity_for_One-Eyed_Jacks.png'),
Oscar(wiki='/wiki/Ernest_Borgnine', name='Ernest Borgnine', date='1955', film='Marty', role='Marty Piletti', description='American actor (1917–2012)', width=257, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Ernest_Borgnine_McHale_McHale%27s_Navy_1962.JPG/257px-Ernest_Borgnine_McHale_McHale%27s_Navy_1962.JPG'),
Oscar(wiki='/wiki/Yul_Brynner', name='Yul Brynner', date='1956', film='The King and I', role='King Mongkut of Siam', description='Russian-born actor, singer, and director', width=249, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Publicity_press_photo_of_Yul_Brynner_in_1960_%28cropped%29.jpg/249px-Publicity_press_photo_of_Yul_Brynner_in_1960_%28cropped%29.jpg'),
Oscar(wiki='/wiki/Alec_Guinness', name='Alec Guinness', date='1957', film='The Bridge on the River Kwai', role='Lt. Colonel Nicholson', description='British actor (1914 – 2000)', width=268, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sir_Alec_Guinness_Allan_Warren_%282%29.jpg/268px-Sir_Alec_Guinness_Allan_Warren_%282%29.jpg'),
Oscar(wiki='/wiki/David_Niven', name='David Niven', date='1958', film='Separate Tables', role='Major Angus Pollock', description='English actor and writer (1910–1983)', width=268, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/David_Niven_4_Allan_Warren.jpg/268px-David_Niven_4_Allan_Warren.jpg'),
Oscar(wiki='/wiki/Charlton_Heston', name='Charlton Heston', date='1959', film='Ben-Hur', role='Judah Ben-Hur', description='American actor and gun-rights activist', width=233, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Charlton_Heston.jpg/233px-Charlton_Heston.jpg'),
Oscar(wiki='/wiki/Burt_Lancaster', name='Burt Lancaster', date='1960', film='Elmer Gantry', role='Elmer Gantry', description='American actor (1913–1994)', width=261, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Burt_Lancaster_-_publicity_1947.JPG/261px-Burt_Lancaster_-_publicity_1947.JPG'),
Oscar(wiki='/wiki/Maximilian_Schell', name='Maximilian Schell', date='1961', film='Judgment at Nuremberg', role='Hans Rolfe', description='Swiss film and stage actor', width=254, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Maximilian_Schell_-_1970-1.jpg/254px-Maximilian_Schell_-_1970-1.jpg'),
Oscar(wiki='/wiki/Gregory_Peck', name='Gregory Peck', date='1962', film='To Kill a Mockingbird', role='Atticus Finch', description='American actor', width=253, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Peck_The_Valley_of_Decision.jpg/253px-Peck_The_Valley_of_Decision.jpg'),
Oscar(wiki='/wiki/Sidney_Poitier', name='Sidney Poitier', date='1963', film='Lilies of the Field', role='Homer Smith', description='Bahamian-American actor, film director, author, and diplomat', width=246, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Sidney_Poitier_1968.jpg/246px-Sidney_Poitier_1968.jpg'),
Oscar(wiki='/wiki/Rex_Harrison', name='Rex Harrison', date='1964', film='My Fair Lady', role='Professor Henry Higgins', description='English actor', width=201, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Rex_Harrison_Allan_Warren.jpg/201px-Rex_Harrison_Allan_Warren.jpg'),
Oscar(wiki='/wiki/Lee_Marvin', name='Lee Marvin', date='1965', film='Cat Ballou', role='Kid Shelleen and Tim Strawn', description='American actor (1924–1987)', width=250, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Lee_marvin_1971.JPG/250px-Lee_marvin_1971.JPG'),
Oscar(wiki='/wiki/Paul_Scofield', name='Paul Scofield', date='1966', film='A Man for All Seasons', role='Sir Thomas More', description='English actor', width=303, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Paul_Scofield_Allan_Warren.jpg/303px-Paul_Scofield_Allan_Warren.jpg'),
Oscar(wiki='/wiki/Rod_Steiger', name='Rod Steiger', date='1967', film='In the Heat of the Night', role='Police Chief Bill Gillespie', description='American actor', width=320, height=264, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Rod_Steiger_Al_Capone_2.jpg/320px-Rod_Steiger_Al_Capone_2.jpg'),
Oscar(wiki='/wiki/Cliff_Robertson', name='Cliff Robertson', date='1968', film='Charly', role='Charly Gordon', description='American actor', width=248, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Cliffrobertson_%28cropped%29.jpg/248px-Cliffrobertson_%28cropped%29.jpg'),
Oscar(wiki='/wiki/John_Wayne', name='John Wayne', date='1969', film='True Grit', role='Reuben "Rooster" Cogburn', description='American actor and filmmaker', width=231, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/John_Wayne_-_still_portrait.jpg/231px-John_Wayne_-_still_portrait.jpg'),
Oscar(wiki='/wiki/Gene_Hackman', name='Gene Hackman', date='1971', film='The French Connection', role='Detective Jimmy "Popeye" Doyle', description='American actor and novelist', width=233, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Gene_Hackman_-_1972.jpg/233px-Gene_Hackman_-_1972.jpg'),
Oscar(wiki='/wiki/Jack_Lemmon', name='Jack Lemmon', date='1973', film='Save the Tiger', role='Harry Stoner', description='American actor (1925-2001)', width=253, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Jack_Lemmon_-_1968.jpg/253px-Jack_Lemmon_-_1968.jpg'),
Oscar(wiki='/wiki/Art_Carney', name='Art Carney', date='1974', film='Harry and Tonto', role='Harry Coombes', description='American actor and comedian', width=255, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Art_Carney_-_1959.jpg/255px-Art_Carney_-_1959.jpg'),
Oscar(wiki='/wiki/Jack_Nicholson', name='Jack Nicholson', date='1975', film="One Flew Over the Cuckoo's Nest", role='Randle Patrick "Mac" McMurphy', description='American actor and filmmaker', width=253, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Jack_Nicholson_2001_%28cropped%29.jpg/253px-Jack_Nicholson_2001_%28cropped%29.jpg'),
Oscar(wiki='/wiki/Richard_Dreyfuss', name='Richard Dreyfuss', date='1977', film='The Goodbye Girl', role='Elliot Garfield', description='American actor', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Richard_Dreyfuss_%2846291399092%29.jpg/240px-Richard_Dreyfuss_%2846291399092%29.jpg'),
Oscar(wiki='/wiki/Jon_Voight', name='Jon Voight', date='1978', film='Coming Home', role='Luke Martin', description='American actor', width=241, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Jon_Voight_2012.jpg/241px-Jon_Voight_2012.jpg'),
Oscar(wiki='/wiki/Dustin_Hoffman', name='Dustin Hoffman', date='1979', film='Kramer vs. Kramer', role='Ted Kramer', description='American actor and director', width=218, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Dustin_Hoffman_Quartet_avp_2013_2.jpg/218px-Dustin_Hoffman_Quartet_avp_2013_2.jpg'),
Oscar(wiki='/wiki/Robert_De_Niro', name='Robert De Niro', date='1980', film='Raging Bull', role='Jake LaMotta', description='American actor, director, and producer', width=205, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Robert_De_Niro_Cannes_2016.jpg/205px-Robert_De_Niro_Cannes_2016.jpg'),
Oscar(wiki='/wiki/Henry_Fonda', name='Henry Fonda', date='1981', film='On Golden Pond', role='Norman Thayer Jr.', description='American actor (1905–1982)', width=241, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Henry_Fonda_in_Warlock.jpg/241px-Henry_Fonda_in_Warlock.jpg'),
Oscar(wiki='/wiki/Ben_Kingsley', name='Ben Kingsley', date='1982', film='Gandhi', role='Mahatma Gandhi', description='English actor', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Ben_Kingsley_by_Gage_Skidmore.jpg/226px-Ben_Kingsley_by_Gage_Skidmore.jpg'),
Oscar(wiki='/wiki/Robert_Duvall', name='Robert Duvall', date='1983', film='Tender Mercies', role='Mac Sledge', description='American actor and director (born 1931)', width=227, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Robert_Duvall_2_by_David_Shankbone_%28cropped%29.jpg/227px-Robert_Duvall_2_by_David_Shankbone_%28cropped%29.jpg'),
Oscar(wiki='/wiki/F._Murray_Abraham', name='F. Murray Abraham', date='1984', film='Amadeus', role='Antonio Salieri', description='American actor', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/F_Murray.Abraham_cropped.jpg/213px-F_Murray.Abraham_cropped.jpg'),
Oscar(wiki='/wiki/William_Hurt', name='William Hurt', date='1985', film='Kiss of the Spider Woman', role='Luis Molina', description='American actor', width=201, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/History_of_Violence_002_%287271227040%29.jpg/201px-History_of_Violence_002_%287271227040%29.jpg'),
Oscar(wiki='/wiki/Paul_Newman', name='Paul Newman', date='1986', film='The Color of Money', role='Fast Eddie Felson', description='American actor and film director', width=260, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Paul_Newman_1954.JPG/260px-Paul_Newman_1954.JPG'),
Oscar(wiki='/wiki/Michael_Douglas', name='Michael Douglas', date='1987', film='Wall Street', role='Gordon Gekko', description='American actor and producer', width=224, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Michael_Douglas_C%C3%A9sar_2016_3.jpg/224px-Michael_Douglas_C%C3%A9sar_2016_3.jpg'),
Oscar(wiki='/wiki/Dustin_Hoffman', name='Dustin Hoffman', date='1988', film='Rain Man', role='Raymond Babbitt', description='American actor and director', width=218, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Dustin_Hoffman_Quartet_avp_2013_2.jpg/218px-Dustin_Hoffman_Quartet_avp_2013_2.jpg'),
Oscar(wiki='/wiki/Daniel_Day-Lewis', name='Daniel Day-Lewis', date='1989', film='My Left Foot', role='Christy Brown', description='British actor', width=239, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Daniel_Day-Lewis%2C_Jaguar%2C_Mille_Miglia_2013_cropped.jpg/239px-Daniel_Day-Lewis%2C_Jaguar%2C_Mille_Miglia_2013_cropped.jpg'),
Oscar(wiki='/wiki/Jeremy_Irons', name='Jeremy Irons', date='1990', film='Reversal of Fortune', role='Claus von Bülow', description='British actor', width=214, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Jeremy_Irons.jpg/214px-Jeremy_Irons.jpg'),
Oscar(wiki='/wiki/Anthony_Hopkins', name='Anthony Hopkins', date='1991', film='The Silence of the Lambs', role='Dr. Hannibal Lecter', description='Welsh actor', width=252, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/AnthonyHopkins10TIFF.jpg/252px-AnthonyHopkins10TIFF.jpg'),
Oscar(wiki='/wiki/Al_Pacino', name='Al Pacino', date='1992', film='Scent of a Woman', role='Lieutenant Colonel Frank Slade', description='American actor', width=232, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Al_Pacino_2016_%2830401544240%29.jpg/232px-Al_Pacino_2016_%2830401544240%29.jpg'),
Oscar(wiki='/wiki/Tom_Hanks', name='Tom Hanks', date='1993', film='Philadelphia', role='Andrew "Andy" Beckett', description='American actor, film producer and comedian', width=230, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Tom_Hanks_TIFF_2019.jpg/230px-Tom_Hanks_TIFF_2019.jpg'),
Oscar(wiki='/wiki/Nicolas_Cage', name='Nicolas Cage', date='1995', film='Leaving Las Vegas', role='Ben Sanderson', description='American actor', width=207, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Nicolas_Cage_Deauville_2013.jpg/207px-Nicolas_Cage_Deauville_2013.jpg'),
Oscar(wiki='/wiki/Geoffrey_Rush', name='Geoffrey Rush', date='1996', film='Shine', role='David Helfgott', description='Australian actor', width=217, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Geoffrey_Rush_Final_Portrait_Red_Carpet_Berlinale_2017_01_%28cropped%29.jpg/217px-Geoffrey_Rush_Final_Portrait_Red_Carpet_Berlinale_2017_01_%28cropped%29.jpg'),
Oscar(wiki='/wiki/Jack_Nicholson', name='Jack Nicholson', date='1997', film='As Good as It Gets', role='Melvin Udall', description='American actor and filmmaker', width=253, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Jack_Nicholson_2001_%28cropped%29.jpg/253px-Jack_Nicholson_2001_%28cropped%29.jpg'),
Oscar(wiki='/wiki/Roberto_Benigni', name='Roberto Benigni', date='1998', film='Life Is Beautiful', role='Guido Orefice', description='Italian actor, comedian, screenwriter and director', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Roberto_Benigni-5274.jpg/213px-Roberto_Benigni-5274.jpg'),
Oscar(wiki='/wiki/Kevin_Spacey', name='Kevin Spacey', date='1999', film='American Beauty', role='Lester Burnham', description='American actor and producer', width=232, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Kevin_Spacey%2C_May_2013.jpg/232px-Kevin_Spacey%2C_May_2013.jpg'),
Oscar(wiki='/wiki/Russell_Crowe', name='Russell Crowe', date='2000', film='Gladiator', role='Maximus Decimus Meridius', description='New Zealand-born actor, film producer and musician', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Russell_Crowe_%2833994020424%29.jpg/213px-Russell_Crowe_%2833994020424%29.jpg'),
Oscar(wiki='/wiki/Denzel_Washington', name='Denzel Washington', date='2001', film='Training Day', role='Det. Sgt. Alonzo Harris', description='American actor, director, and producer', width=210, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Denzel_Washington_%2829479254650%29_%28cropped%29.jpg/210px-Denzel_Washington_%2829479254650%29_%28cropped%29.jpg'),
Oscar(wiki='/wiki/Adrien_Brody', name='Adrien Brody', date='2002', film='The Pianist', role='Władysław Szpilman', description='American actor', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Adrien_Brody_Cannes_2014.jpg/226px-Adrien_Brody_Cannes_2014.jpg'),
Oscar(wiki='/wiki/Sean_Penn', name='Sean Penn', date='2003', film='Mystic River', role='Jimmy Markum', description='American actor, screenwriter, and film director', width=253, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Seanpenn1.jpg/253px-Seanpenn1.jpg'),
Oscar(wiki='/wiki/Jamie_Foxx', name='Jamie Foxx', date='2004', film='Ray', role='Ray Charles', description='American actor, comedian, singer, and presenter from Texas', width=266, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Jamie_Foxx_by_Gage_Skidmore.jpg/266px-Jamie_Foxx_by_Gage_Skidmore.jpg'),
Oscar(wiki='/wiki/Philip_Seymour_Hoffman', name='Philip Seymour Hoffman', date='2005', film='Capote', role='Truman Capote', description='American actor', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Philip_Seymour_Hoffman_2011.jpg/240px-Philip_Seymour_Hoffman_2011.jpg'),
Oscar(wiki='/wiki/Forest_Whitaker', name='Forest Whitaker', date='2006', film='The Last King of Scotland', role='Idi Amin', description='American actor', width=228, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Forest_Whitaker_by_Gage_Skidmore.jpg/228px-Forest_Whitaker_by_Gage_Skidmore.jpg'),
Oscar(wiki='/wiki/Daniel_Day-Lewis', name='Daniel Day-Lewis', date='2007', film='There Will Be Blood', role='Daniel Plainview', description='British actor', width=239, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Daniel_Day-Lewis%2C_Jaguar%2C_Mille_Miglia_2013_cropped.jpg/239px-Daniel_Day-Lewis%2C_Jaguar%2C_Mille_Miglia_2013_cropped.jpg'),
Oscar(wiki='/wiki/Sean_Penn', name='Sean Penn', date='2008', film='Milk', role='Harvey Milk', description='American actor, screenwriter, and film director', width=253, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Seanpenn1.jpg/253px-Seanpenn1.jpg'),
Oscar(wiki='/wiki/Jeff_Bridges', name='Jeff Bridges', date='2009', film='Crazy Heart', role='Otis "Bad" Blake', description='American actor', width=233, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Jeff_Bridges_by_Gage_Skidmore_3.jpg/233px-Jeff_Bridges_by_Gage_Skidmore_3.jpg'),
Oscar(wiki='/wiki/Colin_Firth', name='Colin Firth', date='2010', film="The King's Speech", role='King George VI', description='English actor', width=238, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Colin_Firth_%2836124162705%29_%28cropped%29.jpg/238px-Colin_Firth_%2836124162705%29_%28cropped%29.jpg'),
Oscar(wiki='/wiki/Jean_Dujardin', name='Jean Dujardin', date='2011', film='The Artist', role='George Valentin', description='French actor', width=208, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Christophe_Lambert_et_Jean_Dujardin_%28Cropped%29.jpg/208px-Christophe_Lambert_et_Jean_Dujardin_%28Cropped%29.jpg'),
Oscar(wiki='/wiki/Daniel_Day-Lewis', name='Daniel Day-Lewis', date='2012', film='Lincoln', role='Abraham Lincoln', description='British actor', width=239, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Daniel_Day-Lewis%2C_Jaguar%2C_Mille_Miglia_2013_cropped.jpg/239px-Daniel_Day-Lewis%2C_Jaguar%2C_Mille_Miglia_2013_cropped.jpg'),
Oscar(wiki='/wiki/Matthew_McConaughey', name='Matthew McConaughey', date='2013', film='Dallas Buyers Club', role='Ron Woodroof', description='American actor', width=219, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Matthew_McConaughey_2019_%2848648344772%29.jpg/219px-Matthew_McConaughey_2019_%2848648344772%29.jpg'),
Oscar(wiki='/wiki/Eddie_Redmayne', name='Eddie Redmayne', date='2014', film='The Theory of Everything', role='Stephen Hawking', description='English actor', width=203, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Eddie_Redmayne_2016_%28cropped%29.jpg/203px-Eddie_Redmayne_2016_%28cropped%29.jpg'),
Oscar(wiki='/wiki/Leonardo_DiCaprio', name='Leonardo DiCaprio', date='2015', film='The Revenant', role='Hugh Glass', description='American actor and producer (born 1974)', width=203, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Leonardo_Dicaprio_Cannes_2019.jpg/203px-Leonardo_Dicaprio_Cannes_2019.jpg'),
Oscar(wiki='/wiki/Casey_Affleck', name='Casey Affleck', date='2016', film='Manchester by the Sea', role='Lee Chandler', description='American actor', width=263, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Casey_Affleck_at_the_Manchester_by_the_Sea_premiere_%2830199719155%29_%28cropped%29.jpg/263px-Casey_Affleck_at_the_Manchester_by_the_Sea_premiere_%2830199719155%29_%28cropped%29.jpg'),
Oscar(wiki='/wiki/Gary_Oldman', name='Gary Oldman', date='2017', film='Darkest Hour', role='Winston Churchill', description='British actor and filmmaker', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gary_Oldman_Cannes_2018.jpg/226px-Gary_Oldman_Cannes_2018.jpg'),
Oscar(wiki='/wiki/Joaquin_Phoenix', name='Joaquin Phoenix', date='2019', film='Joker', role='Arthur Fleck / Joker', description='American actor and producer', width=256, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Joaquin_Phoenix_in_2018.jpg/256px-Joaquin_Phoenix_in_2018.jpg'),
Oscar(wiki='/wiki/Anthony_Hopkins', name='Anthony Hopkins', date='2020/21', film='The Father', role='Anthony', description='Welsh actor', width=252, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/AnthonyHopkins10TIFF.jpg/252px-AnthonyHopkins10TIFF.jpg')]





class DragDrop(engmonarchs.DragDrop):
    
    def __init__(self):
        global order
        
        arrangement=list(range(len(deck)))
        random.shuffle(arrangement)
        order=arrangement[:12]
        dragdrop.DragDrop.__init__(self,deck,order)

    def getDeck(self,deck):
        self.contentDeck= [deck[i] for i in order]

    def makeHeader(self,content: Oscar,cardno):
        header_id = f'H{cardno}'
        
        
        fs= "small" if len(content.name)>10 else "large"
        header = html.DIV(
            html.SPAN(
                content.name,id=f'Q{cardno}'
                ),
                          id=header_id,
                          style={'text-align': 'center', 'font-size': fs, 'height': px(30), 'background-color': 'gray', 'border-bottom': 'dotted black', 'padding': '3px', 'font-family': 'sans-serif', 'font-weight': 'bold', "border-radius": "inherit", "margin": px(4), }
                          )
        return header
    
    def makeFrontImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content.source
        return html.DIV(
            html.IMG(
                src=img, 
                id=image_id, 
                style={"width":px(self.card_width),"height":px(self.card_height - 30 - 14)}
            ),
            Class="card-body",
            id=body_id
            )
    
    def makeBackImage(self,content,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content.source
        text=f'<BR><B>Played</B><BR>{content.role}<BR><B>In</B><BR>{content.film}'
        return html.DIV(
            html.A(content.description,href="https://en.wikipedia.org/"+content.wiki,target='_blank')+
            html.SPAN(text)+
#            html.DIV(html.SPAN(content.description))+
#            html.DIV(html.SPAN("<BR>Played<BR>", style={"font-weight": "bold"})+html.SPAN(content.role))+
#            html.DIV(html.SPAN("<BR>In<BR>", style={"font-weight": "bold"})+html.SPAN(content.film))+
            html.DIV(html.SPAN(content.date),Class="date")

            
            ,
            #html.A("X",href="https://en.wikipedia.org/"+content.WikiURL,target='_blank'),
            Class="card-text",
            #style={'font_size': 'small', "text-align": 'center'},
            id=body_id,
            text_align='center'
            )
        pass
    
