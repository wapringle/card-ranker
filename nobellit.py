import time,copy,sys
from dataclasses import dataclass
from browser import document, html, timer, window

import  dragdrop, engmonarchs
from dragdrop import px,order
import random



@dataclass
class NobelLit:
    date: str
    wiki: str
    name: str
    country: str
    genre: str
    width: str
    height: str
    source: str


deck=[\
    NobelLit(date='1901\n', wiki='/wiki/Sully_Prudhomme', name='Sully Prudhomme', country='France', genre='poetry, essay\n', width=202, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Sully_Prudhomme%2C_Ren%C3%A9-Fran%C3%A7ois-Armand%2C_BNF_Gallica.jpg/202px-Sully_Prudhomme%2C_Ren%C3%A9-Fran%C3%A7ois-Armand%2C_BNF_Gallica.jpg'),
     NobelLit(date='1902\n', wiki='/wiki/Theodor_Mommsen', name='Theodor Mommsen', country='Germany', genre='history, law\n', width=218, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Theodor_Mommsen_2.jpg/218px-Theodor_Mommsen_2.jpg'),
     NobelLit(date='1903\n', wiki='/wiki/Bj%C3%B8rnstjerne_Bj%C3%B8rnson', name='Bjørnstjerne Bjørnson', country='Norway', genre='poetry, novel, drama\n', width=223, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Portrett_av_Bj%C3%B8rnstjerne_Bj%C3%B8rnson%2C_1909_-_no-nb_digifoto_20150129_00043_bldsa_BB0791_-_Restoration.jpg/223px-Portrett_av_Bj%C3%B8rnstjerne_Bj%C3%B8rnson%2C_1909_-_no-nb_digifoto_20150129_00043_bldsa_BB0791_-_Restoration.jpg'),
     NobelLit(date='1904\n', wiki='/wiki/Fr%C3%A9d%C3%A9ric_Mistral', name='Frédéric Mistral', country='France', genre='poetry, philology\n', width=232, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Frederic_Mistral_portrait_photo.jpg/232px-Frederic_Mistral_portrait_photo.jpg'),
     NobelLit(date='1905\n', wiki='/wiki/Henryk_Sienkiewicz', name='Henryk Sienkiewicz', country='Poland', genre='novel\n', width=223, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Stanis%C5%82aw_Biza%C5%84ski-H.Sienkiewicz.jpg/223px-Stanis%C5%82aw_Biza%C5%84ski-H.Sienkiewicz.jpg'),
     NobelLit(date='1906\n', wiki='/wiki/Giosu%C3%A8_Carducci', name='Giosuè Carducci', country='Italy', genre='poetry\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Giosu%C3%A8_Carducci2.jpg/240px-Giosu%C3%A8_Carducci2.jpg'),
     NobelLit(date='1907\n', wiki='/wiki/Rudyard_Kipling', name='Rudyard Kipling', country='United Kingdom', genre='novel, short story, poetry\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Rudyard_Kipling_%28portrait%29.jpg/240px-Rudyard_Kipling_%28portrait%29.jpg'),
     NobelLit(date='1908\n', wiki='/wiki/Rudolf_Christoph_Eucken', name='Rudolf Christoph Eucken', country='Germany', genre='philosophy\n', width=211, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Eucken-im-Alter.png/211px-Eucken-im-Alter.png'),
     NobelLit(date='1909\n', wiki='/wiki/Selma_Lagerl%C3%B6f', name='Selma Lagerlöf', country='Sweden', genre='novel, short story\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Selma_Lagerl%C3%B6f.jpg/226px-Selma_Lagerl%C3%B6f.jpg'),
     NobelLit(date='1910\n', wiki='/wiki/Paul_Heyse', name='Paul von Heyse', country='Germany', genre='poetry, drama, novel, short story\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Paul_Heyse_1910.jpg/226px-Paul_Heyse_1910.jpg'),
     NobelLit(date='1911\n', wiki='/wiki/Maurice_Maeterlinck', name='Maurice Maeterlinck', country='Belgium', genre='drama, poetry, essay\n', width=297, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Maurice_Maeterlinck_2.jpg/297px-Maurice_Maeterlinck_2.jpg'),
     NobelLit(date='1912\n', wiki='/wiki/Gerhart_Hauptmann', name='Gerhart Hauptmann', country='Germany', genre='drama, novel\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Gerhart_Hauptmann_nobel.jpg/226px-Gerhart_Hauptmann_nobel.jpg'),
     NobelLit(date='1913\n', wiki='/wiki/Rabindranath_Tagore', name='Rabindranath Tagore', country='India', genre='poetry, novel, drama, short story, music, essay, philosophy, literary criticism, translation\n', width=242, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Rabindranath_Tagore_unknown_location.jpg/242px-Rabindranath_Tagore_unknown_location.jpg'),
     NobelLit(date='1915\n', wiki='/wiki/Romain_Rolland', name='Romain Rolland', country='France', genre='novel\n', width=232, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Romain_Rolland_de_face_au_balcon%2C_Meurisse%2C_1914_retouche.jpg/232px-Romain_Rolland_de_face_au_balcon%2C_Meurisse%2C_1914_retouche.jpg'),
     NobelLit(date='1916\n', wiki='/wiki/Verner_von_Heidenstam', name='Verner von Heidenstam', country='Sweden', genre='poetry, novel\n', width=320, height=247, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Johan_Krouth%C3%A9n_-_Portr%C3%A4tt_av_Verner_von_Heidenstam.jpg/320px-Johan_Krouth%C3%A9n_-_Portr%C3%A4tt_av_Verner_von_Heidenstam.jpg'),
     NobelLit(date='1917\n', wiki='/wiki/Karl_Adolph_Gjellerup', name='Karl Adolph Gjellerup', country='Denmark', genre='poetry\n', width=277, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Karl_Gjellerup.jpg/277px-Karl_Gjellerup.jpg'),
     NobelLit(date='1919\n', wiki='/wiki/Carl_Spitteler', name='Carl Spitteler', country='Switzerland', genre='poetry\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Carl_Spitteler_1919.jpg/226px-Carl_Spitteler_1919.jpg'),
     NobelLit(date='1920\n', wiki='/wiki/Knut_Hamsun', name='Knut Hamsun', country='Norway', genre='novel\n', width=222, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Hamsun_bldsa_HA0341.jpg/222px-Hamsun_bldsa_HA0341.jpg'),
     NobelLit(date='1921\n', wiki='/wiki/Anatole_France', name='Anatole France', country='France', genre='novel, poetry\n', width=241, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Anatole_France_young_years.jpg/241px-Anatole_France_young_years.jpg'),
     NobelLit(date='1922\n', wiki='/wiki/Jacinto_Benavente', name='Jacinto Benavente', country='Spain', genre='drama\n', width=238, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Jacinto_Benavente_y_Martinez.jpg/238px-Jacinto_Benavente_y_Martinez.jpg'),
     NobelLit(date='1923\n', wiki='/wiki/W._B._Yeats', name='William Butler Yeats', country='Ireland', genre='poetry\n', width=239, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Yeats_Boughton.jpg/239px-Yeats_Boughton.jpg'),
     NobelLit(date='1924\n', wiki='/wiki/W%C5%82adys%C5%82aw_Reymont', name='Władysław Reymont', country='Poland', genre='novel\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Wladyslaw_Reymont_1924.jpg/226px-Wladyslaw_Reymont_1924.jpg'),
     NobelLit(date='1925\n', wiki='/wiki/George_Bernard_Shaw', name='George Bernard Shaw', country='UK', genre='drama, literary criticism\n', width=227, height=320, source='https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Bernard-Shaw-ILN-1911-original.jpg/227px-Bernard-Shaw-ILN-1911-original.jpg'),
     NobelLit(date='1926\n', wiki='/wiki/Grazia_Deledda', name='Grazia Deledda', country='Italy', genre='poetry, novel\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Grazia_Deledda_1926.jpg/226px-Grazia_Deledda_1926.jpg'),
     NobelLit(date='1927\n', wiki='/wiki/Henri_Bergson', name='Henri Bergson', country='France', genre='philosophy\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Henri_Bergson_02.jpg/226px-Henri_Bergson_02.jpg'),
     NobelLit(date='1928\n', wiki='/wiki/Sigrid_Undset', name='Sigrid Undset', country='Norway', genre='novel\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Sigrid_Undset_1928.jpg/226px-Sigrid_Undset_1928.jpg'),
     NobelLit(date='1929\n', wiki='/wiki/Thomas_Mann', name='Thomas Mann', country='Germany', genre='novel, short story, essay\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Thomas_Mann_1929.jpg/226px-Thomas_Mann_1929.jpg'),
     NobelLit(date='1930\n', wiki='/wiki/Sinclair_Lewis', name='Sinclair Lewis', country='United States', genre='novel, short story, drama\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Sinclair_Lewis_1930.jpg/226px-Sinclair_Lewis_1930.jpg'),
     NobelLit(date='1931\n', wiki='/wiki/Erik_Axel_Karlfeldt', name='Erik Axel Karlfeldt', country='Sweden', genre='poetry\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Erik_Axel_Karlfeldt_1931.jpg/226px-Erik_Axel_Karlfeldt_1931.jpg'),
     NobelLit(date='1932\n', wiki='/wiki/John_Galsworthy', name='John Galsworthy', country='United Kingdom', genre='novel\n', width=233, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/John_Galsworthy_2.jpg/233px-John_Galsworthy_2.jpg'),
     NobelLit(date='1933\n', wiki='/wiki/Ivan_Bunin', name='Ivan Bunin', country='Russian Empire', genre='short story, poetry, novel\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Ivan_Bunin_%28sepia%29.jpg/240px-Ivan_Bunin_%28sepia%29.jpg'),
     NobelLit(date='1934\n', wiki='/wiki/Luigi_Pirandello', name='Luigi Pirandello', country='Italy', genre='drama, novel, short story\n', width=266, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Luigi_Pirandello_1932.jpg/266px-Luigi_Pirandello_1932.jpg'),
     NobelLit(date='1936\n', wiki='/wiki/Eugene_O%27Neill', name="Eugene O'Neill", country='United States', genre='drama\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/ONeill-Eugene-LOC.jpg/240px-ONeill-Eugene-LOC.jpg'),
     NobelLit(date='1937\n', wiki='/wiki/Roger_Martin_du_Gard', name='Roger Martin du Gard', country='France', genre='novel\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Roger_Martin_du_Gard_1937.jpg/226px-Roger_Martin_du_Gard_1937.jpg'),
     NobelLit(date='1938\n', wiki='/wiki/Pearl_S._Buck', name='Pearl Buck', country='United States', genre='novel, biography\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pearl_Buck_1972.jpg/240px-Pearl_Buck_1972.jpg'),
     NobelLit(date='1939\n', wiki='/wiki/Frans_Eemil_Sillanp%C3%A4%C3%A4', name='Frans Eemil Sillanpää', country='Finland', genre='novel\n', width=232, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/FransEemilSillanp%C3%A4%C3%A4.jpg/232px-FransEemilSillanp%C3%A4%C3%A4.jpg'),
     NobelLit(date='1944\n', wiki='/wiki/Johannes_Vilhelm_Jensen', name='Johannes Vilhelm Jensen', country='Denmark', genre='novel, short story\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Johannes_Vilhelm_Jensen_1944.jpg/226px-Johannes_Vilhelm_Jensen_1944.jpg'),
     NobelLit(date='1945\n', wiki='/wiki/Gabriela_Mistral', name='Gabriela Mistral', country='Chile', genre='poetry\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Gabriela_Mistral_1945.jpg/226px-Gabriela_Mistral_1945.jpg'),
     NobelLit(date='1946\n', wiki='/wiki/Hermann_Hesse', name='Hermann Hesse', country='Germany', genre='novel, poetry\n', width=268, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hermann_Hesse_2.jpg/268px-Hermann_Hesse_2.jpg'),
     NobelLit(date='1947\n', wiki='/wiki/Andr%C3%A9_Gide', name='André Gide', country='France', genre='novel, essay\n', width=300, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Andr%C3%A9_Gide.jpg/300px-Andr%C3%A9_Gide.jpg'),
     NobelLit(date='1948\n', wiki='/wiki/T._S._Eliot', name='Thomas Stearns Eliot', country='United Kingdom', genre='poetry\n', width=276, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Thomas_Stearns_Eliot_by_Lady_Ottoline_Morrell_%281934%29.jpg/276px-Thomas_Stearns_Eliot_by_Lady_Ottoline_Morrell_%281934%29.jpg'),
     NobelLit(date='1949\n', wiki='/wiki/William_Faulkner', name='William Faulkner', country='United States', genre='novel, short story\n', width=250, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Carl_Van_Vechten_-_William_Faulkner_%28greyscale_and_cropped%29.jpg/250px-Carl_Van_Vechten_-_William_Faulkner_%28greyscale_and_cropped%29.jpg'),
     NobelLit(date='1950\n', wiki='/wiki/Bertrand_Russell', name='Bertrand Russell', country='United Kingdom', genre='philosophy\n', width=254, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Bertrand_Russell_1957.jpg/254px-Bertrand_Russell_1957.jpg'),
     NobelLit(date='1951\n', wiki='/wiki/P%C3%A4r_Lagerkvist', name='Pär Lagerkvist', country='Sweden', genre='poetry, novel, short story, drama\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Lagerkvist.jpg/226px-Lagerkvist.jpg'),
     NobelLit(date='1952\n', wiki='/wiki/Fran%C3%A7ois_Mauriac', name='François Mauriac', country='France', genre='novel, short story\n', width=278, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Fran%C3%A7ois_Mauriac_redux.jpg/278px-Fran%C3%A7ois_Mauriac_redux.jpg'),
     NobelLit(date='1953\n', wiki='/wiki/Winston_Churchill', name='Winston Churchill', country='United Kingdom', genre='history, essay, memoirs\n', width=251, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Sir_Winston_Churchill_-_19086236948.jpg/251px-Sir_Winston_Churchill_-_19086236948.jpg'),
     NobelLit(date='1954\n', wiki='/wiki/Ernest_Hemingway', name='Ernest Hemingway', country='United States', genre='novel, short story, screenplay\n', width=256, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/ErnestHemingway.jpg/256px-ErnestHemingway.jpg'),
     NobelLit(date='1955\n', wiki='/wiki/Halld%C3%B3r_Laxness', name='Halldór Laxness', country='Iceland', genre='novel, short story, drama, poetry\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Halld%C3%B3r_Kiljan_Laxness_1955.jpg/226px-Halld%C3%B3r_Kiljan_Laxness_1955.jpg'),
     NobelLit(date='1956\n', wiki='/wiki/Juan_Ram%C3%B3n_Jim%C3%A9nez', name='Juan Ramón Jiménez', country='Spain', genre='poetry\n', width=252, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/JRJimenez.JPG/252px-JRJimenez.JPG'),
     NobelLit(date='1957\n', wiki='/wiki/Albert_Camus', name='Albert Camus', country='France', genre='novel, short story, drama, philosophy, essay\n', width=267, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Albert_Camus%2C_gagnant_de_prix_Nobel%2C_portrait_en_buste%2C_pos%C3%A9_au_bureau%2C_faisant_face_%C3%A0_gauche%2C_cigarette_de_tabagisme.jpg/267px-Albert_Camus%2C_gagnant_de_prix_Nobel%2C_portrait_en_buste%2C_pos%C3%A9_au_bureau%2C_faisant_face_%C3%A0_gauche%2C_cigarette_de_tabagisme.jpg'),
     NobelLit(date='1958\n', wiki='/wiki/Boris_Pasternak', name='Boris Pasternak', country='Soviet Union', genre='novel, poetry, translation\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Boris_Pasternak_1969.jpg/240px-Boris_Pasternak_1969.jpg'),
     NobelLit(date='1959\n', wiki='/wiki/Salvatore_Quasimodo', name='Salvatore Quasimodo', country='Italy', genre='poetry\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Salvatore_Quasimodo_1959.jpg/226px-Salvatore_Quasimodo_1959.jpg'),
     NobelLit(date='1960\n', wiki='/wiki/Saint-John_Perse', name='Saint-John Perse', country='France', genre='poetry\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Saint-John_Perse_1960.jpg/226px-Saint-John_Perse_1960.jpg'),
     NobelLit(date='1961\n', wiki='/wiki/Ivo_Andri%C4%87', name='Ivo Andrić', country='Yugoslavia', genre='novel, short story\n', width=254, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/S._Kragujevic%2C_Ivo_Andric%2C_1961.jpg/254px-S._Kragujevic%2C_Ivo_Andric%2C_1961.jpg'),
     NobelLit(date='1962\n', wiki='/wiki/John_Steinbeck', name='John Steinbeck', country='United States', genre='novel, short story, screenplay\n', width=267, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/John_Steinbeck_1939_%28cropped%29.jpg/267px-John_Steinbeck_1939_%28cropped%29.jpg'),
     NobelLit(date='1963\n', wiki='/wiki/Giorgos_Seferis', name='Giorgos Seferis', country='Greece', genre='poetry, essay, memoirs\n', width=203, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/George_Seferis.JPG/203px-George_Seferis.JPG'),
     NobelLit(date='1964\n', wiki='/wiki/Jean-Paul_Sartre', name='Jean-Paul Sartre', country='France', genre='novel, short story, philosophy, drama, literary criticism, screenplay\n', width=320, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Sartre_1967_crop.jpg/320px-Sartre_1967_crop.jpg'),
     NobelLit(date='1965\n', wiki='/wiki/Mikhail_Sholokhov', name='Mikhail Sholokhov', country='Soviet Union', genre='novel\n', width=235, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Mikhail_Sholokhov_1960.jpg/235px-Mikhail_Sholokhov_1960.jpg'),
     NobelLit(date='1966\n', wiki='/wiki/Shmuel_Yosef_Agnon', name='Shmuel Yosef Agnon', country='Israel', genre='novel, short story\n', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/%D7%A4%D7%95%D7%A8%D7%98%D7%A8%D7%98_%D7%A9%22%D7%99_%D7%A2%D7%92%D7%A0%D7%95%D7%9F_%28cropped%29.jpg/213px-%D7%A4%D7%95%D7%A8%D7%98%D7%A8%D7%98_%D7%A9%22%D7%99_%D7%A2%D7%92%D7%A0%D7%95%D7%9F_%28cropped%29.jpg'),
     NobelLit(date='1967\n', wiki='/wiki/Miguel_%C3%81ngel_Asturias', name='Miguel Ángel Asturias', country='Guatemala', genre='novel, poetry\n', width=241, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Miguel_Angel_Asturias.jpg/241px-Miguel_Angel_Asturias.jpg'),
     NobelLit(date='1968\n', wiki='/wiki/Yasunari_Kawabata', name='Yasunari Kawabata', country='Japan', genre='novel, short story\n', width=303, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Yasunari_Kawabata_1938.jpg/303px-Yasunari_Kawabata_1938.jpg'),
     NobelLit(date='1969\n', wiki='/wiki/Samuel_Beckett', name='Samuel Beckett', country='Ireland', genre='novel, drama, poetry\n', width=235, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Samuel_Beckett%2C_Pic%2C_1_%28cropped%29.jpg/235px-Samuel_Beckett%2C_Pic%2C_1_%28cropped%29.jpg'),
     NobelLit(date='1970\n', wiki='/wiki/Aleksandr_Solzhenitsyn', name='Aleksandr Solzhenitsyn', country='Soviet Union', genre='novel\n', width=255, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Aleksandr_Solzhenitsyn_1974crop.jpg/255px-Aleksandr_Solzhenitsyn_1974crop.jpg'),
     NobelLit(date='1971\n', wiki='/wiki/Pablo_Neruda', name='Pablo Neruda', country='Chile', genre='poetry\n', width=252, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Pablo_Neruda_1963.jpg/252px-Pablo_Neruda_1963.jpg'),
     NobelLit(date='1972\n', wiki='/wiki/Heinrich_B%C3%B6ll', name='Heinrich Böll', country='West Germany', genre='novel, short story\n', width=260, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Bundesarchiv_B_145_Bild-F062164-0004%2C_Bonn%2C_Heinrich_B%C3%B6ll.jpg/260px-Bundesarchiv_B_145_Bild-F062164-0004%2C_Bonn%2C_Heinrich_B%C3%B6ll.jpg'),
     NobelLit(date='1973\n', wiki='/wiki/Patrick_White', name='Patrick White', country='Australia', genre='novel, short story, drama\n', width=288, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Patrick_White_1973.jpg/288px-Patrick_White_1973.jpg'),
     NobelLit(date='1974\n', wiki='/wiki/Eyvind_Johnson', name='Eyvind Johnson', country='Sweden', genre='novel\n', width=215, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Eyvind.JPG/215px-Eyvind.JPG'),
     NobelLit(date='1975\n', wiki='/wiki/Eugenio_Montale', name='Eugenio Montale', country='Italy', genre='poetry\n', width=222, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Eugenio_Montale.jpg/222px-Eugenio_Montale.jpg'),
     NobelLit(date='1976\n', wiki='/wiki/Saul_Bellow', name='Saul Bellow', country='United States', genre='novel, short story\n', width=320, height=252, source='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Saul_Bellow_%28Herzog_portrait%29.jpg/320px-Saul_Bellow_%28Herzog_portrait%29.jpg'),
     NobelLit(date='1977\n', wiki='/wiki/Vicente_Aleixandre', name='Vicente Aleixandre', country='Spain', genre='poetry\n', width=210, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Vicentealeixandre.jpg/210px-Vicentealeixandre.jpg'),
     NobelLit(date='1978\n', wiki='/wiki/Isaac_Bashevis_Singer', name='Isaac Bashevis Singer', country='United States', genre='novel, short story, memoirs\n', width=201, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Dan_Hadani_collection_%28990044399930205171%29.jpg/201px-Dan_Hadani_collection_%28990044399930205171%29.jpg'),
     NobelLit(date='1979\n', wiki='/wiki/Odysseas_Elytis', name='Odysseas Elytis', country='Greece', genre='poetry, essay\n', width=320, height=307, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Odysseas_Elytis_1974.jpg/320px-Odysseas_Elytis_1974.jpg'),
     NobelLit(date='1980\n', wiki='/wiki/Czes%C5%82aw_Mi%C5%82osz', name='Czesław Miłosz', country='Poland', genre='poetry, essay\n', width=210, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Czeslaw_Milosz_3_ap.tif/lossy-page1-210px-Czeslaw_Milosz_3_ap.tif.jpg'),
     NobelLit(date='1981\n', wiki='/wiki/Elias_Canetti', name='Elias Canetti', country='United Kingdom', genre='novel, drama, memoirs, essay\n', width=293, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Elias_Canetti_2.jpg/293px-Elias_Canetti_2.jpg'),
     NobelLit(date='1982\n', wiki='/wiki/Gabriel_Garc%C3%ADa_M%C3%A1rquez', name='Gabriel García Márquez', country='Colombia', genre='novel, short story, screenplay\n', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Gabriel_Garcia_Marquez.jpg/213px-Gabriel_Garcia_Marquez.jpg'),
     NobelLit(date='1983\n', wiki='/wiki/William_Golding', name='William Golding', country='United Kingdom', genre='novel, poetry, drama\n', width=237, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/William_Golding_1983.jpg/237px-William_Golding_1983.jpg'),
     NobelLit(date='1984\n', wiki='/wiki/Jaroslav_Seifert', name='Jaroslav Seifert', country='Czechoslovakia', genre='poetry\n', width=320, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Jaroslav_Seifert_1981_foto_Hana_Hamplov%C3%A1.jpg/320px-Jaroslav_Seifert_1981_foto_Hana_Hamplov%C3%A1.jpg'),
     NobelLit(date='1985\n', wiki='/wiki/Claude_Simon', name='Claude Simon', country='France', genre='novel, literary criticism\n', width=223, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Claude_Simon_1967.jpg/223px-Claude_Simon_1967.jpg'),
     NobelLit(date='1986\n', wiki='/wiki/Wole_Soyinka', name='Wole Soyinka', country='Nigeria', genre='drama, novel, poetry, screenplay\n', width=301, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Wole_Soyinka_in_2018.jpg/301px-Wole_Soyinka_in_2018.jpg'),
     NobelLit(date='1987\n', wiki='/wiki/Joseph_Brodsky', name='Joseph Brodsky', country='United States', genre='poetry, essay\n', width=228, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Joseph_Brodsky_1988.jpg/228px-Joseph_Brodsky_1988.jpg'),
     NobelLit(date='1988\n', wiki='/wiki/Naguib_Mahfouz', name='Naguib Mahfouz', country='Egypt', genre='novel, short story\n', width=221, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Necip_Mahfuz.jpg/221px-Necip_Mahfuz.jpg'),
     NobelLit(date='1989\n', wiki='/wiki/Camilo_Jos%C3%A9_Cela', name='Camilo José Cela', country='Spain', genre='novel, short story, essay, poetry\n', width=228, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Camilo_Jos%C3%A9_Cela._Fototeca._Biblioteca_Virtual_del_Patrimonio_Bibliogr%C3%A1fico.jpg/228px-Camilo_Jos%C3%A9_Cela._Fototeca._Biblioteca_Virtual_del_Patrimonio_Bibliogr%C3%A1fico.jpg'),
     NobelLit(date='1990\n', wiki='/wiki/Octavio_Paz', name='Octavio Paz', country='Mexico', genre='poetry, essay\n', width=232, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Octavio_Paz_-_1988_Malm%C3%B6.jpg/232px-Octavio_Paz_-_1988_Malm%C3%B6.jpg'),
     NobelLit(date='1991\n', wiki='/wiki/Nadine_Gordimer', name='Nadine Gordimer', country='South Africa', genre='novel, short story, essay, drama\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Nadine_Gordimer_01.JPG/240px-Nadine_Gordimer_01.JPG'),
     NobelLit(date='1992\n', wiki='/wiki/Derek_Walcott', name='Derek Walcott', country='Saint Lucia', genre='poetry, drama\n', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Derek_Walcott.jpg/213px-Derek_Walcott.jpg'),
     NobelLit(date='1993\n', wiki='/wiki/Toni_Morrison', name='Toni Morrison', country='United States', genre='novel\n', width=224, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Toni_Morrison.jpg/224px-Toni_Morrison.jpg'),
     NobelLit(date='1994\n', wiki='/wiki/Kenzabur%C5%8D_%C5%8Ce', name='Kenzaburō Ōe', country='Japan', genre='novel, short story, essay\n', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Paris_-_Salon_du_livre_2012_-_Kenzabur%C5%8D_%C5%8Ce_-_003.jpg/213px-Paris_-_Salon_du_livre_2012_-_Kenzabur%C5%8D_%C5%8Ce_-_003.jpg'),
     NobelLit(date='1995\n', wiki='/wiki/Seamus_Heaney', name='Seamus Heaney', country='Ireland', genre='poetry, drama, translation\n', width=320, height=212, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Seamus_Heaney%2C_Irish_poet%2C_brightened.jpg/320px-Seamus_Heaney%2C_Irish_poet%2C_brightened.jpg'),
     NobelLit(date='1996\n', wiki='/wiki/Wis%C5%82awa_Szymborska', name='Wisława Szymborska', country='Poland', genre='poetry, essay, translation\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Wis%C5%82awa_Szymborska_2009.10.23_%281%29.jpg/240px-Wis%C5%82awa_Szymborska_2009.10.23_%281%29.jpg'),
     NobelLit(date='1997\n', wiki='/wiki/Dario_Fo', name='Dario Fo', country='Italy', genre='drama, songwriting\n', width=271, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/DarioFo1.jpg/271px-DarioFo1.jpg'),
     NobelLit(date='1998\n', wiki='/wiki/Jos%C3%A9_Saramago', name='José Saramago', country='Portugal', genre='novel, drama, poetry\n', width=320, height=249, source='https://upload.wikimedia.org/wikipedia/commons/5/5c/JSJoseSaramago.jpg'),
     NobelLit(date='1999\n', wiki='/wiki/G%C3%BCnter_Grass', name='Günter Grass', country='Germany', genre='novel, drama, poetry\n', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/G%C3%BCnter_Grass_auf_dem_Blauen_Sofa.jpg/213px-G%C3%BCnter_Grass_auf_dem_Blauen_Sofa.jpg'),
     NobelLit(date='2000\n', wiki='/wiki/Gao_Xingjian', name='Gao Xingjian', country='France', genre='novel, drama, literary criticism\n', width=226, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Gao_Xingjian_%282012%2C_cropped%29.jpg/226px-Gao_Xingjian_%282012%2C_cropped%29.jpg'),
     NobelLit(date='2001\n', wiki='/wiki/V._S._Naipaul', name='Vidiadhar Surajprasad Naipaul', country='United Kingdom', genre='novel, essay\n', width=320, height=213, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/VS_Naipaul_2016_Dhaka.jpg/320px-VS_Naipaul_2016_Dhaka.jpg'),
     NobelLit(date='2002\n', wiki='/wiki/Imre_Kert%C3%A9sz', name='Imre Kertész', country='Hungary', genre='novel\n', width=230, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Kert%C3%A9sz_Imre_%28Frankl_Aliona%29.jpg/230px-Kert%C3%A9sz_Imre_%28Frankl_Aliona%29.jpg'),
     NobelLit(date='2003\n', wiki='/wiki/J._M._Coetzee', name='John Maxwell Coetzee', country='Australia', genre='novel, essay, translation\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/J.M._Coetzee_by_Kubik.JPG/240px-J.M._Coetzee_by_Kubik.JPG'),
     NobelLit(date='2004\n', wiki='/wiki/Elfriede_Jelinek', name='Elfriede Jelinek', country='Austria', genre='novel, drama\n', width=239, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Elfriede_jelinek_2004_small.jpg/239px-Elfriede_jelinek_2004_small.jpg'),
     NobelLit(date='2005\n', wiki='/wiki/Harold_Pinter', name='Harold Pinter', country='United Kingdom', genre='drama, screenplay\n', width=305, height=241, source='https://upload.wikimedia.org/wikipedia/commons/d/df/Harold-pinter-atp.jpg'),
     NobelLit(date='2006\n', wiki='/wiki/Orhan_Pamuk', name='Orhan Pamuk', country='Turkey', genre='novel, screenplay, autobiography, essay\n', width=229, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Orhan_Pamuk_2009_Shankbone.jpg/229px-Orhan_Pamuk_2009_Shankbone.jpg'),
     NobelLit(date='2007\n', wiki='/wiki/Doris_Lessing', name='Doris Lessing', country='United Kingdom', genre='novel, drama, poetry, short story, memoirs, autobiography\n', width=256, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Doris_Lessing_3.jpg/256px-Doris_Lessing_3.jpg'),
     NobelLit(date='2008\n', wiki='/wiki/J._M._G._Le_Cl%C3%A9zio', name='Jean-Marie Gustave Le Clézio', country='France', genre='novel, short story, essay, translation\n', width=254, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Jean-Marie_Gustave_Le_Cl%C3%A9zio-press_conference_Dec_06th%2C_2008-9_%28cropped%29.jpg/254px-Jean-Marie_Gustave_Le_Cl%C3%A9zio-press_conference_Dec_06th%2C_2008-9_%28cropped%29.jpg'),
     NobelLit(date='2009\n', wiki='/wiki/Herta_M%C3%BCller', name='Herta Müller', country='Germany', genre='novel, short story, poetry, essay\n', width=256, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Herta_M%C3%BCller_%282019%29.jpg/256px-Herta_M%C3%BCller_%282019%29.jpg'),
     NobelLit(date='2010\n', wiki='/wiki/Mario_Vargas_Llosa', name='Mario Vargas Llosa', country='Peru', genre='novel, short story, essay, drama, memoirs\n', width=242, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Mario_Vargas_Llosa_%28crop_2%29.jpg/242px-Mario_Vargas_Llosa_%28crop_2%29.jpg'),
     NobelLit(date='2011\n', wiki='/wiki/Tomas_Transtr%C3%B6mer', name='Tomas Tranströmer', country='Sweden', genre='poetry, translation\n', width=301, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Transtroemer.jpg/301px-Transtroemer.jpg'),
     NobelLit(date='2012\n', wiki='/wiki/Mo_Yan', name='Mo Yan', country='China', genre='novel, short story\n', width=259, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/MoYan_Hamburg_2008.jpg/259px-MoYan_Hamburg_2008.jpg'),
     NobelLit(date='2013\n', wiki='/wiki/Alice_Munro', name='Alice Munro', country='Canada', genre='short story\n', width='ERROR', height='ERROR', source='ERROR'),
     NobelLit(date='2014\n', wiki='/wiki/Patrick_Modiano', name='Patrick Modiano', country='France', genre='novel, screenplay\n', width=257, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Patrick_Modiano_6_dec_2014_-_22.jpg/257px-Patrick_Modiano_6_dec_2014_-_22.jpg'),
     NobelLit(date='2015\n', wiki='/wiki/Svetlana_Alexievich', name='Svetlana Alexievich', country='Belarus', genre='history, essay\n', width=320, height=284, source='https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Swetlana_Alexijewitsch_2013.jpg/320px-Swetlana_Alexijewitsch_2013.jpg'),
     NobelLit(date='2016\n', wiki='/wiki/Bob_Dylan', name='Bob Dylan', country='United States', genre='poetry, songwriting\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Bob_Dylan_-_Azkena_Rock_Festival_2010_2.jpg/240px-Bob_Dylan_-_Azkena_Rock_Festival_2010_2.jpg'),
     NobelLit(date='2017\n', wiki='/wiki/Kazuo_Ishiguro', name='Kazuo Ishiguro', country='United Kingdom', genre='novel, screenplay, short story\n', width=258, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Kazuo_Ishiguro_in_2017_01.jpg/258px-Kazuo_Ishiguro_in_2017_01.jpg'),
     NobelLit(date='2018\n', wiki='/wiki/Olga_Tokarczuk', name='Olga Tokarczuk', country='Poland', genre='novel, short story, poetry, essay, screenplay\n', width=240, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Olga_Tokarczuk-9739.jpg/240px-Olga_Tokarczuk-9739.jpg'),
     NobelLit(date='2019\n', wiki='/wiki/Peter_Handke', name='Peter Handke', country='Austria', genre='novel, short story, drama, translation, screenplay\n', width=213, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Peter-handke.jpg/213px-Peter-handke.jpg'),
     NobelLit(date='2020\n', wiki='/wiki/Louise_Gl%C3%BCck', name='Louise Glück', country='United States', genre='poetry, essay\n', width=247, height=320, source='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Louise_Gl%C3%BCck_circa_1977.jpg/247px-Louise_Gl%C3%BCck_circa_1977.jpg'),
     NobelLit(date='2021\n', wiki='/wiki/Abdulrazak_Gurnah', name='Abdulrazak Gurnah', country='Tanzania', genre='novel\n', width=320, height=256, source='https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/AbulrazakGurnahHebronPanel_%28cropped%29.jpg/320px-AbulrazakGurnahHebronPanel_%28cropped%29.jpg')]



class DragDrop(engmonarchs.DragDrop):
    
    def __init__(self):
        global order
        
        arrangement=list(range(len(deck)))
        random.shuffle(arrangement)
        order=arrangement[:12]
        dragdrop.DragDrop.__init__(self,deck,order)

    def getDeck(self,deck):
        self.contentDeck= [deck[i] for i in order]

    def makeHeader(self,content: NobelLit,cardno):
        return self.makeHeaderText(content.name,cardno)        
    
    def makeFrontImage(self,content: NobelLit,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        img = content.source
        return html.DIV(
            html.IMG(
                src=img, 
                id=image_id, 
                style={"width":px(self.card_width - 10),"height":px(self.card_height - 30 - 14)}
            ),
            Class="card-body",
            id=body_id
            )
    
    def makeBackImage(self,content: NobelLit,cardno):
        image_id = f'I{cardno}'
        body_id = f'B{cardno}'
        txt_id=f'T{cardno}'
        date_id=f'D{cardno}'
        img = content.source
        text=f'{content.country}<br>{content.genre}'
        return html.DIV(
            html.DIV(
            html.A(content.name, href="https://en.wikipedia.org/"+content.wiki,target='_blank')+
            html.DIV(html.SPAN(text)
            ), 
            id=txt_id,           
            Class="card-text" )+
            html.DIV(html.SPAN(content.date),Class="date",id=date_id),
  
            id=body_id
            )
        pass
    
