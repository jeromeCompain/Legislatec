#-*- coding: utf-8 -*-

import scrapy
import re


class liste_candidats_FullList(scrapy.Spider):
    name="candidats_FullList"
    allowed_domains=["http://elections.interieur.gouv.fr"]
    start_urls=["http://elections.interieur.gouv.fr/legislatives-2017/index.html"]
    
    
#    self.fileName = "/home/cloudera/candidats_FullList.csv"


    def parse(self,response):
        print("parse")
        output_file=open("/home/cloudera/candidats_FullList.csv",'w')
        output_file.write("id;Prénom;Nom;sexe;Département;Numéro de département;Numéro de la circonscription\n")
        output_file.close()
        if response is not None :
            lURL = []
            for c in range(2,108) : 
                lURL.append(response.xpath('//*[@id="listeDpt"]/option{0}/@value'.format(c)).extract_first())
                print "detecting page {0}".format(lURL[-1])



        for (i, page) in enumerate(lURL) :
            yield scrapy.Request(page, callback=self.parser2)
    


    def parser2(self, response):
        print("parser2")
        circos=[]
        for c in response.xpath("//table/*a[@href]"):
            circos = c.xpath('./@href').extract_first()
            
        for (i, page) in enumerate(lURL) :
            yield scrapy.Request(page, callback=self.parser3)

    def parser3(self, response):
        print("parser3")
        candidats=[]
        for cand in response.xpath("//table/tbody/tr"):
            infos = cand.xpath("./td/b/text()").extract_first()
            if len(infos) > 0 : 
                infoCandidat = {}
                
                infoCandidat["circonscription"] = ""
                infoCandidat["departement"] = ""
                
                lInfos  = infos.split()
                
                if lInfos[0] == "Mme" : 
                    infoCandidat["sexe"] = "F" 
                else : infoCandidat["sexe"] = "M" 
                infoCandidat["prenom"] = lInfos[1]
                infoCandidat["nom"] = "_".join(lInfos[2:])
                infoCandidat["id"] = "_".join(lInfos[1:])
                
                infoCandidat["nuance"] = cand.xpath("./th/text()").extract_first()
                
                candidats.append(infoCandidat)
        
        
        data = ""
        for c in candidats : 
            entry = [c["id"], c["prenom"], c["nom"], c["sexe"], c["departement"], c["circonscription"]]
            line = ";".join(entry)+'\n'
            output_file=open("/home/cloudera/candidats_FullList.csv",'a')
            output_file.write(line)
            output_file.close()
