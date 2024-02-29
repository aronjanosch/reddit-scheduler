<template>
  <div id="firebaseui-auth-container"></div>
</template>

<script>
import firebase from '../firebaseConfig'; // Import your Firebase configuration
import * as firebaseui from 'firebaseui';
import 'firebaseui/dist/firebaseui.css';

export default {
  name: 'Login',
  mounted() {
    const uiConfig = {
      signInSuccessUrl: '/', // URL to redirect to after sign in
      signInOptions: [
        firebase.auth.EmailAuthProvider.PROVIDER_ID,
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        // Add other providers as needed
      ],
      // Other config options...
    };

    // Initialize the FirebaseUI Widget using Firebase
    const ui = new firebaseui.auth.AuthUI(firebase.auth());
    ui.start('#firebaseui-auth-container', uiConfig);
  },
};
</script>
