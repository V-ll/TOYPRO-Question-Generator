from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askyesno
from tkinter.filedialog import askopenfilename
from tkinter import Tk,Frame,Entry,LEFT,RIGHT,BOTTOM,Radiobutton,Label,Text,Button,NW,W,StringVar,BOTH,Scrollbar,HORIZONTAL,N,NONE
from re import search
from random import randint
from time import sleep,time
import traceback,errno,contextlib,ctypes,threading,os,json
strr=lambda x:f'"{x}"'if type(x)==str else str(x)
formatt=lambda x:x.replace('\n','\\n').replace('"','\\"')
#GUI部品作成ここから＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
if True:#折り畳めるようにインデントした。
    fonts=('',12)
    window=Tk()
    window.title('V.ll式作問エディタβ18.8')
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
    名前ラベル=Label(問題総まとめ,text="アカウントのID→",font=fonts)
    名前ラベル.pack(side=LEFT)
    名前=Entry(問題総まとめ,font=fonts)
    名前.pack()
    #print(テーマ.get())
    問題行1=Frame(window)
    問題行1.pack()
    #問題管理
    問題管理=Frame(問題行1)
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
    制約xすくろぉる=Scrollbar(問題管理,orient=HORIZONTAL,command=制約.xview)
    制約xすくろぉる.pack(fill='x')
    制約["xscrollcommand"]=制約xすくろぉる.set

    #想定解をつくる
    想定解の枠=Frame(問題行1)
    想定解の枠.pack(side=LEFT)
    想定解タグ=Label(想定解の枠,text='想定解↓',font=fonts)
    想定解タグ.pack(anchor=W)
    想定解本文=ScrolledText(想定解の枠,font=fonts,width=43,height=27)
    想定解本文.pack(fill=BOTH)

    #解説を書いてもらいます
    解説枠=Frame(問題行1)
    解説枠.pack(side=LEFT)
    解説タグ=Label(解説枠,font=fonts,text="解説文↓")
    解説タグ.pack(anchor=W)
    解説文=ScrolledText(解説枠,font=fonts,width=43,height=26)
    解説文.pack(fill=BOTH)
    解説文横=Scrollbar(解説枠,orient=HORIZONTAL,command=解説文.xview)
    解説文横.pack(fill='x')
    解説文["xscrollcommand"]=解説文横.set

    問題行2=Frame(window)
    問題行2.pack(anchor=W)
    #テストケース管理
    テストケース管理=Frame(問題行2)
    テストケース管理.pack(side=LEFT,anchor=N)
    ケース=Frame(テストケース管理)
    ケース.pack()
    ケース縦1=Frame(ケース)
    ケース縦1.pack(side=LEFT)
    ケースラベル2=Label(ケース縦1,text='ランダムケース↓',font=fonts,justify='left')
    ケースラベル2.pack(anchor=W)
    テストケース入力部=ScrolledText(ケース縦1,font=fonts,width=30,height=10,wrap=NONE)
    テストケース入力部.pack(anchor=W)
    テスト入力横=Scrollbar(ケース縦1,orient=HORIZONTAL,command=テストケース入力部.xview)
    テスト入力横.pack(fill="x")
    ケースラベル4=Label(ケース縦1,text='コーナーケース↓',font=fonts,justify='left')
    ケースラベル4.pack(anchor=W)
    コーナーケース入力部=ScrolledText(ケース縦1,font=fonts,width=30,height=10,wrap=NONE)
    コーナーケース入力部.pack(anchor=W)
    コーナー入力横=Scrollbar(ケース縦1,orient=HORIZONTAL,command=コーナーケース入力部.xview)
    コーナー入力横.pack(fill="x")
    コーナーケース入力部["xscrollcommand"]=コーナー入力横.set
    ケース縦2=Frame(ケース)
    ケース縦2.pack(side=LEFT)
    ケースラベル3=Label(ケース縦2,text='対応する文字列↓',font=fonts)
    ケースラベル3.pack(anchor=W)
    テストケース出力部=ScrolledText(ケース縦2,font=fonts,width=30,height=10,wrap=NONE)
    テストケース出力部.pack(anchor=W)
    テスト出力横=Scrollbar(ケース縦2,orient=HORIZONTAL,command=テストケース出力部.xview)
    テスト出力横.pack(fill="x")
    テストケース出力部["xscrollcommand"]=テスト出力横.set
    ケースラベル5=Label(ケース縦2,text='対応する文字列↓',font=fonts)
    ケースラベル5.pack(anchor=W)
    コーナーケース出力部=ScrolledText(ケース縦2,font=fonts,width=30,height=10,wrap=NONE)
    コーナーケース出力部.pack(anchor=W)
    コーナー出力横=Scrollbar(ケース縦2,orient=HORIZONTAL,command=コーナーケース出力部.xview)
    コーナー出力横.pack(fill="x")
    コーナーケース出力部["xscrollcommand"]=コーナー出力横.set
    #テストケース生成さん
    ジェネレータ枠=Frame(ケース)
    ジェネレータ枠.pack()
    生成ラベル=Label(ジェネレータ枠,text='ランダムケース生成コード↓',font=fonts)
    生成ラベル.pack()
    ジェネレータコード=ScrolledText(ジェネレータ枠,width=43,height=23,font=fonts)
    ジェネレータコード.pack()
    #厚切り枠
    jsonの枠=Frame(問題行2)
    jsonの枠.pack(side=LEFT)
    生成枠=Frame(jsonの枠)
    生成枠.pack(fill=BOTH)
    生成タグ=Label(生成枠,font=fonts,text="ケース生成個数→")
    生成タグ.pack(side=LEFT)
    生成個数=Entry(生成枠,font=fonts,width=4)
    生成個数.pack(side=LEFT)
    生成個数.insert(0,'1')
    生成ボタン=Button(生成枠,text='ランダムケースを生成',font=fonts)
    生成ボタン.pack(fill=BOTH)
    生成枠2=Frame(jsonの枠)
    生成枠2.pack(fill=BOTH)
    反映タグ=Label(生成枠2,font=fonts,text="入出力例反映個数→")
    反映タグ.pack(side=LEFT)
    反映個数=Entry(生成枠2,font=fonts,width=4)
    反映個数.pack(side=LEFT)
    反映個数.insert(0,'1')
    色々反映ボタン=Button(生成枠2,text="制約など反映",font=fonts)
    色々反映ボタン.pack(fill=BOTH)
    生成枠3=Frame(jsonの枠)
    生成枠3.pack(fill=BOTH)
    想定解から出力を求めるボタン=Button(生成枠3,text='プログラムから出力を生成',font=fonts)
    想定解から出力を求めるボタン.pack(side=LEFT,fill=BOTH)
    json化ボタン=Button(生成枠3,text='jsonに変換',font=fonts)
    json化ボタン.pack(fill=BOTH)
    jsonスペース枠=Frame(jsonの枠)
    jsonスペース枠.pack()
    jsonタグ=Label(jsonスペース枠,text='jsonの出力↓',font=fonts)
    jsonタグ.pack(anchor=W)
    jsonスペース=ScrolledText(jsonスペース枠,width=49,height=19,wrap=NONE)
    jsonスペース.pack()
    jsonxすくろぉる=Scrollbar(jsonスペース枠,orient=HORIZONTAL,command=jsonスペース.xview)
    jsonxすくろぉる.pack(fill='x')
    jsonスペース["xscrollcommand"]=jsonxすくろぉる.set
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
        名前="guest",
        問題文='A,Bが与えられる。\nAのB乗を求めよ。',
        必要変数='A:int,B:int',
        制約='1<=A and A<=10**3 and 1<=B and B<=10**3',
        テストケース="2,3\n3,2",
        出力="8\n9",
        コーナー入力="1,1",
        コーナー出力="1",
        想定解="A=B=1\nprint(A**B)",
        生成機="from random import randint\nA=randint(1,1000)\nB=randint(1,1000)",
        解説="AのB乗はA**Bです。\nそれをprintするだけ!"
        ):
        for i in['タイトル','得点','タグ','名前','問題文','必要変数','制約','テストケース','出力','コーナー入力','コーナー出力','想定解','生成機','解説']:exec(f'self.{i}={i}')
    def 反映(self):
        self.タイトル=タイトル.get()
        if not 得点.get().isdecimal():
            raise ValueError('得点が整数ではありません:'+strr(得点.get()))
        self.得点=int(得点.get())
        self.タグ=タグ.get()
        self.名前=名前.get()
        self.問題文=問題文.get(0.0,'end -1c')
        self.必要変数=必要変数.get()
        self.制約=制約.get()
        self.テストケース=テストケース入力部.get(0.0,'end -1c')
        self.出力=テストケース出力部.get(0.0,'end -1c')
        self.コーナー入力=コーナーケース入力部.get(0.0,'end-1c')
        self.コーナー出力=コーナーケース出力部.get(0.0,'end-1c')
        self.想定解=想定解本文.get(0.0,'end -1c')
        self.生成機=ジェネレータコード.get(0.0,'end -1c')
        self.解説=解説文.get(0.0,'end -1c')
    def output(self):
        変数ズ=[]if self.必要変数==""else[i[:i.index(':')]for i in self.必要変数.split(',')]
        return json.dumps(
            {'title':self.タイトル,'rating':self.得点,'tag':self.タグ,'restrict':self.制約,'question':self.問題文,
                'test_case':{
                    'variables':eval('{'+','.join(['"'+i.replace(':','":"')+'"'for i in self.必要変数.split(',')])+'}'),
                    'cases':シン支援('ランダム',self.テストケース,self.出力,変数ズ),'corner_cases':シン支援('コーナー',self.コーナー入力,self.コーナー出力,変数ズ)},
                'expected_answer':self.想定解,'test_case_generator':self.生成機,'comment':self.解説},indent=2,ensure_ascii=False)
    def __eq__(self,other):
        if type(other)!=self.__class__:return False
        for i in [j for j in dir(other)if j[0]!='_' and j not in['反映','output']]:
            if eval(f'self.{i}!=other.{i}'):return False
        return True
    def __ne__(self,other):return not(self==other)
