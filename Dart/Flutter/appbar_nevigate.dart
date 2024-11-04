import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp( title:'Flutter Code Sample', home:MyStatelessWidget() );
}

final GlobalKey<ScaffoldState> scaffoldKey = GlobalKey<ScaffoldState>();
final SnackBar snackBar = const SnackBar(content: Text('Showing Snackbar'));

void openPage(BuildContext context) {
  Navigator.push(context, MaterialPageRoute(
    builder: (BuildContext context){
      return Scaffold(
        appBar: AppBar( title:const Text('Next page') ),
        body: const Center( child:Text('This is the next page',style:TextStyle(fontSize:24)) )
      );
    },
  ));
}

/// This is the stateless widget that the main application instantiates.
class MyStatelessWidget extends StatelessWidget {
  MyStatelessWidget({Key key}):super(key:key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      appBar: AppBar(
        title: const Text('AppBar Demo'),
        actions: <Widget>[
          IconButton(
            icon: const Icon(Icons.add_alert),
            tooltip: 'Show Snackbar?',                     // hint
            onPressed: (){scaffoldKey.currentState.showSnackBar(snackBar);},
	  ),
          IconButton(
            icon: const Icon(Icons.navigate_next),
            tooltip: 'Next page',
            onPressed: (){openPage(context);},
	  ),
        ],
      ),
      body: const Center(child: Text('This is the home page haha',style:TextStyle(fontSize:24)))
    );
  }
}
