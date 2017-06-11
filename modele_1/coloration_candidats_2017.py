# -*- coding: utf-8 -*-

raw_file=open("candidats_2017.csv","r")
raw_lines=raw_file.read().splitlines()
headers=raw_lines[0].split(";")
raw_lines=raw_lines[1:]

codes_circos=["1_1","1_2","1_3","1_4","1_5","2_1","2_2","2_3","2_4","2_5","3_1","3_2","3_3","4_1","4_2","5_1","5_2","6_1","6_2","6_3","6_4","6_5","6_6","6_7","6_8","6_9","7_1","7_2","7_3","8_1","8_2","8_3","9_1","9_2","10_1","10_2","10_3","11_1","11_2","11_3","12_1","12_2","12_3","13_1","13_2","13_3","13_4","13_5","13_6","13_7","13_8","13_9","13_10","13_11","13_12","13_13","13_14","13_15","13_16","14_1","14_2","14_3","14_4","14_5","14_6","15_1","15_2","16_1","16_2","16_3","17_1","17_2","17_3","17_4","17_5","18_1","18_2","18_3","19_1","19_2","2A_1","2A_2","2B_1","2B_2","21_1","21_2","21_3","21_4","21_5","22_1","22_2","22_3","22_4","22_5","23_1","24_1","24_2","24_3","24_4","25_1","25_2","25_3","25_4","25_5","26_1","26_2","26_3","26_4","27_1","27_2","27_3","27_4","27_5","28_1","28_2","28_3","28_4","29_1","29_2","29_3","29_4","29_5","29_6","29_7","29_8","30_1","30_2","30_3","30_4","30_5","30_6","31_1","31_2","31_3","31_4","31_5","31_6","31_7","31_8","31_9","31_10","32_1","32_2","33_1","33_2","33_3","33_4","33_5","33_6","33_7","33_8","33_9","33_10","33_11","33_12","34_1","34_2","34_3","34_4","34_5","34_6","34_7","34_8","34_9","35_1","35_2","35_3","35_4","35_5","35_6","35_7","35_8","36_1","36_2","37_1","37_2","37_3","37_4","37_5","38_1","38_2","38_3","38_4","38_5","38_6","38_7","38_8","38_9","38_10","39_1","39_2","39_3","40_1","40_2","40_3","41_1","41_2","41_3","42_1","42_2","42_3","42_4","42_5","42_6","43_1","43_2","44_1","44_2","44_3","44_4","44_5","44_6","44_7","44_8","44_9","44_10","45_1","45_2","45_3","45_4","45_5","45_6","46_1","46_2","47_1","47_2","47_3","48_1","49_1","49_2","49_3","49_4","49_5","49_6","49_7","50_1","50_2","50_3","50_4","51_1","51_2","51_3","51_4","51_5","52_1","52_2","53_1","53_2","53_3","54_1","54_2","54_3","54_4","54_5","54_6","55_1","55_2","56_1","56_2","56_3","56_4","56_5","56_6","57_1","57_2","57_3","57_4","57_5","57_6","57_7","57_8","57_9","58_1","58_2","59_1","59_2","59_3","59_4","59_5","59_6","59_7","59_8","59_9","59_10","59_11","59_12","59_13","59_14","59_15","59_16","59_17","59_18","59_19","59_20","59_21","60_1","60_2","60_3","60_4","60_5","60_6","60_7","61_1","61_2","61_3","62_1","62_2","62_3","62_4","62_5","62_6","62_7","62_8","62_9","62_10","62_11","62_12","63_1","63_2","63_3","63_4","63_5","64_1","64_2","64_3","64_4","64_5","64_6","65_1","65_2","66_1","66_2","66_3","66_4","67_1","67_2","67_3","67_4","67_5","67_6","67_7","67_8","67_9","68_1","68_2","68_3","68_4","68_5","68_6","69_1","69_2","69_3","69_4","69_5","69_6","69_7","69_8","69_9","69_10","69_11","69_12","69_13","69_14","70_1","70_2","71_1","71_2","71_3","71_4","71_5","72_1","72_2","72_3","72_4","72_5","73_1","73_2","73_3","73_4","74_1","74_2","74_3","74_4","74_5","74_6","75_1","75_2","75_3","75_4","75_5","75_6","75_7","75_8","75_9","75_10","75_11","75_12","75_13","75_14","75_15","75_16","75_17","75_18","76_1","76_2","76_3","76_4","76_5","76_6","76_7","76_8","76_9","76_10","77_1","77_2","77_3","77_4","77_5","77_6","77_7","77_8","77_9","77_10","77_11","78_1","78_2","78_3","78_4","78_5","78_6","78_7","78_8","78_9","78_10","78_11","78_12","79_1","79_2","79_3","80_1","80_2","80_3","80_4","80_5","81_1","81_2","81_3","82_1","82_2","83_1","83_2","83_3","83_4","83_5","83_6","83_7","83_8","84_1","84_2","84_3","84_4","84_5","85_1","85_2","85_3","85_4","85_5","86_1","86_2","86_3","86_4","87_1","87_2","87_3","88_1","88_2","88_3","88_4","89_1","89_2","89_3","90_1","90_2","91_1","91_2","91_3","91_4","91_5","91_6","91_7","91_8","91_9","91_10","92_1","92_2","92_3","92_4","92_5","92_6","92_7","92_8","92_9","92_10","92_11","92_12","92_13","93_1","93_2","93_3","93_4","93_5","93_6","93_7","93_8","93_9","93_10","93_11","93_12","94_1","94_2","94_3","94_4","94_5","94_6","94_7","94_8","94_9","94_10","94_11","95_1","95_2","95_3","95_4","95_5","95_6","95_7","95_8","95_9","95_10","971_1","971_2","971_3","971_4","972_1","972_2","972_3","972_4","973_1","973_2","974_1","974_2","974_3","974_4","974_5","974_6","974_7","985_1","985_2","988_1","988_2","987_1","987_2","987_3","975_1","986_1","979_1","99_1","99_2","99_3","99_4","99_5","99_6","99_7","99_8","99_9","99_10","99_11"]
couleurs=["LFI","PCF","EELV","PS","EM","UDI","LR","DLF","FN"]
candidats_colores_par_circo={}
candidats_RDG={}
for code in codes_circos :
	candidats_colores_par_circo[code]={}
	for couleur in couleurs :
		candidats_colores_par_circo[code][couleur]=[]
		candidats_RDG[code]=[]