class ErrorMessage:
    def __init__(self,text):self.text=text
    def __enter__(self):pass
    def __exit__(self,*args):
        if args[0]is not None:
            a=traceback.format_exc()
            while search('File .*?, ',a):a=a.replace(search('File .*?, ',a).group(),'')
            jsonスペース.delete(0.0,'end')
            jsonスペース.insert(0.0,self.text+f'({args[0].__name__})\n\n{str(args[1])or"(エラーメッセージなし)"}\n\n{a}')
#関数定義＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def シン支援(message,inputs,outputs,変数ズ):
    if inputs=="":return[]
    else:
        cases=[eval(f'[{i}]')for i in inputs.split('\n')]
        if set(map(len,cases))!={len(変数ズ),}:
            text=[f'テストケース{i+1}'for i in range(len(cases))if len(cases[i])!=len(変数ズ)]
            raise ValueError(message+'ケースの中に、入力の数が必要な変数の数と\n一致しないものがあります\n'+','.join(text))
        outputs=outputs.split('\n')
        if len(cases)!=len(outputs):
            raise ValueError(message+'ケースの入力と出力の数が一致しません。\n｢プログラムから出力を生成｣ボタンで\n改善できる場合があります。')
        return [{'inputs':{変数ズ[j]:cases[i][j]for j in range(len(cases[i]))},'output':outputs[i]}for i in range(len(outputs))]
