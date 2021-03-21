from tkinter.scrolledtext import*
from tkinter.messagebox import*
from tkinter.filedialog import*
from tkinter.ttk import*
from tkinter import*
from re import*
from random import randint
from time import sleep,time
import errno
import contextlib
import ctypes
import threading
import os
strr=lambda x:f'"{x}"'if type(x)==str else str(x)
formatt=lambda x:x.replace('\n','\\n').replace('"','\\"')
#GUI部品作成ここから＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
fonts=('',12)
window=Tk()
window.title('V.ll式作問エディタβ11.2')
#問題総まとめ
問題総まとめ=Frame(window)
問題総まとめ.pack(anchor=NW)
テーマ=StringVar()
ライトボタン=Radiobutton(問題総まとめ,text='ライトモード',value='light',variable=テーマ,font=fonts)
ダークボタン=Radiobutton(問題総まとめ,text='ダークモード',value='dark',variable=テーマ,font=fonts)
テーマ.set('dark')
ライトボタン.pack(side=LEFT)
ダークボタン.pack(side=LEFT)
開く=Button(問題総まとめ,text='ファイルから読み込む',font=fonts)
開く.pack(side=LEFT)
#print(テーマ.get())
#問題管理
問題管理=Frame(window)
問題管理.pack(side=LEFT,anchor=NW)
問題ヘッダ=Frame(問題管理)
問題ヘッダ.pack()
問題ヘッダ1=Frame(問題ヘッダ)
問題ヘッダ1.pack(side=LEFT)
問題タイトル=Label(問題ヘッダ1,text='タイトル↓',font=fonts)
問題タイトル.pack(anchor=W)
タイトル=Entry(問題ヘッダ1,font=fonts)
タイトル.pack(fill=BOTH)
問題ヘッダ2=Frame(問題ヘッダ)
問題ヘッダ2.pack(side=LEFT)
得点タグ=Label(問題ヘッダ2,text='得点↓',font=fonts)
得点タグ.pack(anchor=W)
得点=Entry(問題ヘッダ2,font=fonts)
得点.pack(fill=BOTH)
問題ヘッダ3=Frame(問題ヘッダ)
問題ヘッダ3.pack(side=LEFT)
タグのタグ=Label(問題ヘッダ3,text='タグ↓(コンマ区切り,#不要)',font=fonts)
タグのタグ.pack(anchor=W)
タグ=Entry(問題ヘッダ3,font=fonts)
タグ.pack(anchor=W)
問題ラベル=Label(問題管理,text='問題文↓',font=fonts)
問題ラベル.pack(anchor=W)
問題文=ScrolledText(問題管理,width=60,height=20,font=fonts)
問題文.pack(fill=BOTH,expand=1)
変数司令=Label(問題管理,text='必要な変数(A:int,B:strのような形で)↓',font=fonts)
変数司令.pack(anchor=W)
必要変数=Entry(問題管理,font=fonts)
必要変数.pack(fill=BOTH,expand=1)
制約ラベル=Label(問題管理,text='満たすべき制約↓(python書式)',font=fonts)
制約ラベル.pack(anchor=W)
制約=Entry(問題管理,width=60,font=fonts)
制約.pack(fill=BOTH)
#テストケース管理
テストケース管理=Frame(window)
テストケース管理.pack(side=LEFT,anchor=N)
ケース=Frame(テストケース管理)
ケース.pack()
ケース縦1=Frame(ケース)
ケース縦1.pack(side=LEFT)
ケースラベル2=Label(ケース縦1,text='テストケース↓',font=fonts,justify='left')
ケースラベル2.pack(anchor=W)
テストケース入力部=ScrolledText(ケース縦1,font=fonts,width=10,height=5,wrap=NONE)
テストケース入力部.pack(anchor=W)
ケース縦2=Frame(ケース)
ケース縦2.pack(side=LEFT)
ケースラベル3=Label(ケース縦2,text='対応する文字列↓',font=fonts)
ケースラベル3.pack(anchor=W)
テストケース出力部=ScrolledText(ケース縦2,font=fonts,width=30,height=5,wrap=NONE)
テストケース出力部.pack(anchor=W)
#テストケース生成さん
ジェネレータ枠=Frame(テストケース管理)
ジェネレータ枠.pack()
生成ラベル=Label(ジェネレータ枠,text='テストケース生成コード↓',font=fonts)
生成ラベル.pack()
ジェネレータコード=ScrolledText(ジェネレータ枠,width=43,height=11,font=fonts)
ジェネレータコード.pack()
生成ボタン=Button(ジェネレータ枠,text='ランダムテストケースを1つ生成',font=fonts)
生成ボタン.pack(fill=BOTH)
#厚切り枠
jsonの枠=Frame(テストケース管理)
jsonの枠.pack()
json化ボタン=Button(jsonの枠,text='jsonに変換',font=fonts)
json化ボタン.pack(fill=BOTH)
jsonスペース=ScrolledText(jsonの枠,width=50,height=8,wrap=NONE)
jsonスペース.pack()
#想定解をつくる
想定解の枠=Frame(window)
想定解の枠.pack()
想定解タグ=Label(想定解の枠,text='想定解↓',font=fonts)
想定解タグ.pack(anchor=W)
想定解本文=ScrolledText(想定解の枠,font=fonts,width=43,height=26)
想定解本文.pack(fill=BOTH)
想定解から出力を求めるボタン=Button(想定解の枠,text='プログラムから出力を生成',font=fonts)
想定解から出力を求めるボタン.pack(fill=BOTH)
#GUI部品作成ここまで＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#クラス定義＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#↓https://qiita.com/Jacomb/items/92503b11aef68ec4748a から引用したコードです
class TimeoutException(IOError):
    errno = errno.EINTR
