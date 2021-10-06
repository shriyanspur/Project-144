import React, { Component } from 'react';
import {
  Text,
  View,
  StyleSheet,
  TouchableOpacity,
  TextInput,
} from 'react-native';
import HomeScreen from './screens/Home';
import PopularScreen from './screens/Popular';
import Recommended from './screens/Recommended';
import { createAppContainer } from "react-navigation";
import { createStackNavigator } from "react-navigation-stack";
import { createMaterialTopTabNavigator } from "react-navigation-tabs";
import { RFValue } from "react-native-responsive-fontsize";

export default class App extends Component {
  button_function() {
    //This is a function
  }

  render() {
    return (
      <View>
        <Text style={styles.headText}>Movie-Recommender</Text>
        <TextInput style={styles.textBox} placeholder="Text" />
        <TouchableOpacity style={styles.button} onPress={this.button_function}>
          <Text style={styles.buttonText}>.</Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  headText: {
    alignSelf: 'center',
    marginTop: 15,
    fontSize: 27,
  },
  textBox: {
    backgroundColor: 'white',
    alignSelf: 'center',
    marginTop: 20,
    height: 50,
    width: 500,
    borderWidth: 3,
    borderColor: 'black',
    borderRadius: 10,
    textAlign: 'center',
    fontSize: 20,
  },
  button: {
    backgroundColor: '#EA6C6C',
    alignSelf: 'center',
    marginTop: 20,
    height: 50,
    width: 300,
    borderColor: 'black',
    borderRadius: 17,
  },
  buttonText: {
    alignSelf: 'center',
    marginTop: 7,
    fontSize: 25,
  },
});