def 二つの配列ドッキング(a,b):
    if len(a)!=len(b):raise ValueError(f'次の二つは要素数が等しくありません\nその1: {a}\nその2: {b}')
    for i in range(len(a)):
        yield (a[i],b[i])
def 問題データを反映します(*e,data=Problem()):
    for i in['タイトル','得点','タグ','名前','必要変数','制約']:exec(f'{i}.delete(0,"end");{i}.insert(0,data.{i})')
    for i in[[問題文,data.問題文],[想定解本文,data.想定解],[テストケース入力部,data.テストケース],[テストケース出力部,data.出力],[ジェネレータコード,data.生成機],[解説文,data.解説],[コーナーケース入力部,data.コーナー入力],[コーナーケース出力部,data.コーナー出力]]:i[0].delete(0.0,'end');i[0].insert(0.0,i[1])
def 新しい問題を作成します(*e):
    問題データを反映します(data=Problem())
    return
def てすと(testcase,code):
    #global ぐろぉばる
    #ぐろぉばる=""
    #print('caught:',testcase)
    text=code
    for i in testcase:text=text.replace(search(i+' ?= ?',text).group(),'',1)
    変数ズ=';'.join([i+'='+strr(testcase[i])for i in testcase])
    a={}
    変数名=''.join(map(lambda x:chr(randint(97,122)),range(500)))
    with time_limit_with_thread(2):
        try:
            exec(f'def print(*value,sep=" ",end="\\n",file="",flush=""):\n global {変数名}\n {変数名}+=sep.join(map(str,value))+end\n{変数名}="";'+変数ズ+';'+text,a)
            return formatt(a[変数名][:-1])
        except TimeoutException:
            raise TimeoutError('コード実行時間が長すぎます')
        except Exception as e:
            raise e
