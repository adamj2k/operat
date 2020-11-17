# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:51:03 2020

@author: Adam
"""

DROP TABLE IF EXISTS robota;

CREATE TABLE robota (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  idpracy TEXT UNIQUE NOT NULL,
  wojew TEXT NOT NULL,
  powiat TEXT NOT NULL,
  jdnewid TEXT NOT NULL,
  obreb TEXT NOT NULL,
  obiekt TEXT NOT NULL,
  dzialki TEXT,
  data_operat TEXT,
  obszar TEXT,
  pocz TEXT,
  kierownik TEXT,
  licencja TEXT,
  datalic TEXT,
  osnowapoz TEXT,
  osnowawys TEXT,
  osnowapom TEXT,
  sekcje65 TEXT,
  sekcje2000 TEXT,
  pomiar TEXT,
  gpsref TEXT,
  niwelacja INTEGER,
  kalibracja INTEGER,
  szkicepolowe TEXT,
  zakresbaz TEXT
);