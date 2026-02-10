"""
Nifty 500 Stock List
Curated list of NSE-listed stocks for analysis.
Format: symbol.NS for Yahoo Finance compatibility
All tickers verified for Yahoo Finance availability (Feb 2026).
"""

# ~350 verified, active NSE stocks
NIFTY_STOCKS = [
    # ========== NIFTY 50 ==========
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "HINDUNILVR.NS", "BHARTIARTL.NS", "SBIN.NS", "KOTAKBANK.NS", "BAJFINANCE.NS",
    "ITC.NS", "LICI.NS", "LT.NS", "HCLTECH.NS", "AXISBANK.NS",
    "ASIANPAINT.NS", "MARUTI.NS", "SUNPHARMA.NS", "TITAN.NS", "DMART.NS",
    "ULTRACEMCO.NS", "BAJAJFINSV.NS", "WIPRO.NS", "ONGC.NS", "NTPC.NS",
    "NESTLEIND.NS", "TATAMOTORS.NS", "M&M.NS", "JSWSTEEL.NS", "POWERGRID.NS",
    "TATASTEEL.NS", "ADANIENT.NS", "ADANIPORTS.NS", "COALINDIA.NS", "TECHM.NS",
    "HINDZINC.NS", "LTIM.NS", "BAJAJ-AUTO.NS", "SBILIFE.NS", "HDFCLIFE.NS",
    "BRITANNIA.NS", "INDUSINDBK.NS", "GRASIM.NS", "CIPLA.NS", "EICHERMOT.NS",
    "DRREDDY.NS", "DIVISLAB.NS", "APOLLOHOSP.NS", "BPCL.NS", "HEROMOTOCO.NS",

    # ========== NIFTY NEXT 50 ==========
    "ADANIGREEN.NS", "ADANIPOWER.NS", "AMBUJACEM.NS", "ATGL.NS", "AUROPHARMA.NS",
    "BANDHANBNK.NS", "BANKBARODA.NS", "BERGEPAINT.NS", "BIOCON.NS", "BOSCHLTD.NS",
    "CANBK.NS", "CHOLAFIN.NS", "COLPAL.NS", "DABUR.NS", "DLF.NS",
    "GAIL.NS", "GODREJCP.NS", "HAVELLS.NS", "HINDPETRO.NS", "ICICIPRULI.NS",
    "IDEA.NS", "IDFCFIRSTB.NS", "IGL.NS", "INDHOTEL.NS", "INDIGO.NS",
    "IOC.NS", "IRCTC.NS", "JINDALSTEL.NS", "JSWENERGY.NS", "JUBLFOOD.NS",
    "LALPATHLAB.NS", "LUPIN.NS", "MCDOWELL-N.NS", "MOTHERSON.NS", "MUTHOOTFIN.NS",
    "NAUKRI.NS", "NMDC.NS", "OBEROIRLTY.NS", "OFSS.NS", "PAGEIND.NS",
    "PEL.NS", "PETRONET.NS", "PFC.NS", "PIDILITIND.NS", "PIIND.NS",
    "PNB.NS", "POLYCAB.NS", "RECLTD.NS", "SAIL.NS", "SBICARD.NS",
    "SHREECEM.NS", "SIEMENS.NS", "SRF.NS", "TATACOMM.NS", "TATACONSUM.NS",
    "TATAPOWER.NS", "TORNTPHARM.NS", "TRENT.NS", "UPL.NS",
    "VBL.NS", "VEDL.NS", "VOLTAS.NS", "YESBANK.NS", "ZOMATO.NS",

    # ========== LARGE CAP ADDITIONS ==========
    "ABB.NS", "ACC.NS", "ALKEM.NS", "ASHOKLEY.NS",
    "ASTRAL.NS", "ATUL.NS", "AUBANK.NS", "BALKRISIND.NS", "BEL.NS",
    "BHEL.NS", "BHARATFORG.NS", "CANFINHOME.NS", "CGPOWER.NS", "CONCOR.NS",
    "COROMANDEL.NS", "CROMPTON.NS", "CUMMINSIND.NS", "DEEPAKNTR.NS", "ESCORTS.NS",
    "EXIDEIND.NS", "FEDERALBNK.NS", "GLAND.NS", "GODREJPROP.NS",
    "GNFC.NS", "GSPL.NS", "GUJGASLTD.NS", "HAL.NS",
    "HDFCAMC.NS", "HONAUT.NS", "IPCALAB.NS", "IRFC.NS", "JKCEMENT.NS",
    "JSL.NS", "KANSAINER.NS", "KEI.NS", "LICHSGFIN.NS",
    "LTTS.NS", "MANAPPURAM.NS", "MFSL.NS", "MGL.NS",
    "MPHASIS.NS", "MRF.NS", "NAM-INDIA.NS", "NATIONALUM.NS", "NAVINFLUOR.NS",
    "OIL.NS", "PERSISTENT.NS",
    "PHOENIXLTD.NS", "PRESTIGE.NS", "PVRINOX.NS", "RAMCOCEM.NS", "RBLBANK.NS",
    "RELAXO.NS", "SCHAEFFLER.NS", "SHRIRAMFIN.NS",
    "SUNDARMFIN.NS", "SUNTV.NS", "SYNGENE.NS", "TATAELXSI.NS",
    "TIINDIA.NS", "TIMKEN.NS", "TVSMOTOR.NS", "UBL.NS",
    "IREDA.NS", "KALYANKJIL.NS",
    "KPITTECH.NS", "LAURUSLABS.NS", "MARICO.NS", "MAXHEALTH.NS", "MCX.NS",
    "METROPOLIS.NS", "NHPC.NS",
    "SUZLON.NS", "THERMAX.NS",
    "COFORGE.NS", "JIOFIN.NS", "MANKIND.NS", "TATATECH.NS", "ZYDUSLIFE.NS",

    # ========== MIDCAP STOCKS ==========
    "AARTIIND.NS", "AFFLE.NS", "APLAPOLLO.NS",
    "BDL.NS", "BEML.NS", "BLUESTARCO.NS", "BRIGADE.NS", "BSE.NS",
    "CDSL.NS", "CESC.NS",
    "COCHINSHIP.NS", "CRISIL.NS", "CYIENT.NS", "DATAPATTNS.NS",
    "DCMSHRIRAM.NS", "DELHIVERY.NS", "DEVYANI.NS", "DIXON.NS",
    "ECLERX.NS", "EIDPARRY.NS", "ELGIEQUIP.NS", "EMAMILTD.NS", "ENGINERSIN.NS",
    "EQUITASBNK.NS", "FINCABLES.NS", "FINEORG.NS", "FLUOROCHEM.NS",
    "GALAXYSURF.NS", "GRINDWELL.NS", "GRSE.NS",
    "GSFC.NS", "HAPPSTMNDS.NS", "HFCL.NS", "HINDCOPPER.NS",
    "HOMEFIRST.NS", "HUDCO.NS",
    "JINDALSAW.NS", "JKLAKSHMI.NS",
    "JKPAPER.NS", "JMFINANCIL.NS",
    "KAJARIACER.NS", "KEC.NS", "KRBL.NS", "LATENTVIEW.NS",
    "MAPMYINDIA.NS", "MASTEK.NS", "MAZAGON.NS",
    "MIDHANI.NS", "MMTC.NS", "MOIL.NS",
    "NATCOPHARM.NS", "NBCC.NS", "NCC.NS",
    "OLECTRA.NS", "PNBHOUSING.NS", "PNCINFRA.NS",
    "RADICO.NS", "RAIN.NS", "RALLIS.NS", "RATNAMANI.NS",
    "RAYMOND.NS", "RCF.NS", "REDINGTON.NS", "RITES.NS",
    "RVNL.NS",
    "SKFINDIA.NS", "SOBHA.NS",
    "STARHEALTH.NS", "SUNDRMFAST.NS",
    "TANLA.NS", "TATAINVEST.NS", "TCI.NS",
    "TRIDENT.NS", "UTIAMC.NS",
    "VGUARD.NS", "VIPIND.NS",
    "WELCORP.NS", "WELSPUNLIV.NS",
    "WHIRLPOOL.NS", "ZEEL.NS",

    # ========== NIFTY MIDCAP 150 ADDITIONS ==========
    "ABCAPITAL.NS", "AJANTPHARM.NS", "BSOFT.NS",
    "CHAMBLFERT.NS", "CUB.NS",
    "FDC.NS", "FORTIS.NS", "GLENMARK.NS", "GRAPHITE.NS",
    "HBLPOWER.NS", "HEG.NS", "IDBI.NS",
    "INDIACEM.NS", "IONEXCHANG.NS", "IRCON.NS",
    "JAMNAAUTO.NS", "JUSTDIAL.NS", "KALPATPOWR.NS", "KIMS.NS",
    "KNRCON.NS", "KOLTEPATIL.NS", "KPIL.NS", "KSB.NS", "MAZDOCK.NS",
    "NESCO.NS",
    "PCBL.NS", "PTC.NS",
    "SAREGAMA.NS", "SCI.NS",
    "SJVN.NS", "STRIDES.NS",
    "SYMPHONY.NS", "TORNTPOWER.NS", "TRIVENI.NS", "UJJIVANSFB.NS", "UNOMINDA.NS",

    # ========== ADDITIONAL MID/LARGE CAPS ==========
    "ABSLAMC.NS", "ADANIENSOL.NS", "ANGELONE.NS",
    "CAMS.NS", "DALBHARAT.NS",
    "GICRE.NS", "KARURVYSYA.NS", "KFINTECH.NS",
    "LTFOODS.NS", "M&MFIN.NS",
    "METROBRAND.NS", "MRPL.NS",
    "NUVAMA.NS", "POONAWALLA.NS", "POWERINDIA.NS",
    "RATEGAIN.NS",
    "SAFARI.NS", "SANOFI.NS",
    "SUNTECK.NS", "TITAGARH.NS", "TMB.NS",
    "TTKPRESTIGE.NS",

    # ========== SMALL CAPS & TRENDING ==========
    "BALRAMCHIN.NS", "ARVIND.NS", "KITEX.NS",
    "FACT.NS", "NFL.NS", "NOCIL.NS", "VINATIORG.NS",
    "NEWGEN.NS", "SYRMA.NS", "AMBER.NS",
    "ALLCARGO.NS", "BLUEDART.NS",
    "CREDITACC.NS", "AAVAS.NS", "NIACL.NS",
    "CEATLTD.NS", "BALAMINES.NS", "CARBORUNIV.NS",
    "BIRLASOFT.NS", "DATAMATICS.NS",
    "IEX.NS", "NLCINDIA.NS", "SENCO.NS",
    "KPIGREEN.NS",

    # ========== ADDITIONAL BANKING & FINANCE ==========
    "CHOLAHLDNG.NS", "360ONE.NS", "BAJAJHLDNG.NS",
    "ICICIGI.NS", "ICICIBANK.NS", "SBICARD.NS",
    
    # ========== ADDITIONAL IT & TECHNOLOGY ==========
    "ROUTE.NS", "INTELLECT.NS", "ZENSARTECH.NS", "SONATSOFTW.NS",
    "MINDACORP.NS", "3MINDIA.NS",
    "PPLPHARMA.NS", "WESTLIFE.NS", "CAMPUS.NS", "EASEMYTRIP.NS",
    
    # ========== ADDITIONAL PHARMA & HEALTHCARE ==========
    "GRANULES.NS", "CAPLIPOINT.NS", "THYROCARE.NS",
    "ERIS.NS", "JUBLPHARMA.NS", "SUVEN.NS", "NEULANDLAB.NS",
    "SHILPAMED.NS", "SOLARA.NS", "IOLCP.NS",
    
    # ========== ADDITIONAL AUTO & ANCILLARY ==========
    "FORCEMOT.NS", "APOLLOTYRE.NS", "ENDURANCE.NS", "SUPRAJIT.NS",
    "RKFORGE.NS", "MRPL.NS", "SANDUMA.NS", "GABRIEL.NS",
    "FMGOETZE.NS", "ANANDRATHI.NS",
    
    # ========== ADDITIONAL METALS & MINING ==========
    "ADANIPOWER.NS", "HINDALCO.NS",
    "SESHAPAPER.NS", "SAIL.NS",
    
    # ========== ADDITIONAL INFRASTRUCTURE ==========
    "ADANIGREEN.NS", "EIDPARRY.NS", "HINDWAREAP.NS",
    "LEMONTREE.NS", "MAHLOG.NS", "PRAJIND.NS", "SHAREINDIA.NS",
    "VAIBHAVGBL.NS", "GATEWAY.NS", "PPLPHARMA.NS",
    
    # ========== ADDITIONAL POWER & UTILITIES ==========
    "CESC.NS", "JPPOWER.NS", "RELINFRA.NS", "RPOWER.NS",
    
    # ========== ADDITIONAL FMCG & CONSUMER ==========
    "GILLETTE.NS", "PGHH.NS", "HERITGFOOD.NS",
    "BIKAJI.NS", "TASTYBITE.NS", "GMDCLTD.NS", "ZYDUSWELL.NS",
    "JYOTHYLAB.NS", "VMART.NS", "SPANDANA.NS",
    
    # ========== ADDITIONAL RETAIL & CONSUMER DURABLES ==========
    "CANTABIL.NS", "CENTURYPLY.NS",
    "GREENPANEL.NS", "KTKBANK.NS", "ORIENTELEC.NS", "SHOPERSTOP.NS",
    "VGUARD.NS", "WONDERLA.NS",
    
    # ========== ADDITIONAL PAINTS & CHEMICALS ==========
    "ALKYLAMINE.NS", "ARIES.NS", "CHEMFAB.NS", "CLEAN.NS",
    "DCAL.NS", "FINPIPE.NS", "GULFOILLUB.NS",
    "HEMIPROP.NS", "NEULANDLAB.NS", "POLYMED.NS",
    "ROSSARI.NS", "SHALBY.NS", "SUDARSCHEM.NS", "VSSL.NS",
    
    # ========== ADDITIONAL TELECOM & MEDIA ==========
    "TVTODAY.NS", "VINATIORGA.NS",
    
    # ========== ADDITIONAL ENGINEERING & MANUFACTURING ==========
    "AIAENG.NS", "AJMERA.NS", "AKZOINDIA.NS",
    "ANANTRAJ.NS", "APARINDS.NS", "ASAHIINDIA.NS", "ASALCBR.NS",
    "ASHIANA.NS", "AVANTIFEED.NS", "AXISCADES.NS",
    "BASF.NS", "BCG.NS", "BGRENERGY.NS", "BHAGERIA.NS",
    "BIRLACORPN.NS", "BLISSGVS.NS", "BMETRICS.NS",
    
    # ========== ADDITIONAL TEXTILES & APPAREL ==========
    "GOKEX.NS", "GOKUL.NS", "GRASIM.NS",
    "HIMATSEIDE.NS", "JISLJALEQS.NS",
    "MADHAV.NS", "NIITLTD.NS", "PGEL.NS", "TEXRAIL.NS",
    
    # ========== ADDITIONAL LOGISTICS & TRANSPORT ==========
    "MAHSEAMLES.NS", "MAPMYINDIA.NS", "MOLDTKPAC.NS",
    "SHRIPISTON.NS", "VARROC.NS",
    
    # ========== EMERGING & NEW AGE ==========
    "PAYTM.NS", "POLICYBZR.NS", "NYKAA.NS", "CARTRADE.NS",
    "ADANIENSOL.NS", "RENUKA.NS", "RML.NS",
]

