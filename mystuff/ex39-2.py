# -*- coding: utf-8 -*-

fylker  = {
	'Oslo':  'Osl',
	'Akershus': 'Akhus',
	'Telemark': 'TMark'
}

towns = {
	'Osl': 'Grefsen',
	'Akhus': 'Jessheim',
	'TMark': 'Skien'
	
	}
	
towns['Osl'] = 'Okern'
towns['Akershus'] = 'Eidsvoll'
towns['Telemark'] = 'Porsgrunn'
#1
print '~' *12
print "Oslo fylke has: ", towns['Osl']
print "Akershus fylke has: ", towns['Akhus']

#2
print '~' *12
print "Oslo's abbreviation is: ", fylker['Oslo']
print "Telemark's abbreviation is: ", fylker['Telemark']

#3
print '~' *12
print "Oslo has: ", towns[fylker['Oslo']]
print "Telemark has: ", towns[fylker['Telemark']]