@contextlib.contextmanager
def time_limit_with_thread(timeout_secs):
    thread_id = ctypes.c_long(threading.get_ident())
    def raise_exception():
        modified_thread_state_nums = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(TimeoutException))
        if modified_thread_state_nums == 0:
            raise ValueError('Invalid thread id. thread_id:{}'.format(thread_id))
        elif modified_thread_state_nums > 1:
            # 通常このパスを通ることはないが、念のため保留中のExceptionをクリアしておく
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            raise SystemError('PyThreadState_SetAsyncExc failure.')

    timer = threading.Timer(timeout_secs, raise_exception)
    timer.setDaemon(True)
    timer.start()
    try:
        yield
    finally:
        timer.cancel()
        timer.join()
class Problem:
    "問題を管理するためのクラスです\njsonメソッドでdictにして出力とか考えてる。それをstrにするかもね?"
    def __init__(
        self,
        タイトル='累乗',
        得点=100,
        タグ="四則演算",
        問題文='A,Bが与えられる。\nAのB乗を求めよ。',
        必要変数='A:int,B:int',
        制約='1<=A and A<=10**3 and 1<=B and B<=10**3',
        テストケース="2,3\n3,2",
        出力="8\n9",
        想定解="A=B=1\nprint(A**B)",
        生成機="from random import randint\nA=randint(1,1000)\nB=randint(1,1000)"
        ):
        self.タイトル=タイトル
        self.得点=得点
        self.タグ=タグ
        self.問題文=問題文
        self.必要変数=必要変数
        self.制約=制約
        self.テストケース=テストケース
        self.出力=出力
        self.想定解=想定解
        self.生成機=生成機
    def 反映(self):
        self.タイトル=タイトル.get()
        self.得点=int(得点.get())
        self.タグ=タグ.get()
        self.問題文=問題文.get(0.0,'end -1c')
        self.必要変数=必要変数.get()
        self.制約=制約.get()
        self.テストケース=テストケース入力部.get(0.0,'end -1c')
        self.出力=テストケース出力部.get(0.0,'end -1c')
        self.想定解=想定解本文.get(0.0,'end -1c')
        self.生成機=ジェネレータコード.get(0.0,'end -1c')
    def output(self):
        変数ズ=[i[:i.index(':')]for i in self.必要変数.split(',')]
        cases=[eval(f'[{i}]')for i in self.テストケース.split('\n')]
        outputs=self.出力.split('\n')
        #print('"'+self.必要変数.replace(':','":"').replace(',','","').replace(' ','')+'"')
        text=f'''{{\n  "title":"{self.タイトル}",\n  "rating":{self.得点},\n  "tag":"{self.タグ}",\n  "restrict":"'''
        text+=formatt(self.制約)+'",\n  "question":"'+formatt(self.問題文)
        text+='",\n  "test_case":{\n    "variables":{\n'
        text+=',\n'.join(['      "'+i.replace(':','":"')+'"'for i in self.必要変数.split(',')])+'\n    },\n    "case":[\n'
        text+=',\n'.join(['      {\n        "inputs":{\n'+',\n'.join(['          "'+変数ズ[j]+'":'+strr(cases[i][j])for j in range(len(cases[i]))])+'\n        },\n        "output":"'+formatt(outputs[i])+'"\n      }'for i in range(len(outputs))])
        text+='\n    ]\n  },\n  "expected_answer":"'+formatt(self.想定解)+'",\n  "test_case_generator":'+strr(formatt(self.生成機))+'\n}'
        return text