for line in raw_lines :
	champs=line.split(";")
	champs[0]=champs[0].replace("ZA","971").replace("ZB","972").replace("ZC","973").replace("ZD","974").replace("ZM","985").replace("ZN","988").replace("ZP","987").replace("ZS","975").replace("ZW","986").replace("ZX","979").replace("ZZ","99")
#	print(champs[0]+'_'+champs[2])
	if champs[10]=="COM" :
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["PCF"].append(champs[8]+' '+champs[7])
	elif champs[10]=="FI" :
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["LFI"].append(champs[8]+' '+champs[7])
	elif champs[10]=="SOC":
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["PS"].append(champs[8]+' '+champs[7])
	elif champs[10]=="ECO" :
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["EELV"].append(champs[8]+' '+champs[7])
	elif champs[10]=="REM" or champs[10]=="MDM":
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["EM"].append(champs[8]+' '+champs[7])
	elif champs[10]=="UDI" :
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["UDI"].append(champs[8]+' '+champs[7])
	elif champs[10]=="LR" :
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["LR"].append(champs[8]+' '+champs[7])
	elif champs[10]=="DLF" :
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["DLF"].append(champs[8]+' '+champs[7])
	elif champs[10]=="FN" :
		candidats_colores_par_circo[champs[0]+'_'+champs[2]]["FN"].append(champs[8]+' '+champs[7])
	elif champs[10]=="RDG" :
		candidats_RDG[champs[0]+'_'+champs[2]].append(champs[8]+' '+champs[7])
#	print(candidats_colores_par_circo[champs[0]+'_'+champs[2]])

