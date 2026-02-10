"""
Nifty 500 Stock List
Complete list of NSE-listed stocks for analysis.
Format: symbol.NS for Yahoo Finance compatibility
"""

# Top 200 most liquid Nifty stocks for faster initial load
# Full Nifty 500 can be enabled by uncommenting the extended list below

NIFTY_STOCKS = [
    # Nifty 50 constituents
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
    
    # Nifty Next 50
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
    "TATAPOWER.NS", "TORNTPHARM.NS", "TRENT.NS", "UNIONBANK.NS", "UPL.NS",
    "VBL.NS", "VEDL.NS", "VOLTAS.NS", "YESBANK.NS", "ZOMATO.NS",
    
    # Additional large caps for broader coverage
    "ABB.NS", "ACC.NS", "ADANITRANS.NS", "ALKEM.NS", "ASHOKLEY.NS",
    "ASTRAL.NS", "ATUL.NS", "AUBANK.NS", "BALKRISIND.NS", "BEL.NS",
    "BHEL.NS", "BHARATFORG.NS", "CANFINHOME.NS", "CGPOWER.NS", "CONCOR.NS",
    "COROMANDEL.NS", "CROMPTON.NS", "CUMMINSIND.NS", "DEEPAKNTR.NS", "ESCORTS.NS",
    "EXIDEIND.NS", "FEDERALBNK.NS", "GLAND.NS", "GLAXO.NS", "GMRINFRA.NS",
    "GNFC.NS", "GODREJPROP.NS", "GSPL.NS", "GUJGASLTD.NS", "HAL.NS",
    "HDFCAMC.NS", "HONAUT.NS", "IPCALAB.NS", "IRFC.NS", "JKCEMENT.NS",
    "JSL.NS", "KANSAINER.NS", "KEI.NS", "L&TFH.NS", "LICHSGFIN.NS",
    "LTTS.NS", "MANAPPURAM.NS", "MFSL.NS", "MGL.NS", "MINDTREE.NS",
    "MPHASIS.NS", "MRF.NS", "NAM-INDIA.NS", "NATIONALUM.NS", "NAVINFLUOR.NS",
    "NIACL.NS", "OIL.NS", "PAYTM.NS", "PERSISTENT.NS", "PFIZER.NS",
    "PHOENIXLTD.NS", "PRESTIGE.NS", "PVRINOX.NS", "RAMCOCEM.NS", "RBLBANK.NS",
    "RELAXO.NS", "SCHAEFFLER.NS", "SHRIRAMFIN.NS", "SONACOMS.NS", "STAR.NS",
    "SUNDARMFIN.NS", "SUNTV.NS", "SYNGENE.NS", "TATACHEM.NS", "TATAELXSI.NS",
    "TIINDIA.NS", "TIMKEN.NS", "TVSMOTOR.NS", "UBL.NS", "UCOBANK.NS",
    "INDIAMART.NS", "IIFL.NS", "IREDA.NS", "KALYANKJIL.NS", "KAYNES.NS",
    "KPITTECH.NS", "LAURUSLABS.NS", "MARICO.NS", "MAXHEALTH.NS", "MCX.NS",
    "METROPOLIS.NS", "NHPC.NS", "NYKAA.NS", "PATANJALI.NS", "POLICYBZR.NS",
    "PW.NS", "RAJESHEXPO.NS", "SOLARINDS.NS", "SONATSOFTW.NS", "SUPREMEIND.NS",
    "SUVENPHAR.NS", "SUZLON.NS", "THERMAX.NS", "TRITURBINE.NS", "TTML.NS",
    
    # ========== SMALL CAP STOCKS ==========
    # High growth potential small caps
    "AARTIIND.NS", "AFFLE.NS", "APLAPOLLO.NS", "ARE&M.NS", "AVANTIFEED.NS",
    "BDL.NS", "BEML.NS", "BLUESTARCO.NS", "BRIGADE.NS", "BSE.NS",
    "CAMPUS.NS", "CARTRADE.NS", "CDSL.NS", "CENTRALBK.NS", "CESC.NS",
    "CLEAN.NS", "COCHINSHIP.NS", "CRISIL.NS", "CYIENT.NS", "DATAPATTNS.NS",
    "DCMSHRIRAM.NS", "DELHIVERY.NS", "DEVYANI.NS", "DIXON.NS", "EASEMYTRIP.NS",
    "ECLERX.NS", "EIDPARRY.NS", "ELGIEQUIP.NS", "EMAMILTD.NS", "ENGINERSIN.NS",
    "EQUITASBNK.NS", "FINCABLES.NS", "FINEORG.NS", "FLUOROCHEM.NS", "FSL.NS",
    "GALAXYSURF.NS", "GARFIBRES.NS", "GESHIP.NS", "GRINDWELL.NS", "GRSE.NS",
    "GSFC.NS", "HAPPSTMNDS.NS", "HATSUN.NS", "HFCL.NS", "HINDCOPPER.NS",
    "HOMEFIRST.NS", "HUDCO.NS", "IIFLWAM.NS", "INDIGOPNTS.NS", "INTELLECT.NS",
    "IOB.NS", "JBCHEPHARM.NS", "JBMA.NS", "JINDALSAW.NS", "JKLAKSHMI.NS",
    "JKPAPER.NS", "JMFINANCIL.NS", "JSWINFRA.NS", "JTEKTINDIA.NS", "JUBLINGREA.NS",
    "KAJARIACER.NS", "KEC.NS", "KRBL.NS", "LATENTVIEW.NS", "LAXMIMACH.NS",
    "LEMONTREE.NS", "LLOYDSME.NS", "LTF.NS", "MAHABANK.NS", "MAHLIFE.NS",
    "MAHSEAMLES.NS", "MAPMYINDIA.NS", "MASTEK.NS", "MAZAGON.NS", "MEDANTA.NS",
    "MEDPLUS.NS", "MIDHANI.NS", "MINDACORP.NS", "MMTC.NS", "MOIL.NS",
    "NATCOPHARM.NS", "NBCC.NS", "NCC.NS", "NETWORK18.NS", "NIITMTS.NS",
    "OLECTRA.NS", "ORIENTELEC.NS", "PNBHOUSING.NS", "PNCINFRA.NS", "PRSMJOHNSN.NS",
    "QUICKHEAL.NS", "RADICO.NS", "RAIN.NS", "RALLIS.NS", "RATNAMANI.NS",
    "RAYMOND.NS", "RCF.NS", "REDINGTON.NS", "RENUKA.NS", "RITES.NS",
    "RMDR.NS", "ROUTE.NS", "RVNL.NS", "SAPPHIRE.NS", "SARDAEN.NS",
    "SHARDACROP.NS", "SHYAMMETL.NS", "SKFINDIA.NS", "SNOWMAN.NS", "SOBHA.NS",
    "SPARC.NS", "SPLPETRO.NS", "STARHEALTH.NS", "STLTECH.NS", "SUNDRMFAST.NS",
    "TANLA.NS", "TATAINVEST.NS", "TCI.NS", "TECHNO.NS", "THYROCARE.NS",
    "TINPLATE.NS", "TRIDENT.NS", "UJJIVAN.NS", "UTIAMC.NS", "VAIBHAVGBL.NS",
    "VAKRANGEE.NS", "VENKEYS.NS", "VGUARD.NS", "VIJAYA.NS", "VIPIND.NS",
    "VSTIND.NS", "WABCOINDIA.NS", "WELCORP.NS", "WELSPUNLIV.NS", "WESTLIFE.NS",
    "WHIRLPOOL.NS", "ZEEL.NS", "ZENSARTECH.NS", "ZFCVINDIA.NS", "ZODIACJRD.NS",

    # ========== NIFTY MIDCAP 150 ADDITIONS ==========
    # Midcap stocks not already listed above
    "ABCAPITAL.NS", "AJANTPHARM.NS", "APLLTD.NS", "BAYERCROP.NS", "BSOFT.NS",
    "CENTURYTEX.NS", "CHAMBLFERT.NS", "CUB.NS", "DELTACORP.NS", "EDELWEISS.NS",
    "FDC.NS", "FORTIS.NS", "GLENMARK.NS", "GRAPHITE.NS", "GREAVESCOT.NS",
    "HBLPOWER.NS", "HEG.NS", "IBREALEST.NS", "IDBI.NS", "IFBIND.NS",
    "INDIACEM.NS", "IONEXCHANG.NS", "IRCON.NS", "ISEC.NS", "ITI.NS",
    "JAMNAAUTO.NS", "JSWHL.NS", "JUSTDIAL.NS", "KALPATPOWR.NS", "KIMS.NS",
    "KNRCON.NS", "KOLTEPATIL.NS", "KPIL.NS", "KSB.NS", "MAZDOCK.NS",
    "MOTILALOFS.NS", "MSTCLTD.NS", "NESCO.NS", "NILKAMAL.NS", "NUCLEUS.NS",
    "PARAS.NS", "PCBL.NS", "PGHH.NS", "PTC.NS", "QUESS.NS",
    "RKFORGE.NS", "ROSSARI.NS", "RPOWER.NS", "SAREGAMA.NS", "SCI.NS",
    "SJVN.NS", "SJS.NS", "SOLARA.NS", "STRIDES.NS", "SWANENERGY.NS",
    "SYMPHONY.NS", "TARSONS.NS", "TATAMETALI.NS", "TEAMLEASE.NS", "TIRUMALCHM.NS",
    "TORNTPOWER.NS", "TRIVENI.NS", "UJJIVANSFB.NS", "UNOMINDA.NS", "VMART.NS",
    "WELSPUNIND.NS", "ZYDUSWELL.NS",

    # ========== ADDITIONAL MIDCAP INDUSTRIALS ==========
    "AIAENG.NS", "ANURAS.NS", "CHOICEIN.NS", "DOMS.NS", "EMCURE.NS",
    "ERIS.NS", "EXPLEOSOL.NS", "GPIL.NS", "HPL.NS", "IBULHSGFIN.NS",
    "INOXWIND.NS", "JPPOWER.NS", "JYOTHYLAB.NS", "KIRLOSENG.NS", "LXCHEM.NS",
    "MANINFRA.NS", "MTARTECH.NS",

    # ========== ADDITIONAL LARGE/MID CAPS ==========
    # Recently listed and popular stocks
    "ABSLAMC.NS", "ADANIENSOL.NS", "AETHER.NS", "ANGELONE.NS", "AWL.NS",
    "CAMS.NS", "CANFINHOME.NS", "CENTRALBK.NS", "CHALET.NS", "CONCORDBIO.NS",
    "COFORGE.NS", "CRAFTSMAN.NS", "CSBBANK.NS", "DALBHARAT.NS", "DEEPAKFERT.NS",
    "DRPATTHY.NS", "EICHERMOT.NS", "ELECON.NS", "EPL.NS", "FINPIPE.NS",
    "GICRE.NS", "GODFRYPHLP.NS", "GOLDIAM.NS", "GPPL.NS", "GRINFRA.NS",
    "GTLINFRA.NS", "GUFICBIO.NS", "HGINFRA.NS", "HINDWAREAP.NS", "HONASA.NS",
    "ICIL.NS", "IIFLSEC.NS", "INDIANB.NS", "INOXGREEN.NS", "JAIBALAJI.NS",
    "JIOFIN.NS", "JKIL.NS", "JUBLPHARMA.NS", "KARURVYSYA.NS", "KFINTECH.NS",
    "KIRLPNU.NS", "KMSUGAR.NS", "KRSNAA.NS", "LANDMARK.NS", "LLOYDSENGG.NS",
    "LTFOODS.NS", "LUXIND.NS", "M&MFIN.NS", "MAHSCOOTER.NS", "MANKIND.NS",
    "MANYAVAR.NS", "MASFIN.NS", "MAXFIN.NS", "METROBRAND.NS", "MHRIL.NS",
    "MOLDTKPAC.NS", "MRPL.NS", "MSUMI.NS", "MUTHOOTMF.NS", "NAVNETEDUL.NS",
    "NETWEB.NS", "NUVAMA.NS", "ODYSSE.NS", "OPTIEMUS.NS", "PAISALO.NS",
    "PARADEEP.NS", "PGEL.NS", "POONAWALLA.NS", "POWERINDIA.NS", "PRINCEPIPE.NS",
    "PRIVISCL.NS", "RAINBOW.NS", "RATEGAIN.NS", "RBA.NS", "RHIM.NS",
    "SAFARI.NS", "SANOFI.NS", "SBCL.NS", "SHILPAMED.NS", "SHOPERSTOP.NS",
    "SIGNATUREGLOBAL.NS", "SMCGLOBAL.NS", "SONACOMS.NS", "SUDARSCHEM.NS", "SUMICHEM.NS",
    "SUNDARMHLD.NS", "SUNTECK.NS", "SUPRIYA.NS", "SWSOLAR.NS", "TATATECH.NS",
    "TATVA.NS", "TEGA.NS", "TEXRAIL.NS", "TITAGARH.NS", "TMB.NS",
    "TTKPRESTIGE.NS", "TV18BRDCST.NS", "UNIPARTS.NS", "USHAMART.NS", "UTKARSHBNK.NS",
    "VARROC.NS", "VIJAYA.NS", "VOLTAMP.NS", "WOCKPHARMA.NS", "YATHARTH.NS",
    "ZOMATO.NS", "ZYDUSLIFE.NS",
    
    # ========== NEW ADDITIONS (RECENT IPOs & OTHERS) ==========
    "OLA.NS", "FIRSTCRY.NS", "IXIGO.NS", "AWFIS.NS", "CELLO.NS",
    "RRKABEL.NS", "HAPPYFORGE.NS", "INOXINDIA.NS", "AZAD.NS", "JYOTICNC.NS",
    "EPACK.NS", "BLSE.NS", "VIBHOR.NS", "JUNIPER.NS", "EXICOM.NS",
    "PLATINUM.NS", "MUKKA.NS", "GOPAL.NS", "JGCHEM.NS", "KRYSTAL.NS",
    "BHARTIHEXA.NS", "JNKINDIA.NS", "INDGIG.NS", "TBZ.NS", "SENCO.NS",
    "PCJEWELLER.NS", "THANGAMAYL.NS", "ASTRAMICRO.NS", "ZEN.NS", "KPIGREEN.NS",
    "PCBL.NS", "JUPITERIN.NS", "IEX.NS", "NLCINDIA.NS", "HUDCO.NS",

    # ========== BATCH 2 – SMALLCAP 250, MICRO-CAPS & TRENDING ==========
    # Textiles & Apparel
    "PGHL.NS", "SOMANYCERA.NS", "RAYMOND.NS", "ARVIND.NS", "KITEX.NS",
    "GOKEX.NS", "DOLLAR.NS", "SPANDANA.NS",
    # Sugar & Agri
    "BALRAMCHIN.NS", "DHAMPUR.NS", "TRIVENI.NS", "DWARIKESH.NS", "RENUKA.NS",
    "UGARSUGAR.NS", "AVANTIFEED.NS",
    # Fertilizers & Chemicals
    "GSFC.NS", "FACT.NS", "NFL.NS", "MADRASFERT.NS", "NOCIL.NS",
    "VINATIORG.NS", "TATACOFFEE.NS", "IGPL.NS",
    # Defence & Aerospace
    "PARAS.NS", "DCXINDIA.NS", "IDEAFORGE.NS", "STEL.NS",
    "GANDHAR.NS", "NEWGEN.NS",
    # EMS & Electronics
    "KAYNES.NS", "SYRMA.NS", "CEINSYSTECH.NS", "PGEL.NS", "AMBER.NS",
    # Logistics & Shipping
    "ALLCARGO.NS", "MAHINDCIE.NS", "BLUEDART.NS", "TCI.NS", "GESHIP.NS",
    # Speciality Finance & Insurance
    "CREDITACC.NS", "AAVAS.NS", "HOMEFIRST.NS", "STARHEALTH.NS", "NIACL.NS",
    # Miscellaneous Popular
    "CEATLTD.NS", "BALAMINES.NS", "CARBORUNIV.NS", "GPPL.NS", "IIITM.NS",
    "SAKSOFT.NS", "MASTEK.NS", "BIRLASOFT.NS", "ZENSAR.NS", "MPHASIS.NS",
    "PERSISTENT.NS", "COFORGE.NS", "CYIENT.NS", "TTML.NS", "DATAMATICS.NS",
    "SUBEXLTD.NS", "BECTORFOOD.NS", "PRATAAP.NS", "ACI.NS", "TINPLATE.NS",
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
    
    # IT & Technology
    "TCS.NS": "IT", "INFY.NS": "IT", "HCLTECH.NS": "IT", "WIPRO.NS": "IT",
    "TECHM.NS": "IT", "LTIM.NS": "IT", "MPHASIS.NS": "IT", "COFORGE.NS": "IT",
    "PERSISTENT.NS": "IT", "LTTS.NS": "IT", "TATAELXSI.NS": "IT",
    "NAUKRI.NS": "IT", "KPITTECH.NS": "IT",
    
    # Oil & Gas
    "RELIANCE.NS": "Oil & Gas", "ONGC.NS": "Oil & Gas", "BPCL.NS": "Oil & Gas",
    "IOC.NS": "Oil & Gas", "HINDPETRO.NS": "Oil & Gas", "GAIL.NS": "Oil & Gas",
    "OIL.NS": "Oil & Gas", "PETRONET.NS": "Oil & Gas", "IGL.NS": "Oil & Gas",
    "MGL.NS": "Oil & Gas", "GSPL.NS": "Oil & Gas", "GUJGASLTD.NS": "Oil & Gas",
    "ATGL.NS": "Oil & Gas",
    
    # Pharma & Healthcare
    "SUNPHARMA.NS": "Pharma", "DRREDDY.NS": "Pharma", "CIPLA.NS": "Pharma",
    "DIVISLAB.NS": "Pharma", "APOLLOHOSP.NS": "Healthcare", "LUPIN.NS": "Pharma",
    "AUROPHARMA.NS": "Pharma", "BIOCON.NS": "Pharma", "TORNTPHARM.NS": "Pharma",
    "ALKEM.NS": "Pharma", "IPCALAB.NS": "Pharma", "GLAND.NS": "Pharma",
    "LALPATHLAB.NS": "Healthcare", "MAXHEALTH.NS": "Healthcare",
    "METROPOLIS.NS": "Healthcare", "SYNGENE.NS": "Pharma",
    
    # Auto & Auto Ancillary
    "TATAMOTORS.NS": "Auto", "M&M.NS": "Auto", "MARUTI.NS": "Auto",
    "BAJAJ-AUTO.NS": "Auto", "HEROMOTOCO.NS": "Auto", "EICHERMOT.NS": "Auto",
    "TVSMOTOR.NS": "Auto", "ASHOKLEY.NS": "Auto", "MOTHERSON.NS": "Auto Ancillary",
    "BOSCHLTD.NS": "Auto Ancillary", "BHARATFORG.NS": "Auto Ancillary",
    "BALKRISIND.NS": "Auto Ancillary", "MRF.NS": "Auto Ancillary",
    "EXIDEIND.NS": "Auto Ancillary", "TIINDIA.NS": "Auto Ancillary",
    
    # Metals & Mining
    "TATASTEEL.NS": "Metals", "JSWSTEEL.NS": "Metals", "HINDZINC.NS": "Metals",
    "VEDL.NS": "Metals", "COALINDIA.NS": "Mining", "NMDC.NS": "Mining",
    "JINDALSTEL.NS": "Metals", "SAIL.NS": "Metals", "NATIONALUM.NS": "Metals",
    "JSL.NS": "Metals",
    
    # Infrastructure & Construction
    "LT.NS": "Infrastructure", "ADANIPORTS.NS": "Infrastructure",
    "ULTRACEMCO.NS": "Cement", "SHREECEM.NS": "Cement", "AMBUJACEM.NS": "Cement",
    "ACC.NS": "Cement", "GRASIM.NS": "Cement", "JKCEMENT.NS": "Cement",
    "RAMCOCEM.NS": "Cement", "DLF.NS": "Real Estate", "GODREJPROP.NS": "Real Estate",
    "OBEROIRLTY.NS": "Real Estate", "PRESTIGE.NS": "Real Estate",
    "PHOENIXLTD.NS": "Real Estate",
    
    # Power & Utilities
    "NTPC.NS": "Power", "POWERGRID.NS": "Power", "TATAPOWER.NS": "Power",
    "ADANIGREEN.NS": "Power", "ADANIPOWER.NS": "Power", "JSWENERGY.NS": "Power",
    "NHPC.NS": "Power", "IRFC.NS": "Infrastructure",
    
    # FMCG & Consumer
    "HINDUNILVR.NS": "FMCG", "ITC.NS": "FMCG", "NESTLEIND.NS": "FMCG",
    "BRITANNIA.NS": "FMCG", "TATACONSUM.NS": "FMCG", "DABUR.NS": "FMCG",
    "MARICO.NS": "FMCG", "GODREJCP.NS": "FMCG", "COLPAL.NS": "FMCG",
    "VBL.NS": "FMCG", "UBL.NS": "FMCG", "MCDOWELL-N.NS": "FMCG",
    "JUBLFOOD.NS": "Food & Beverages", "ZOMATO.NS": "Food Tech",
    "PATANJALI.NS": "FMCG",
    
    # Retail & Consumer Durables
    "TITAN.NS": "Retail", "DMART.NS": "Retail", "TRENT.NS": "Retail",
    "PAGEIND.NS": "Retail", "RELAXO.NS": "Retail", "KALYANKJIL.NS": "Retail",
    "NYKAA.NS": "Retail", "VOLTAS.NS": "Consumer Durables",
    "HAVELLS.NS": "Consumer Durables", "CROMPTON.NS": "Consumer Durables",
    "POLYCAB.NS": "Consumer Durables", "KEI.NS": "Consumer Durables",
    
    # Paints & Chemicals
    "ASIANPAINT.NS": "Paints", "BERGEPAINT.NS": "Paints", "KANSAINER.NS": "Paints",
    "PIDILITIND.NS": "Chemicals", "SRF.NS": "Chemicals", "PIIND.NS": "Chemicals",
    "ATUL.NS": "Chemicals", "DEEPAKNTR.NS": "Chemicals", "NAVINFLUOR.NS": "Chemicals",
    "TATACHEM.NS": "Chemicals", "GNFC.NS": "Chemicals", "COROMANDEL.NS": "Chemicals",
    
    # Telecom & Media
    "BHARTIARTL.NS": "Telecom", "IDEA.NS": "Telecom", "TATACOMM.NS": "Telecom",
    "INDIGO.NS": "Aviation", "IRCTC.NS": "Travel", "INDHOTEL.NS": "Hotels",
    "PVRINOX.NS": "Media", "SUNTV.NS": "Media", "STAR.NS": "Media",

    # Conglomerates & Others
    "ADANIENT.NS": "Conglomerate", "SIEMENS.NS": "Engineering",
    "ABB.NS": "Engineering", "HONAUT.NS": "Engineering", "HAL.NS": "Defence",
    "BEL.NS": "Defence", "BHEL.NS": "Engineering", "CUMMINSIND.NS": "Engineering",
    "THERMAX.NS": "Engineering", "CGPOWER.NS": "Engineering",
    "ESCORTS.NS": "Engineering", "ASTRAL.NS": "Plastics",
    "SUPREMEIND.NS": "Plastics", "LICI.NS": "Insurance",

    # ========== NEW STOCK SECTOR MAPPINGS ==========
    # Nifty Midcap 150 additions
    "ABCAPITAL.NS": "NBFC", "AJANTPHARM.NS": "Pharma", "APLLTD.NS": "Pharma",
    "BAYERCROP.NS": "Chemicals", "BSOFT.NS": "IT", "CENTURYTEX.NS": "Textiles",
    "CHAMBLFERT.NS": "Chemicals", "CUB.NS": "Banking", "DELTACORP.NS": "Hotels",
    "EDELWEISS.NS": "NBFC", "FDC.NS": "Pharma", "FORTIS.NS": "Healthcare",
    "GLENMARK.NS": "Pharma", "GRAPHITE.NS": "Metals", "GREAVESCOT.NS": "Auto",
    "HBLPOWER.NS": "Engineering", "HEG.NS": "Metals", "IBREALEST.NS": "Real Estate",
    "IDBI.NS": "Banking", "IFBIND.NS": "Consumer Durables", "INDIACEM.NS": "Cement",
    "IONEXCHANG.NS": "Engineering", "IRCON.NS": "Infrastructure", "ISEC.NS": "NBFC",
    "ITI.NS": "Telecom", "JAMNAAUTO.NS": "Auto Ancillary", "JSWHL.NS": "Metals",
    "JUSTDIAL.NS": "IT", "KALPATPOWR.NS": "Infrastructure", "KIMS.NS": "Healthcare",
    "KNRCON.NS": "Infrastructure", "KOLTEPATIL.NS": "Real Estate",
    "KPIL.NS": "Infrastructure", "KSB.NS": "Engineering", "MAZDOCK.NS": "Defence",
    "MOTILALOFS.NS": "NBFC", "MSTCLTD.NS": "Infrastructure", "NESCO.NS": "Real Estate",
    "NILKAMAL.NS": "Plastics", "NUCLEUS.NS": "IT", "PARAS.NS": "Healthcare",
    "PCBL.NS": "Chemicals", "PGHH.NS": "FMCG", "PTC.NS": "Power",
    "QUESS.NS": "IT", "RKFORGE.NS": "Auto Ancillary", "ROSSARI.NS": "Chemicals",
    "RPOWER.NS": "Power", "SAREGAMA.NS": "Media", "SCI.NS": "Shipping",
    "SJVN.NS": "Power", "SJS.NS": "Auto Ancillary", "SOLARA.NS": "Pharma",
    "STRIDES.NS": "Pharma", "SWANENERGY.NS": "Power", "SYMPHONY.NS": "Consumer Durables",
    "TARSONS.NS": "Healthcare", "TATAMETALI.NS": "Metals",
    "TEAMLEASE.NS": "IT", "TIRUMALCHM.NS": "Chemicals", "TORNTPOWER.NS": "Power",
    "TRIVENI.NS": "Engineering", "UJJIVANSFB.NS": "Banking", "UNOMINDA.NS": "Auto Ancillary",
    "VMART.NS": "Retail", "WELSPUNIND.NS": "Metals", "ZYDUSWELL.NS": "FMCG",

    # Additional Midcap Industrials
    "AIAENG.NS": "Engineering", "ANURAS.NS": "Engineering", "CHOICEIN.NS": "NBFC",
    "DOMS.NS": "Stationery", "EMCURE.NS": "Pharma", "ERIS.NS": "Pharma",
    "EXPLEOSOL.NS": "IT", "GPIL.NS": "Metals", "HPL.NS": "Consumer Durables",
    "IBULHSGFIN.NS": "NBFC", "INOXWIND.NS": "Power", "JPPOWER.NS": "Power",
    "JYOTHYLAB.NS": "FMCG", "KIRLOSENG.NS": "Engineering", "LXCHEM.NS": "Chemicals",
    "MANINFRA.NS": "Infrastructure", "MTARTECH.NS": "Defence",

    # Additional Large/Mid Caps
    "ABSLAMC.NS": "AMC", "ADANIENSOL.NS": "Power", "AETHER.NS": "Chemicals",
    "ANGELONE.NS": "NBFC", "AWL.NS": "FMCG", "CAMS.NS": "AMC",
    "CHALET.NS": "Hotels", "CONCORDBIO.NS": "Pharma", "COFORGE.NS": "IT",
    "CRAFTSMAN.NS": "Auto Ancillary", "CSBBANK.NS": "Banking", "DALBHARAT.NS": "Cement",
    "DEEPAKFERT.NS": "Chemicals", "DRPATTHY.NS": "Healthcare", "ELECON.NS": "Engineering",
    "EPL.NS": "Plastics", "FINPIPE.NS": "Plastics", "GICRE.NS": "Insurance",
    "GODFRYPHLP.NS": "FMCG", "GOLDIAM.NS": "Retail", "GPPL.NS": "Oil & Gas",
    "GRINFRA.NS": "Infrastructure", "GTLINFRA.NS": "Infrastructure",
    "GUFICBIO.NS": "Pharma", "HGINFRA.NS": "Infrastructure",
    "HINDWAREAP.NS": "Consumer Durables", "HONASA.NS": "FMCG",
    "ICIL.NS": "IT", "IIFLSEC.NS": "NBFC", "INDIANB.NS": "Banking",
    "INOXGREEN.NS": "Power", "JAIBALAJI.NS": "Metals", "JIOFIN.NS": "NBFC",
    "JKIL.NS": "Engineering", "JUBLPHARMA.NS": "Pharma", "KARURVYSYA.NS": "Banking",
    "KFINTECH.NS": "IT", "KIRLPNU.NS": "Engineering", "KMSUGAR.NS": "FMCG",
    "KRSNAA.NS": "Healthcare", "LANDMARK.NS": "Retail", "LLOYDSENGG.NS": "Engineering",
    "LTFOODS.NS": "FMCG", "LUXIND.NS": "Textiles", "M&MFIN.NS": "NBFC",
    "MAHSCOOTER.NS": "Auto", "MANKIND.NS": "Pharma", "MANYAVAR.NS": "Retail",
    "MASFIN.NS": "NBFC", "MAXFIN.NS": "NBFC", "METROBRAND.NS": "Retail",
    "MHRIL.NS": "Hotels", "MOLDTKPAC.NS": "Plastics", "MRPL.NS": "Oil & Gas",
    "MSUMI.NS": "Auto Ancillary", "MUTHOOTMF.NS": "NBFC", "NAVNETEDUL.NS": "IT",
    "NETWEB.NS": "IT", "NUVAMA.NS": "NBFC", "ODYSSE.NS": "Auto",
    "OPTIEMUS.NS": "IT", "PAISALO.NS": "NBFC", "PARADEEP.NS": "Chemicals",
    "PGEL.NS": "Power", "POONAWALLA.NS": "NBFC", "POWERINDIA.NS": "Engineering",
    "PRINCEPIPE.NS": "Plastics", "PRIVISCL.NS": "IT", "RAINBOW.NS": "Healthcare",
    "RATEGAIN.NS": "IT", "RBA.NS": "Banking", "RHIM.NS": "Engineering",
    "SAFARI.NS": "Retail", "SANOFI.NS": "Pharma", "SBCL.NS": "Infrastructure",
    "SHILPAMED.NS": "Healthcare", "SHOPERSTOP.NS": "Retail",
    "SIGNATUREGLOBAL.NS": "Real Estate", "SMCGLOBAL.NS": "NBFC",
    "SUDARSCHEM.NS": "Chemicals", "SUMICHEM.NS": "Chemicals",
    "SUNDARMHLD.NS": "NBFC", "SUNTECK.NS": "Real Estate", "SUPRIYA.NS": "Pharma",
    "SWSOLAR.NS": "Power", "TATATECH.NS": "IT", "TATVA.NS": "Healthcare",
    "TEGA.NS": "Mining", "TEXRAIL.NS": "Engineering", "TITAGARH.NS": "Engineering",
    "TMB.NS": "Banking", "TTKPRESTIGE.NS": "Consumer Durables",
    "TV18BRDCST.NS": "Media", "UNIPARTS.NS": "Auto Ancillary",
    "USHAMART.NS": "Engineering", "UTKARSHBNK.NS": "Banking", "VARROC.NS": "Auto Ancillary",
    "VOLTAMP.NS": "Engineering", "WOCKPHARMA.NS": "Pharma", "YATHARTH.NS": "Healthcare",
    "ZYDUSLIFE.NS": "Pharma",
    
    # New Mappings
    "OLA.NS": "Auto", "FIRSTCRY.NS": "Retail", "IXIGO.NS": "Travel",
    "AWFIS.NS": "Real Estate", "CELLO.NS": "Consumer Durables", "RRKABEL.NS": "Consumer Durables",
    "HAPPYFORGE.NS": "Engineering", "INOXINDIA.NS": "Engineering", "AZAD.NS": "Engineering",
    "JYOTICNC.NS": "Engineering", "EPACK.NS": "Consumer Durables", "BLSE.NS": "IT",
    "VIBHOR.NS": "Metals", "JUNIPER.NS": "Hotels", "EXICOM.NS": "Power",
    "PLATINUM.NS": "Chemicals", "MUKKA.NS": "Food", "GOPAL.NS": "Food",
    "JGCHEM.NS": "Chemicals", "KRYSTAL.NS": "Services", "BHARTIHEXA.NS": "Telecom",
    "JNKINDIA.NS": "Engineering", "INDGIG.NS": "Healthcare", "TBZ.NS": "Retail",
    "SENCO.NS": "Retail", "PCJEWELLER.NS": "Retail", "THANGAMAYL.NS": "Retail",
    "ASTRAMICRO.NS": "Defence", "ZEN.NS": "Defence", "KPIGREEN.NS": "Power",
    "JUPITERIN.NS": "Engineering", "IEX.NS": "Exchange", "NLCINDIA.NS": "Power",

    # Batch 2 – New sector mappings
    "PGHL.NS": "FMCG", "SOMANYCERA.NS": "Consumer Durables", "ARVIND.NS": "Textiles",
    "KITEX.NS": "Textiles", "GOKEX.NS": "Textiles", "DOLLAR.NS": "Textiles",
    "SPANDANA.NS": "NBFC", "BALRAMCHIN.NS": "Sugar", "DHAMPUR.NS": "Sugar",
    "DWARIKESH.NS": "Sugar", "UGARSUGAR.NS": "Sugar",
    "FACT.NS": "Chemicals", "NFL.NS": "Chemicals", "MADRASFERT.NS": "Chemicals",
    "NOCIL.NS": "Chemicals", "VINATIORG.NS": "Chemicals", "TATACOFFEE.NS": "FMCG",
    "IGPL.NS": "Chemicals", "DCXINDIA.NS": "Defence", "IDEAFORGE.NS": "Defence",
    "STEL.NS": "Defence", "GANDHAR.NS": "Chemicals", "NEWGEN.NS": "IT",
    "SYRMA.NS": "Electronics", "CEINSYSTECH.NS": "IT", "AMBER.NS": "Consumer Durables",
    "ALLCARGO.NS": "Logistics", "MAHINDCIE.NS": "Auto Ancillary",
    "BLUEDART.NS": "Logistics", "CREDITACC.NS": "NBFC", "AAVAS.NS": "NBFC",
    "CEATLTD.NS": "Auto Ancillary", "BALAMINES.NS": "Chemicals",
    "CARBORUNIV.NS": "Engineering", "IIITM.NS": "IT", "SAKSOFT.NS": "IT",
    "BIRLASOFT.NS": "IT", "ZENSAR.NS": "IT", "DATAMATICS.NS": "IT",
    "SUBEXLTD.NS": "IT", "BECTORFOOD.NS": "FMCG", "PRATAAP.NS": "FMCG",
    "ACI.NS": "Infrastructure",
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
