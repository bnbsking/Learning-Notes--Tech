### preprocess.py
+ For yoloFloat data format only
+ Distil intersected data
+ Image shape check, class check, out-of-boundary check
+ Generate cleaned data
+ Generate data format for map.py and confusion matrix.py

### map.py
+ Compute mAP from specified format
+ Single image mode and Total images mode

### prt_ranking.ipynb
+ Plot PR-curve, P-curve, R-curve and compute best thershold from output of map.py
+ Execute map.py image-by-image. Rank the worst detected image