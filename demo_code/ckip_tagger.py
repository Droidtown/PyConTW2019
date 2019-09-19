#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import os

from ckiptagger import data_utils, construct_dictionary, WS, POS, NER

startTime = time.time()
G_modelPath = "{}/data".format(os.path.dirname(os.path.abspath(__file__)))
ws = WS(G_modelPath)
pos = POS(G_modelPath)
ner = NER(G_modelPath)

print("\n{} CKIPtagger 模型載入完成時間: {} 秒 {}".format('='*4, round(time.time()-startTime, 4), '='*4))

executeTime = time.time()
sentenceLIST = ["你的模型超胖。"]
wordLIST = ws(sentenceLIST)
posLIST = pos(wordLIST)
entityLIST = ner(wordLIST, posLIST)

segLIST = []
segposLIST = []
for i, sLIST in enumerate(wordLIST):
    tempLIST = []
    for j, word in enumerate(sLIST):
        tempLIST.append("{}({})".format(word, posLIST[i][j]))
    segLIST.append("/".join(sLIST))
    segposLIST.append(" ".join(tempLIST))

print("\nSegmentation ===>\n", segLIST)
print("POS ===>\n", segposLIST)
print("Entity ===>\n", entityLIST)

print("\n{} 斷詞執行時間: {} 秒 {}".format('+'*11, round(time.time()-executeTime, 4), '+'*11))
print("\n{} 總執行時間: {} 秒 {}".format('='*12, round(time.time()-startTime, 4), '='*12))

