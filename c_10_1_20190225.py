# challange 10 -1

"""
word.csv      単語リスト

word_pool_l[]: 候補単語群のリスト (cvsから作成)
word: 出題単語 (string)
word_l: 出題単語 (list)
wrong: 失敗した回数
correct: 正解した回数
stages[]: Hangmanの絵文字リスト
disp_w: _ で隠した単語　(正解時、キャラクタ)
disp_w_l: disp_w のリスト、キャラクタ置き換え用


module (* 組込み):
    csvtolist: csv file からリストに変換
    random *: リストからランダムに単語を抽出
    hangman: Hangman 戻り値にHangman絵文字

"""

import random

import sys
sys.path.append ("/Users/kamezou/Docs/Python_working/module_made")
import csvtolist
import hangman

#word_l = []
word_pool_l = csvtolist.csv2list0 ("word.csv") #list宣言しなくても、リストになってる
word = random.choice(word_pool_l) # choose test word
word_l = list (word) # 出題単語をListにする、あとで使えるようにする

stages = []
stages = hangman.hmstrg()


wrong = 0
correct = 0
print ("word = ", word)
length = len (word)
disp_w =  (" ").join ("_" * length)
disp_w_l = list (disp_w)

#game start
print ("\nHangman game スタート")
while wrong < len (stages)+1:
    guess = input ("アルファベット一文字を予測してねー  :")
    if guess not in word:
        print ("\n".join(stages [0:wrong])) #要素を1行づつ表示
        wrong += 1
        if wrong >= len (stages):
            gameover = "あんたの　負けー！"
    else:
        ind = word_l.index (guess) #
        word_l [ind] = "$"
        disp_w_l [ind * 2] = guess
        disp_w = "".join (disp_w_l)
        print (disp_w)
        if "_" not in (disp_w):
            gameover = "まいりました！"
            break

print ("おしまい, \"こたえは", word, "\": ", gameover)

