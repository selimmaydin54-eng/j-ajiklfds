meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys(1):
    print(meme_dict.keys(1))
if word in meme_dict.keys(2):
    print(meme_dict.keys(2))    
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("Böyle bir kelime bulunamadı.")
    # Kelime eşleşmiyorsa ne yapmalıyız?