def 必要変数の配列():
    a=[]
    for i in 必要変数.get().split(','):
        if i=='':raise ValueError(f'{len(a)+1}番目の必要な変数が定義されていません')
        if ':'not in i:raise ValueError(f'{len(a)+1}番目の必要な変数の型が定義されていません\nA:intのようにコロンの後に型を指定してください。\n対応するエラーの部分-> '+i)
        a+=[i[:i.index(':')]]
        if a[-1]=='':raise ValueError(f'{len(a)}番目の必要な変数の名前が定義されていません')
    return a
def テストケースから出力を得る(*e):
    jsonスペース.delete(0.0,'end')
    テストケース実行支援('ランダム',テストケース入力部,テストケース出力部)
    jsonスペース.insert('end','\n')
    テストケース実行支援('コーナー',コーナーケース入力部,コーナーケース出力部)
def テストケース実行支援(name,inputs,outputs):
    outputs.delete(0.0,'end')
    jsonスペース.insert('end',f'{name}ケースを出力します...')
    if inputs.get(0.0,'end -1c'):
        t=time()
        変数の個数=len(必要変数.get().split(','))
        for m,l in enumerate(inputs.get(0.0,'end -1c').split('\n')):
            with ErrorMessage(f'{name}ケースその{m+1}を実行中に\nエラーが発生したよ'):
                outputs.insert('end','\n'*(m>0)+てすと({i:j for i,j in 二つの配列ドッキング(必要変数の配列(),eval(f'[{l}]'))},想定解本文.get(0.0,'end')))
            if time()-t>0.1:
                window.update()
                t=time()
    jsonスペース.insert('end','出力完了')
def いい感じマン(*e):
    with ErrorMessage('保存時にエラーが起こったよ'):
        必要変数の配列()
        global current_problem
        current_problem.反映()
        flag=not os.path.exists((current_problem.タイトル or'無題')+'.json')
        if not flag:flag=askyesno("上書き保存?", "指定されたタイトルのファイルはすでに存在します。上書きしますか?")
        if flag:
            jsonスペース.delete(0.0,'end')
            jsonスペース.insert(0.0,current_problem.output())
            for i in['ANSI','SJIS','UTF-8','UTF-16']:
                try:
                    with open((current_problem.タイトル or'無題')+'.json','w',-1,i)as f:f.write(jsonスペース.get(0.0,'end -1c'));flag=0;break
                except:pass
            if flag:raise IOError('保存に失敗しました')
            global prev
            prev.反映()
def 色変えるマン(*e,t=window):
    #print(t)
    if t.children!={}:
        for i in t.children:色変えるマン(t=t.children[i])
    try:t['bg']=("#eeeeee"if type(t)not  in[Entry,ScrolledText] else"#ffffff")if テーマ.get()=='light'else("#333333"if type(t)in[Entry,ScrolledText] else"#444444");t['fg']="#000000"if テーマ.get()=='light'else"#eeeeee"
    except:pass
def 開いて反映する(*e):
    a=askopenfilename(filetypes=[("jsonファイル","*.json")],initialdir=os.path.abspath(os.path.dirname(__file__)))
    if a:
        #print(厚切りジェイソン)
        global current_problem,prev
        with ErrorMessage('読み込み時にエラーが起こったよ'):
            jsonスペース.delete(0.0,'end')
            jsonスペース.insert(0.0,'ファイル読込中...')
            frag=1
            for i in ['SJIS','UTF-16','UTF-8']:
                try:
                    jsonスペース.insert('end','\n'+i+'で読み込みます...')
                    with open(a,'r',-1,i)as f:b=eval(f.read());frag=0;jsonスペース.insert('end','成功');break
                except:jsonスペース.insert('end','失敗')
            if frag:raise IOError('ファイルの読み込みに失敗しました')
            current_problem=Problem(
                b["title"],
                b["rating"],
                b["tag"],
                ""if"user_id"not in b else b["user_id"],
                b["question"],
                ','.join([f'{i}:{b["test_case"]["variables"][i]}'for i in b["test_case"]["variables"]]),
                b["restrict"],
                '\n'.join([','.join([strr(j)for j in i["inputs"].values()]) for i in b["test_case"]["case"+'s'*("cases"in b["test_case"])]]),
                '\n'.join([formatt(i["output"])for i in b["test_case"]["case"+'s'*("cases"in b["test_case"])]]),
                ""if"corner_cases"not in b["test_case"]else'\n'.join([','.join([strr(j)for j in i["inputs"].values()]) for i in b["test_case"]["corner_cases"]]),
                ""if"corner_cases"not in b["test_case"]else'\n'.join([formatt(i["output"])for i in b["test_case"]["corner_cases"]]),
                ""if "expected_answer"not in b else b["expected_answer"],
                ""if "test_case_generator"not in b else b["test_case_generator"],
                ""if"comment"not in b else b["comment"]
                )
            問題データを反映します(data=current_problem)
            prev.反映()
