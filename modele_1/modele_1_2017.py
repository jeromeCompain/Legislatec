# -*- coding: utf-8 -*-

def premier_tour (score_macron, score_lepen, score_meluche, score_filou, score_hamon, score_nda,LFI,PCF,EELV,PS,EM,UDI,LR,DLF,FN):

#	print([LFI,PCF,EELV,PS,EM,UDI,LR,DLF,FN])

	meluche2lfi=0.57
	hamon2lfi=0.08
	lepen2lfi=0.03
	macron2lfi=0
	nda2lfi=0
	filou2lfi=0
	meluche2pcf=0.07
	hamon2pcf=0.03
	lepen2pcf=0
	macron2pcf=0
	nda2pcf=0
	filou2pcf=0
	meluche2eelv=0.02
	hamon2eelv=0.13
	lepen2eelv=0
	macron2eelv=0.03
	nda2eelv=0
	filou2eelv=0
	meluche2ps=0.08
	hamon2ps=0.4
	lepen2ps=0
	macron2ps=0.09
	nda2ps=0
	filou2ps=0
	meluche2em=0.04
	hamon2em=0.14
	lepen2em=0
	macron2em=0.66
	nda2em=0.1
	filou2em=0.12
	meluche2udi=0
	hamon2udi=0
	lepen2udi=0
	macron2udi=0.02
	nda2udi=0
	filou2udi=0.07
	meluche2lr=0
	hamon2lr=0
	lepen2lr=0.06
	macron2lr=0.03
	nda2lr=0.23
	filou2lr=0.56
	meluche2dlf=0
	hamon2dlf=0
	lepen2dlf=0.02
	macron2dlf=0
	nda2dlf=0.37
	filou2dlf=0
	meluche2fn=0
	hamon2fn=0
	lepen2fn=0.67
	macron2fn=0
	nda2fn=0.08
	filou2fn=0.03

	if not EM:
#		print("no EM")
		meluche2ps=0.106
		hamon2ps=0.491
		macron2ps=0.519
		filou2ps=0.078
		nda2ps=0.065

		lepen2udi=0.06
		macron2udi=0.129
		nda2udi=0.245
		filou2udi=0.578
		hamon2udi=0.021
		meluche2udi=0.006
		if not DLF:
#			print("no EM/DLF")
			lepen2lr=0.072
			macron2lr=0.162
			nda2lr=0.472
			filou2lr=0.584
			hamon2lr=0.028
			meluche2lr=0.008
			if not UDI:
#				print("no EM/DLF/UDI")
				lepen2lr=0.072
				macron2lr=0.281
				nda2lr=0.487
				filou2lr=0.672
				hamon2lr=0.049
				meluche2lr=0.014
		else:	
			if not UDI:
#				print("no EM/UDI")
				lepen2lr=0.06
				macron2lr=0.281
				nda2lr=0.265
				filou2lr=0.672
				hamon2lr=0.049
				meluche2lr=0.014
			else:
				if not PS:
#					print("no EM/PS")
					if not EELV:
#						print("no EM/PS/EELV")
						if not PCF:
#							print("no EM/PS/EELV/PS")
							meluche2lfi=0.766
							hamon2lfi=0.731
							lepen2lfi=0.03
							macron2lfi=0.549
							filou2lfi=0.078
							nda2lfi=0.065
				else:
					if not EELV:
#						print("no EM/EELV")
						meluche2ps=0.126
						hamon2ps=0.621
						macron2ps=0.549
						filou2ps=0.078
						nda2ps=0.065
						if not PCF:
#							print("no EM/EELV/PCF")
							meluche2ps=0.194
							hamon2ps=0.644
							macron2ps=0.516
							filou2ps=0.072
							nda2ps=0.06
	else:
		if not PS:
#			print("no PS")
			meluche2lfi=0.598
			hamon2lfi=0.22
			lepen2lfi=0.03
			macron2lfi=0.031

			meluche2pcf=0.078
			hamon2pcf=0.07
			macron2pcf=0.009

			meluche2eelv=0.036
			hamon2eelv=0.21
			macron2eelv=0.048

			meluche2em=0.068
			hamon2em=0.28
			macron2em=0.692
			filou2em=0.12
			nda2em=0.1
			if not EELV:
#				print("no PS/EELV")
				meluche2lfi=0.624
				hamon2lfi=0.371
				lepen2lfi=0.03
				macron2lfi=0.066

				meluche2pcf=0.084
				hamon2pcf=0.109
				macron2pcf=0.018
				if not PCF:
