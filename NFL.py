nfl = {}


nfl["sf"] = 0
nfl["nyg"] = 1/7
nfl["tb"] = 2/7
nfl["chi"] = 3/8
nfl["az"] = 3/7
nfl["wsh"] = 3/7
nfl["det"] = 3/7
nfl["dal"] = 4/7
nfl["atl"] = 4/7
nfl["car"] = 5/8
nfl["gb"] = 4/7
nfl["sea"] = 5/7
nfl["no"] = 5/7
nfl["stl"] = 5/7
nfl["min"] = 6/8
nfl["phi"] = 7/8

nfl["cle"] = 0
nfl["ind"] = 2/8
nfl["cin"] = 3/7
nfl["oak"] = 3/8
nfl["sd"] = 3/8
nfl["nyj"] = 3/8
nfl["bal"] = 4/8
nfl["hou"] = 3/7
nfl["den"] = 3/7
nfl["jax"] = 4/7
nfl["mia"] = 4/7
nfl["buf"] = 5/7
nfl["ten"] = 4/7
nfl["ne"] = 6/8
nfl["kc"] = 6/8
nfl["pit"] = 6/8

stat = {}
stat1 = {}
stat2 = {}
stat3 = {}
stat4 = {}
stat5 = {}
stat6 = {}
stat7 = {}
stat8 = {}
stat9 = {}
stat10 = {}
stat11 = {}
stat12 = {}
stat13 = {}
stat14 = {}
stat15 = {}
stat16 = {}

total = {0:stat,1:stat1,2:stat2,3:stat3,3:stat3,4:stat4,5:stat5,6:stat6,7:stat7,8:stat8,9:stat9,10:stat10,11:stat11,12:stat12,13:stat13,14:stat14,15:stat15,16:stat16}

stat["sf"] = 0
stat["cle"] = 0
stat["nyg"] = nfl["den"] /7
stat["tb"] = (nfl["chi"] + nfl["nyg"]) / 7
stat["ind"] = (nfl["cle"] + nfl["sf"])/8
stat["cin"] = (nfl["cle"] + nfl["buf"]+ nfl["ind"])/7
stat["oak"] = (nfl["ten"] + nfl["nyj"] + nfl["kc"])/8
stat["az"] = (nfl["tb"])/7
stat["chi"] = (nfl["pit"] + nfl["bal"] + nfl["car"]) / 8
stat["sd"] = (nfl["oak"] + nfl["nyg"] + nfl["den"])/8
stat["nyj"] = (nfl["mia"] + nfl["jax"])/8
stat["bal"] = (nfl["cin"] + nfl["oak"]+ nfl["mia"])/8
stat["hou"] = (nfl["cin"] + nfl["ten"])/7
stat["den"] = (nfl["sd"] + nfl["dal"] + nfl["oak"])/7
stat["wsh"] = (nfl["stl"] + nfl["oak"] + nfl["sf"])/7
stat["det"] = (nfl["min"] + nfl["az"] + nfl["nyg"])/7
stat["dal"] = (nfl["nyg"] + nfl["az"] + nfl["sf"]+ nfl["wsh"])/7
stat["atl"] = (nfl["chi"] + nfl["det"] + nfl["gb"]+nfl["nyj"])/7
stat["car"] = (nfl["buf"] + nfl["ne"] + nfl["det"]+nfl["tb"])/8
stat["gb"] = (nfl["sea"] + nfl["cle"] + nfl["chi"] + nfl["dal"])/7
stat["jax"] = (nfl["hou"] + nfl["bal"] + nfl["pit"] + nfl["ind"])/7
stat["sea"] = (nfl["ind"] + nfl["stl"] + nfl["nyg"]+nfl["hou"])/7
stat["no"] = (nfl["car"] + nfl["mia"] + nfl["det"] +nfl["gb"]+nfl["chi"])/7
stat["mia"] = (nfl["sd"] + nfl["ten"] + nfl["atl"] + nfl["nyj"])/7
stat["buf"] = (nfl["nyj"] + nfl["den"] + nfl["atl"] + nfl["tb"]+nfl["oak"])/7
stat["ten"] = (nfl["jax"] + nfl["sea"] + nfl["ind"])/7
stat["ne"] = (nfl["no"] + nfl["hou"] + nfl["tb"] +nfl["nyj"] + nfl["atl"]+nfl["sd"])/8
stat["kc"] = (nfl["ne"] + nfl["phi"] + nfl["sd"] +nfl["hou"] + nfl["wsh"]+nfl["den"])/8
stat["pit"] = (nfl["min"] + nfl["bal"] + nfl["ind"] +nfl["kc"] + nfl["cin"]+nfl["det"])/8
stat["stl"] = (nfl["ind"] + nfl["dal"] + nfl["jax"] +nfl["az"])/7
stat["min"] = (nfl["no"] + nfl["tb"] + nfl["chi"] +nfl["gb"] + nfl["bal"])/8
stat["phi"] = (nfl["wsh"] + nfl["nyg"] + nfl["sd"] +nfl["az"] + nfl["car"] + nfl["wsh"])/8

