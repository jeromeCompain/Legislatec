# -*- coding: utf-8 -*-

def qualification(resultats_circo):
	max_score=0
	winner=''
	for couleur in couleurs:
		if resultats_circo[couleur]["%_Voix/Exp"]>max_score:
			winner=couleur
			max_score=resultats_circo[couleur]["%_Voix/Exp"]
	if max_score>50 and resultats_circo[couleur]["%_Voix/Ins"]>=25:
		return [winner]
	else:
		qualifies=[winner]
		nd_max_score=0
		nd_winner=''
		for couleur in couleurs:
			if couleur!=winner and resultats_circo[couleur]["%_Voix/Exp"]>nd_max_score:
				nd_winner=couleur
				nd_max_score=resultats_circo[couleur]["%_Voix/Exp"]
		qualifies.append(nd_winner)
		for couleur in couleurs:
			if couleur!=winner and couleur!=nd_winner and resultats_circo[couleur]["%_Voix/Ins"]>=12.5:
				qualifies.append(couleur)
		return qualifies

def second_tour (resultats,presents):

	em2em=0
	fn2em=0
	lr2em=0
	udi2em=0
	lfi2em=0
	ps2em=0
	eelv2em=0
	dlf2em=0
	pcf2em=0

	em2fn=0
	fn2fn=0
	lr2fn=0
	udi2fn=0
	lfi2fn=0
	ps2fn=0
	eelv2fn=0
	dlf2fn=0
	pcf2fn=0

	em2lr=0
	fn2lr=0
	lr2lr=0
	udi2lr=0
	lfi2lr=0
	ps2lr=0
	eelv2lr=0
	dlf2lr=0
	pcf2lr=0

	em2udi=0
	fn2udi=0
	lr2udi=0
	udi2udi=0
	lfi2udi=0
	ps2udi=0
	eelv2udi=0
	dlf2udi=0
	pcf2udi=0

	em2lfi=0
	fn2lfi=0
	lr2lfi=0
	udi2lfi=0
	lfi2lfi=0
	ps2lfi=0
	eelv2lfi=0
	dlf2lfi=0
	pcf2lfi=0

	em2ps=0
	fn2ps=0
	lr2ps=0
	udi2ps=0
	lfi2ps=0
	ps2ps=0
	eelv2ps=0
	dlf2ps=0
	pcf2ps=0

	em2eelv=0
	fn2eelv=0
	lr2eelv=0
	udi2eelv=0
	lfi2eelv=0
	ps2eelv=0
	eelv2eelv=0
	dlf2eelv=0
	pcf2eelv=0

	em2dlf=0
	fn2dlf=0
	lr2dlf=0
	udi2dlf=0
	lfi2dlf=0
	ps2dlf=0
	eelv2dlf=0
	dlf2dlf=0
	pcf2dlf=0

	em2pcf=0
	fn2pcf=0
	lr2pcf=0
	udi2pcf=0
	lfi2pcf=0
	ps2pcf=0
	eelv2pcf=0
	dlf2pcf=0
	pcf2pcf=0
