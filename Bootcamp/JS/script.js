
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.17.1/firebase-analytics.js";

const firebaseConfig = {
    apiKey: "AIzaSyA426f5fCI0WXyZJEye6C0FROKGrsAhaDA",
    authDomain: "bootcamp-55fcb.firebaseapp.com",
    projectId: "bootcamp-55fcb",
    storageBucket: "bootcamp-55fcb.appspot.com",
    messagingSenderId: "678896890728",
    appId: "1:678896890728:web:e46b3863fd88f96a505cdd",
    measurementId: "G-4521WZ7GBV"
  };

  //Initialize firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();

//Login Fields
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const submitButton = document.getElementById("submit");