#関数定義＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def 問題データを反映します(*e,data=Problem()):
    タイトル.delete(0,'end')
    タイトル.insert(0,data.タイトル)
    得点.delete(0,'end')
    得点.insert(0,data.得点)
    タグ.delete(0,'end')
    タグ.insert(0,data.タグ)
    問題文.delete(0.0,'end')
    問題文.insert(0.0,data.問題文)
    必要変数.delete(0,'end')
    必要変数.insert(0,data.必要変数)
    制約.delete(0,'end')
    制約.insert(0,data.制約)
    想定解本文.delete(0.0,'end')
    想定解本文.insert(0.0,data.想定解)
    テストケース入力部.delete(0.0,'end')
    テストケース入力部.insert(0.0,data.テストケース)
    テストケース出力部.delete(0.0,'end')
    テストケース出力部.insert(0.0,data.出力)
    ジェネレータコード.delete(0.0,'end')
    ジェネレータコード.insert(0.0,data.生成機)
def 新しい問題を作成します(*e):
    問題データを反映します(data=Problem())
    return
def てすと(testcase,code):
    #global ぐろぉばる
    #ぐろぉばる=""
    #print('caught:',testcase)
    text=code
    for i in testcase:text=text.replace(match(i+' ?= ?',text).group(),'',1)
    変数ズ=';'.join([i+'='+(str(testcase[i])if type(testcase[i])!=str else '"'+testcase[i].replace('"','\\"')+'"')for i in testcase])
    a={}
    変数名=''.join(map(lambda x:chr(randint(97,122)),range(500)))
    with time_limit_with_thread(2):
        try:
            exec(f'def print(*value,sep=" ",end="\\n",file="",flush=""):\n global {変数名}\n {変数名}+=sep.join(map(str,value))+end\n{変数名}="";'+変数ズ+';'+text,a,{})
            return formatt(a[変数名][:-1])
        except:
            raise TimeoutError('コード実行時間が長すぎます')
    window.update()
def テストケースから出力を得る(*e):
    テストケース出力部.delete(0.0,'end')
    try:
        テストケース出力部.insert(0.0,'\n'.join([
            てすと({k:eval('['+テストケース入力部.get(0.0,'end').split('\n')[l]+']')[j]for j,k in enumerate([i[:i.index(':')]
            for i in 必要変数.get().split(',')])},想定解本文.get(0.0,'end'))for l in range(テストケース入力部.get(0.0,'end').count('\n'))]))
    except Exception as e:
        テストケース出力部.insert(0.0,f'実行中にエラーが発生したよ(ざっくり)\n{e.__class__.__name__}:{e}')
        raise Exception from e
def いい感じマン(*e):
    try:
        global current_problem
        current_problem.反映()
        flag=not os.path.exists((current_problem.タイトル or'無題')+'.json')
        if not flag:flag=askyesno("上書き保存?", "指定されたタイトルのファイルはすでに存在します。上書きしますか?")
        if flag:
            jsonスペース.delete(0.0,'end')
            jsonスペース.insert(0.0,current_problem.output())
            with open((current_problem.タイトル or'無題')+'.json','w')as f:f.write(jsonスペース.get(0.0,'end -1c'))
    except Exception as e:
        jsonスペース.delete(0.0,'end')
        jsonスペース.insert(0.0,f'どこかは知らないけどエラーが起こったよ(ざっくり)\n{e.__class__.__name__}:{e}')
        raise Exception from e