def テストケース求めるer():
    with time_limit_with_thread(2):
        try:
            a={}
            exec(ジェネレータコード.get(0.0,'end -1c'),{},a)
            if False not in[i in a for i in 必要変数の配列()]:
                #print([a[i[:i.index(':')]]for i in 必要変数.get().split(',')])
                テストケース入力部.insert('end','\n'+','.join([strr(a[i[:i.index(':')]])for i in 必要変数.get().split(',')]))
            else:raise ValueError('変数の定義がきちんと行われていません\n定義されていない変数は'+str([i[:i.index(':')]for i in 必要変数.get().split(',') if i[:i.index(':')] not in a]))
        except TimeoutException as e:raise TimeoutError('ソースコード実行時間が長すぎます')
        except Exception as e:raise e
def テストケース生成er(*e):
    jsonスペース.delete(0.0,'end')
    jsonスペース.insert(0.0,'作成します...')
    with ErrorMessage('テストケース生成中にエラーが起こったよ'):
        if not 生成個数.get().isdecimal():raise ValueError('生成回数が整数ではありません')
        t=time()
        for i in range(int(生成個数.get())):
            テストケース求めるer()
            if time()-t>0.1:
                window.update()
                t=time()
        jsonスペース.insert('end','作成完了')
    #print(a)
def 変数と入出力例反映er(*e):#コンマがあるとエラーになるんだったよね。入力例と出力例どっちも改造する必要がありそうだ。
    with ErrorMessage('文章生成中にエラーが起こったよ'):
        if not 反映個数.get().isdecimal():raise ValueError('反映個数が整数ではありません')
        if int(反映個数.get())>テストケース入力部.get(0.0,'end').count('\n'):raise ValueError('反映個数がランダムケース数の個数を超えています')
        if テストケース入力部.get(0.0,'end').count('\n')!=テストケース出力部.get(0.0,'end').count('\n'):raise ValueError('ランダムケースの入力と出力の数が一致しません。\n｢プログラムから出力を生成｣ボタンで\n改善できる場合があります。')
        text='\n\n\n### 制約\n```python\n'+制約.get()+"\n```\n### 必要な変数\n```python\n"+'\n'.join([i[:i.index(':')]for i in 必要変数.get().split(',')])+'\n```'
        for i in range(1,int(反映個数.get())+1):
            text+=f'\n### 入力例{i}\n```python\n'
            text+='\n'.join([f'{k} = {strr(j)}'for k,j in 二つの配列ドッキング(必要変数の配列(),eval('['+テストケース入力部.get(f"{i}.0",f"{i+1}.0")+']'))])+f'\n```\n### 出力例{i}\n```\n'
            text+=テストケース出力部.get(f"{i}.0",f"{i+1}.0").replace('\\n','\n')+'```'
        問題文.insert('end',text)
def 保存するか確認するer(*e):
    global current_problem,prev
    with ErrorMessage('終了時にエラーが起こったよ'):
        current_problem.反映()
    if prev!=current_problem:
        jsonスペース.delete(0.0,'end')
        jsonスペース.insert(0.0,'終了します...')
        if askyesno("保存?", "このファイルは変更されています。終了前に保存しますか?"):
            いい感じマン()
            if prev==current_problem:window.destroy()
        else:window.destroy()
    else:window.destroy()
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
想定解から出力を求めるボタン["command"]=テストケースから出力を得る
json化ボタン["command"]=いい感じマン
ライトボタン["command"]=ダークボタン["command"]=色変えるマン
開く["command"]=開いて反映する
生成ボタン["command"]=テストケース生成er
色々反映ボタン["command"]=変数と入出力例反映er
window.bind('<Control-s>',いい感じマン)
window.protocol('WM_DELETE_WINDOW',保存するか確認するer)
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
current_problem=Problem()
prev=Problem()
問題データを反映します()
色変えるマン()
#window.update()
window.resizable(width=0,height=0)
window.mainloop()