# -*- coding: utf-8 -*-

def premier_tour (score_hollande, score_lepen, score_meluche, score_sarko, score_bayrou,EXG,FG,PS,EELV,MODEM,UMP,FN):

	meluche2exg=0.0160824742
	meluche2fg=0.353814433
	meluche2ps=0.3055670103
	meluche2eelv=0.072371134
	meluche2modem=0.0080412371
	meluche2ump=0.0160824742
	meluche2fn=0.0080412371

	hollande2exg=0
	hollande2fg=0.0393939394
	hollande2ps=0.6460606061
	hollande2eelv=0.063030303
	hollande2modem=0.0078787879
	hollande2ump=0.0157575758
	hollande2fn=0.0078787879

	bayrou2exg=0.0082978723
	bayrou2fg=0.0082978723
	bayrou2ps=0.2157446809
	bayrou2eelv=0.049787234
	bayrou2modem=0.1327659574
	bayrou2ump=0.3485106383
	bayrou2fn=0.024893617

	sarko2exg=0
	sarko2fg=0
	sarko2ps=0.023877551
	sarko2eelv=0
	sarko2modem=0
	sarko2ump=0.7083673469
	sarko2fn=0.047755102

	lepen2exg=0.0082978723
	lepen2fg=0.0082978723
	lepen2ps=0.0331914894
	lepen2eelv=0.0082978723
	lepen2modem=0
	lepen2ump=0.1825531915
	lepen2fn=0.5891489362

	if not MODEM:
		meluche2exg=0.0160824742
		meluche2fg=0.353814433
		meluche2ps=0.3055670103+0.0080412371
		meluche2eelv=0.072371134
		meluche2modem=0
		meluche2ump=0.0160824742
		meluche2fn=0.0080412371

		hollande2exg=0
		hollande2fg=0.0393939394
		hollande2ps=0.6460606061+0.0078787879
		hollande2eelv=0.063030303
		hollande2modem=0
		hollande2ump=0.0157575758
		hollande2fn=0.0078787879

		bayrou2exg=0.0082978723
		bayrou2fg=0.0082978723
		bayrou2ps=0.2157446809+2*0.1327659574/3
		bayrou2eelv=0.049787234
		bayrou2modem=0
		bayrou2ump=0.3485106383+0.1327659574/3
		bayrou2fn=0.024893617

		sarko2exg=0
		sarko2fg=0
		sarko2ps=0.023877551
		sarko2eelv=0
		sarko2modem=0
		sarko2ump=0.7083673469
		sarko2fn=0.047755102

		lepen2exg=0.0082978723
		lepen2fg=0.0082978723
		lepen2ps=0.0331914894
		lepen2eelv=0.0082978723
		lepen2modem=0
		lepen2ump=0.1825531915
		lepen2fn=0.5891489362
		if not PS:
			meluche2exg=0.0160824742
			meluche2fg=0.353814433+0.3055670103+0.0080412371
			meluche2ps=0
			meluche2eelv=0.072371134
			meluche2modem=0
			meluche2ump=0.0160824742
			meluche2fn=0.0080412371

			hollande2exg=0
			hollande2fg=0.0393939394+2*0.6460606061+0.0078787879/3
			hollande2ps=0
			hollande2eelv=0.063030303+0.6460606061+0.0078787879/3
			hollande2modem=0
			hollande2ump=0.0157575758
			hollande2fn=0.0078787879

			bayrou2exg=0.0082978723
			bayrou2fg=0.0082978723+0.2157446809
			bayrou2ps=0
			bayrou2eelv=0.049787234
			bayrou2modem=0
			bayrou2ump=0.3485106383+0.1327659574
			bayrou2fn=0.024893617

			sarko2exg=0
			sarko2fg=0.023877551
			sarko2ps=0
			sarko2eelv=0
			sarko2modem=0
			sarko2ump=0.7083673469
			sarko2fn=0.047755102

			lepen2exg=0.0082978723
			lepen2fg=0.0082978723+0.0331914894
			lepen2ps=0
			lepen2eelv=0.0082978723
			lepen2modem=0
			lepen2ump=0.1825531915
			lepen2fn=0.5891489362
			if not EXG and not FG and not FN:
				meluche2exg=0
				meluche2fg=0
				meluche2ps=0
				meluche2eelv=0.072371134+0.353814433+0.3055670103+0.0080412371+0.0160824742
				meluche2modem=0
				meluche2ump=0.0160824742+0.0080412371
				meluche2fn=0

				hollande2exg=0
				hollande2fg=0
				hollande2ps=0
				hollande2eelv=0.063030303+0.6460606061+0.0078787879/3+0.0393939394+2*0.6460606061+0.0078787879/3
				hollande2modem=0
				hollande2ump=0.0157575758+0.0078787879
				hollande2fn=0

				bayrou2exg=0
				bayrou2fg=0
				bayrou2ps=0
				bayrou2eelv=0.049787234+0.0082978723+0.2157446809+0.0082978723
				bayrou2modem=0
				bayrou2ump=0.3485106383+0.1327659574+0.024893617
				bayrou2fn=0

				sarko2exg=0
				sarko2fg=0
				sarko2ps=0
				sarko2eelv=0.023877551
				sarko2modem=0
				sarko2ump=0.7083673469+0.047755102
				sarko2fn=0

				lepen2exg=0
				lepen2fg=0
				lepen2ps=0
				lepen2eelv=0.0082978723+0.0082978723+0.0331914894+0.0082978723
				lepen2modem=0
				lepen2ump=0.1825531915+0.5891489362/2
				lepen2fn=0
		else:
			if not EELV:
				meluche2exg=0.0160824742
				meluche2fg=0.353814433
				meluche2ps=0.3055670103+0.0080412371+0.072371134
				meluche2eelv=0
				meluche2modem=0
				meluche2ump=0.0160824742
				meluche2fn=0.0080412371

				hollande2exg=0
				hollande2fg=0.0393939394
				hollande2ps=0.6460606061+0.0078787879+0.063030303
				hollande2eelv=0
				hollande2modem=0
				hollande2ump=0.0157575758
				hollande2fn=0.0078787879

				bayrou2exg=0.0082978723
				bayrou2fg=0.0082978723
				bayrou2ps=0.2157446809+2*0.1327659574/3+0.049787234
				bayrou2eelv=0
				bayrou2modem=0
				bayrou2ump=0.3485106383+0.1327659574/3
				bayrou2fn=0.024893617

				sarko2exg=0
				sarko2fg=0
				sarko2ps=0.023877551
				sarko2eelv=0
				sarko2modem=0
				sarko2ump=0.7083673469
				sarko2fn=0.047755102

				lepen2exg=0.0082978723
				lepen2fg=0.0082978723
				lepen2ps=0.0331914894+0.0082978723
				lepen2eelv=0
				lepen2modem=0
				lepen2ump=0.1825531915
				lepen2fn=0.5891489362
				if not EXG:
					meluche2exg=0
					meluche2fg=0.353814433+0.0160824742
					meluche2ps=0.3055670103+0.0080412371+0.072371134
					meluche2eelv=0
					meluche2modem=0
					meluche2ump=0.0160824742
					meluche2fn=0.0080412371

					hollande2exg=0
					hollande2fg=0.0393939394
					hollande2ps=0.6460606061+0.0078787879+0.063030303
					hollande2eelv=0
					hollande2modem=0
					hollande2ump=0.0157575758
					hollande2fn=0.0078787879

					bayrou2exg=0
					bayrou2fg=0.0082978723+0.0082978723
					bayrou2ps=0.2157446809+2*0.1327659574/3+0.049787234
					bayrou2eelv=0
					bayrou2modem=0
					bayrou2ump=0.3485106383+0.1327659574/3
					bayrou2fn=0.024893617

					sarko2exg=0
					sarko2fg=0
					sarko2ps=0.023877551
					sarko2eelv=0
					sarko2modem=0
					sarko2ump=0.7083673469
					sarko2fn=0.047755102

					lepen2exg=0
					lepen2fg=0.0082978723+0.0082978723
					lepen2ps=0.0331914894+0.0082978723
					lepen2eelv=0
					lepen2modem=0
					lepen2ump=0.1825531915
					lepen2fn=0.5891489362
					if not FG:
						meluche2exg=0
						meluche2fg=0
						meluche2ps=0.3055670103+0.0080412371+0.072371134+0.353814433+0.0160824742
						meluche2eelv=0
						meluche2modem=0
						meluche2ump=0.0160824742
						meluche2fn=0.0080412371

						hollande2exg=0
						hollande2fg=0
						hollande2ps=0.6460606061+0.0078787879+0.063030303+0.0393939394
						hollande2eelv=0
						hollande2modem=0
						hollande2ump=0.0157575758
						hollande2fn=0.0078787879

						bayrou2exg=0
						bayrou2fg=0
						bayrou2ps=0.2157446809+2*0.1327659574/3+0.049787234+0.0082978723+0.0082978723
						bayrou2eelv=0
						bayrou2modem=0
						bayrou2ump=0.3485106383+0.1327659574/3
						bayrou2fn=0.024893617

						sarko2exg=0
						sarko2fg=0
						sarko2ps=0.023877551
						sarko2eelv=0
						sarko2modem=0
						sarko2ump=0.7083673469
						sarko2fn=0.047755102

						lepen2exg=0
						lepen2fg=0
						lepen2ps=0.0331914894+0.0082978723+0.0082978723+0.0082978723
						lepen2eelv=0
						lepen2modem=0
						lepen2ump=0.1825531915
						lepen2fn=0.5891489362
			else:
				if not FG:
					meluche2exg=0.0160824742
					meluche2fg=0
					meluche2ps=0.3055670103+0.0080412371+0.353814433
					meluche2eelv=0.072371134
					meluche2modem=0
					meluche2ump=0.0160824742
					meluche2fn=0.0080412371

					hollande2exg=0
					hollande2fg=0
					hollande2ps=0.6460606061+0.0078787879+0.0393939394
					hollande2eelv=0.063030303
					hollande2modem=0
					hollande2ump=0.0157575758
					hollande2fn=0.0078787879

					bayrou2exg=0.0082978723
					bayrou2fg=0
					bayrou2ps=0.2157446809+2*0.1327659574/3+0.0082978723
					bayrou2eelv=0.049787234
					bayrou2modem=0
					bayrou2ump=0.3485106383+0.1327659574/3
					bayrou2fn=0.024893617

					sarko2exg=0
					sarko2fg=0
					sarko2ps=0.023877551
					sarko2eelv=0
					sarko2modem=0
					sarko2ump=0.7083673469
					sarko2fn=0.047755102

					lepen2exg=0.0082978723
					lepen2fg=0
					lepen2ps=0.0331914894+0.0082978723
					lepen2eelv=0.0082978723
					lepen2modem=0
					lepen2ump=0.1825531915
					lepen2fn=0.5891489362
					if not EXG:
						meluche2exg=0
						meluche2fg=0
						meluche2ps=0.3055670103+0.0080412371+0.353814433+0.0160824742
						meluche2eelv=0.072371134
						meluche2modem=0
						meluche2ump=0.0160824742
						meluche2fn=0.0080412371

						hollande2exg=0
						hollande2fg=0
						hollande2ps=0.6460606061+0.0078787879+0.0393939394
						hollande2eelv=0.063030303
						hollande2modem=0
						hollande2ump=0.0157575758
						hollande2fn=0.0078787879

						bayrou2exg=0
						bayrou2fg=0
						bayrou2ps=0.2157446809+2*0.1327659574/3+0.0082978723+0.0082978723
						bayrou2eelv=0.049787234
						bayrou2modem=0
						bayrou2ump=0.3485106383+0.1327659574/3
						bayrou2fn=0.024893617

						sarko2exg=0
						sarko2fg=0
						sarko2ps=0.023877551
						sarko2eelv=0
						sarko2modem=0
						sarko2ump=0.7083673469
						sarko2fn=0.047755102

						lepen2exg=0
						lepen2fg=0
						lepen2ps=0.0331914894+0.0082978723+0.0082978723
						lepen2eelv=0.0082978723
						lepen2modem=0
						lepen2ump=0.1825531915
						lepen2fn=0.5891489362
						if not FN:
							meluche2exg=0
							meluche2fg=0
							meluche2ps=0.3055670103+0.0080412371+0.353814433+0.0160824742
							meluche2eelv=0.072371134
							meluche2modem=0
							meluche2ump=0.0160824742+0.0080412371
							meluche2fn=0

							hollande2exg=0
							hollande2fg=0
							hollande2ps=0.6460606061+0.0078787879+0.0393939394
							hollande2eelv=0.063030303
							hollande2modem=0
							hollande2ump=0.0157575758+0.0078787879
							hollande2fn=0

							bayrou2exg=0
							bayrou2fg=0
							bayrou2ps=0.2157446809+2*0.1327659574/3+0.0082978723+0.0082978723
							bayrou2eelv=0.049787234
							bayrou2modem=0
							bayrou2ump=0.3485106383+0.1327659574/3+0.024893617
							bayrou2fn=0

							sarko2exg=0
							sarko2fg=0
							sarko2ps=0.023877551
							sarko2eelv=0
							sarko2modem=0
							sarko2ump=0.7083673469+0.047755102
							sarko2fn=0

							lepen2exg=0
							lepen2fg=0
							lepen2ps=0.0331914894+0.0082978723+0.0082978723+0.5891489362/4
							lepen2eelv=0.0082978723
							lepen2modem=0
							lepen2ump=0.1825531915+0.5891489362/2
							lepen2fn=0
					
				else:
					if not EXG:
						meluche2exg=0
						meluche2fg=0.353814433+0.0160824742
						meluche2ps=0.3055670103+0.0080412371
						meluche2eelv=0.072371134
						meluche2modem=0
						meluche2ump=0.0160824742
						meluche2fn=0.0080412371

						hollande2exg=0
						hollande2fg=0.0393939394
						hollande2ps=0.6460606061+0.0078787879
						hollande2eelv=0.063030303
						hollande2modem=0
						hollande2ump=0.0157575758
						hollande2fn=0.0078787879

						bayrou2exg=0
						bayrou2fg=0.0082978723+0.0082978723
						bayrou2ps=0.2157446809+2*0.1327659574/3
						bayrou2eelv=0.049787234
						bayrou2modem=0
						bayrou2ump=0.3485106383+0.1327659574/3
						bayrou2fn=0.024893617

						sarko2exg=0
						sarko2fg=0
						sarko2ps=0.023877551
						sarko2eelv=0
						sarko2modem=0
						sarko2ump=0.7083673469
						sarko2fn=0.047755102

						lepen2exg=0
						lepen2fg=0.0082978723+0.0082978723
						lepen2ps=0.0331914894
						lepen2eelv=0.0082978723
						lepen2modem=0
						lepen2ump=0.1825531915
						lepen2fn=0.5891489362
	else:
		if not PS:
			meluche2exg=0.0160824742
			meluche2fg=0.353814433+0.3055670103
			meluche2ps=0
			meluche2eelv=0.072371134
			meluche2modem=0.0080412371
			meluche2ump=0.0160824742
			meluche2fn=0.0080412371

			hollande2exg=0
			hollande2fg=0.0393939394+0.6460606061/2
			hollande2ps=0
			hollande2eelv=0.063030303+0.6460606061/2
			hollande2modem=0.0078787879
			hollande2ump=0.0157575758
			hollande2fn=0.0078787879

			bayrou2exg=0.0082978723
			bayrou2fg=0.0082978723
			bayrou2ps=0
			bayrou2eelv=0.049787234
			bayrou2modem=0.1327659574+0.2157446809
			bayrou2ump=0.3485106383
			bayrou2fn=0.024893617

			sarko2exg=0
			sarko2fg=0
			sarko2ps=0
			sarko2eelv=0
			sarko2modem=0.023877551
			sarko2ump=0.7083673469
			sarko2fn=0.047755102

			lepen2exg=0.0082978723
			lepen2fg=0.0082978723+0.0331914894
			lepen2ps=0
			lepen2eelv=0.0082978723
			lepen2modem=0
			lepen2ump=0.1825531915
			lepen2fn=0.5891489362
		else:
			if not EELV:
				meluche2exg=0.0160824742
				meluche2fg=0.353814433
				meluche2ps=0.3055670103+0.072371134
				meluche2eelv=0
				meluche2modem=0.0080412371
				meluche2ump=0.0160824742
				meluche2fn=0.0080412371

				hollande2exg=0
				hollande2fg=0.0393939394
				hollande2ps=0.6460606061+0.063030303
				hollande2eelv=0
				hollande2modem=0.0078787879
				hollande2ump=0.0157575758
				hollande2fn=0.0078787879

				bayrou2exg=0.0082978723
				bayrou2fg=0.0082978723
				bayrou2ps=0.2157446809+0.049787234
				bayrou2eelv=0
				bayrou2modem=0.1327659574
				bayrou2ump=0.3485106383
				bayrou2fn=0.024893617

				sarko2exg=0
				sarko2fg=0
				sarko2ps=0.023877551
				sarko2eelv=0
				sarko2modem=0
				sarko2ump=0.7083673469
				sarko2fn=0.047755102

				lepen2exg=0.0082978723
				lepen2fg=0.0082978723
				lepen2ps=0.0331914894+0.0082978723
				lepen2eelv=0
				lepen2modem=0
				lepen2ump=0.1825531915
				lepen2fn=0.5891489362
				if not FG:
					meluche2exg=0.0160824742
					meluche2fg=0
					meluche2ps=0.3055670103+0.072371134+0.353814433
					meluche2eelv=0
					meluche2modem=0.0080412371
					meluche2ump=0.0160824742
					meluche2fn=0.0080412371

					hollande2exg=0
					hollande2fg=0
					hollande2ps=0.6460606061+0.063030303+0.0393939394
					hollande2eelv=0
					hollande2modem=0.0078787879
					hollande2ump=0.0157575758
					hollande2fn=0.0078787879

					bayrou2exg=0.0082978723
					bayrou2fg=0
					bayrou2ps=0.2157446809+0.049787234+0.0082978723
					bayrou2eelv=0
					bayrou2modem=0.1327659574
					bayrou2ump=0.3485106383
					bayrou2fn=0.024893617

					sarko2exg=0
					sarko2fg=0
					sarko2ps=0.023877551
					sarko2eelv=0
					sarko2modem=0
					sarko2ump=0.7083673469
					sarko2fn=0.047755102

					lepen2exg=0.0082978723
					lepen2fg=0
					lepen2ps=0.0331914894+0.0082978723+0.0082978723
					lepen2eelv=0
					lepen2modem=0
					lepen2ump=0.1825531915
					lepen2fn=0.5891489362
					if not EXG:
						meluche2exg=0
						meluche2fg=0
						meluche2ps=0.3055670103+0.072371134+0.353814433+0.0160824742
						meluche2eelv=0
						meluche2modem=0.0080412371
						meluche2ump=0.0160824742
						meluche2fn=0.0080412371

						hollande2exg=0
						hollande2fg=0
						hollande2ps=0.6460606061+0.063030303+0.0393939394
						hollande2eelv=0
						hollande2modem=0.0078787879
						hollande2ump=0.0157575758
						hollande2fn=0.0078787879

						bayrou2exg=0
						bayrou2fg=0
						bayrou2ps=0.2157446809+0.049787234+0.0082978723+0.0082978723
						bayrou2eelv=0
						bayrou2modem=0.1327659574
						bayrou2ump=0.3485106383
						bayrou2fn=0.024893617

						sarko2exg=0
						sarko2fg=0
						sarko2ps=0.023877551
						sarko2eelv=0
						sarko2modem=0
						sarko2ump=0.7083673469
						sarko2fn=0.047755102

						lepen2exg=0
						lepen2fg=0
						lepen2ps=0.0331914894+0.0082978723+0.0082978723+0.0082978723
						lepen2eelv=0
						lepen2modem=0
						lepen2ump=0.1825531915
						lepen2fn=0.5891489362
						if not FN:
							meluche2exg=0
							meluche2fg=0
							meluche2ps=0.3055670103+0.072371134+0.353814433+0.0160824742
							meluche2eelv=0
							meluche2modem=0.0080412371
							meluche2ump=0.0160824742+0.0080412371
							meluche2fn=0

							hollande2exg=0
							hollande2fg=0
							hollande2ps=0.6460606061+0.063030303+0.0393939394
							hollande2eelv=0
							hollande2modem=0.0078787879
							hollande2ump=0.0157575758+0.0078787879
							hollande2fn=0

							bayrou2exg=0
							bayrou2fg=0
							bayrou2ps=0.2157446809+0.049787234+0.0082978723+0.0082978723
							bayrou2eelv=0
							bayrou2modem=0.1327659574
							bayrou2ump=0.3485106383+0.024893617
							bayrou2fn=0

							sarko2exg=0
							sarko2fg=0
							sarko2ps=0.023877551
							sarko2eelv=0
							sarko2modem=0
							sarko2ump=0.7083673469+0.047755102
							sarko2fn=0

							lepen2exg=0
							lepen2fg=0
							lepen2ps=0.0331914894+0.0082978723+0.0082978723+0.0082978723+0.5891489362/4
							lepen2eelv=0
							lepen2modem=0
							lepen2ump=0.1825531915+0.5891489362/2
							lepen2fn=0
				else:
					if not EXG:
						meluche2exg=0
						meluche2fg=0.353814433+0.0160824742
						meluche2ps=0.3055670103+0.072371134
						meluche2eelv=0
						meluche2modem=0.0080412371
						meluche2ump=0.0160824742
						meluche2fn=0.0080412371

						hollande2exg=0
						hollande2fg=0.0393939394
						hollande2ps=0.6460606061+0.063030303
						hollande2eelv=0
						hollande2modem=0.0078787879
						hollande2ump=0.0157575758
						hollande2fn=0.0078787879

						bayrou2exg=0
						bayrou2fg=0.0082978723+0.0082978723
						bayrou2ps=0.2157446809+0.049787234
						bayrou2eelv=0
						bayrou2modem=0.1327659574
						bayrou2ump=0.3485106383
						bayrou2fn=0.024893617

						sarko2exg=0
						sarko2fg=0
						sarko2ps=0.023877551
						sarko2eelv=0
						sarko2modem=0
						sarko2ump=0.7083673469
						sarko2fn=0.047755102

						lepen2exg=0
						lepen2fg=0.0082978723+0.0082978723
						lepen2ps=0.0331914894+0.0082978723
						lepen2eelv=0
						lepen2modem=0
						lepen2ump=0.1825531915
						lepen2fn=0.5891489362
			else:
				if not EXG:
					meluche2exg=0
					meluche2fg=0.353814433+0.0160824742
					meluche2ps=0.3055670103
					meluche2eelv=0.072371134
					meluche2modem=0.0080412371
					meluche2ump=0.0160824742
					meluche2fn=0.0080412371

					hollande2exg=0
					hollande2fg=0.0393939394
					hollande2ps=0.6460606061
					hollande2eelv=0.063030303
					hollande2modem=0.0078787879
					hollande2ump=0.0157575758
					hollande2fn=0.0078787879

					bayrou2exg=0
					bayrou2fg=0.0082978723+0.0082978723
					bayrou2ps=0.2157446809
					bayrou2eelv=0.049787234
					bayrou2modem=0.1327659574
					bayrou2ump=0.3485106383
					bayrou2fn=0.024893617

					sarko2exg=0
					sarko2fg=0
					sarko2ps=0.023877551
					sarko2eelv=0
					sarko2modem=0
					sarko2ump=0.7083673469
					sarko2fn=0.047755102

					lepen2exg=0
					lepen2fg=0.0082978723+0.0082978723
					lepen2ps=0.0331914894
					lepen2eelv=0.0082978723
					lepen2modem=0
					lepen2ump=0.1825531915
					lepen2fn=0.5891489362
					if not FN:
						meluche2exg=0
						meluche2fg=0.353814433+0.0160824742
						meluche2ps=0.3055670103
						meluche2eelv=0.072371134
						meluche2modem=0.0080412371
						meluche2ump=0.0160824742+0.0080412371
						meluche2fn=0

						hollande2exg=0
						hollande2fg=0.0393939394
						hollande2ps=0.6460606061
						hollande2eelv=0.063030303
						hollande2modem=0.0078787879
						hollande2ump=0.0157575758+0.0078787879
						hollande2fn=0

						bayrou2exg=0
						bayrou2fg=0.0082978723+0.0082978723
						bayrou2ps=0.2157446809
						bayrou2eelv=0.049787234
						bayrou2modem=0.1327659574
						bayrou2ump=0.3485106383+0.024893617
						bayrou2fn=0

						sarko2exg=0
						sarko2fg=0
						sarko2ps=0.023877551
						sarko2eelv=0
						sarko2modem=0
						sarko2ump=0.7083673469+0.047755102
						sarko2fn=0

						lepen2exg=0
						lepen2fg=0.0082978723+0.0082978723
						lepen2ps=0.0331914894+0.5891489362/4
						lepen2eelv=0.0082978723
						lepen2modem=0
						lepen2ump=0.1825531915+0.5891489362/2
						lepen2fn=0
						if not UMP:
							meluche2exg=0
							meluche2fg=0.353814433+0.0160824742
							meluche2ps=0.3055670103
							meluche2eelv=0.072371134
							meluche2modem=0.0080412371+0.0160824742+0.0080412371
							meluche2ump=0
							meluche2fn=0

							hollande2exg=0
							hollande2fg=0.0393939394
							hollande2ps=0.6460606061
							hollande2eelv=0.063030303
							hollande2modem=0.0078787879+0.0157575758+0.0078787879
							hollande2ump=0
							hollande2fn=0

							bayrou2exg=0
							bayrou2fg=0.0082978723+0.0082978723
							bayrou2ps=0.2157446809
							bayrou2eelv=0.049787234
							bayrou2modem=0.1327659574+0.3485106383+0.024893617
							bayrou2fn=0

							sarko2exg=0
							sarko2fg=0
							sarko2ps=0.023877551
							sarko2eelv=0
							sarko2modem=0.7083673469+0.047755102
							sarko2ump=0
							sarko2fn=0

							lepen2exg=0
							lepen2fg=0.0082978723+0.0082978723
							lepen2ps=0.0331914894+0.5891489362/4
							lepen2eelv=0.0082978723
							lepen2modem=0.1825531915+0.5891489362/2
							lepen2ump=0
							lepen2fn=0
				else:
					if not FG:
						meluche2exg=0.0160824742+0.353814433/5
						meluche2fg=0
						meluche2ps=0.3055670103+4*0.353814433/5
						meluche2eelv=0.072371134
						meluche2modem=0.0080412371
						meluche2ump=0.0160824742
						meluche2fn=0.0080412371

						hollande2exg=0
						hollande2fg=0
						hollande2ps=0.6460606061+0.0393939394
						hollande2eelv=0.063030303
						hollande2modem=0.0078787879
						hollande2ump=0.0157575758
						hollande2fn=0.0078787879

						bayrou2exg=0.0082978723
						bayrou2fg=0
						bayrou2ps=0.2157446809+0.0082978723
						bayrou2eelv=0.049787234
						bayrou2modem=0.1327659574
						bayrou2ump=0.3485106383
						bayrou2fn=0.024893617

						sarko2exg=0
						sarko2fg=0
						sarko2ps=0.023877551
						sarko2eelv=0
						sarko2modem=0
						sarko2ump=0.7083673469
						sarko2fn=0.047755102

						lepen2exg=0.0082978723
						lepen2fg=0
						lepen2ps=0.0331914894+0.0082978723
						lepen2eelv=0.0082978723
						lepen2modem=0
						lepen2ump=0.1825531915
						lepen2fn=0.5891489362
					else:
						if not FN:
							meluche2exg=0.0160824742
							meluche2fg=0.353814433+0.0080412371
							meluche2ps=0.3055670103
							meluche2eelv=0.072371134
							meluche2modem=0.0080412371
							meluche2ump=0.0160824742
							meluche2fn=0

							hollande2exg=0
							hollande2fg=0.0393939394
							hollande2ps=0.6460606061+0.0078787879
							hollande2eelv=0.063030303
							hollande2modem=0.0078787879
							hollande2ump=0.0157575758
							hollande2fn=0

							bayrou2exg=0.0082978723
							bayrou2fg=0.0082978723
							bayrou2ps=0.2157446809
							bayrou2eelv=0.049787234
							bayrou2modem=0.1327659574+0.024893617
							bayrou2ump=0.3485106383
							bayrou2fn=0

							sarko2exg=0
							sarko2fg=0
							sarko2ps=0.023877551
							sarko2eelv=0
							sarko2modem=0
							sarko2ump=0.7083673469+0.047755102
							sarko2fn=0

							lepen2exg=0.0082978723
							lepen2fg=0.0082978723+0.5891489362/4
							lepen2ps=0.0331914894+0.5891489362/4
							lepen2eelv=0.0082978723
							lepen2modem=0
							lepen2ump=0.1825531915+0.5891489362/2
							lepen2fn=0

	res_FG=int(round(meluche2fg*score_meluche+hollande2fg*score_hollande+lepen2fg*score_lepen+bayrou2fg*score_bayrou+sarko2fg*score_sarko))
	res_EXG=int(round(meluche2exg*score_meluche+hollande2exg*score_hollande+lepen2exg*score_lepen+bayrou2exg*score_bayrou+sarko2exg*score_sarko))
	res_FN=int(round(meluche2fn*score_meluche+hollande2fn*score_hollande+lepen2fn*score_lepen+bayrou2fn*score_bayrou+sarko2fn*score_sarko))
	res_PS=int(round(meluche2ps*score_meluche+hollande2ps*score_hollande+lepen2ps*score_lepen+bayrou2ps*score_bayrou+sarko2ps*score_sarko))
	res_UMP=int(round(meluche2ump*score_meluche+hollande2ump*score_hollande+lepen2ump*score_lepen+bayrou2ump*score_bayrou+sarko2ump*score_sarko))
	res_EELV=int(round(meluche2eelv*score_meluche+hollande2eelv*score_hollande+lepen2eelv*score_lepen+bayrou2eelv*score_bayrou+sarko2eelv*score_sarko))
	res_MODEM=int(round(meluche2modem*score_meluche+hollande2modem*score_hollande+lepen2modem*score_lepen+bayrou2modem*score_bayrou+sarko2modem*score_sarko))

	resultats={"FG":res_FG,"EXG":res_EXG,"EELV":res_EELV,"PS":res_PS,"MODEM":res_MODEM,"UMP":res_UMP,"FN":res_FN}

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

	exg2exg=0
	exg2fg=0
	exg2ps=0
	exg2eelv=0
	exg2modem=0
	exg2ump=0
	exg2fn=0

	fg2exg=0
	fg2fg=0
	fg2ps=0
	fg2eelv=0
	fg2modem=0
	fg2ump=0
	fg2fn=0

	ps2exg=0
	ps2fg=0
	ps2ps=0
	ps2eelv=0
	ps2modem=0
	ps2ump=0
	ps2fn=0

	eelv2exg=0
	eelv2fg=0
	eelv2ps=0
	eelv2eelv=0
	eelv2modem=0
	eelv2ump=0
	eelv2fn=0

	modem2exg=0
	modem2fg=0
	modem2ps=0
	modem2eelv=0
	modem2modem=0
	modem2ump=0
	modem2fn=0

	ump2exg=0
	ump2fg=0
	ump2ps=0
	ump2eelv=0
	ump2modem=0
	ump2ump=0
	ump2fn=0

	fn2exg=0
	fn2fg=0
	fn2ps=0
	fn2eelv=0
	fn2modem=0
	fn2ump=0
	fn2fn=0
	if presents==["MODEM","PS"]:
		exg2ps=0.92
		fg2ps=0.92
		exg2modem=0.02
		fg2modem=0.02
		ps2ps=0.97
		ps2modem=0.01
		eelv2ps=0.98
		modem2modem=0.8
		modem2ps=0.1
		ump2ps=0.02
		ump2modem=0.9
		fn2ps=0.13
		fn2modem=0.6
	elif presents==["EELV","FG","FN","UMP"]:
		exg2fg=0.92
		fg2fg=0.92
		exg2ump=0.02
		fg2ump=0.02
		ps2fg=0.4
		ps2eelv=0.5
		eelv2eelv=0.98
		modem2eelv=0.2
		modem2fg=0.1
		modem2ump=0.6
		ump2ump=0.98
		fn2fn=0.95
	elif presents==["FG","FN","UMP"]:
		exg2fg=0.92
		fg2fg=0.92
		exg2ump=0.02
		fg2ump=0.02
		ps2fg=0.9
		eelv2fg=0.8
		modem2fg=0.1
		modem2ump=0.7
		ump2ump=0.98
		fn2fn=0.95
	elif presents==["FN","PS","UMP"]:
		exg2ps=0.92
		fg2ps=0.92
		exg2ump=0.02
		fg2ump=0.02
		ps2ps=0.95
		eelv2ps=0.95
		modem2ps=0.3
		modem2ump=0.5
		ump2ump=0.98
		fn2fn=0.95
	elif presents==["FN","UMP"]:
		exg2ump=0.5
		fg2ump=0.6
		exg2fn=0.02
		fg2fn=0.02
		ps2ump=0.7
		eelv2ump=0.8
		ump2ump=0.98
		modem2ump=0.9
		fn2fn=1
	elif presents==["FG","UMP"]:
		exg2fg=0.92
		fg2fg=0.92
		exg2ump=0.02
		fg2ump=0.02
		ps2fg=0.8
		ps2ump=0.01
		eelv2fg=0.8
		modem2ump=0.8
		modem2fg=0.1
		ump2fg=0.02
		ump2ump=0.98
		fn2fg=0.13
		fn2ump=0.6
	elif presents==["EELV","FG","UMP"]:
		exg2fg=0.92
		fg2fg=0.92
		exg2ump=0.02
		fg2ump=0.02
		ps2fg=0.5
		ps2eelv=0.4
		ps2ump=0.01
		eelv2eelv=0.8
		modem2ump=0.6
		modem2eelv=0.1
		modem2fg=0.1
		ump2fg=0.02
		ump2ump=0.98
		fn2fg=0.13
		fn2ump=0.6
	elif presents==["EELV","UMP"]:
		exg2eelv=0.92
		fg2eelv=0.92
		exg2ump=0.02
		fg2ump=0.02
		ps2eelv=0.8
		ps2ump=0.01
		eelv2eelv=0.8
		modem2ump=0.7
		modem2eelv=0.2
		ump2eelv=0.02
		ump2ump=0.98
		fn2eelv=0.13
		fn2ump=0.6
	elif presents==["PS","UMP"]:
		exg2ps=0.92
		fg2ps=0.92
		exg2ump=0.02
		fg2ump=0.02
		ps2ps=0.9
		ps2ump=0.01
		eelv2ps=0.8
		modem2ump=0.6
		modem2ps=0.3
		ump2ps=0.02
		ump2ump=0.98
		fn2ps=0.13
		fn2ump=0.6
	else:
