  // Initialize Firebase
	var config = {
	apiKey: "AIzaSyDiSCgQWGOkJhfUo31CvS0Yba5BbqAN3YU",
	authDomain: "app-authentication-e1ee7.firebaseapp.com",
	databaseURL: "https://app-authentication-e1ee7.firebaseio.com",
	projectId: "app-authentication-e1ee7",
	storageBucket: "app-authentication-e1ee7.appspot.com",
	messagingSenderId: "700623114287"
	};

	firebase.initializeApp(config);

	const txtEmail1 = document.getElementById("txtEmail1")
	const txtPassword1 = document.getElementById("txtPassword1")
	const txtEmail2 = document.getElementById("txtEmail2")
	const txtPassword2 = document.getElementById("txtPassword2")
	const btnSignUp = document.getElementById("btnSignUp")
	const btnLogIn = document.getElementById("btnLogIn")
	const btnLogOut = document.getElementById("logOut")
	const logLabel = document.getElementById("logLabel")

	btnSignUp.addEventListener('click', e=> {
		const email = txtEmail1.value
		const pass = txtPassword1.value
		const auth = firebase.auth();
		const promise = auth.createUserWithEmailAndPassword(email, pass).catch(function(error){
			console.log(error.code);
			console.log(error.message);
		});
	});

	btnLogIn.addEventListener('click', e=> {
		console.log(logLabel.value);
		const email = txtEmail2.value
		const pass = txtPassword2.value
		const auth = firebase.auth();
		const promise = auth.signInWithEmailAndPassword(email, pass).catch(function(error){
			console.log(error.code);
			console.log(error.message);
		});
	});

	btnLogOut.addEventListener('click', e=> {
	 	firebase.auth().signOut();
	});

	firebase.auth().onAuthStateChanged(firebaseUser => {
		var text = document.querySelector("#user")
		var hiText = document.querySelector("#hiText")
		if(firebaseUser){
			var email = firebaseUser.email
			document.getElementById("signLabel").style.display = "none";
			document.getElementById("logLabel").style.display = "none";
			document.getElementById("hiText").style.display = "block";
			document.getElementById("logOut").style.display = "block";
			text.textContent = "The current user is " + email + ".";
			hiText.textContent = "Hi " + email
			console.log(firebaseUser);
		} else {
			document.getElementById("hiText").style.display = "none";
			document.getElementById("logOut").style.display = "none";
			document.getElementById("signLabel").style.display = "block";
			document.getElementById("logLabel").style.display = "block";
			text.textContent = "No one is logged in.";
			console.log('not logged in');
		}
	});

	