#					print("no PS/EELV/PCF")
					meluche2lfi=0.74
					hamon2lfi=0.64
					lepen2lfi=0.03
					macron2lfi=0.12
			else:
				if not PCF:
#					print("no PS/PCF")
					meluche2lfi=0.676
					hamon2lfi=0.29
					lepen2lfi=0.03
					macron2lfi=0.04

					meluche2eelv=0.11
					hamon2eelv=0.26
					macron2eelv=0.053
		else:
			if not EELV:
#				print("no EELV")
				meluche2ps=0.1
				hamon2ps=0.53
				macron2ps=0.12
				if not PCF:
#					print("no EELV/PCF")
					meluche2ps=0.17
					hamon2ps=0.56
					macron2ps=0.012

					meluche2lfi=0.66
					hamon2lfi=0.24
					lepen2lfi=0.03
					macron2lfi=0.03
			else:
				if not PCF:
#					print("no PCF")
					meluche2lfi=0.64
					hamon2lfi=0.11
					lepen2lfi=0.03

					meluche2eelv=0.09
					hamon2eelv=0.16
					macron2eelv=0.03
				else:
					if not UDI:
#						print("no UDI")
						lepen2lr=0.06
						macron2lr=0.05
						nda2lr=0.23
						filou2lr=0.63
						if not LR:
#							print("no UDI/LR")
							meluche2em=0.068
							hamon2em=0.28
							macron2em=0.724
							filou2em=0.414
							nda2em=0.192
							lepen2em=0.024

							lepen2fn=0.696
							nda2fn=0.297
							filou2fn=0.198
							macron2fn=0.009
						else:
							if not DLF:
#								print("no UDI/DLF")
								lepen2lr=0.072
								macron2lr=0.05
								nda2lr=0.452
								filou2lr=0.63
								if not FN:
#									print("no UDI/DLF/FN")
									lepen2lr=0.34
									macron2lr=0.05
									nda2lr=0.484
									filou2lr=0.642
					else:
						if not DLF:
#							print("no DLF")
							lepen2lr=0.072
							macron2lr=0.162
							nda2lr=0.472
							filou2lr=0.584
							hamon2lr=0.028
							meluche2lr=0.008

							lepen2fn=0.67
							nda2fn=0.228
							filou2fn=0.03
							if not FN:
#								print("no DLF/FN")
								lepen2lr=0.407
								macron2lr=0.03
								nda2lr=0.492
								filou2lr=0.575


	if not LFI:
		meluche2lfi=0
		hamon2lfi=0
		lepen2lfi=0
		macron2lfi=0
		nda2lfi=0
		filou2lfi=0

	if not PS:
		meluche2ps=0
		hamon2ps=0
		lepen2ps=0
		macron2ps=0
		nda2ps=0
		filou2ps=0

	if not EELV:
		meluche2eelv=0
		hamon2leelv=0
		lepen2leelv=0
		macron2eelv=0
		nda2leelv=0
		filou2leelv=0

	if not PCF:
		meluche2pcf=0
		hamon2pcf=0
		lepen2pcf=0
		macron2pcf=0
		nda2pcf=0
		filou2pcf=0

	if not EM:
		meluche2em=0
		hamon2em=0
		lepen2em=0
		macron2em=0
		nda2em=0
		filou2em=0

	if not LR:
		meluche2lr=0
		hamon2lr=0
		lepen2lr=0
		macron2lr=0
		nda2lr=0
		filou2lr=0

	if not FN:
		meluche2fn=0
		hamon2fn=0
		lepen2fn=0
		macron2fn=0
		nda2fn=0
		filou2fn=0

	if not UDI:
		meluche2udi=0
		hamon2udi=0
		lepen2udi=0
		macron2udi=0
		nda2udi=0
		filou2udi=0

	if not DLF:
		meluche2dlf=0
		hamon2dlf=0
		lepen2dlf=0
		macron2dlf=0
		nda2dlf=0
		filou2dlf=0