#	print(presents)
	if len(presents)==1:
		resultats={}
		for couleur in couleurs:
			if couleur in presents:
				resultats[couleur]=7
			else:
				resultats[couleur]=0
		return resultats
	else:
		if presents==["EM","LR"]:
			ps2em=0.6
			eelv2em=0.6
			lfi2em=0.05
			pcf2em=0.05
			fn2lr=0.4
			dlf2lr=0.75
			udi2em=0.15
			udi2lr=0.8
			em2em=1
			lr2lr=1
		elif presents==["EM","FN"]:
			lr2em=0.55
			udi2em=0.55
			ps2em=0.9
			eelv2em=0.9
			lfi2em=0.35
			pcf2em=0.35
			lr2fn=0.35
			udi2fn=0.35
			dlf2fn=0.4
			lfi2fn=0.05
			pcf2fn=0.05
			em2em=1
			fn2fn=1
		elif presents==["EM","LFI"]:
			ps2lfi=0.6
			eelv2lfi=0.6
			fn2lfi=0.05
			pcf2lfi=0.95
			ps2em=0.35
			eelv2em=0.35
			lr2em=0.6
			udi2em=0.6
			em2em=1
			lfi2lfi=1
		elif presents==["EM","PCF"]:
			ps2pcf=0.6
			eelv2pcf=0.6
			fn2pcf=0.05
			pcf2pcf=1
			ps2em=0.35
			eelv2em=0.35
			lr2em=0.6
			udi2em=0.6
			em2em=1
			lfi2pcf=0.95
		elif presents==["FN","LR"]:
			em2lr=0.8
			ps2lr=0.6
			eelv2lr=0.6
			dlf2lr=0.4
			lfi2lr=0.2
			pcf2lr=0.2
			dlf2fn=0.4
			lfi2fn=0.05
			pcf2fn=0.05
			udi2lr=0.9
			lr2lr=1
			fn2fn=1
		elif presents==["FN","UDI"]:
			em2udi=0.8
			ps2udi=0.6
			eelv2udi=0.6
			dlf2udi=0.4
			lfi2udi=0.2
			pcf2udi=0.2
			dlf2fn=0.4
			lfi2fn=0.05
			pcf2fn=0.05
			lr2udi=0.9
			fn2fn=1
			udi2udi=1
		elif presents==["EM","FN","LR"]:
			ps2em=0.7
			eelv2em=0.7
			lfi2em=0.05
			pcf2em=0.05
			dlf2lr=0.55
			dlf2fn=0.35
			udi2lr=0.8
			udi2em=0.15
			em2em=1
			lr2lr=1
			fn2fn=1
		elif presents==["FN","LFI"]:
			pcf2lfi=0.95
			ps2lfi=0.95
			eelv2lfi=0.95
			em2lfi=0.65
			dlf2fn=0.5
			lr2fn=0.35
			udi2fn=0.35
			lr2lfi=0.15
			udi2lfi=0.15
			fn2fn=1
			lfi2lfi=1
		elif presents==["FN","PCF"]:
			pcf2pcf=1
			ps2pcf=0.95
			eelv2pcf=0.95
			em2pcf=0.65
			dlf2fn=0.5
			lr2fn=0.35
			udi2fn=0.35
			lr2pcf=0.15
			udi2pcf=0.15
			fn2fn=1
			lfi2pcf=1
		elif presents==["FN","PS"]:
			pcf2ps=0.95
			lfi2ps=0.95
			eelv2ps=0.95
			em2ps=0.65
			dlf2fn=0.5
			lr2fn=0.35
			udi2fn=0.35
			lr2ps=0.15
			udi2ps=0.15
			fn2fn=1
			ps2ps=1
		elif presents==["EELV","FN"]:
			pcf2eelv=0.95
			lfi2eelv=0.95
			eelv2eelv=1
			em2eelv=0.65
			dlf2fn=0.5
			lr2fn=0.35
			udi2fn=0.35
			lr2eelv=0.15
			udi2eelv=0.15
			fn2fn=1
			ps2eelv=1
		elif presents==["LR","PS"]:
			eelv2ps=0.9
			lfi2ps=0.7
			pcf2ps=0.7
			em2ps=0.55
			dlf2lr=0.6
			fn2lr=0.4
			em2lr=0.35
			udi2lr=0.9
			lr2lr=1
			ps2ps=1
		elif presents==["EM","PS"]:
			eelv2ps=0.9
			lfi2ps=0.4
			pcf2ps=0.5
			em2ps=0.1
			dlf2em=0.3
			fn2em=0.3
			em2em=1
			udi2em=0.8
			lr2em=0.75
			ps2ps=1
		elif presents==["EELV","LR"]:
			ps2eelv=0.9
			lfi2eelv=0.7
			pcf2eelv=0.7
			em2eelv=0.55
			dlf2lr=0.6
			fn2lr=0.4
			em2lr=0.35
			udi2lr=0.9
			lr2lr=1
			eelv2eelv=1
		elif presents==["EELV","EM"]:
			ps2eelv=0.9
			lfi2eelv=0.7
			pcf2eelv=0.7
			em2eelv=0.55
			dlf2em=0.4
			fn2em=0.3
			em2em=1
			udi2em=0.9
			lr2em=0.8
			eelv2eelv=1
		elif presents==["EELV","LFI"]:
			ps2eelv=0.5
			pcf2eelv=0.2
			em2eelv=0.7
			fn2lfi=0.1
			udi2eelv=0.1
			lfi2lfi=1
			pcf2lfi=0.8
			ps2lfi=0.3
			eelv2eelv=1
		elif presents==["FN","LR","PS"]:
			em2ps=0.6
			eelv2ps=0.9
			lfi2ps=0.7
			pcf2ps=0.7
			em2lr=0.35
			dlf2lr=0.45
			dlf2fn=0.35
			udi2lr=0.9
			lr2lr=1
			fn2fn=1
			ps2ps=1
		elif presents==["EM","FN","LFI"]:
			ps2lfi=0.5
			eelv2lfi=0.5
			ps2em=0.4
			eelv2em=0.4
			lr2em=0.5
			udi2em=0.5
			lr2fn=0.35
			udi2fn=0.35
			dlf2fn=0.4
			pcf2lfi=0.9
			em2em=1
			fn2fn=1
			lfi2lfi=1
		elif presents==["LFI","LR","PS"]:
			pcf2lfi=0.7
			em2ps=0.5
			pcf2ps=0.2
			fn2lr=0.35
			dlf2lr=0.75
			em2lr=0.4
			eelv2lfi=0.3
			eelv2ps=0.6
			lr2lr=1
			lfi2lfi=1
			ps2ps=1
		elif presents==["EM","LFI","LR"]:
			pcf2lfi=0.9
			ps2lfi=0.5
			eelv2lfi=0.5
			ps2em=0.4
			eelv2em=0.4
			fn2lr=0.4
			dlf2lr=0.75
			em2em=1
			lr2lr=1
			lfi2lfi=1
		elif presents==["LFI","PS"]:
			fn2lfi=0.05
			em2ps=0.5
			lfi2lfi=1
			ps2ps=1
		elif presents==["LFI","LR"]:
			ps2lfi=0.8
			eelv2lfi=0.8
			fn2lfi=0.05
			em2lfi=0.25
			em2lr=0.5
			fn2lr=0.35
			dlf2lr=0.5
			udi2lr=0.9
			lr2lr=1
			lfi2lfi=1
		elif presents==["LFI","UDI"]:
			ps2lfi=0.8
			eelv2lfi=0.8
			fn2lfi=0.05
			em2lfi=0.25
			em2udi=0.5
			fn2udi=0.35
			dlf2udi=0.5
			lr2udi=0.9
			lfi2lfi=1
			udi2udi=1
		elif presents==["LR","UDI"]:
			em2udi=0.5
			em2lr=0.2
			dlf2lr=0.4
			fn2lr=0.35
			lr2lr=1
			udi2udi=1
		elif presents==["PS","UDI"]:
			eelv2ps=0.9
			lfi2ps=0.7
			pcf2ps=0.7
			em2ps=0.4
			dlf2udi=0.2
			em2udi=0.4
			lr2udi=0.9
			udi2udi=1
			ps2ps=1

		else:
			print(presents)
			return {"LFI":0,"PCF":0,"EELV":0,"PS":0,"EM":0,"UDI":0,"LR":0,"DLF":999999999,"FN":0}

		
		res_LFI=int(round(lfi2lfi*resultats["LFI"]["voix"]+pcf2lfi*resultats["PCF"]["voix"]+eelv2lfi*resultats["EELV"]["voix"]+ps2lfi*resultats["PS"]["voix"]+em2lfi*resultats["EM"]["voix"]+udi2lfi*resultats["UDI"]["voix"]+lr2lfi*resultats["LR"]["voix"]+dlf2lfi*resultats["DLF"]["voix"]+fn2lfi*resultats["FN"]["voix"]))
		res_PCF=int(round(lfi2pcf*resultats["LFI"]["voix"]+pcf2pcf*resultats["PCF"]["voix"]+eelv2pcf*resultats["EELV"]["voix"]+ps2pcf*resultats["PS"]["voix"]+em2pcf*resultats["EM"]["voix"]+udi2pcf*resultats["UDI"]["voix"]+lr2pcf*resultats["LR"]["voix"]+dlf2pcf*resultats["DLF"]["voix"]+fn2pcf*resultats["FN"]["voix"]))
		res_EELV=int(round(lfi2eelv*resultats["LFI"]["voix"]+pcf2eelv*resultats["PCF"]["voix"]+eelv2eelv*resultats["EELV"]["voix"]+ps2eelv*resultats["PS"]["voix"]+em2eelv*resultats["EM"]["voix"]+udi2eelv*resultats["UDI"]["voix"]+lr2eelv*resultats["LR"]["voix"]+dlf2eelv*resultats["DLF"]["voix"]+fn2eelv*resultats["FN"]["voix"]))
		res_PS=int(round(lfi2ps*resultats["LFI"]["voix"]+pcf2ps*resultats["PCF"]["voix"]+eelv2ps*resultats["EELV"]["voix"]+ps2ps*resultats["PS"]["voix"]+em2ps*resultats["EM"]["voix"]+udi2ps*resultats["UDI"]["voix"]+lr2ps*resultats["LR"]["voix"]+dlf2ps*resultats["DLF"]["voix"]+fn2ps*resultats["FN"]["voix"]))
		res_EM=int(round(lfi2em*resultats["LFI"]["voix"]+pcf2em*resultats["PCF"]["voix"]+eelv2em*resultats["EELV"]["voix"]+ps2em*resultats["PS"]["voix"]+em2em*resultats["EM"]["voix"]+udi2em*resultats["UDI"]["voix"]+lr2em*resultats["LR"]["voix"]+dlf2em*resultats["DLF"]["voix"]+fn2em*resultats["FN"]["voix"]))
		res_UDI=int(round(lfi2udi*resultats["LFI"]["voix"]+pcf2udi*resultats["PCF"]["voix"]+eelv2udi*resultats["EELV"]["voix"]+ps2udi*resultats["PS"]["voix"]+em2udi*resultats["EM"]["voix"]+udi2udi*resultats["UDI"]["voix"]+lr2udi*resultats["LR"]["voix"]+dlf2udi*resultats["DLF"]["voix"]+fn2udi*resultats["FN"]["voix"]))
		res_LR=int(round(lfi2lr*resultats["LFI"]["voix"]+pcf2lr*resultats["PCF"]["voix"]+eelv2lr*resultats["EELV"]["voix"]+ps2lr*resultats["PS"]["voix"]+em2lr*resultats["EM"]["voix"]+udi2lr*resultats["UDI"]["voix"]+lr2lr*resultats["LR"]["voix"]+dlf2lr*resultats["DLF"]["voix"]+fn2lr*resultats["FN"]["voix"]))
		res_DLF=int(round(lfi2dlf*resultats["LFI"]["voix"]+pcf2dlf*resultats["PCF"]["voix"]+eelv2dlf*resultats["EELV"]["voix"]+ps2dlf*resultats["PS"]["voix"]+em2dlf*resultats["EM"]["voix"]+udi2dlf*resultats["UDI"]["voix"]+lr2dlf*resultats["LR"]["voix"]+dlf2dlf*resultats["DLF"]["voix"]+fn2dlf*resultats["FN"]["voix"]))
		res_FN=int(round(lfi2fn*resultats["LFI"]["voix"]+pcf2fn*resultats["PCF"]["voix"]+eelv2fn*resultats["EELV"]["voix"]+ps2fn*resultats["PS"]["voix"]+em2fn*resultats["EM"]["voix"]+udi2fn*resultats["UDI"]["voix"]+lr2fn*resultats["LR"]["voix"]+dlf2fn*resultats["DLF"]["voix"]+fn2fn*resultats["FN"]["voix"]))

		resultats={"LFI":res_LFI,"PCF":res_PCF,"EELV":res_EELV,"PS":res_PS,"EM":res_EM,"UDI":res_UDI,"LR":res_LR,"DLF":res_DLF,"FN":res_FN}

		return resultats