for code in codes_circos :
	if len(candidats_colores_par_circo[code]["PS"])==0 and len(candidats_RDG[code])>1:
		candidats_colores_par_circo[code]["PS"]=candidats_RDG[code]

candidats_eelv=[["8_1","Christophe Dumont"],["8_3","Cédric Sauvage"],["10_1","Michel Gueritte"],["10_2","Benjamin Birêne"],["51_1","Marie-Ange Petit"],["51_2","Patricia Coradel"],["51_3","David Nicanor"],["51_4","Françoise Brunel"],["52_1","Patrick Varney"],["52_2","Valérie Roffidal"],["67_1","Abdelkarim Ramdane"],["67_2","Leyla Binici"],["67_3","Christelle Syllas"],["67_4","Nathalie Palmier"],["67_5","Caroline Reys"],["67_6","Alexandre Gonçalves"],["67_7","Sandrine Lombard"],["68_1","Frédéric Hilbert"],["68_2","Laurent Dreyfus"],["68_4","Michel Knoerr"],["68_5","Florence Peter"],["54_3","Mikael Agopiantz"],["54_4","Marie-Neige Houchard"],["54_5","Patrick Baranger"],["54_6","Stéphane Léonardi"],["55_1","Jean-Marc Fleury"],["57_2","Marie-Pierre Comte"],["57_3","Mathias Boquet"],["57_4","Brigitte Albertus"],["57_5","Elisabeth Parachini"],["57_6","Chantal Mary"],["57_7","Martine Jung"],["57_8","Pascal Didier"],["57_9","Guy Harau"],["88_1","Lou Noirclere"],["88_2","Christine L'Heureux"],["88_4","Florence Lamaze"],["24_2","Brigitte Allain"],["24_4","François Coq"],["33_1","Nelson Palis-Niermann"],["33_2","Pierre Hurmic"],["33_4","Laure Desvalois"],["33_5","Stéphane Saubusse"],["33_6","Ludovic Guitton"],["33_7","Jean-Yves Grandidier"],["33_8","Nicolas Dubot"],["33_9","Dominique Baude"],["33_10","Agnès Séjournet"],["33_11","Oliver Richard"],["33_12","Anne-Laure Fabre-Nadler"],["40_1","Fanette Billard"],["40_2","Marie-Ange Delavenne"],["40_3","Richard Bidegaray"],["47_1","Maryse Combres"],["47_2","Mathilde Bœuf"],["47_3","Lionel Feuillas"],["64_2","Hélèna Timmer Blanchard"],["64_4","Véronique Zenoni"],["64_5","Thibault Pathias"],["64_6","Sophie Bussière"],["19_1","Mumine Ozsoy"],["19_2","Bruno Meura"],["23_1","Pierrette Bidon"],["87_1","Jean-Louis Pagès"],["87_2","Lucien Coindeau"],["87_3","Marcel Bayle"],["16_1","Odile Achard"],["16_2","Pascale Lacourarie"],["16_3","Anabelle Sicre"],["17_1","Jean-Marc Soubeste"],["17_2","Brigitte Desveaux"],["17_4","Laurence Marcillaud"],["17_5","Stéphanie Muzard"],["79_1","Alain Piveteau"],["79_2","Laurence Réau"],["79_3","Armelle Boivin"],["86_1","Marjorie Monni"],["86_2","Yohan Magneron"],["86_3","Florian Séjourné"],["86_4","Jean-Paul Bodin"],["11_2","Marie-Laure Arripe"],["11_3","Daniel Dedies"],["30_1","Dominique Andrieu Bonnet"],["30_2","Béatrice Leccia"],["30_3","Marie-Pierre Mercier"],["30_4","Dirk Offringa"],["30_5","Benjamin Deceuninck"],["30_6","Sibylle Jannekeyn"],["34_1","Jean-Louis Roumegas"],["34_2","Coralie Mantion"],["34_4","Laurent Dupont"],["34_9","Bertrand Coisne"],["66_1","Jean Codognès"],["66_4","Franck Huette"],["9_1","Florence Cortes"],["9_2","Jérôme Brosseron"],["12_1","Christian Lammens"],["12_2","Guy Pezet"],["31_1","Xavier Bigot"],["31_2","Salah Amokrane"],["31_3","Yannick Bourles"],["31_4","Elisabeth Matak"],["31_5","Clémentine Renaud"],["31_6","Stéphane Renaux"],["31_7","Catherine Renaux"],["31_8","Sophie Handschutter"],["31_9","Christine Arrighi"],["31_10","Henri Arevalo"],["32_1","Sylviane Baudois"],["32_2","Jean-Paul Dugoujon"],["46_1","Mathieu Ebbesen Goudin"],["46_2","Florence Rouch"],["65_1","Henri Lourdou"],["65_2","Cécile Bourdeu d’Aguerre"],["81_1","Julia Rivet"],["81_2","Pascal Pragnère"],["81_3","Stéphane Deleforge"],["82_1","Guillaume Arnaud"],["82_2","Dominique Parcellier"],["3_2","Philippe Buvat"],["3_3","Pascal Devos"],["15_1","Stéphane Frechou"],["15_2","Elise Brugiere"],["43_1","Anne Babian Lhermet"],["43_2","Marie-Laure Busselot"],["63_3","Nicolas Bonnet"],["63_4","Jean Baptiste Pegeon"],["63_5","Claire Lespagnol"],["1_2","Albane Colin"],["1_3","Jean Mercier"],["1_4","Anne Partensky-Leibman"],["1_5","Carole Pontier"],["7_1","Olivier Keller"],["7_2","Nadia Senni"],["7_3","Guillaume Vermorel"],["26_1","Annie Roche"],["26_2","Danielle Persico"],["26_3","Martine Morvan"],["26_4","Dominique Reynaud"],["38_1","Nicolas Kada"],["38_2","Elisabeh Letz"],["38_3","Soukaïna Larabi"],["38_4","Henry Tidy"],["38_5","Gaël  Roustan"],["38_6","Cécile Viallon"],["38_7","Nadine Reux"],["38_9","Patrick Cholat"],["38_10","Frédéric Espinosa"],["42_2","Olivier Longeon"],["42_3","Patricia Simonin-Chaillot"],["42_5","Alain Valentin"],["42_6","Jean Duverger"],["69_1","Bertrand Artigny"],["69_2","Rémi Zinck"],["69_3","Fanny Dubot"],["69_4","Véronique Dubois-Bertrand"],["69_5","Jérôme Trotignon"],["69_6","Béatrice Vessiller"],["69_7","Pierre Didier Tchetche-Apea"],["69_8","Bénédicte Hominal"],["69_9","Brigitte Ealet"],["69_10","Victor Fornito"],["69_11","Jérôme Bub"],["69_12","Hélène Dromain"],["69_13","Axel Marin"],["69_14","Véronique Giromagny"],["73_2","Yves Durieux"],["73_4","Yves Peutot"],["74_1","Jean-Jacques Bouchet"],["74_2","Jeanie Tremblay"],["74_3","Annie Collinet"],["74_4","Catherine Walthert Selosse"],["74_6","Jacques Venjean"],["14_1","Rudy L'Orphelin"],["14_2","Noëlle Le Maulf"],["14_4","Sophie Börner"],["14_6","Sibylle Corblet-Aznar"],["27_1","Laetitia Sanchez"],["27_3","Christine Regentête"],["27_4","Alexis Fraisse"],["50_1","Jérôme Virlouvet"],["50_2","Sophie Nicklaus"],["50_3","Laurent Huet"],["50_4","Jean-Sébastien Hederer"],["61_1","Isabelle Robert"],["61_2","Pierre Ristic"],["61_3","Corinne Malignac"],["76_1","Véronique Bérégovoy"],["76_4","David Cormand"],["76_5","Christophe Manchon"],["76_7","Alexis Deck"],["76_8","Joséphine Landormi"],["76_9","Thierry Lecerf"],["76_10","Annette Roussel"],["21_1","Olivier Muller"],["21_2","Catherine Hervieu"],["21_3","Michel Procureur"],["21_4","Jean Baloutch"],["21_5","Carole Bernhard"],["58_1","Sylvie Dupart-Muzerelle  "],["58_2","Gilbert Champagne"],["71_1","Claire Mallard"],["71_2","Dominique Cornet"],["71_3","Pierre-Etienne Graffard"],["71_4","Marie-Claude Colin"],["71_5","François Lotteau"],["89_1","Maud Navarre"],["89_2","Guillaume Durand"],["25_3","Odile Joannès"],["25_4","Anna Maillard"],["25_5","Anthony Poulin"],["39_2","Christophe Masson"],["70_1","Corinne Guyonnet"],["70_2","Marie-Claire Thomas"],["90_2","Vincent Jeudy"],["22_1","Aurélien Danvert"],["22_2","Jocelyne Leclerc"],["22_3","Nicolas Hervé"],["22_4","Sylvie Bourbigot"],["22_5","Yves Nédélec"],["29_1","Jean-Pierre Bigorgne"],["29_2","Nathalie Chaline"],["29_3","Patrick Appéré"],["29_4","Christine Prigent"],["29_5","Rosalie Salaun"],["29_6","Nathanaël Legeard"],["29_7","Jean Cathala"],["29_8","Marie-Andrée Jérôme-Clovis"],["35_1","Didier Chapellon"],["35_2","Lucile Koch-Schlund"],["35_3","Gaëlle Rougier"],["35_4","Sarah Trichet-Allaire"],["35_5","Bernard Martin"],["35_7","Solenn Hallou (PCF)"],["35_8","Matthieu Theurier"],["56_1","Pascal Baudont"],["56_2","Didier Coupeau"],["56_3","Patrick Naizain"],["56_4","Nathalie Landriau-Berhault"],["56_5","Damien Girard"],["59_1","Anne Mikolajczak"],["59_2","Hélène Hardy"],["59_3","Franck Lesueur-Bonte"],["59_4","Stéphane Baly"],["59_5","Yannick Brohard"],["59_6","Maryse Faber-Rossi"],["59_7","Karima Chouia"],["59_8","Chritian Carlier"],["59_9","Sandrine Rousseau"],["59_10","Olivier Descamps"],["59_11","Lise Daleux"],["59_12","Elisabeth Saint-Guily"],["59_13","Virginie Henocq"],["59_14","Myriam Santhune"],["59_15","Guillaume Fache"],["59_16","Philippe Bernard"],["59_17","Lucile Wacheux"],["59_18","Thomas Fremond"],["59_19","Xavier Blottière"],["59_20","Frédéric Bigot"],["59_21","Pauline Pottier"],["62_1","Sylvie Joniaux"],["62_2","Laure Olivier"],["62_3","Jamel Oufqir"],["62_4","Martine Minne"],["62_5","Cindy Pacques"],["62_6","Charlotte Talpaert"],["62_7","Francis Gest"],["62_8","Florian Quèze"],["62_9","Marie-Andrée Queste"],["62_10","Lisette Sudic"],["62_11","Marine Tondelier"],["62_12","Daniel Ludwikowski"],["2_1","Brigitte Fournié Turquin"],["2_2","Michel Magniez"],["2_3","Christophe Parent"],["2_5","Dominique Jourdain"],["60_2","Jacqueline Fontaine"],["60_4","Martine Bernard"],["60_5","Luc Blanchard"],["60_6","Caroline Marzuchetti"],["80_4","Elodie Héren"],["18_1","Françoise Pouzet"],["18_2","Marie Thérèse Petit"],["18_3","Catherine Menguy"],["28_2","Youssef Lamrini"],["28_3","Françoise Réparat"],["28_4","Nachida Barre"],["36_1","Muriel Beffara"],["36_2","Raphaël Tillie"],["37_1","Christophe Dupin"],["37_2","Eric Beaugendre"],["37_3","Marie Agnès Peltier"],["37_4","Michel Gendron"],["37_5","Erwan Deliz"],["41_1","Nicolas Orgelet"],["41_2","Marie Robin"],["41_3","Christian Guellier"],["45_2","Jean-Philippe Grand"],["45_3","Cedric Petit"],["45_4","Massila Salemkour"],["45_5","Benoit Varin"],["4_1","Colette Charriau"],["5_2","Agnès Antoine"],["6_3","Juliette Chesnel"],["6_4","Laurent Lanquar"],["6_6","Antoine Marchese"],["6_7","Elisabeth Deborde"],["6_8","Fabien Torres"],["6_9","Didier Cherel"],["13_1","Anne-Marie Danièle"],["13_2","Christine Juste"],["13_3","Karim Mouaci"],["13_5","Daniel Vanetti"],["13_6","Hervé Menchon"],["13_7","Lydia Frentzel"],["13_8","Mathieu Saintagne"],["13_10","Rémy Carrodano"],["13_11","Dorian Hispa"],["13_12","Nathalie Sirben"],["13_13","Eveline Lelieur"],["13_15","Hélène Haensler"],["83_1","Delphine Deluca"],["83_2","Guy Rebec"],["83_3","Chantal Mouttet"],["83_4","Jean Laurent Felizia"],["83_5","Jacky Giral"],["83_7","Denise Reverdito"],["83_8","Bruno Delport"],["84_1","Jean Pierre Cerventès"],["84_2","Annie Rosenblatt"],["84_4","Serge Marolleau"],["84_5","Marie-Christine Kadler"],["44_1","Jean-Michel Mezange"],["44_2","Pascale Chiron"],["44_3","Judith Leray"],["44_4","François Nicolas"],["44_5","Franco Fedele"],["44_7","Yves Coquard"],["44_8","Fabrice Bazin"],["44_9","Corine Guignard"],["44_10","Brigitte Héridel"],["49_1","Romain Laveau"],["49_2","Romain Dolais"],["49_3","Daphné Raveneau"],["49_4","Christelle Cardet"],["49_5","Franck Loiseau"],["49_7","Hervé Dubosclard"],["53_1","Maël Rannou"],["53_2","Françoise Marchand"],["53_3","Sophie Leterrier"],["72_1","Isabelle Sévère"],["72_2","Elisabeth Sesma"],["72_3","Dominique Trichet-Allaire"],["72_4","Alexis Braud"],["72_5","Sophie Bringuy"],["85_1","Guy Batiot"],["85_3","Laurent Akriche"],["85_4","Claudine Goichon"],["85_5","Ghislaine Rautureau"],["75_1","Victoria Barigant"],["75_2","Gilles Seignan"],["75_3","Adrien Delassus"],["75_4","Hanna Clairière"],["75_5","Julien Bayou"],["75_6","Cécile Duflot"],["75_7","Corinne Faugeron"],["75_8","Emmanuelle Pierre-Marie"],["75_9","Claire Monod"],["75_10","Sybille Bernard"],["75_11","Florentin Letissier"],["75_12","France Talandier"],["75_13","Thibaut Bragé"],["75_14","Rémi Lété"],["75_15","Antoinette Guhl"],["75_16","Dan Lert"],["75_17","Douchka Markovic"],["75_18","Caroline de Haas"],["77_2","Rose De La Fuente"],["77_3","Rosa Lacerda"],["77_4","Quentin Picquenot"],["77_6","Séverine Leclercq"],["77_7","Farid Djabali"],["77_8","Sabrina Seghiri"],["77_9","Fernande Trezentos Oliveira"],["77_10","Pascal Vesvre"],["78_1","Olivier Pareja"],["78_2","Tanguy Ruellan"],["78_4","Marie-Françoise D'Arras"],["78_7","Ghislaine Senée"],["78_9","Salah Anouar"],["78_10","David Jutier"],["78_12","Patricia Charton"],["91_2","Patrick Polverelli"],["91_4","Claire Pinto"],["91_5","Didier Missenard"],["91_6","Anne-Charlotte Benichou"],["91_7","Eva Sas"],["91_10","Isabelle Catrain"],["92_1","Délia Toumi"],["92_2","Laurent Guillard"],["92_3","Joëlle Paris"],["92_4","Alexis Martin"],["92_5","Marie-Claude Fournier"],["92_6","Vincent Dubail"],["92_7","Vincent  Poizat"],["92_8","Renaud Dubois"],["92_9","Aminata Niakaté"],["92_10","Pauline Couvent"],["92_11","Carmélina De Pablo"],["92_12","Théo Garcia Badin"],["92_13","Denis Delrieu"],["93_1","Dina Deffairi-Sessac"],["93_2","Laurent Servières"],["93_3","Eric Manfredi"],["93_4","Nahiba Rezkalla"],["93_5","Fatimata Sy"],["93_6","Nadia Azoug"],["93_7","Pierre Serne"],["93_8","Aurélien Berthou"],["93_9","Dominique Busson"],["93_11","Céline Fréby"],["93_12","Ginette Contrastin"],["94_1","Catherine Monié"],["94_2","Ali Id Elouali "],["94_4","Samuel Szymanski"],["94_6","Laurence Abeille"],["94_7","Marie Leclerc-Bruant"],["94_8","Rémi Houley"],["94_10","Mehdy Belabbas"],["94_11","Marianne Jaouen"],["95_1","Bénédicte Ariès"],["95_2","Marc Denis"],["95_3","Pierrette Borgne"],["95_4","Emmanuel Rodriguez"],["95_5","Pascal Bertolini"],["95_6","François Delcombre"],["95_7","Célia Jousserand"],["95_8","Laetitia Zidée"],["95_9","Dominique Dufumier"],["95_10","Dominique Damour"],["99_1","Jocelyne Le Boulicaut"],["99_2","Sergio Coronado"],["99_3","Karine Daudicourt"],["99_4","Perrine Ledan"],["99_5","François Ralle Andréoli"],["99_6","Jean Rossiaud"],["99_7","Anna Deparnay-Grunenberg"],["99_8","Nil Delahaye"],["99_9","Yann Roustan"],["974_1","Jean-Pierre Marchau"],["974_2","Charles Moyac"],["974_4","Danon Odayen"]]