#		print(presents)
		return {"EXG":0,"FG":0,"PS":0,"EELV":0,"MODEM":0,"UMP":0,"FN":999999999}

		
	res_EXG=int(round(exg2exg*resultats["EXG"]["voix"]+fg2exg*resultats["FG"]["voix"]+ps2exg*resultats["PS"]["voix"]+eelv2exg*resultats["EELV"]["voix"]+modem2exg*resultats["MODEM"]["voix"]+ump2exg*resultats["UMP"]["voix"]+fn2exg*resultats["FN"]["voix"]))
	res_FG=int(round(exg2fg*resultats["EXG"]["voix"]+fg2fg*resultats["FG"]["voix"]+ps2fg*resultats["PS"]["voix"]+eelv2fg*resultats["EELV"]["voix"]+modem2fg*resultats["MODEM"]["voix"]+ump2fg*resultats["UMP"]["voix"]+fn2fg*resultats["FN"]["voix"]))
	res_PS=int(round(exg2ps*resultats["EXG"]["voix"]+fg2ps*resultats["FG"]["voix"]+ps2ps*resultats["PS"]["voix"]+eelv2ps*resultats["EELV"]["voix"]+modem2ps*resultats["MODEM"]["voix"]+ump2ps*resultats["UMP"]["voix"]+fn2ps*resultats["FN"]["voix"]))
	res_EELV=int(round(exg2eelv*resultats["EXG"]["voix"]+fg2eelv*resultats["FG"]["voix"]+ps2eelv*resultats["PS"]["voix"]+eelv2eelv*resultats["EELV"]["voix"]+modem2eelv*resultats["MODEM"]["voix"]+ump2eelv*resultats["UMP"]["voix"]+fn2eelv*resultats["FN"]["voix"]))
	res_MODEM=int(round(exg2modem*resultats["EXG"]["voix"]+fg2modem*resultats["FG"]["voix"]+ps2modem*resultats["PS"]["voix"]+eelv2modem*resultats["EELV"]["voix"]+modem2modem*resultats["MODEM"]["voix"]+ump2modem*resultats["UMP"]["voix"]+fn2modem*resultats["FN"]["voix"]))
	res_UMP=int(round(exg2ump*resultats["EXG"]["voix"]+fg2ump*resultats["FG"]["voix"]+ps2ump*resultats["PS"]["voix"]+eelv2ump*resultats["EELV"]["voix"]+modem2ump*resultats["MODEM"]["voix"]+ump2ump*resultats["UMP"]["voix"]+fn2ump*resultats["FN"]["voix"]))
	res_FN=int(round(exg2fn*resultats["EXG"]["voix"]+fg2fn*resultats["FG"]["voix"]+ps2fn*resultats["PS"]["voix"]+eelv2fn*resultats["EELV"]["voix"]+modem2fn*resultats["MODEM"]["voix"]+ump2fn*resultats["UMP"]["voix"]+fn2fn*resultats["FN"]["voix"]))


	resultats={"EXG":res_EXG,"FG":res_FG,"PS":res_PS,"EELV":res_EELV,"MODEM":res_MODEM,"UMP":res_UMP,"FN":res_FN}

	return resultats