#	print("res_LFI=int(round("+str(meluche2lfi)+"*"+str(score_meluche)+"+"+str(hamon2lfi)+"*"+str(score_hamon)+"+"+str(lepen2lfi)+"*"+str(score_lepen)+"+"+str(macron2lfi)+"*"+str(score_macron)+"+"+str(filou2lfi)+"*"+str(score_filou)+"+"+str(nda2lfi)+"*"+str(score_nda)+")")
#	print("res_EM=int(round("+str(meluche2em)+"*"+str(score_meluche)+"+"+str(hamon2em)+"*"+str(score_hamon)+"+"+str(lepen2em)+"*"+str(score_lepen)+"+"+str(macron2em)+"*"+str(score_macron)+"+"+str(filou2em)+"*"+str(score_filou)+"+"+str(nda2em)+"*"+str(score_nda)+")")
#	print("res_FN=int(round("+str(meluche2fn)+"*"+str(score_meluche)+"+"+str(hamon2fn)+"*"+str(score_hamon)+"+"+str(lepen2fn)+"*"+str(score_lepen)+"+"+str(macron2fn)+"*"+str(score_macron)+"+"+str(filou2fn)+"*"+str(score_filou)+"+"+str(nda2fn)+"*"+str(score_nda)+")")
#	print("res_PS=int(round("+str(meluche2ps)+"*"+str(score_meluche)+"+"+str(hamon2ps)+"*"+str(score_hamon)+"+"+str(lepen2ps)+"*"+str(score_lepen)+"+"+str(macron2ps)+"*"+str(score_macron)+"+"+str(filou2ps)+"*"+str(score_filou)+"+"+str(nda2ps)+"*"+str(score_nda)+")")
#	print("res_LR=int(round("+str(meluche2lr)+"*"+str(score_meluche)+"+"+str(hamon2lr)+"*"+str(score_hamon)+"+"+str(lepen2lr)+"*"+str(score_lepen)+"+"+str(macron2lr)+"*"+str(score_macron)+"+"+str(filou2lr)+"*"+str(score_filou)+"+"+str(nda2lr)+"*"+str(score_nda)+")")
#	print("res_UDI=int(round("+str(meluche2udi)+"*"+str(score_meluche)+"+"+str(hamon2udi)+"*"+str(score_hamon)+"+"+str(lepen2udi)+"*"+str(score_lepen)+"+"+str(macron2udi)+"*"+str(score_macron)+"+"+str(filou2udi)+"*"+str(score_filou)+"+"+str(nda2udi)+"*"+str(score_nda)+")")
#	print("res_DLF=int(round("+str(meluche2dlf)+"*"+str(score_meluche)+"+"+str(hamon2dlf)+"*"+str(score_hamon)+"+"+str(lepen2dlf)+"*"+str(score_lepen)+"+"+str(macron2dlf)+"*"+str(score_macron)+"+"+str(filou2dlf)+"*"+str(score_filou)+"+"+str(nda2dlf)+"*"+str(score_nda)+")")
#	print("res_EELV=int(round("+str(meluche2eelv)+"*"+str(score_meluche)+"+"+str(hamon2eelv)+"*"+str(score_hamon)+"+"+str(lepen2eelv)+"*"+str(score_lepen)+"+"+str(macron2eelv)+"*"+str(score_macron)+"+"+str(filou2eelv)+"*"+str(score_filou)+"+"+str(nda2eelv)+"*"+str(score_nda)+")")
#	print("res_PCF=int(round("+str(meluche2pcf)+"*"+str(score_meluche)+"+"+str(hamon2pcf)+"*"+str(score_hamon)+"+"+str(lepen2pcf)+"*"+str(score_lepen)+"+"+str(macron2pcf)+"*"+str(score_macron)+"+"+str(filou2pcf)+"*"+str(score_filou)+"+"+str(nda2pcf)+"*"+str(score_nda)+")")


	res_LFI=int(round(meluche2lfi*score_meluche+hamon2lfi*score_hamon+lepen2lfi*score_lepen+macron2lfi*score_macron+filou2lfi*score_filou+nda2lfi*score_nda))
	res_EM=int(round(meluche2em*score_meluche+hamon2em*score_hamon+lepen2em*score_lepen+macron2em*score_macron+filou2em*score_filou+nda2em*score_nda))
	res_FN=int(round(meluche2fn*score_meluche+hamon2fn*score_hamon+lepen2fn*score_lepen+macron2fn*score_macron+filou2fn*score_filou+nda2fn*score_nda))
	res_PS=int(round(meluche2ps*score_meluche+hamon2ps*score_hamon+lepen2ps*score_lepen+macron2ps*score_macron+filou2ps*score_filou+nda2ps*score_nda))
	res_LR=int(round(meluche2lr*score_meluche+hamon2lr*score_hamon+lepen2lr*score_lepen+macron2lr*score_macron+filou2lr*score_filou+nda2lr*score_nda))
	res_UDI=int(round(meluche2udi*score_meluche+hamon2udi*score_hamon+lepen2udi*score_lepen+macron2udi*score_macron+filou2udi*score_filou+nda2udi*score_nda))
	res_DLF=int(round(meluche2dlf*score_meluche+hamon2dlf*score_hamon+lepen2dlf*score_lepen+macron2dlf*score_macron+filou2dlf*score_filou+nda2dlf*score_nda))
	res_EELV=int(round(meluche2eelv*score_meluche+hamon2eelv*score_hamon+lepen2eelv*score_lepen+macron2eelv*score_macron+filou2eelv*score_filou+nda2eelv*score_nda))
	res_PCF=int(round(meluche2pcf*score_meluche+hamon2pcf*score_hamon+lepen2pcf*score_lepen+macron2pcf*score_macron+filou2pcf*score_filou+nda2pcf*score_nda))

	resultats={"LFI":res_LFI,"PCF":res_PCF,"EELV":res_EELV,"PS":res_PS,"EM":res_EM,"UDI":res_UDI,"LR":res_LR,"DLF":res_DLF,"FN":res_FN}

	return resultats

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
candidats_pres=["macron","le_pen","fillon","melenchon","hamon","dupont-aignan","lassalle","poutou","asselineau","arthaud","cheminade"]
candidats_pres_top5=["macron","le_pen","fillon","melenchon","hamon"]

