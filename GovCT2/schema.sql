/* (Beta) Export of data model GovCT2 of the subject dataModel.EnergyCIM for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE GovCT2_type AS ENUM ('GovCT2');
CREATE TABLE GovCT2 (address JSON, alternateName TEXT, areaServed TEXT, aset NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, db NUMERIC, description TEXT, dm NUMERIC, flim1 NUMERIC, flim10 NUMERIC, flim2 NUMERIC, flim3 NUMERIC, flim4 NUMERIC, flim5 NUMERIC, flim6 NUMERIC, flim7 NUMERIC, flim8 NUMERIC, flim9 NUMERIC, ka NUMERIC, kdgov NUMERIC, kigov NUMERIC, kiload NUMERIC, kimw NUMERIC, kpgov NUMERIC, kpload NUMERIC, kturb NUMERIC, ldref NUMERIC, maxerr NUMERIC, minerr NUMERIC, mwbase NUMERIC, name TEXT, owner JSON, plim1 NUMERIC, plim10 NUMERIC, plim2 NUMERIC, plim3 NUMERIC, plim4 NUMERIC, plim5 NUMERIC, plim6 NUMERIC, plim7 NUMERIC, plim8 NUMERIC, plim9 NUMERIC, prate NUMERIC, r NUMERIC, rclose NUMERIC, rdown NUMERIC, ropen NUMERIC, rselect NUMERIC, rup NUMERIC, source TEXT, ta NUMERIC, tact NUMERIC, tb NUMERIC, tc NUMERIC, tdgov NUMERIC, teng NUMERIC, tfload NUMERIC, tpelec NUMERIC, tsa NUMERIC, tsb NUMERIC, type GovCT2_type, vmax NUMERIC, vmin NUMERIC, wfnl NUMERIC, wfspd NUMERIC);