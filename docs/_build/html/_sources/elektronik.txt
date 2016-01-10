Elektronik
==========

Stromverbrauch und Stromversorgung
----------------------------------
Zu klären:

* Wie groß ist der Stromverbrauch? (min/max)
* Wie lange soll das Boot ohne Sonne fahren können?
* Wie schnell sollen die Ackus wieder geladen sein?
* Wie viele Ackus könne wir mitnehmen? 

Stromverbrauch:
^^^^^^^^^^^^^^^

============================	===================  ===================  ===================  ======
Verbraucher  			U_{in}  	     I max.  		  I avr.               Quelle
----------------------------	-------------------  -------------------  -------------------  ------
Rasperry Pi    			5V		     500 mA	       	  (200-500) mA	       `Raspberry Stromverbrauch`_ 
Servos				(4.5-6) V	     (1.15-1.6) A	  (175-250) mA	       http://www.flyheli.de/rxversorgung.htm
Sat.-mobile RockBLOCK		5V		     450 mA		  100 mA	       http://www.makersnake.com/rockblock/
Adafruit GPS shield		3.3 V (from Pi)	     20 mA		  20 mA		       https://www.adafruit.com/products/2324
Adafruit 9-DOF (2x)		3-5 V (from Pi)	     ~mA		  ~mA		       https://www.adafruit.com/products/2021
============================	===================  ===================  ===================  ======

.. _Raspberry Stromverbrauch: https://www.elektronik-kompendium.de/sites/raspberry-pi/1910071.html

In der Summe ein ungefährer Stromverbrauch von ~750 mA bei ca. U~5 V.

Bei einer Dunkelzeit von 24 muss der Acku bei einer Spannung von 5 V eine Kapazität von: 

* 24 h * 750 mA = 18 Ah
* 24 h * 0,750 A * 5 V = 24 h * 3,75 W = 90 Wh

Verlustleistung Spannungswandler:
20%-30% Verlustleistung `DC/DC-Wandler`_ 12V/5V

.. _DC/DC-Wandler: https://www.conrad.de/de/dcdc-wandler-mean-well-sd-15b-5-5-vdc-3-a-1297246.html?gclid=Cj0KEQiAn8i0BRDur-HV1PCTy4UBEiQAPuFr9HGKw4jSRbwyD_14551PHsOlSse1eryOi-f7nrH6cfsaArnb8P8HAQ&insert_kz=VQ&hk=SEM&WT.srch=1&WT.mc_id=google_pla&s_kwcid=AL!222!3!61621373937!!!g!!&ef_id=VDqdIwAAABRY9cC2:20160110204649:s

Solarzellen:
^^^^^^^^^^^^
Dei meisten Solarzellen besitzten eine Ausgangsspannung von 12 V, deswegen gibt es in diesem Bereich das meiste Angebot und ich habe jetzt mal eine 12 V Solarpanel angenommen. Acku und Umspanner müssen dann angepasst werden.

=================== 	======================  ======================	=============   ==============  =========
Solarzelle		Ausgangsspannung	Ausgangsstrom max.	Leistung	Link		Preis
-------------------  	----------------------  ----------------------  -------------   --------------	---------
Offgridtec® Poly 	12 V			570 mA			10 Watt		`Offgridtec`_	22,90 €
===================  	======================  ======================  =============  	==============  =========

.. _Offgridtec: https://www.offgridtec.com/offgridtecr-10-watt-poly-12v-solarpanel.html

Ackus:
^^^^^^

=================== 	======================	======================	=============	==============  ========
Acku			Ausgangsspannung	Kapazität		Gewicht		Link		Preis
-------------------  	----------------------  ----------------------  -------------	--------------  --------
FLOUREON®		11,1 V			5500 mAh/61 Wh		417 g		`FLOUREON`_	~30 €
===================  	======================  ======================  =============	==============	========

.. _FLOUREON: http://www.amazon.de/FLOUREON%C2%AE-XT60-Stecker-Modellbau-Hubschrauber-Helicopter/dp/B00LMPYTOU/ref=sr_1_10?ie=UTF8&qid=1452456938&sr=8-10&keywords=modellbau+akku