codes_circos=["1_1","1_2","1_3","1_4","1_5","2_1","2_2","2_3","2_4","2_5","3_1","3_2","3_3","4_1","4_2","5_1","5_2","6_1","6_2","6_3","6_4","6_5","6_6","6_7","6_8","6_9","7_1","7_2","7_3","8_1","8_2","8_3","9_1","9_2","10_1","10_2","10_3","11_1","11_2","11_3","12_1","12_2","12_3","13_1","13_2","13_3","13_4","13_5","13_6","13_7","13_8","13_9","13_10","13_11","13_12","13_13","13_14","13_15","13_16","14_1","14_2","14_3","14_4","14_5","14_6","15_1","15_2","16_1","16_2","16_3","17_1","17_2","17_3","17_4","17_5","18_1","18_2","18_3","19_1","19_2","2A_1","2A_2","2B_1","2B_2","21_1","21_2","21_3","21_4","21_5","22_1","22_2","22_3","22_4","22_5","23_1","24_1","24_2","24_3","24_4","25_1","25_2","25_3","25_4","25_5","26_1","26_2","26_3","26_4","27_1","27_2","27_3","27_4","27_5","28_1","28_2","28_3","28_4","29_1","29_2","29_3","29_4","29_5","29_6","29_7","29_8","30_1","30_2","30_3","30_4","30_5","30_6","31_1","31_2","31_3","31_4","31_5","31_6","31_7","31_8","31_9","31_10","32_1","32_2","33_1","33_2","33_3","33_4","33_5","33_6","33_7","33_8","33_9","33_10","33_11","33_12","34_1","34_2","34_3","34_4","34_5","34_6","34_7","34_8","34_9","35_1","35_2","35_3","35_4","35_5","35_6","35_7","35_8","36_1","36_2","37_1","37_2","37_3","37_4","37_5","38_1","38_2","38_3","38_4","38_5","38_6","38_7","38_8","38_9","38_10","39_1","39_2","39_3","40_1","40_2","40_3","41_1","41_2","41_3","42_1","42_2","42_3","42_4","42_5","42_6","43_1","43_2","44_1","44_2","44_3","44_4","44_5","44_6","44_7","44_8","44_9","44_10","45_1","45_2","45_3","45_4","45_5","45_6","46_1","46_2","47_1","47_2","47_3","48_1","49_1","49_2","49_3","49_4","49_5","49_6","49_7","50_1","50_2","50_3","50_4","51_1","51_2","51_3","51_4","51_5","52_1","52_2","53_1","53_2","53_3","54_1","54_2","54_3","54_4","54_5","54_6","55_1","55_2","56_1","56_2","56_3","56_4","56_5","56_6","57_1","57_2","57_3","57_4","57_5","57_6","57_7","57_8","57_9","58_1","58_2","59_1","59_2","59_3","59_4","59_5","59_6","59_7","59_8","59_9","59_10","59_11","59_12","59_13","59_14","59_15","59_16","59_17","59_18","59_19","59_20","59_21","60_1","60_2","60_3","60_4","60_5","60_6","60_7","61_1","61_2","61_3","62_1","62_2","62_3","62_4","62_5","62_6","62_7","62_8","62_9","62_10","62_11","62_12","63_1","63_2","63_3","63_4","63_5","64_1","64_2","64_3","64_4","64_5","64_6","65_1","65_2","66_1","66_2","66_3","66_4","67_1","67_2","67_3","67_4","67_5","67_6","67_7","67_8","67_9","68_1","68_2","68_3","68_4","68_5","68_6","69_1","69_2","69_3","69_4","69_5","69_6","69_7","69_8","69_9","69_10","69_11","69_12","69_13","69_14","70_1","70_2","71_1","71_2","71_3","71_4","71_5","72_1","72_2","72_3","72_4","72_5","73_1","73_2","73_3","73_4","74_1","74_2","74_3","74_4","74_5","74_6","75_1","75_2","75_3","75_4","75_5","75_6","75_7","75_8","75_9","75_10","75_11","75_12","75_13","75_14","75_15","75_16","75_17","75_18","76_1","76_2","76_3","76_4","76_5","76_6","76_7","76_8","76_9","76_10","77_1","77_2","77_3","77_4","77_5","77_6","77_7","77_8","77_9","77_10","77_11","78_1","78_2","78_3","78_4","78_5","78_6","78_7","78_8","78_9","78_10","78_11","78_12","79_1","79_2","79_3","80_1","80_2","80_3","80_4","80_5","81_1","81_2","81_3","82_1","82_2","83_1","83_2","83_3","83_4","83_5","83_6","83_7","83_8","84_1","84_2","84_3","84_4","84_5","85_1","85_2","85_3","85_4","85_5","86_1","86_2","86_3","86_4","87_1","87_2","87_3","88_1","88_2","88_3","88_4","89_1","89_2","89_3","90_1","90_2","91_1","91_2","91_3","91_4","91_5","91_6","91_7","91_8","91_9","91_10","92_1","92_2","92_3","92_4","92_5","92_6","92_7","92_8","92_9","92_10","92_11","92_12","92_13","93_1","93_2","93_3","93_4","93_5","93_6","93_7","93_8","93_9","93_10","93_11","93_12","94_1","94_2","94_3","94_4","94_5","94_6","94_7","94_8","94_9","94_10","94_11","95_1","95_2","95_3","95_4","95_5","95_6","95_7","95_8","95_9","95_10","971_1","971_2","971_3","971_4","972_1","972_2","972_3","972_4","973_1","973_2","974_1","974_2","974_3","974_4","974_5","974_6","974_7","985_1","985_2","988_1","988_2","987_1","987_2","987_3","975_1","986_1","979_1","99_1","99_2","99_3","99_4","99_5","99_6","99_7","99_8","99_9","99_10","99_11"]
couleurs=["LFI","PCF","EELV","PS","EM","UDI","LR","DLF","FN"]
inscrits={"1_1":82652,"1_2":93332,"1_3":75427,"1_4":89262,"1_5":75213,"2_1":72292,"2_2":73948,"2_3":68126,"2_4":79155,"2_5":82231,"3_1":89715,"3_2":84644,"3_3":79149,"4_1":61220,"4_2":65358,"5_1":57744,"5_2":52163,"6_1":80459,"6_2":85688,"6_3":89098,"6_4":85748,"6_5":87923,"6_6":78084,"6_7":92847,"6_8":82014,"6_9":79900,"7_1":77905,"7_2":93041,"7_3":78312,"8_1":73335,"8_2":63879,"8_3":57165,"9_1":56738,"9_2":60671,"10_1":64362,"10_2":73837,"10_3":65648,"11_1":95107,"11_2":88881,"11_3":88707,"12_1":76555,"12_2":69922,"12_3":71799,"13_1":78383,"13_2":78743,"13_3":73470,"13_4":59654,"13_5":69043,"13_6":75634,"13_7":65369,"13_8":99985,"13_9":96939,"13_10":106026,"13_11":90215,"13_12":92147,"13_13":93715,"13_14":97727,"13_15":104767,"13_16":90577,"14_1":70096,"14_2":67569,"14_3":78941,"14_4":101077,"14_5":89928,"14_6":93542,"15_1":63016,"15_2":54409,"16_1":84955,"16_2":84019,"16_3":90980,"17_1":103263,"17_2":104381,"17_3":82245,"17_4":89933,"17_5":111547,"18_1":72589,"18_2":70174,"18_3":86220,"19_1":92693,"19_2":92584,"2A_1":50859,"2A_2":57922,"2B_1":58797,"2B_2":66078,"21_1":68424,"21_2":68731,"21_3":70372,"21_4":68751,"21_5":84380,"22_1":89797,"22_2":96816,"22_3":86758,"22_4":78646,"22_5":103941,"23_1":93113,"24_1":76207,"24_2":82465,"24_3":67497,"24_4":87851,"25_1":75233,"25_2":78335,"25_3":65897,"25_4":66908,"25_5":82028,"26_1":75247,"26_2":93273,"26_3":106778,"26_4":94191,"27_1":86358,"27_2":78432,"27_3":84440,"27_4":89885,"27_5":88418,"28_1":89168,"28_2":74281,"28_3":70797,"28_4":67220,"29_1":88759,"29_2":78509,"29_3":89479,"29_4":82219,"29_5":94400,"29_6":89304,"29_7":80529,"29_8":87372,"30_1":86922,"30_2":89059,"30_3":93671,"30_4":91115,"30_5":95968,"30_6":81204,"31_1":83659,"31_2":101370,"31_3":79396,"31_4":71190,"31_5":98451,"31_6":111612,"31_7":99799,"31_8":85552,"31_9":80368,"31_10":95256,"32_1":73499,"32_2":71460,"33_1":95058,"33_2":65979,"33_3":81017,"33_4":93636,"33_5":110593,"33_6":103656,"33_7":77005,"33_8":109207,"33_9":93615,"33_10":80812,"33_11":92975,"33_12":83429,"34_1":84607,"34_2":60414,"34_3":85110,"34_4":111980,"34_5":94276,"34_6":91224,"34_7":102086,"34_8":88586,"34_9":82111,"35_1":89581,"35_2":92235,"35_3":86076,"35_4":90205,"35_5":103147,"35_6":86855,"35_7":98661,"35_8":83382,"36_1":80311,"36_2":90098,"37_1":68655,"37_2":88635,"37_3":97490,"37_4":90174,"37_5":83917,"38_1":83049,"38_2":77363,"38_3":59637,"38_4":89807,"38_5":102333,"38_6":83217,"38_7":91433,"38_8":78602,"38_9":97285,"38_10":93640,"39_1":65565,"39_2":55264,"39_3":69503,"40_1":101405,"40_2":112245,"40_3":96547,"41_1":82778,"41_2":80317,"41_3":82226,"42_1":65602,"42_2":53156,"42_3":82438,"42_4":100995,"42_5":101076,"42_6":107542,"43_1":97723,"43_2":79435,"44_1":74879,"44_2":85800,"44_3":92183,"44_4":88921,"44_5":116188,"44_6":109489,"44_7":108216,"44_8":85491,"44_9":117855,"44_10":114516,"45_1":75641,"45_2":85239,"45_3":70843,"45_4":74602,"45_5":74498,"45_6":71784,"46_1":70850,"46_2":65472,"47_1":88218,"47_2":77018,"47_3":75695,"48_1":59508,"49_1":83953,"49_2":90343,"49_3":70395,"49_4":74248,"49_5":77305,"49_6":95358,"49_7":77823,"50_1":87002,"50_2":95573,"50_3":107881,"50_4":88648,"51_1":72050,"51_2":73074,"51_3":80714,"51_4":78833,"51_5":77025,"52_1":72475,"52_2":61673,"53_1":72670,"53_2":77756,"53_3":71899,"54_1":79265,"54_2":68590,"54_3":82832,"54_4":98018,"54_5":78690,"54_6":87696,"55_1":77360,"55_2":60269,"56_1":105402,"56_2":104343,"56_3":90733,"56_4":105130,"56_5":80730,"56_6":90674,"57_1":91406,"57_2":76507,"57_3":75312,"57_4":81516,"57_5":74010,"57_6":70169,"57_7":90402,"57_8":92473,"57_9":99476,"58_1":76928,"58_2":82497,"59_1":61682,"59_2":86550,"59_3":94050,"59_4":99215,"59_5":99888,"59_6":89060,"59_7":72350,"59_8":67704,"59_9":91893,"59_10":81911,"59_11":92042,"59_12":93593,"59_13":89193,"59_14":98767,"59_15":95832,"59_16":82976,"59_17":73591,"59_18":91651,"59_19":79065,"59_20":81085,"59_21":82570,"60_1":83057,"60_2":88723,"60_3":73830,"60_4":92482,"60_5":72727,"60_6":75206,"60_7":76060,"61_1":69542,"61_2":67550,"61_3":71642,"62_1":104255,"62_2":85270,"62_3":85594,"62_4":88511,"62_5":89795,"62_6":91172,"62_7":93184,"62_8":92986,"62_9":79203,"62_10":90289,"62_11":94861,"62_12":95248,"63_1":83422,"63_2":87847,"63_3":89014,"63_4":98579,"63_5":102077,"64_1":68721,"64_2":80056,"64_3":82776,"64_4":80215,"64_5":90986,"64_6":99624,"65_1":88376,"65_2":89314,"66_1":70971,"66_2":96684,"66_3":83066,"66_4":97193,"67_1":60939,"67_2":69497,"67_3":68848,"67_4":94497,"67_5":104112,"67_6":96017,"67_7":85409,"67_8":94578,"67_9":92642,"68_1":76090,"68_2":92204,"68_3":85592,"68_4":102537,"68_5":77394,"68_6":92373,"69_1":69433,"69_2":74964,"69_3":72007,"69_4":80092,"69_5":88108,"69_6":82377,"69_7":67959,"69_8":102508,"69_9":91672,"69_10":95232,"69_11":92433,"69_12":79772,"69_13":84726,"69_14":74321,"70_1":88490,"70_2":90724,"71_1":72884,"71_2":78438,"71_3":82777,"71_4":82320,"71_5":89999,"72_1":71726,"72_2":81903,"72_3":85273,"72_4":79619,"72_5":86919,"73_1":86996,"73_2":75951,"73_3":72640,"73_4":74650,"74_1":100828,"74_2":95025,"74_3":82253,"74_4":86717,"74_5":96156,"74_6":79054,"75_1":80756,"75_2":71736,"75_3":68669,"75_4":69718,"75_5":75853,"75_6":76611,"75_7":76041,"75_8":82156,"75_9":68343,"75_10":67293,"75_11":70966,"75_12":73940,"75_13":75350,"75_14":72316,"75_15":76216,"75_16":70283,"75_17":58153,"75_18":67237,"76_1":65496,"76_2":94778,"76_3":69575,"76_4":88340,"76_5":96251,"76_6":109605,"76_7":87582,"76_8":67636,"76_9":93651,"76_10":108744,"77_1":70891,"77_2":79697,"77_3":75449,"77_4":87907,"77_5":84928,"77_6":78045,"77_7":85317,"77_8":89117,"77_9":85704,"77_10":79711,"77_11":64792,"78_1":83366,"78_2":85323,"78_3":83492,"78_4":78395,"78_5":73673,"78_6":75762,"78_7":80529,"78_8":73760,"78_9":90878,"78_10":88776,"78_11":68238,"78_12":68956,"79_1":90245,"79_2":97393,"79_3":84747,"80_1":84262,"80_2":75497,"80_3":83829,"80_4":83987,"80_5":81439,"81_1":83800,"81_2":106028,"81_3":101366,"82_1":89963,"82_2":93378,"83_1":74822,"83_2":90494,"83_3":100795,"83_4":106247,"83_5":96198,"83_6":118396,"83_7":103518,"83_8":104307,"84_1":72960,"84_2":83274,"84_3":75536,"84_4":88713,"84_5":81840,"85_1":109546,"85_2":103483,"85_3":122127,"85_4":97831,"85_5":81455,"86_1":79610,"86_2":77533,"86_3":74137,"86_4":75734,"87_1":85076,"87_2":97847,"87_3":83399,"88_1":77066,"88_2":73276,"88_3":65636,"88_4":66634,"89_1":76975,"89_2":75754,"89_3":89189,"90_1":47813,"90_2":47477,"91_1":71168,"91_2":90695,"91_3":95774,"91_4":96472,"91_5":68257,"91_6":81929,"91_7":74142,"91_8":76390,"91_9":79226,"91_10":61174,"92_1":62383,"92_2":67876,"92_3":81028,"92_4":76065,"92_5":70269,"92_6":74221,"92_7":86563,"92_8":68737,"92_9":68013,"92_10":80592,"92_11":69206,"92_12":92760,"92_13":89017,"93_1":61738,"93_2":54054,"93_3":72227,"93_4":60819,"93_5":63728,"93_6":52564,"93_7":75987,"93_8":60044,"93_9":70118,"93_10":68564,"93_11":62536,"93_12":64515,"94_1":84583,"94_2":63262,"94_3":72042,"94_4":72443,"94_5":89365,"94_6":81214,"94_7":65531,"94_8":76702,"94_9":53598,"94_10":64408,"94_11":62392,"95_1":81533,"95_2":76435,"95_3":91564,"95_4":76024,"95_5":68513,"95_6":76338,"95_7":69534,"95_8":54205,"95_9":69895,"95_10":66456,"971_1":76361,"971_2":86914,"971_3":83768,"971_4":69302,"972_1":79411,"972_2":81795,"972_3":65881,"972_4":83725,"973_1":53535,"973_2":39400,"974_1":80368,"974_2":92748,"974_3":92629,"974_4":104763,"974_5":83034,"974_6":75685,"974_7":110254,"985_1":37794,"985_2":45253,"988_1":84944,"988_2":104539,"987_1":72516,"987_2":66640,"987_3":64784,"975_1":4966,"986_1":8464,"979_1":25385,"99_1":199931,"99_2":74767,"99_3":120576,"99_4":123130,"99_5":91263,"99_6":127368,"99_7":105776,"99_8":121400,"99_9":107607,"99_10":99748,"99_11":92547}

