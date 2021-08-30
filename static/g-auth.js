function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
}

// To show google profile details on dashboard, use the following commands
function getUserInfo(googleUser) {
  var profile = googleUser.getBasicProfile();
  document.querySelector('#content').innerText=profile.getName();
  document.querySelector('#content').innerText=profile.getEmail();
}

//To sign out, implement a sign out button on dashboard with the following function
function signOut() {
    gapi.auth2.getAuthInstance().signOut().then(function() {
    console.log('User has signed out')
  })
}
  