for candidat in candidats_eelv :
#	print(candidat[0]+" et "+candidat[1])
	candidats_colores_par_circo[candidat[0]]["EELV"]=[candidat[1]]

for code in codes_circos :
	if len(candidats_colores_par_circo[code]["EELV"])>1:
		candidats_colores_par_circo[code]["EELV"]=[candidats_colores_par_circo[code]["EELV"][0]]

candidats_colores_par_circo["971_3"]["PS"]=["Adrien BARON"]
candidats_colores_par_circo["985_2"]["EM"]=["Jacques HENRY"]
candidats_colores_par_circo["971_1"]["UDI"]=["Rudy FARO,Jessica COMPPER"]
candidats_colores_par_circo["971_2"]["UDI"]=["Marie-Jeanne QUINOL,Philibert CARVIGAN"]

surpop_file=open("surpopulation_2017.txt","w")

for code in codes_circos :
	for couleur in couleurs :
		if len(candidats_colores_par_circo[code][couleur])>1 :
			surpop_file.write(code+","+couleur+" :"+",".join(candidats_colores_par_circo[code][couleur])+"\n")

surpop_file.close()

desert_file=open("desert_2017.txt","w")

for code in codes_circos :
	for couleur in couleurs :
		if len(candidats_colores_par_circo[code][couleur])==0 :
			desert_file.write(code+","+couleur+"\n")

desert_file.close()

#configurations={}
#for code in codes_circos :
#	presents=[]
#	for couleur in couleurs :
#		if len(candidats_colores_par_circo[code][couleur])>0 :
#			presents.append(couleur)
#	configurations[",".join(presents)]="oui"
#
#print(configurations)

clean_headers=["circo","EM","FN","LR","LFI","PS","EELV","UDI","PCF","DLF"]
clean_csv=open("1candidat_couleur_circo_2017.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in codes_circos :
	valeurs=[code]
	for champ in clean_headers[1:]:
		if len(candidats_colores_par_circo[code][champ])==0:
			valeurs.append("")
		else:
			valeurs.append(candidats_colores_par_circo[code][champ][0])
	clean_csv.write(";".join(valeurs)+"\n")

clean_csv.close()