for i in range(16):
    total[i+1]["sf"] = 0
    total[i+1]["cle"] = 0
    total[i+1]["nyg"] = total[i]["den"] /7
    total[i+1]["tb"] = (total[i]["chi"] + total[i]["nyg"]) / 7
    total[i+1]["ind"] = (total[i]["cle"] + total[i]["sf"])/8
    total[i+1]["cin"] = (total[i]["cle"] + total[i]["buf"]+ total[i]["ind"])/7
    total[i+1]["oak"] = (total[i]["ten"] + total[i]["nyj"] + total[i]["kc"])/8
    total[i+1]["az"] = (total[i]["tb"])/7
    total[i+1]["chi"] = (total[i]["pit"] + total[i]["bal"] + total[i]["car"]) / 8
    total[i+1]["sd"] = (total[i]["oak"] + total[i]["nyg"] + total[i]["den"])/8
    total[i+1]["nyj"] = (total[i]["mia"] + total[i]["jax"])/8
    total[i+1]["bal"] = (total[i]["cin"] + total[i]["oak"]+ total[i]["mia"])/8
    total[i+1]["hou"] = (total[i]["cin"] + total[i]["ten"])/7
    total[i+1]["den"] = (total[i]["sd"] + total[i]["dal"] + total[i]["oak"])/7
    total[i+1]["wsh"] = (total[i]["stl"] + total[i]["oak"] + total[i]["sf"])/7
    total[i+1]["det"] = (total[i]["min"] + total[i]["az"] + total[i]["nyg"])/7
    total[i+1]["dal"] = (total[i]["nyg"] + total[i]["az"] + total[i]["sf"]+total[i]["wsh"])/7
    total[i+1]["atl"] = (total[i]["chi"] + total[i]["det"] + total[i]["gb"]+total[i]["nyj"])/7
    total[i+1]["car"] = (total[i]["buf"] + total[i]["ne"] + total[i]["det"]+total[i]["tb"])/8
    total[i+1]["gb"] = (total[i]["sea"] + total[i]["cle"] + total[i]["chi"] + total[i]["dal"])/7
    total[i+1]["jax"] = (total[i]["hou"] + total[i]["bal"] + total[i]["pit"] + total[i]["ind"])/7
    total[i+1]["sea"] = (total[i]["ind"] + total[i]["stl"] + total[i]["nyg"]+ total[i]["hou"])/7
    total[i+1]["no"] = (total[i]["car"] + total[i]["mia"] + total[i]["det"] +total[i]["gb"]+total[i]["chi"])/7
    total[i+1]["mia"] = (total[i]["sd"] + total[i]["ten"] + total[i]["atl"] + total[i]["nyj"])/7
    total[i+1]["buf"] = (total[i]["nyj"] + total[i]["den"] + total[i]["atl"] + total[i]["tb"]+ total[i]["oak"])/7
    total[i+1]["ten"] = (total[i]["jax"] + total[i]["sea"] + total[i]["ind"])/7
    total[i+1]["ne"] = (total[i]["no"] + total[i]["hou"] + total[i]["tb"] +total[i]["nyj"] + total[i]["atl"]+total[i]["sd"])/8
    total[i+1]["kc"] = (total[i]["ne"] + total[i]["phi"] + total[i]["sd"] +total[i]["hou"] + total[i]["wsh"]+total[i]["den"])/8
    total[i+1]["pit"] = (total[i]["min"] + total[i]["bal"] + total[i]["ind"] +total[i]["kc"] + total[i]["cin"]+total[i]["det"])/8
    total[i+1]["stl"] = (total[i]["ind"] + total[i]["dal"] + total[i]["jax"] +total[i]["az"])/7
    total[i+1]["min"] = (total[i]["no"] + total[i]["tb"] + total[i]["chi"] +total[i]["gb"] + total[i]["bal"])/8
    total[i+1]["phi"] = (total[i]["wsh"] + total[i]["nyg"] + total[i]["sd"] +total[i]["az"] + total[i]["car"] + total[i]["wsh"])/8


y = sorted(total[16].items(), key=lambda x:x[1])

for i in range(32):
    print(str(i+1) + ". "  + str(y[31-i][0]) + " - " + str(y[31-i][1]))