res_pres_t1={}
for code in codes_circos :
	res_pres_t1[code]={}

raw_file=open("res_pres2017_t1.csv","r")
raw_lines=raw_file.read().splitlines()
headers=raw_lines[0].replace(' ','_').split(";")
raw_lines=raw_lines[1:]

for line in raw_lines :
	champs=line.split(";")
	for i in range(1,len(headers)):
		res_pres_t1[champs[0]][headers[i]]=champs[i]

raw_file.close()

#print(res_pres_t1["75_18"])

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

#print(candidats_colores_par_circo["986_1"])

pred_t1={}
qualifies={}
for code in codes_circos :
#for code in ["75_18"] :

	presents={}
	for couleur in couleurs:
		if candidats_colores_par_circo[code][couleur]=="":
			presents[couleur]=False
		else:
			presents[couleur]=True
#	if code=="986_1":
#		print(presents)
	pred_t1[code]=premier_tour(int(res_pres_t1[code]["macron"]),int(res_pres_t1[code]["le_pen"]),int(res_pres_t1[code]["melenchon"]),int(res_pres_t1[code]["fillon"]),int(res_pres_t1[code]["hamon"]),int(res_pres_t1[code]["dupont-aignan"]),presents["LFI"],presents["PCF"],presents["EELV"],presents["PS"],presents["EM"],presents["UDI"],presents["LR"],presents["DLF"],presents["FN"])
#	print(pred_t1[code])
	pred_t1[code]["Inscrits"]=int(res_pres_t1[code]["Inscrits"])
	exprimes=0
	for couleur in couleurs:
		exprimes+=pred_t1[code][couleur]
	pred_t1[code]["Exprimés"]=exprimes
	pred_t1[code]["%_Exp/Ins"]=round(100.0*pred_t1[code]["Exprimés"]/pred_t1[code]["Inscrits"],2)
	for couleur in couleurs:
		resultat=pred_t1[code][couleur]
		pred_t1[code][couleur]={}
		pred_t1[code][couleur]["nom"]=candidats_colores_par_circo[code][couleur]
		pred_t1[code][couleur]["voix"]=resultat
		pred_t1[code][couleur]["%_Voix/Ins"]=round(100.0*pred_t1[code][couleur]["voix"]/pred_t1[code]["Inscrits"],2)
		pred_t1[code][couleur]["%_Voix/Exp"]=round(100.0*pred_t1[code][couleur]["voix"]/pred_t1[code]["Exprimés"],2)

	qualifies[code]=qualification(pred_t1[code])


#print(pred_t1["986_1"])

clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins"]
for couleur in couleurs:
	clean_headers.append(couleur)
	clean_headers.extend(["voix","%_Voix/Ins","%_Voix/Exp"])
