<template>
    <div class="login-page">
      <h1>Login</h1>
      <p>Please log in to continue to the dashboard.</p>
      <!-- FirebaseUI Auth Container will go here -->
      <div id="firebaseui-auth-container"></div>
    </div>
  </template>
  
  <script>
  // If you're using FirebaseUI, you'll eventually initialize it here as shown in the previous steps.
  export default {
    name: 'LoginPage',
  };
  </script>
  
  <style scoped>
  .login {
    padding: 20px;
  }
  </style>