#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 07:04:16 2017

@author: cloudera
"""
#######################################################################
## Récupération des infos wikipédia à partir d'une liste de candidats
#######################################################################

from bs4 import BeautifulSoup
import urllib2
import collections
import pandas as pd
from urllib2 import URLError, HTTPError
import json

## Liste candidat = lsCand 
lsCand = ['Marine Le Pen', 'gningn gna','Jean-Luc Melenchon']
i=0
log = ""

def get_soup(candidat): ## récupère la page wiki
    soup = None
    site= "http://fr.wikipedia.org/wiki/"+ candidat.replace(" ", "_")
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site,headers=hdr)
    
    try:
         page = urllib2.urlopen(req)
    except URLError, HTTPError:
        global i,log
        i+=1
        log+="skip url : "+candidat+ "\n"
    else:
        soup = BeautifulSoup(page.read(),  "lxml")
    
    return soup

def get_infobox(soup):  ## récupère infobox
    table = None
    table = soup.find('table', class_='infobox_v2')
    return table

def get_sexe(soup): ## récupère le sexe
    sexe = None
    firstRow = soup.find('p').getText()
    if 'homme' in firstRow :
        sexe = 'M'
    else:
        sexe = 'F'
    return sexe

def get_age(info): ## récupère l'age
    age = None
    ageold = info.find('span', class_='noprint').getText()
    age = ageold[1:3]
    return age

def get_fonction(info):
    lsFct=[]
    for t in info.findAll('tr'):
        if t.find('th', style="padding:4px;text-align:center;background-color:#B0C4DE;color:#000000") :
            funct = 'Fonction : ' + t.find('th', style="padding:4px;text-align:center;background-color:#B0C4DE;color:#000000").getText()
        if t.find('b') :
            date = 'Periode : ' + t.find('b').getText()
            lsFct.append(funct +' ; '+ date)
    return lsFct

def get_profession(info):
    prof = None
    for row in info.findAll('tr'):
        row_h = row.find('th', scope ='row')
        if row_h != None :
            if row_h.getText() == 'Profession':
                prof = row.find('td').getText().split('\n')
    return prof

def get_pol(info):
    pol = None
    for row in info.findAll('tr'):
        row_h = row.find('th', scope ='row')
        if row_h != None :
            if row_h.getText() == 'Parti politique':
                pol = row.find('td').getText().split('\n')
    return pol

def get_cara(candidat):  ## centralise les infos candidats
    data = collections.defaultdict()
    
    data['Nom'] = candidat.split(' ')[1:]
    data['Prenom'] = candidat.split(' ')[0]
 #   data['Infobox'] = None
    data['Sexe'] = None
    data['Age'] = None
    data['Fonction'] = None
    data['Profession'] = None
    data['Parti politique'] = None
    
    soup_c = get_soup(candidat)
    if soup_c == None :
        return dict(data)
    else :    
        info = get_infobox(soup_c)
 #       data['Infobox'] = info
        data['Sexe'] = get_sexe(soup_c)
        data['Age'] = get_age(info)
        data['Fonction'] = get_fonction(info)
        data['Profession'] = get_profession(info)
        data['Parti politique'] = get_pol(info)
        return dict(data)

################################################################
## Resultats pour l'ensemble des candidats dans items(list)
################################################################


items = []

for candidat in lsCand :
    item=get_cara(candidat) 
    items.append(item) # compile dans chaque boucle

log+= str(i) + ' urls non definis sur '+ str(len(lsCand))+ ' candidats'


################################################################
## Sauvegarde 
################################################################

if len(log)>1 :
    with open('error_wiki.txt','w') as r :
        r.write(log)


df = pd.DataFrame(items)
df.to_csv('Candidat_wiki.csv', sep=';', encoding='utf-8')  

with open('Candidat_wiki.json','w') as f :
    json.dump(items,f)
    