clean_csv=open("pred_t1_2017.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in codes_circos :
#for code in ["75_18"] :
	valeurs=[code,str(pred_t1[code]["Inscrits"]),str(pred_t1[code]["Exprimés"]),str(pred_t1[code]["%_Exp/Ins"])]
	for couleur in couleurs:
		valeurs.extend([pred_t1[code][couleur]["nom"],str(pred_t1[code][couleur]["voix"]),str(pred_t1[code][couleur]["%_Voix/Ins"]),str(pred_t1[code][couleur]["%_Voix/Exp"])])
	clean_csv.write(";".join(valeurs)+"\n")

clean_csv.close()

clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins","Couleur","nom","Voix","%_Voix/Ins","%_Voix/Exp"]
clean_csv=open("pred_t1_2017_portrait.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in codes_circos :
#for code in ["75_18"] :
	for couleur in couleurs:
		valeurs=[code,str(pred_t1[code]["Inscrits"]),str(pred_t1[code]["Exprimés"]),str(pred_t1[code]["%_Exp/Ins"]),couleur,pred_t1[code][couleur]["nom"],str(pred_t1[code][couleur]["voix"]),str(pred_t1[code][couleur]["%_Voix/Ins"]),str(pred_t1[code][couleur]["%_Voix/Exp"])]
		clean_csv.write(";".join(valeurs)+"\n")
clean_csv.close()


qualifies_csv=open("qualifies_2017.csv","w")
for code in codes_circos:
	qualifies_csv.write(code+";"+";".join(qualifies[code])+"\n")

occurences={}
for code in codes_circos:
	presents=qualifies[code]
	presents.sort()
	clef=";".join(presents)
	if clef in occurences:
		occurences[clef]+=1
	else:
		occurences[clef]=1
qualifies_csv.write("\n\noccurences\n")
for occurence in occurences:
	qualifies_csv.write(occurence+" : "+str(occurences[occurence])+"\n")

qualifies_csv.close()


pred_t2={}
victors={}
for code in codes_circos :
#for code in ["75_18"] :
	victors[code]={}
	presents=qualifies[code]
	presents.sort()
#	if code=="75_18":
#		print(presents)
	pred_t2[code]=second_tour(pred_t1[code],presents)
#	print(pred_t2[code])
	pred_t2[code]["Inscrits"]=int(res_pres_t1[code]["Inscrits"])
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
	if len(qualifies[code])==1:
		victors[code]["tour"]="1er tour"
	else:
		victors[code]["tour"]="2nd tour"
	victors[code]["%_Voix/Ins_t2"]=pred_t2[code][victor]["%_Voix/Ins"]
	victors[code]["%_Voix/Ins_t1"]=pred_t1[code][victor]["%_Voix/Ins"]

clean_csv=open("pred_t2.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in codes_circos :
#for code in ["75_18"] :
	valeurs=[code,str(pred_t2[code]["Inscrits"]),str(pred_t2[code]["Exprimés"]),str(pred_t2[code]["%_Exp/Ins"])]
	for couleur in couleurs:
		valeurs.extend([pred_t2[code][couleur]["nom"],str(pred_t2[code][couleur]["voix"]),str(pred_t2[code][couleur]["%_Voix/Ins"]),str(pred_t2[code][couleur]["%_Voix/Exp"])])
	clean_csv.write(";".join(valeurs)+"\n")

clean_csv.close()

clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins","Couleur","nom","Voix","%_Voix/Ins","%_Voix/Exp"]
clean_csv=open("pred_t2_2017_portrait.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in codes_circos :
#for code in ["75_18"] :
	for couleur in couleurs:
		valeurs=[code,str(pred_t2[code]["Inscrits"]),str(pred_t2[code]["Exprimés"]),str(pred_t2[code]["%_Exp/Ins"]),couleur,pred_t2[code][couleur]["nom"],str(pred_t2[code][couleur]["voix"]),str(pred_t2[code][couleur]["%_Voix/Ins"]),str(pred_t2[code][couleur]["%_Voix/Exp"])]
		clean_csv.write(";".join(valeurs)+"\n")
clean_csv.close()


victors_csv=open("victors_2017.csv","w")
victors_csv.write("circo;Couleur;Nom;Round;%_Voix/Ins_2nd_tour;%_Voix/Ins_1er_tour\n")
for code in codes_circos:
	victors_csv.write(code+";"+victors[code]["Couleur"]+";"
	+victors[code]["Nom"]+";"+victors[code]["tour"]+";"+str(victors[code]["%_Voix/Ins_t2"])+";"+str(victors[code]["%_Voix/Ins_t1"])+"\n")

sieges={}
for couleur in couleurs:
	sieges[couleur]=0

for code in codes_circos:
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