codes_circos=["1_1","1_2","1_3","1_4","1_5","2_1","2_2","2_3","2_4","2_5","3_1","3_2","3_3","4_1","4_2","5_1","5_2","6_1","6_2","6_3","6_4","6_5","6_6","6_7","6_8","6_9","7_1","7_2","7_3","8_1","8_2","8_3","9_1","9_2","10_1","10_2","10_3","11_1","11_2","11_3","12_1","12_2","12_3","13_1","13_2","13_3","13_4","13_5","13_6","13_7","13_8","13_9","13_10","13_11","13_12","13_13","13_14","13_15","13_16","14_1","14_2","14_3","14_4","14_5","14_6","15_1","15_2","16_1","16_2","16_3","17_1","17_2","17_3","17_4","17_5","18_1","18_2","18_3","19_1","19_2","2A_1","2A_2","2B_1","2B_2","21_1","21_2","21_3","21_4","21_5","22_1","22_2","22_3","22_4","22_5","23_1","24_1","24_2","24_3","24_4","25_1","25_2","25_3","25_4","25_5","26_1","26_2","26_3","26_4","27_1","27_2","27_3","27_4","27_5","28_1","28_2","28_3","28_4","29_1","29_2","29_3","29_4","29_5","29_6","29_7","29_8","30_1","30_2","30_3","30_4","30_5","30_6","31_1","31_2","31_3","31_4","31_5","31_6","31_7","31_8","31_9","31_10","32_1","32_2","33_1","33_2","33_3","33_4","33_5","33_6","33_7","33_8","33_9","33_10","33_11","33_12","34_1","34_2","34_3","34_4","34_5","34_6","34_7","34_8","34_9","35_1","35_2","35_3","35_4","35_5","35_6","35_7","35_8","36_1","36_2","37_1","37_2","37_3","37_4","37_5","38_1","38_2","38_3","38_4","38_5","38_6","38_7","38_8","38_9","38_10","39_1","39_2","39_3","40_1","40_2","40_3","41_1","41_2","41_3","42_1","42_2","42_3","42_4","42_5","42_6","43_1","43_2","44_1","44_2","44_3","44_4","44_5","44_6","44_7","44_8","44_9","44_10","45_1","45_2","45_3","45_4","45_5","45_6","46_1","46_2","47_1","47_2","47_3","48_1","49_1","49_2","49_3","49_4","49_5","49_6","49_7","50_1","50_2","50_3","50_4","51_1","51_2","51_3","51_4","51_5","52_1","52_2","53_1","53_2","53_3","54_1","54_2","54_3","54_4","54_5","54_6","55_1","55_2","56_1","56_2","56_3","56_4","56_5","56_6","57_1","57_2","57_3","57_4","57_5","57_6","57_7","57_8","57_9","58_1","58_2","59_1","59_2","59_3","59_4","59_5","59_6","59_7","59_8","59_9","59_10","59_11","59_12","59_13","59_14","59_15","59_16","59_17","59_18","59_19","59_20","59_21","60_1","60_2","60_3","60_4","60_5","60_6","60_7","61_1","61_2","61_3","62_1","62_2","62_3","62_4","62_5","62_6","62_7","62_8","62_9","62_10","62_11","62_12","63_1","63_2","63_3","63_4","63_5","64_1","64_2","64_3","64_4","64_5","64_6","65_1","65_2","66_1","66_2","66_3","66_4","67_1","67_2","67_3","67_4","67_5","67_6","67_7","67_8","67_9","68_1","68_2","68_3","68_4","68_5","68_6","69_1","69_2","69_3","69_4","69_5","69_6","69_7","69_8","69_9","69_10","69_11","69_12","69_13","69_14","70_1","70_2","71_1","71_2","71_3","71_4","71_5","72_1","72_2","72_3","72_4","72_5","73_1","73_2","73_3","73_4","74_1","74_2","74_3","74_4","74_5","74_6","75_1","75_2","75_3","75_4","75_5","75_6","75_7","75_8","75_9","75_10","75_11","75_12","75_13","75_14","75_15","75_16","75_17","75_18","76_1","76_2","76_3","76_4","76_5","76_6","76_7","76_8","76_9","76_10","77_1","77_2","77_3","77_4","77_5","77_6","77_7","77_8","77_9","77_10","77_11","78_1","78_2","78_3","78_4","78_5","78_6","78_7","78_8","78_9","78_10","78_11","78_12","79_1","79_2","79_3","80_1","80_2","80_3","80_4","80_5","81_1","81_2","81_3","82_1","82_2","83_1","83_2","83_3","83_4","83_5","83_6","83_7","83_8","84_1","84_2","84_3","84_4","84_5","85_1","85_2","85_3","85_4","85_5","86_1","86_2","86_3","86_4","87_1","87_2","87_3","88_1","88_2","88_3","88_4","89_1","89_2","89_3","90_1","90_2","91_1","91_2","91_3","91_4","91_5","91_6","91_7","91_8","91_9","91_10","92_1","92_2","92_3","92_4","92_5","92_6","92_7","92_8","92_9","92_10","92_11","92_12","92_13","93_1","93_2","93_3","93_4","93_5","93_6","93_7","93_8","93_9","93_10","93_11","93_12","94_1","94_2","94_3","94_4","94_5","94_6","94_7","94_8","94_9","94_10","94_11","95_1","95_2","95_3","95_4","95_5","95_6","95_7","95_8","95_9","95_10","971_1","971_2","971_3","971_4","972_1","972_2","972_3","972_4","973_1","973_2","974_1","974_2","974_3","974_4","974_5","974_6","974_7","985_1","985_2","988_1","988_2","987_1","987_2","987_3","975_1","986_1","979_1","99_1","99_2","99_3","99_4","99_5","99_6","99_7","99_8","99_9","99_10","99_11"]
couleurs=["EXG","FG","PS","EELV","MODEM","UMP","FN"]

