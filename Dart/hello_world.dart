/*
import 'package:flutter/material.dart';
void main() => runApp(Center(
  child: Text('Hello Flutter',textDirection:TextDirection.ltr)
));
*/

import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {                  // root application.
  @override                                            // inherit and rewrite
  Widget build(BuildContext context) => MaterialApp(title:'Flutter Demo', theme:ThemeData(primarySwatch:Colors.green), 
    home:MyHomePage(title:'Flutter Demo Home Page'));  // App title v.s. GUI title // note console command
}

class MyHomePage extends StatefulWidget {              // home page (varied)
  MyHomePage({Key key, this.title}):super(key:key);    // init object with key and title, then call parents constructor with key
  final String title;                                  // variable assignable constant
  @override
  _MyHomePageState createState() => _MyHomePageState();// varied as state changes
}

class _MyHomePageState extends State<MyHomePage> {     // container<element type> //  e.g. vector<int>
  int _counter = 10;
  void _incrementCounter() {
    setState( () { _counter++; } );  // This call tells the Flutter framework that something has changed in this State
  }
  @override
  Widget build(BuildContext context) { // This method is rerun every time setState is called (_incrementCounter method) above.
    return Scaffold(
      appBar:AppBar(title:Text(widget.title)),
      body:Center(
        child:Column(                                 // or Row
	  mainAxisAlignment:MainAxisAlignment.center, // start, end, center, space between, space evently 
          children:<Widget>[
            Text('You have pushed the button this many times:'),
	    Text('$_counter',style:Theme.of(context).textTheme.headline4)
	  ],
        ),
      ),
      floatingActionButton: FloatingActionButton(onPressed:_incrementCounter, tooltip:'Increment', child: Icon(Icons.add))
    );
  }
}