candidats_colores_par_circo={}
for code in codes_circos :
	candidats_colores_par_circo[code]={}

raw_file=open("1candidat_couleur_circo_2017.csv","r")
raw_lines=raw_file.read().splitlines()
headers=raw_lines[0].split(";")
raw_lines=raw_lines[1:]

for line in raw_lines :
	champs=line.split(";")
	for i in range(1,len(headers)):
		candidats_colores_par_circo[champs[0]][headers[i]]=champs[i]

raw_file.close()

file_t1_modele2=open("modele2_t1_2017.csv","r")
raw_lines=file_t1_modele2.read().splitlines()
headers=raw_lines[0].replace(' ','_').split(";")
raw_lines=raw_lines[1:]
#print(raw_lines[0])

reel_t1={}
pred_t1={}
for circo in codes_circos:
	pred_t1[circo]={"Inscrits":inscrits[circo]}
	reel_t1[circo]={"Inscrits":inscrits[circo]}
	for couleur in couleurs:
		pred_t1[circo][couleur]={"voix":0,"nom":""}
		reel_t1[circo][couleur]={"voix":0,"nom":""}

for line in raw_lines :
	champs=line.split(";")
#	print(champs)
	circo=champs[0]+"_"+champs[1]
	pred_t1[circo][champs[3]]["voix"]=int(champs[4])
	pred_t1[circo][champs[3]]["nom"]=champs[2]
	reel_t1[circo][champs[3]]["voix"]=int(champs[5])
	reel_t1[circo][champs[3]]["nom"]=champs[2]

