class Video{
  String title;
  int time;
  bool val18;
  Video(String title, int time, bool val18){
    this.title = title;
    this.time = time;
    this.val18 = val18;
  }
  void printStatus(){
    print('title=${this.title}');
    print('time=${this.time}');
    print('val18=${this.val18}');
  }
}

class Mp4 extends Video {
  Mp4(String title, int time, bool val18):super(title, time, val18);
}

void main() {
  var a=10, b=3, c=3.0;
  var d="1.2", e=true;
  print(a); print(c); print('');
  print(a is int); print(c is double); print(d is String); print(e is bool);
    print('');
  print(a+c); print(a-c); print(a*c); print(a/c); print(a%c); print('');
  print(a<<2); print(a>>1); print(a&a); print(a|a); print(~a); print(a^a); print('');
  print(a>c); print(a==c); print(a!=c); print('');
  print(e&true); print(e|true); print(e&&true); print(e||false); print('');
  print(d); print(d[0]); print(d.length); print(d+d*2); print('');
  
  a = a+1; print(a); print('');
  dynamic f=10; f = '10'; print(f); print('');
  
  if(a==11){ print("a is ten"); }
  if(a<0){print('a is negative;\n');}
  else if(a==0){print('a is zero\n');}
  else{print('a is positive\n');}
  
  for(int i=0; i<5; i++){
    print('hello ${i + 1}');
  }
  
  int i=0;
  while(i<5){
    print(i);
    if(i==2){break;}
    i+=1;
  }
  
  var L = [-1,1.0,'1.0',true];
  print(L);
  L.add(7);
  print(L);
  L.removeLast();
  print(L);
  print(L.sublist(1,2));
  L.shuffle();
  print(L);
  L.reversed.toList();
  print(L);
  //L.sort();
  //print(L);
  print(L.indexOf('1.0'));
  print(L.length); print('');
  for(int i=0; i<L.length; i++){print(L[i]);}
  for(var num in L){print(num);} print('');
  
  var M = {'apple':30, 'banana':15, 'guava':20};
  print(M);
  print(M['apple']);
  M['mango']=100;
  print(M);
  M.remove('apple');
  print(M);
  print('${M.length}\n');
  
  int sumf(int x, int y){
    return x+y;
  }
  print(sumf(3,5));
  
  int minusf(int x, int y)=>x-y;
  print(minusf(3,5));
  
  try{print(1/0);}
  catch(e){print(e);}
  print('');
  
  Video ti = new Video('Attack', 100, true);
  ti.printStatus();
  print(ti.title);print('');

  Mp4 m = new Mp4('Attack', 100, true);
  m.printStatus();
  
  Future<void> introduction(){
    return Future.delayed(Duration(seconds:2), ()=>print("--Dart tutorial--") );
  }
  print("Before introduction");
  introduction();
  print("After introduction");
  
  //dict function
  void main() => print(birthday(name:'John',day:22));
  birthday({String name='Amy', int month, int day}) => "${name}'s birthday is $month/$day."
    
  //final: can not change. can be variable
  //const: can not change. can not be variable
  //e.g. int a=5; final b=a; //(O)
  //e.g. int a=5; final b=a; //(X) 
}
