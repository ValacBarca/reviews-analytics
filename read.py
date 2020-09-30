date = []
count = 0
with open ("reviews.txt", "r") as f:
	for line in f:
		date.append(line)
		count += 1
		if count % 1000 == 0:
		  print(len(date))
print("檔案讀取完了,共有", len(date), "筆資料。")

sum_len = 0
for d in date:
	sum_len = sum_len + len(d)
print("留言平均長度為",sum_len/ len(date))

#篩選出少於一百字的筆數
new = []
for d in date:
	if  len(d) < 100:
		new.append(d)
print("一共有",len(new),"留言長度小於100")

#篩選含有good的評論
good = [] 
for d in new:
	if "good" in d:
		good.append(d)
print("一共有",len(good),"則留言提到good")		