#print(pred_t1["75_18"]["Inscrits"])

qualifies_pred={}
qualifies_reel={}
lost_file=open("lost_in_modele2.csv","w")
lost=[]
for code in codes_circos :
#	print(code)
	exprimes_pred=0
	exprimes_reel=0
	for couleur in couleurs:
		exprimes_pred+=pred_t1[code][couleur]["voix"]
		exprimes_reel+=reel_t1[code][couleur]["voix"]
	if exprimes_pred==0:
#		print(code+", exprime pred=0")
		lost_file.write(code+"\n")
		lost.append(code)
#	if exprimes_reel==0:
#		print(code+", exprime reel=0")
	pred_t1[code]["Exprimés"]=exprimes_pred
	reel_t1[code]["Exprimés"]=exprimes_reel
	pred_t1[code]["%_Exp/Ins"]=round(100.0*pred_t1[code]["Exprimés"]/pred_t1[code]["Inscrits"],2)
	reel_t1[code]["%_Exp/Ins"]=round(100.0*reel_t1[code]["Exprimés"]/reel_t1[code]["Inscrits"],2)
	for couleur in couleurs:
		pred_t1[code][couleur]["%_Voix/Ins"]=round(100.0*pred_t1[code][couleur]["voix"]/pred_t1[code]["Inscrits"],2)
		if pred_t1[code]["Exprimés"]>0:
			pred_t1[code][couleur]["%_Voix/Exp"]=round(100.0*pred_t1[code][couleur]["voix"]/pred_t1[code]["Exprimés"],2)
		else:
			pred_t1[code][couleur]["%_Voix/Exp"]=0
		reel_t1[code][couleur]["%_Voix/Ins"]=round(100.0*reel_t1[code][couleur]["voix"]/reel_t1[code]["Inscrits"],2)
		if reel_t1[code]["Exprimés"]>0:
			reel_t1[code][couleur]["%_Voix/Exp"]=round(100.0*reel_t1[code][couleur]["voix"]/reel_t1[code]["Exprimés"],2)
		else:
			reel_t1[code][couleur]["%_Voix/Exp"]=0
	qualifies_pred[code]=qualification(pred_t1[code])
	qualifies_reel[code]=qualification(reel_t1[code])