res_pres_t1={}
for code in codes_circos :
	res_pres_t1[code]={}

raw_file=open("Presidentielle_2012_T1_T2.csv","r")
raw_lines=raw_file.read().splitlines()
headers=raw_lines[0].replace(' ','_').split(";")
raw_lines=raw_lines[1:]

for line in raw_lines :
	champs=line.split(";")
	code=champs[0].replace("ZA","971").replace("ZB","972").replace("ZC","973").replace("ZD","974").replace("ZM","985").replace("ZN","988").replace("ZP","987").replace("ZS","975").replace("ZW","986").replace("ZX","979").replace("ZZ","99")+"_"+champs[1]
	
	for i in range(2,len(headers)):
		res_pres_t1[code][headers[i]]=champs[i]

raw_file.close()

#print(res_pres_t1["75_18"])

candidats_colores_par_circo={}
for code in codes_circos :
	candidats_colores_par_circo[code]={}

raw_file=open("1candidat_couleur_circo_2012.csv","r")
raw_lines=raw_file.read().splitlines()
headers=raw_lines[0].split(";")
raw_lines=raw_lines[1:]

for line in raw_lines :
	champs=line.split(";")
	for i in range(1,len(headers)):
		candidats_colores_par_circo[champs[0]][headers[i]]=champs[i]

