# -*- coding: utf-8 -*-

raw_file=open("Leg2012_t1.csv","r")
raw_lines=raw_file.read().splitlines()
headers=raw_lines[0].split(";")
raw_lines=raw_lines[1:]

codes_circos=["1_1","1_2","1_3","1_4","1_5","2_1","2_2","2_3","2_4","2_5","3_1","3_2","3_3","4_1","4_2","5_1","5_2","6_1","6_2","6_3","6_4","6_5","6_6","6_7","6_8","6_9","7_1","7_2","7_3","8_1","8_2","8_3","9_1","9_2","10_1","10_2","10_3","11_1","11_2","11_3","12_1","12_2","12_3","13_1","13_2","13_3","13_4","13_5","13_6","13_7","13_8","13_9","13_10","13_11","13_12","13_13","13_14","13_15","13_16","14_1","14_2","14_3","14_4","14_5","14_6","15_1","15_2","16_1","16_2","16_3","17_1","17_2","17_3","17_4","17_5","18_1","18_2","18_3","19_1","19_2","2A_1","2A_2","2B_1","2B_2","21_1","21_2","21_3","21_4","21_5","22_1","22_2","22_3","22_4","22_5","23_1","24_1","24_2","24_3","24_4","25_1","25_2","25_3","25_4","25_5","26_1","26_2","26_3","26_4","27_1","27_2","27_3","27_4","27_5","28_1","28_2","28_3","28_4","29_1","29_2","29_3","29_4","29_5","29_6","29_7","29_8","30_1","30_2","30_3","30_4","30_5","30_6","31_1","31_2","31_3","31_4","31_5","31_6","31_7","31_8","31_9","31_10","32_1","32_2","33_1","33_2","33_3","33_4","33_5","33_6","33_7","33_8","33_9","33_10","33_11","33_12","34_1","34_2","34_3","34_4","34_5","34_6","34_7","34_8","34_9","35_1","35_2","35_3","35_4","35_5","35_6","35_7","35_8","36_1","36_2","37_1","37_2","37_3","37_4","37_5","38_1","38_2","38_3","38_4","38_5","38_6","38_7","38_8","38_9","38_10","39_1","39_2","39_3","40_1","40_2","40_3","41_1","41_2","41_3","42_1","42_2","42_3","42_4","42_5","42_6","43_1","43_2","44_1","44_2","44_3","44_4","44_5","44_6","44_7","44_8","44_9","44_10","45_1","45_2","45_3","45_4","45_5","45_6","46_1","46_2","47_1","47_2","47_3","48_1","49_1","49_2","49_3","49_4","49_5","49_6","49_7","50_1","50_2","50_3","50_4","51_1","51_2","51_3","51_4","51_5","52_1","52_2","53_1","53_2","53_3","54_1","54_2","54_3","54_4","54_5","54_6","55_1","55_2","56_1","56_2","56_3","56_4","56_5","56_6","57_1","57_2","57_3","57_4","57_5","57_6","57_7","57_8","57_9","58_1","58_2","59_1","59_2","59_3","59_4","59_5","59_6","59_7","59_8","59_9","59_10","59_11","59_12","59_13","59_14","59_15","59_16","59_17","59_18","59_19","59_20","59_21","60_1","60_2","60_3","60_4","60_5","60_6","60_7","61_1","61_2","61_3","62_1","62_2","62_3","62_4","62_5","62_6","62_7","62_8","62_9","62_10","62_11","62_12","63_1","63_2","63_3","63_4","63_5","64_1","64_2","64_3","64_4","64_5","64_6","65_1","65_2","66_1","66_2","66_3","66_4","67_1","67_2","67_3","67_4","67_5","67_6","67_7","67_8","67_9","68_1","68_2","68_3","68_4","68_5","68_6","69_1","69_2","69_3","69_4","69_5","69_6","69_7","69_8","69_9","69_10","69_11","69_12","69_13","69_14","70_1","70_2","71_1","71_2","71_3","71_4","71_5","72_1","72_2","72_3","72_4","72_5","73_1","73_2","73_3","73_4","74_1","74_2","74_3","74_4","74_5","74_6","75_1","75_2","75_3","75_4","75_5","75_6","75_7","75_8","75_9","75_10","75_11","75_12","75_13","75_14","75_15","75_16","75_17","75_18","76_1","76_2","76_3","76_4","76_5","76_6","76_7","76_8","76_9","76_10","77_1","77_2","77_3","77_4","77_5","77_6","77_7","77_8","77_9","77_10","77_11","78_1","78_2","78_3","78_4","78_5","78_6","78_7","78_8","78_9","78_10","78_11","78_12","79_1","79_2","79_3","80_1","80_2","80_3","80_4","80_5","81_1","81_2","81_3","82_1","82_2","83_1","83_2","83_3","83_4","83_5","83_6","83_7","83_8","84_1","84_2","84_3","84_4","84_5","85_1","85_2","85_3","85_4","85_5","86_1","86_2","86_3","86_4","87_1","87_2","87_3","88_1","88_2","88_3","88_4","89_1","89_2","89_3","90_1","90_2","91_1","91_2","91_3","91_4","91_5","91_6","91_7","91_8","91_9","91_10","92_1","92_2","92_3","92_4","92_5","92_6","92_7","92_8","92_9","92_10","92_11","92_12","92_13","93_1","93_2","93_3","93_4","93_5","93_6","93_7","93_8","93_9","93_10","93_11","93_12","94_1","94_2","94_3","94_4","94_5","94_6","94_7","94_8","94_9","94_10","94_11","95_1","95_2","95_3","95_4","95_5","95_6","95_7","95_8","95_9","95_10","971_1","971_2","971_3","971_4","972_1","972_2","972_3","972_4","973_1","973_2","974_1","974_2","974_3","974_4","974_5","974_6","974_7","985_1","985_2","988_1","988_2","987_1","987_2","987_3","975_1","986_1","979_1","99_1","99_2","99_3","99_4","99_5","99_6","99_7","99_8","99_9","99_10","99_11"]
couleurs=["EXG","FG","PS","EELV","MODEM","UMP","FN"]
candidats_colores_par_circo={}
for code in codes_circos :
	candidats_colores_par_circo[code]={}
	for couleur in couleurs :
		candidats_colores_par_circo[code][couleur]=[]