lost_file.close()

#print(pred_t1["986_1"])

clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins"]
for couleur in couleurs:
	clean_headers.append(couleur)
	clean_headers.extend(["voix","%_Voix/Ins","%_Voix/Exp"])
clean_csv_pred=open("pred_t1_modele2_2017.csv","w")
clean_csv_reel=open("reel_t1_2017.csv","w")
clean_csv_pred.write(";".join(clean_headers)+"\n")
clean_csv_reel.write(";".join(clean_headers)+"\n")
for code in codes_circos :
#for code in ["75_18"] :
	valeurs_pred=[code,str(pred_t1[code]["Inscrits"]),str(pred_t1[code]["Exprimés"]),str(pred_t1[code]["%_Exp/Ins"])]
	valeurs_reel=[code,str(reel_t1[code]["Inscrits"]),str(reel_t1[code]["Exprimés"]),str(reel_t1[code]["%_Exp/Ins"])]
	for couleur in couleurs:
		valeurs_pred.extend([pred_t1[code][couleur]["nom"],str(pred_t1[code][couleur]["voix"]),str(pred_t1[code][couleur]["%_Voix/Ins"]),str(pred_t1[code][couleur]["%_Voix/Exp"])])
		valeurs_reel.extend([reel_t1[code][couleur]["nom"],str(reel_t1[code][couleur]["voix"]),str(reel_t1[code][couleur]["%_Voix/Ins"]),str(reel_t1[code][couleur]["%_Voix/Exp"])])
	clean_csv_pred.write(";".join(valeurs_pred)+"\n")
	clean_csv_reel.write(";".join(valeurs_reel)+"\n")