raw_file.close()

#print(candidats_colores_par_circo["75_18"])

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
#	if code=="75_18":
#		print(presents)
	pred_t1[code]=premier_tour(int(res_pres_t1[code]["HOLLANDE"]),int(res_pres_t1[code]["LE_PEN"]),int(res_pres_t1[code]["MELENCHON"]),int(res_pres_t1[code]["SARKOZY"]),int(res_pres_t1[code]["BAYROU"]),presents["EXG"],presents["FG"],presents["PS"],presents["EELV"],presents["MODEM"],presents["UMP"],presents["FN"])
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


#print(pred_t1["75_18"])
#print(qualifies)

clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins"]
for couleur in couleurs:
	clean_headers.append(couleur)
	clean_headers.extend(["voix","%_Voix/Ins","%_Voix/Exp"])
clean_csv=open("pred_t1_2012.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in codes_circos :
#for code in ["75_18"] :
	valeurs=[code,str(pred_t1[code]["Inscrits"]),str(pred_t1[code]["Exprimés"]),str(pred_t1[code]["%_Exp/Ins"])]
	for couleur in couleurs:
		valeurs.extend([pred_t1[code][couleur]["nom"],str(pred_t1[code][couleur]["voix"]),str(pred_t1[code][couleur]["%_Voix/Ins"]),str(pred_t1[code][couleur]["%_Voix/Exp"])])
	clean_csv.write(";".join(valeurs)+"\n")

clean_csv.close()

clean_headers=["circo","Inscrits","Exprimés","%_Exp/Ins","Couleur","nom","Voix","%_Voix/Ins","%_Voix/Exp"]
clean_csv=open("pred_t1_2012_portrait.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in codes_circos :
#for code in ["75_18"] :
	for couleur in couleurs:
		valeurs=[code,str(pred_t1[code]["Inscrits"]),str(pred_t1[code]["Exprimés"]),str(pred_t1[code]["%_Exp/Ins"]),couleur,pred_t1[code][couleur]["nom"],str(pred_t1[code][couleur]["voix"]),str(pred_t1[code][couleur]["%_Voix/Ins"]),str(pred_t1[code][couleur]["%_Voix/Exp"])]
		clean_csv.write(";".join(valeurs)+"\n")
clean_csv.close()


qualifies_csv=open("qualifies_2102.csv","w")
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

clean_csv=open("pred_t2_2012.csv","w")
clean_csv.write(";".join(clean_headers)+"\n")
for code in codes_circos :
#for code in ["75_18"] :
	valeurs=[code,str(pred_t2[code]["Inscrits"]),str(pred_t2[code]["Exprimés"]),str(pred_t2[code]["%_Exp/Ins"])]
	for couleur in couleurs:
		valeurs.extend([pred_t2[code][couleur]["nom"],str(pred_t2[code][couleur]["voix"]),str(pred_t2[code][couleur]["%_Voix/Ins"]),str(pred_t2[code][couleur]["%_Voix/Exp"])])
	clean_csv.write(";".join(valeurs)+"\n")

clean_csv.close()


victors_csv=open("victors_2012.csv","w")
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