# Stock sector mapping for sector analysis
STOCK_SECTORS = {
    # Banking & Finance
    "HDFCBANK.NS": "Banking", "ICICIBANK.NS": "Banking", "SBIN.NS": "Banking",
    "KOTAKBANK.NS": "Banking", "AXISBANK.NS": "Banking", "INDUSINDBK.NS": "Banking",
    "BAJFINANCE.NS": "NBFC", "BAJAJFINSV.NS": "NBFC", "SBILIFE.NS": "Insurance",
    "HDFCLIFE.NS": "Insurance", "ICICIPRULI.NS": "Insurance", "SBICARD.NS": "NBFC",
    "MUTHOOTFIN.NS": "NBFC", "CHOLAFIN.NS": "NBFC", "BANDHANBNK.NS": "Banking",
    "IDFCFIRSTB.NS": "Banking", "PNB.NS": "Banking", "BANKBARODA.NS": "Banking",
    "CANBK.NS": "Banking", "FEDERALBNK.NS": "Banking", "YESBANK.NS": "Banking",
    "AUBANK.NS": "Banking", "RBLBANK.NS": "Banking", "PFC.NS": "NBFC",
    "RECLTD.NS": "NBFC", "LICHSGFIN.NS": "NBFC", "CANFINHOME.NS": "NBFC",
    "HDFCAMC.NS": "AMC", "NAM-INDIA.NS": "AMC",
    "ABCAPITAL.NS": "NBFC", "CUB.NS": "Banking", "IDBI.NS": "Banking",
    "KARURVYSYA.NS": "Banking", "TMB.NS": "Banking", "UJJIVANSFB.NS": "Banking",
    "ABSLAMC.NS": "AMC", "CAMS.NS": "AMC", "ANGELONE.NS": "NBFC",
    "M&MFIN.NS": "NBFC", "JIOFIN.NS": "NBFC", "POONAWALLA.NS": "NBFC",
    "NUVAMA.NS": "NBFC", "CREDITACC.NS": "NBFC", "AAVAS.NS": "NBFC",
    "MANAPPURAM.NS": "NBFC", "MFSL.NS": "NBFC", "SHRIRAMFIN.NS": "NBFC",
    "SUNDARMFIN.NS": "NBFC", "IREDA.NS": "NBFC", "STARHEALTH.NS": "Insurance",
    "GICRE.NS": "Insurance", "NIACL.NS": "Insurance", "LICI.NS": "Insurance",

    # IT & Technology
    "TCS.NS": "IT", "INFY.NS": "IT", "HCLTECH.NS": "IT", "WIPRO.NS": "IT",
    "TECHM.NS": "IT", "LTIM.NS": "IT", "MPHASIS.NS": "IT", "COFORGE.NS": "IT",
    "PERSISTENT.NS": "IT", "LTTS.NS": "IT", "TATAELXSI.NS": "IT",
    "NAUKRI.NS": "IT", "KPITTECH.NS": "IT", "BSOFT.NS": "IT",
    "HAPPSTMNDS.NS": "IT", "CYIENT.NS": "IT", "MASTEK.NS": "IT",
    "BIRLASOFT.NS": "IT", "DATAMATICS.NS": "IT", "NEWGEN.NS": "IT",
    "ECLERX.NS": "IT", "LATENTVIEW.NS": "IT", "TATATECH.NS": "IT",
    "KFINTECH.NS": "IT", "RATEGAIN.NS": "IT",

    # Oil & Gas
    "RELIANCE.NS": "Oil & Gas", "ONGC.NS": "Oil & Gas", "BPCL.NS": "Oil & Gas",
    "IOC.NS": "Oil & Gas", "HINDPETRO.NS": "Oil & Gas", "GAIL.NS": "Oil & Gas",
    "OIL.NS": "Oil & Gas", "PETRONET.NS": "Oil & Gas", "IGL.NS": "Oil & Gas",
    "MGL.NS": "Oil & Gas", "GSPL.NS": "Oil & Gas", "GUJGASLTD.NS": "Oil & Gas",
    "ATGL.NS": "Oil & Gas", "MRPL.NS": "Oil & Gas",

    # Pharma & Healthcare
    "SUNPHARMA.NS": "Pharma", "DRREDDY.NS": "Pharma", "CIPLA.NS": "Pharma",
    "DIVISLAB.NS": "Pharma", "APOLLOHOSP.NS": "Healthcare", "LUPIN.NS": "Pharma",
    "AUROPHARMA.NS": "Pharma", "BIOCON.NS": "Pharma", "TORNTPHARM.NS": "Pharma",
    "ALKEM.NS": "Pharma", "IPCALAB.NS": "Pharma", "GLAND.NS": "Pharma",
    "LALPATHLAB.NS": "Healthcare", "MAXHEALTH.NS": "Healthcare",
    "METROPOLIS.NS": "Healthcare", "SYNGENE.NS": "Pharma",
    "AJANTPHARM.NS": "Pharma", "FDC.NS": "Pharma", "GLENMARK.NS": "Pharma",
    "FORTIS.NS": "Healthcare", "KIMS.NS": "Healthcare", "STRIDES.NS": "Pharma",
    "SANOFI.NS": "Pharma", "NATCOPHARM.NS": "Pharma", "LAURUSLABS.NS": "Pharma",
    "MANKIND.NS": "Pharma", "ZYDUSLIFE.NS": "Pharma",

    # Auto & Auto Ancillary
    "TATAMOTORS.NS": "Auto", "M&M.NS": "Auto", "MARUTI.NS": "Auto",
    "BAJAJ-AUTO.NS": "Auto", "HEROMOTOCO.NS": "Auto", "EICHERMOT.NS": "Auto",
    "TVSMOTOR.NS": "Auto", "ASHOKLEY.NS": "Auto", "MOTHERSON.NS": "Auto Ancillary",
    "BOSCHLTD.NS": "Auto Ancillary", "BHARATFORG.NS": "Auto Ancillary",
    "BALKRISIND.NS": "Auto Ancillary", "MRF.NS": "Auto Ancillary",
    "EXIDEIND.NS": "Auto Ancillary", "TIINDIA.NS": "Auto Ancillary",
    "JAMNAAUTO.NS": "Auto Ancillary", "CEATLTD.NS": "Auto Ancillary",
    "UNOMINDA.NS": "Auto Ancillary",

    # Metals & Mining
    "TATASTEEL.NS": "Metals", "JSWSTEEL.NS": "Metals", "HINDZINC.NS": "Metals",
    "VEDL.NS": "Metals", "COALINDIA.NS": "Mining", "NMDC.NS": "Mining",
    "JINDALSTEL.NS": "Metals", "SAIL.NS": "Metals", "NATIONALUM.NS": "Metals",
    "JSL.NS": "Metals", "GRAPHITE.NS": "Metals", "HEG.NS": "Metals",
    "HINDCOPPER.NS": "Metals", "MOIL.NS": "Mining", "JINDALSAW.NS": "Metals",

    # Infrastructure & Construction
    "LT.NS": "Infrastructure", "ADANIPORTS.NS": "Infrastructure",
    "ULTRACEMCO.NS": "Cement", "SHREECEM.NS": "Cement", "AMBUJACEM.NS": "Cement",
    "ACC.NS": "Cement", "GRASIM.NS": "Cement", "JKCEMENT.NS": "Cement",
    "RAMCOCEM.NS": "Cement", "DLF.NS": "Real Estate", "GODREJPROP.NS": "Real Estate",
    "OBEROIRLTY.NS": "Real Estate", "PRESTIGE.NS": "Real Estate",
    "PHOENIXLTD.NS": "Real Estate", "DALBHARAT.NS": "Cement",
    "INDIACEM.NS": "Cement", "JKLAKSHMI.NS": "Cement",
    "IRFC.NS": "Infrastructure", "IRCON.NS": "Infrastructure",
    "KNRCON.NS": "Infrastructure", "KALPATPOWR.NS": "Infrastructure",
    "KPIL.NS": "Infrastructure", "PNCINFRA.NS": "Infrastructure",
    "KEC.NS": "Infrastructure", "NCC.NS": "Infrastructure",
    "NBCC.NS": "Infrastructure", "RVNL.NS": "Infrastructure",
    "KOLTEPATIL.NS": "Real Estate", "SOBHA.NS": "Real Estate",
    "BRIGADE.NS": "Real Estate", "SUNTECK.NS": "Real Estate",

    # Power & Utilities
    "NTPC.NS": "Power", "POWERGRID.NS": "Power", "TATAPOWER.NS": "Power",
    "ADANIGREEN.NS": "Power", "ADANIPOWER.NS": "Power", "JSWENERGY.NS": "Power",
    "NHPC.NS": "Power", "SJVN.NS": "Power", "TORNTPOWER.NS": "Power",
    "NLCINDIA.NS": "Power", "PTC.NS": "Power", "SUZLON.NS": "Power",
    "KPIGREEN.NS": "Power", "ADANIENSOL.NS": "Power",

    # FMCG & Consumer
    "HINDUNILVR.NS": "FMCG", "ITC.NS": "FMCG", "NESTLEIND.NS": "FMCG",
    "BRITANNIA.NS": "FMCG", "TATACONSUM.NS": "FMCG", "DABUR.NS": "FMCG",
    "MARICO.NS": "FMCG", "GODREJCP.NS": "FMCG", "COLPAL.NS": "FMCG",
    "VBL.NS": "FMCG", "UBL.NS": "FMCG", "MCDOWELL-N.NS": "FMCG",
    "JUBLFOOD.NS": "Food & Beverages", "ZOMATO.NS": "Food Tech",
    "EMAMILTD.NS": "FMCG", "RADICO.NS": "FMCG",

    # Retail & Consumer Durables
    "TITAN.NS": "Retail", "DMART.NS": "Retail", "TRENT.NS": "Retail",
    "PAGEIND.NS": "Retail", "RELAXO.NS": "Retail", "KALYANKJIL.NS": "Retail",
    "VOLTAS.NS": "Consumer Durables", "METROBRAND.NS": "Retail",
    "HAVELLS.NS": "Consumer Durables", "CROMPTON.NS": "Consumer Durables",
    "POLYCAB.NS": "Consumer Durables", "KEI.NS": "Consumer Durables",
    "SYMPHONY.NS": "Consumer Durables", "TTKPRESTIGE.NS": "Consumer Durables",
    "AMBER.NS": "Consumer Durables", "SAFARI.NS": "Retail", "SENCO.NS": "Retail",
    "WHIRLPOOL.NS": "Consumer Durables", "BLUESTARCO.NS": "Consumer Durables",

    # Paints & Chemicals
    "ASIANPAINT.NS": "Paints", "BERGEPAINT.NS": "Paints", "KANSAINER.NS": "Paints",
    "PIDILITIND.NS": "Chemicals", "SRF.NS": "Chemicals", "PIIND.NS": "Chemicals",
    "ATUL.NS": "Chemicals", "DEEPAKNTR.NS": "Chemicals", "NAVINFLUOR.NS": "Chemicals",
    "GNFC.NS": "Chemicals", "COROMANDEL.NS": "Chemicals",
    "CHAMBLFERT.NS": "Chemicals", "FLUOROCHEM.NS": "Chemicals",
    "NOCIL.NS": "Chemicals", "VINATIORG.NS": "Chemicals", "BALAMINES.NS": "Chemicals",
    "FACT.NS": "Chemicals", "RALLIS.NS": "Chemicals",

    # Telecom & Media
    "BHARTIARTL.NS": "Telecom", "IDEA.NS": "Telecom", "TATACOMM.NS": "Telecom",
    "INDIGO.NS": "Aviation", "IRCTC.NS": "Travel", "INDHOTEL.NS": "Hotels",
    "PVRINOX.NS": "Media", "SUNTV.NS": "Media", "SAREGAMA.NS": "Media",
    "ZEEL.NS": "Media",

    # Conglomerates & Engineering
    "ADANIENT.NS": "Conglomerate", "SIEMENS.NS": "Engineering",
    "ABB.NS": "Engineering", "HONAUT.NS": "Engineering", "HAL.NS": "Defence",
    "BEL.NS": "Defence", "BHEL.NS": "Engineering", "CUMMINSIND.NS": "Engineering",
    "THERMAX.NS": "Engineering", "CGPOWER.NS": "Engineering",
    "ESCORTS.NS": "Engineering", "ASTRAL.NS": "Plastics",
    "MAZAGON.NS": "Defence", "BDL.NS": "Defence", "BEML.NS": "Defence",
    "COCHINSHIP.NS": "Defence", "GRSE.NS": "Defence", "MIDHANI.NS": "Defence",
    "MAZDOCK.NS": "Defence", "TITAGARH.NS": "Engineering",
    "POWERINDIA.NS": "Engineering", "ELGIEQUIP.NS": "Engineering",
    "IONEXCHANG.NS": "Engineering", "KSB.NS": "Engineering",
    "CARBORUNIV.NS": "Engineering", "SKFINDIA.NS": "Engineering",
    "TIMKEN.NS": "Engineering", "SCHAEFFLER.NS": "Engineering",
    "RATNAMANI.NS": "Engineering", "APLAPOLLO.NS": "Metals",
    "DIXON.NS": "Electronics", "SYRMA.NS": "Electronics",

    # Textiles
    "ARVIND.NS": "Textiles", "KITEX.NS": "Textiles", "RAYMOND.NS": "Textiles",

    # Sugar
    "BALRAMCHIN.NS": "Sugar", "TRIVENI.NS": "Engineering",

    # Logistics
    "ALLCARGO.NS": "Logistics", "BLUEDART.NS": "Logistics",
    "CONCOR.NS": "Logistics", "DELHIVERY.NS": "Logistics",

    # Miscellaneous
    "BSE.NS": "Exchange", "CDSL.NS": "Exchange", "MCX.NS": "Exchange",
    "IEX.NS": "Exchange", "CRISIL.NS": "Ratings",
    "AARTIIND.NS": "Chemicals", "AFFLE.NS": "IT",
    "DCMSHRIRAM.NS": "Chemicals", "DEVYANI.NS": "Food & Beverages",
    "EIDPARRY.NS": "Sugar", "ENGINERSIN.NS": "Engineering",
    "EQUITASBNK.NS": "Banking", "FINCABLES.NS": "Consumer Durables",
    "FINEORG.NS": "Chemicals", "GALAXYSURF.NS": "Chemicals",
    "GRINDWELL.NS": "Engineering", "GSFC.NS": "Chemicals",
    "HFCL.NS": "Telecom", "HOMEFIRST.NS": "NBFC", "HUDCO.NS": "NBFC",
    "JMFINANCIL.NS": "NBFC", "JKPAPER.NS": "Paper",
    "KRBL.NS": "FMCG", "MMTC.NS": "Trading",
    "OLECTRA.NS": "Auto", "PNBHOUSING.NS": "NBFC",
    "RAIN.NS": "Chemicals", "RCF.NS": "Chemicals",
    "REDINGTON.NS": "IT", "RITES.NS": "Infrastructure",
    "SUNDRMFAST.NS": "Auto Ancillary", "TANLA.NS": "IT",
    "TATAINVEST.NS": "Conglomerate", "TCI.NS": "Logistics",
    "TRIDENT.NS": "Textiles", "UTIAMC.NS": "AMC",
    "VGUARD.NS": "Consumer Durables", "VIPIND.NS": "Retail",
    "WELCORP.NS": "Metals", "WELSPUNLIV.NS": "Textiles",
    "DATAPATTNS.NS": "Defence", "NESCO.NS": "Real Estate",
    "PCBL.NS": "Chemicals", "SCI.NS": "Shipping",
    "STRIDES.NS": "Pharma", "NFL.NS": "Chemicals",
    "LTFOODS.NS": "FMCG", "OFSS.NS": "IT", "PEL.NS": "Consumer Durables",
}


def get_stock_sector(symbol: str) -> str:
    """Get sector for a stock symbol."""
    return STOCK_SECTORS.get(symbol, "Others")


def get_stocks_by_sector(sector: str) -> list:
    """Get all stocks in a particular sector."""
    return [s for s, sec in STOCK_SECTORS.items() if sec == sector]


def get_all_sectors() -> list:
    """Get list of unique sectors."""
    return list(set(STOCK_SECTORS.values()))


# Nifty 50 index symbol
NIFTY_INDEX = "^NSEI"