clean_csv_pred.close()
clean_csv_reel.close()

#clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins","Couleur","nom","Voix","%_Voix/Ins","%_Voix/Exp"]
#clean_csv=open("pred_t1_2017_portrait.csv","w")
#clean_csv.write(";".join(clean_headers)+"\n")
#for code in codes_circos :
#for code in ["75_18"] :
#	for couleur in couleurs:
#		valeurs=[code,str(pred_t1[code]["Inscrits"]),str(pred_t1[code]["Exprimés"]),str(pred_t1[code]["%_Exp/Ins"]),couleur,pred_t1[code][couleur]["nom"],str(pred_t1[code][couleur]["voix"]),str(pred_t1[code][couleur]["%_Voix/Ins"]),str(pred_t1[code][couleur]["%_Voix/Exp"])]
#		clean_csv.write(";".join(valeurs)+"\n")
#clean_csv.close()


qualifies_csv_pred=open("qualifies_modele2_2017.csv","w")
qualifies_csv_reel=open("qualifies_reel_2017.csv","w")
for code in codes_circos:
	qualifies_csv_pred.write(code+";"+";".join(qualifies_pred[code])+"\n")
	qualifies_csv_reel.write(code+";"+";".join(qualifies_reel[code])+"\n")

occurences_pred={}
occurences_reel={}
for code in codes_circos:
	presents_pred=qualifies_pred[code]
	presents_reel=qualifies_reel[code]
	presents_pred.sort()
	presents_reel.sort()
	clef_pred=";".join(presents_pred)
	clef_reel=";".join(presents_reel)
	if clef_pred in occurences_pred:
		occurences_pred[clef_pred]+=1
	else:
		occurences_pred[clef_pred]=1
	if clef_reel in occurences_reel:
		occurences_reel[clef_reel]+=1
	else:
		occurences_reel[clef_reel]=1
qualifies_csv_pred.write("\n\noccurences\n")
qualifies_csv_reel.write("\n\noccurences\n")
for occurence_pred in occurences_pred:
	qualifies_csv_pred.write(occurence_pred+" : "+str(occurences_pred[occurence_pred])+"\n")
for occurence_reel in occurences_reel:
	qualifies_csv_reel.write(occurence_reel+" : "+str(occurences_reel[occurence_reel])+"\n")

qualifies_csv_pred.close()
qualifies_csv_reel.close()

circos_restreintes=[x for x in codes_circos if x not in lost]
#print(circos_restreintes)

pred_t2={}
victors={}
for code in circos_restreintes :
#for code in ["75_18"] :
	victors[code]={}
	presents=qualifies_pred[code]
	presents.sort()
#	if code=="75_18":
#		print(presents)
	pred_t2[code]=second_tour(pred_t1[code],presents)
#	print(pred_t2[code])
#	print(pred_t2[code])
	pred_t2[code]["Inscrits"]=int(pred_t1[code]["Inscrits"])
	exprimes=0
	for couleur in couleurs:
		exprimes+=pred_t2[code][couleur]
	pred_t2[code]["Exprimés"]=exprimes
	pred_t2[code]["%_Exp/Ins"]=round(100.0*pred_t1[code]["Exprimés"]/pred_t2[code]["Inscrits"],2)
	max_score=0
	victor=0
	for couleur in couleurs:
		resultat=pred_t2[code][couleur]
		pred_t2[code][couleur]={}
		pred_t2[code][couleur]["nom"]=candidats_colores_par_circo[code][couleur]
		pred_t2[code][couleur]["voix"]=resultat
		pred_t2[code][couleur]["%_Voix/Ins"]=round(100.0*pred_t2[code][couleur]["voix"]/pred_t2[code]["Inscrits"],2)
		pred_t2[code][couleur]["%_Voix/Exp"]=round(100.0*pred_t2[code][couleur]["voix"]/pred_t2[code]["Exprimés"],2)
		if pred_t2[code][couleur]["voix"]>max_score:
			max_score=pred_t2[code][couleur]["voix"]
			victor=couleur
	victors[code]["Couleur"]=victor
	victors[code]["Nom"]=pred_t2[code][victor]["nom"]
	if len(qualifies_pred[code])==1:
		victors[code]["tour"]="1er tour"
	else:
		victors[code]["tour"]="2nd tour"
	victors[code]["%_Voix/Ins_t2"]=pred_t2[code][victor]["%_Voix/Ins"]
	victors[code]["%_Voix/Ins_t1"]=pred_t1[code][victor]["%_Voix/Ins"]