def 色変えるマン(*e,t=window):
    #print(t)
    if t.children!={}:
        for i in t.children:色変えるマン(t=t.children[i])
    try:t['bg']=("#eeeeee"if type(t)not  in[Entry,ScrolledText] else"#ffffff")if テーマ.get()=='light'else("#333333"if type(t)in[Entry,ScrolledText] else"#444444");t['fg']="#000000"if テーマ.get()=='light'else"#eeeeee"
    except:pass
def 開いて反映する(*e):
    a=askopenfilename(filetypes=[("jsonファイル","*.json")],initialdir=os.path.abspath(os.path.dirname(__file__)))
    if a:
        with open(a)as f:b=eval(f.read())
        #print(厚切りジェイソン)
        global current_problem
        try:
            current_problem=Problem(
                b["title"],
                b["rating"],
                b["tag"],
                b["question"],
                ','.join([f'{i}:{b["test_case"]["variables"][i]}'for i in b["test_case"]["variables"]]),
                b["restrict"],
                '\n'.join([','.join([str(j)if type(j)!=str else '"'+j.replace('"','\\"')+'"' for j in i["inputs"].values()]) for i in b["test_case"]["case"]]),
                '\n'.join([str(i["output"]) for i in b["test_case"]["case"]]),
                ""if "expected_answer"not in b else b["expected_answer"],
                ""if "test_case_generator"not in b else b["test_case_generator"],
                )
            問題データを反映します(data=current_problem)
        except Exception as e:
            jsonスペース.delete(0.0,'end')
            jsonスペース.insert(0.0,f'読み込み時にエラーが起こったよ(ざっくり)\n{e.__class__.__name__}:{e}')
            raise Exception from e
def テストケース生成er(*e):
    a={}
    with time_limit_with_thread(2):
        try:exec(ジェネレータコード.get(0.0,'end -1c'),{},a)
        except TimeoutException as e:
            jsonスペース.delete(0.0,'end')
            jsonスペース.insert(0.0,f'テストケース生成中にエラーが起こったよ(ざっくり)\n{e.__class__.__name__}:ソースコード実行時間が長すぎます')
            raise Exception from e
        except Exception as e:
            jsonスペース.delete(0.0,'end')
            jsonスペース.insert(0.0,f'テストケース生成中にエラーが起こったよ(ざっくり)\n{e.__class__.__name__}:{e}')
            raise Exception from e
    #print(a)
    if False not in[i[:i.index(':')] in a for i in 必要変数.get().split(',')]:
        print([a[i[:i.index(':')]]for i in 必要変数.get().split(',')])
        テストケース入力部.insert('end','\n'+','.join([strr(a[i[:i.index(':')]])for i in 必要変数.get().split(',')]))
    else:
        jsonスペース.delete(0.0,'end')
        jsonスペース.insert(0.0,'変数の定義がきちんと行われていません\n定義された変数は'+str(list(a)))
#色変えるマン()
#print(type(jsonスペース))
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
想定解から出力を求めるボタン["command"]=テストケースから出力を得る
json化ボタン["command"]=いい感じマン
ライトボタン["command"]=ダークボタン["command"]=色変えるマン
開く["command"]=開いて反映する
生成ボタン["command"]=テストケース生成er
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
current_problem=Problem()
問題データを反映します()
色変えるマン()
#print(current_problem.output())
#新しい問題を作成します()
#問題データを反映します()
#print(Problem().output())
#print(てすと({"A":3,"B":2},Problem().想定解),{k:Problem().テストケース.split('\n')[0].split(',')[j] for j,k in enumerate([i[:i.index(':')]for i in Problem().必要変数.split(',')])})
#テストケースから出力を得る()
window.update()
size=list(map(int,window.winfo_geometry().split('+')[0].split('x')))
window.geometry(f'{size[0]+1}x{size[1]+1}')
window.update()
window.geometry(f'{size[0]}x{size[1]}')
window.resizable(width=0,height=0)
window.mainloop()