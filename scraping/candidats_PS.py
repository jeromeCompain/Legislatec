#-*- coding: utf-8 -*-

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import scrapy
import re

def xstr(s):
	if s is None:
		return ''
	return str(s)

class liste_candidats_PS(scrapy.Spider):
	name="candidats_PS"
	allowed_domains=["parti-socialiste.fr"]
	start_urls=["http://www.parti-socialiste.fr/liste-candidats-aux-legislatives-investis-ps/"]



	def parse(self,response):
		print("parse")
		output_file=open("/home/cloudera/candidats_PS.csv",'w')
		output_file.write("Prénom;Nom;Département;Numéro de département;Numéro de la circonscription;facebook;twitter;url\n")
		output_file.close()
		urls_file=open("/home/cloudera/urls_candidats_PS.txt",'w')
		if response is not None :
			lURL = []
			for c in response.xpath("//div[@class='collapseomatic_content ']/a"):
				lURL.append(c.xpath("@href").extract_first())
				urls_file.write(str(c.xpath("@href").extract_first())+'\n')
		urls_file.close()



		for (i, page) in enumerate(lURL) :
			yield scrapy.Request(page, callback=self.parser2)
    


	def parser2(self, response):
		print("parser2")
		url=str(response).split()[1][:-2]+'/'
		entry=[]
		for cand in response.xpath("//div[@class='article-header']"):
			prenom = xstr(cand.xpath("./h1/text()").extract_first().split()[0])
			entry.append(prenom)
			nom = xstr(' '.join(cand.xpath("./h1/text()").extract_first().split()[1:]))
			entry.append(nom)
			desc=cand.xpath("./p/text()").extract_first()
			if desc is None:
				entry.append("")
				entry.append("")
				entry.append("")
			else:
				print(desc)
				departement=xstr(desc.split('(')[0].split()[-1].split("'")[-1])
				entry.append(departement)
				dpt=xstr(re.findall(r'\d+',desc.split('(')[1])[0])
				entry.append(dpt)
				circo=xstr(re.findall(r'\d+',desc.split('(')[0])[0])
				entry.append(circo)
			fb=xstr(cand.xpath("//a[@class='btn btn-sm btn-outline-blue btn-facebook']/@href").extract_first())
			entry.append(fb)
			twt=xstr(cand.xpath("//a[@class='btn btn-sm btn-outline-blue btn-twitter']/@href").extract_first())
			entry.append(twt)
			entry.append(url)
			print(entry)
			output_file=open("/home/cloudera/candidats_PS.csv",'a')
			output_file.write(";".join(entry)+'\n')
			output_file.close()