candidats={}

for line in raw_lines :
	champs=line.split(";")
	candidats[champs[2]+" "+champs[1]+"_"+champs[0]]={}
	candidats[champs[2]+" "+champs[1]+"_"+champs[0]]["Circo"]=champs[0]
	candidats[champs[2]+" "+champs[1]+"_"+champs[0]]["Nom"]=champs[2]+" "+champs[1]
	candidats[champs[2]+" "+champs[1]+"_"+champs[0]]["Couleur"]=champs[3].replace("SOC","PS").replace("FDG","FG").replace("PRG","PS").replace("ECO","EELV").replace("DVG","PS").replace("COM","PS").replace("FRN","FN").replace("NouvC","UMP").replace("PRV","UMP").replace("MODEM-","MODEM").replace("DVD","UMP")
	candidats[champs[2]+" "+champs[1]+"_"+champs[0]]["Voix"]=champs[4]
	candidats[champs[2]+" "+champs[1]+"_"+champs[0]]["%_Voix/Ins"]=champs[5]
	candidats[champs[2]+" "+champs[1]+"_"+champs[0]]["%_Voix/Exp"]=champs[6]
	if champs[7]=="N":
		candidats[champs[2]+" "+champs[1]+"_"+champs[0]]["Qualifié?"]=False
	elif champs[7]=="O":
		candidats[champs[2]+" "+champs[1]+"_"+champs[0]]["Qualifié?"]=True

for candidat in candidats:
	for couleur in couleurs:
		if candidats[candidat]["Couleur"]==couleur:
			candidats_colores_par_circo[candidats[candidat]["Circo"]][couleur].append(candidats[candidat]["Nom"])

#print(candidats_colores_par_circo["75_18"])

for code in codes_circos :
#	if len(candidats_colores_par_circo[code]["PS"])+len(candidats_colores_par_circo[code]["FG"])+len(candidats_colores_par_circo[code]["EELV"])>1 :
#		gauche=[]
#		gauche.append(candidats_colores_par_circo[code]["PS"])
#		gauche.append(candidats_colores_par_circo[code]["FG"])
#		gauche.append(candidats_colores_par_circo[code]["EELV"])
#		max_score=0
#		winner=""
#		for candidat in gauche:
#			if int(candidats[candidat]["Voix"])>max_score:
#				winner=candidat
#				max_score=candidats[candidat]["Voix"]
#		for couleur in ["PS","EELV","FG"]:
#			if candidats[winner]["Couleur"]==couleur:
#				candidats_colores_par_circo[code][couleur]=[winner]
#			else:
#				candidats_colores_par_circo[code][couleur]=[]
	for couleur in couleurs:
		if len(candidats_colores_par_circo[code][couleur])>1 :
			max_score=0
			winner=""
			for candidat in candidats_colores_par_circo[code][couleur]:
				if int(candidats[candidat+"_"+code]["Voix"])>max_score:
					winner=candidat
					max_score=candidats[candidat+"_"+code]["Voix"]
				candidats_colores_par_circo[code][couleur]=[winner]

candidats_colores_par_circo["988_2"]["PS"]=["JEAN-PIERRE DJAIWE"]


#print(candidats_colores_par_circo["75_18"])

surpop_file=open("surpopulation_2012.txt","w")

for code in codes_circos :
	for couleur in couleurs :
		if len(candidats_colores_par_circo[code][couleur])>1 :
			surpop_file.write(code+","+couleur+" :"+",".join(candidats_colores_par_circo[code][couleur])+"\n")

surpop_file.close()


desert_file=open("desert_2012.txt","w")

for code in codes_circos :
	absents=[]
	for couleur in couleurs :
		if len(candidats_colores_par_circo[code][couleur])==0 :
			absents.append(couleur)
	desert_file.write(code+" : "+",".join(absents)+"\n")

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

clean_headers=["circo","EXG","FG","PS","EELV","MODEM","UMP","FN"]
clean_csv=open("1candidat_couleur_circo_2012.csv","w")
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