clean_csv=open("pred_t2_modele2.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in circos_restreintes :
#for code in ["75_18"] :
	valeurs=[code,str(pred_t2[code]["Inscrits"]),str(pred_t2[code]["Exprimés"]),str(pred_t2[code]["%_Exp/Ins"])]
	for couleur in couleurs:
		valeurs.extend([pred_t2[code][couleur]["nom"],str(pred_t2[code][couleur]["voix"]),str(pred_t2[code][couleur]["%_Voix/Ins"]),str(pred_t2[code][couleur]["%_Voix/Exp"])])
	clean_csv.write(";".join(valeurs)+"\n")

clean_csv.close()

clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins","Couleur","nom","Voix","%_Voix/Ins","%_Voix/Exp"]
clean_csv=open("pred_t2_2017_portrait_modele2.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in circos_restreintes :
#for code in ["75_18"] :
	for couleur in couleurs:
		valeurs=[code,str(pred_t2[code]["Inscrits"]),str(pred_t2[code]["Exprimés"]),str(pred_t2[code]["%_Exp/Ins"]),couleur,pred_t2[code][couleur]["nom"],str(pred_t2[code][couleur]["voix"]),str(pred_t2[code][couleur]["%_Voix/Ins"]),str(pred_t2[code][couleur]["%_Voix/Exp"])]
		clean_csv.write(";".join(valeurs)+"\n")
clean_csv.close()


victors_csv=open("victors_2017.csv","w")
victors_csv.write("circo;Couleur;Nom;Round;%_Voix/Ins_2nd_tour;%_Voix/Ins_1er_tour\n")
for code in circos_restreintes:
	victors_csv.write(code+";"+victors[code]["Couleur"]+";"
	+victors[code]["Nom"]+";"+victors[code]["tour"]+";"+str(victors[code]["%_Voix/Ins_t2"])+";"+str(victors[code]["%_Voix/Ins_t1"])+"\n")

sieges={}
for couleur in couleurs:
	sieges[couleur]=0

for code in circos_restreintes:
	for couleur in couleurs:
		if victors[code]["Couleur"]==couleur:
			sieges[couleur]+=1

victors_csv.write("\n\nComposition Assemblée\n")
for couleur in couleurs:
	victors_csv.write(couleur+";"+str(sieges[couleur])+"\n")
total=0
for couleur in couleurs:
	total+=sieges[couleur]
victors_csv.write("total;"+str(total))
victors_csv.close()







pred_t2={}
victors={}
for code in circos_restreintes :
#for code in ["75_18"] :
	victors[code]={}
	presents=qualifies_reel[code]
	presents.sort()
#	if code=="75_18":
#		print(presents)
	pred_t2[code]=second_tour(reel_t1[code],presents)
#	print(pred_t2[code])
#	print(pred_t2[code])
	pred_t2[code]["Inscrits"]=int(reel_t1[code]["Inscrits"])
	exprimes=0
	for couleur in couleurs:
		exprimes+=pred_t2[code][couleur]
	pred_t2[code]["Exprimés"]=exprimes
	pred_t2[code]["%_Exp/Ins"]=round(100.0*reel_t1[code]["Exprimés"]/pred_t2[code]["Inscrits"],2)
	max_score=0
	victor=0
	for couleur in couleurs:
		resultat=pred_t2[code][couleur]
		pred_t2[code][couleur]={}
		pred_t2[code][couleur]["nom"]=candidats_colores_par_circo[code][couleur]
		pred_t2[code][couleur]["voix"]=resultat
		pred_t2[code][couleur]["%_Voix/Ins"]=round(100.0*pred_t2[code][couleur]["voix"]/pred_t2[code]["Inscrits"],2)
		pred_t2[code][couleur]["%_Voix/Exp"]=round(100.0*pred_t2[code][couleur]["voix"]/pred_t2[code]["Exprimés"],2)
		if pred_t2[code][couleur]["voix"]>max_score:
			max_score=pred_t2[code][couleur]["voix"]
			victor=couleur
	victors[code]["Couleur"]=victor
	victors[code]["Nom"]=pred_t2[code][victor]["nom"]
	if len(qualifies_reel[code])==1:
		victors[code]["tour"]="1er tour"
	else:
		victors[code]["tour"]="2nd tour"
	victors[code]["%_Voix/Ins_t2"]=pred_t2[code][victor]["%_Voix/Ins"]
	victors[code]["%_Voix/Ins_t1"]=reel_t1[code][victor]["%_Voix/Ins"]

clean_csv=open("pred_t2_reel.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in circos_restreintes :
#for code in ["75_18"] :
	valeurs=[code,str(pred_t2[code]["Inscrits"]),str(pred_t2[code]["Exprimés"]),str(pred_t2[code]["%_Exp/Ins"])]
	for couleur in couleurs:
		valeurs.extend([pred_t2[code][couleur]["nom"],str(pred_t2[code][couleur]["voix"]),str(pred_t2[code][couleur]["%_Voix/Ins"]),str(pred_t2[code][couleur]["%_Voix/Exp"])])
	clean_csv.write(";".join(valeurs)+"\n")

clean_csv.close()

clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins","Couleur","nom","Voix","%_Voix/Ins","%_Voix/Exp"]
clean_csv=open("pred_t2_2017_portrait_reel.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in circos_restreintes :
#for code in ["75_18"] :
	for couleur in couleurs:
		valeurs=[code,str(pred_t2[code]["Inscrits"]),str(pred_t2[code]["Exprimés"]),str(pred_t2[code]["%_Exp/Ins"]),couleur,pred_t2[code][couleur]["nom"],str(pred_t2[code][couleur]["voix"]),str(pred_t2[code][couleur]["%_Voix/Ins"]),str(pred_t2[code][couleur]["%_Voix/Exp"])]
		clean_csv.write(";".join(valeurs)+"\n")
clean_csv.close()


victors_csv=open("victors_2017_from_t1reel.csv","w")
victors_csv.write("circo;Couleur;Nom;Round;%_Voix/Ins_2nd_tour;%_Voix/Ins_1er_tour\n")
for code in circos_restreintes:
	victors_csv.write(code+";"+victors[code]["Couleur"]+";"
	+victors[code]["Nom"]+";"+victors[code]["tour"]+";"+str(victors[code]["%_Voix/Ins_t2"])+";"+str(victors[code]["%_Voix/Ins_t1"])+"\n")

sieges={}
for couleur in couleurs:
	sieges[couleur]=0

for code in circos_restreintes:
	for couleur in couleurs:
		if victors[code]["Couleur"]==couleur:
			sieges[couleur]+=1

victors_csv.write("\n\nComposition Assemblée\n")
for couleur in couleurs:
	victors_csv.write(couleur+";"+str(sieges[couleur])+"\n")
total=0
for couleur in couleurs:
	total+=sieges[couleur]
victors_csv.write("total;"+str(total))
victors_csv.close()


