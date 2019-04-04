// Initialize Firebase
var config = {
  apiKey: "AIzaSyDw2uL8Yg-lb3dpW5Peo3ghTmaSwOwbr64",
  authDomain: "pythontest-233123.firebaseapp.com",
  databaseURL: "https://pythontest-233123.firebaseio.com",
  projectId: "pythontest-233123",
  storageBucket: "pythontest-233123.appspot.com",
  messagingSenderId: "1026046022529"
};
firebase.initializeApp(config);

firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    window.location = "https://accounts.ssw215.com"
  } else {
    window.location = "https://login.ssw215.com"
  }
})