<script>
  import { onMount } from "svelte";
let isUserAuth = false
let userId = -1;
onMount( async () => {
        const token = document.cookie
            .split("; ")
            .find((row) => row.startsWith("token="))
            ?.split("=")[1];

        if(token === undefined) return;
        else{
            isUserAuth = true
            await getUserInformations(token)
        }
});

async function getUserInformations(token){
    const res = await fetch("http://localhost:8000/database/users/info/", {
        method: "POST",
        body : JSON.stringify('{"token" : "'+ token + '"}')
    });

    const json = await res.json();
    if (res.ok){
userId = json["id"]

        document.getElementById("fname").value = json["name"];
        document.getElementById("lname").value = json["last_name"];
        document.getElementById("email").value = json["email"];
        document.getElementById("phone").value = json["phone"];
        document.getElementById("location").value = json["location"];
    }
}

async function createUser(user) {
    const res = await fetch("http://localhost:8000/database/users/", {
        method: "POST",
        body : JSON.stringify(user),
    });
    const json = await res.json();
    console.log(json);

    if (res.ok) {
        return json["id"]
    } else {
        const outputElement = document.getElementById("error");
        outputElement.textContent = "Error: wrong info ";
        return -1;
    }
    
}


async function postApplication(application) {
    const res = await fetch("http://localhost:8000/database/applications/", {
        method: "POST",
        body : JSON.stringify(application),
    });
    const json = await res.json();

    if (res.ok) {
        window.location.replace("/Apply/applied")
} else {

    const outputElement = document.getElementById("error");
    outputElement.textContent = "Error: wrong info ";
}

}

function processApplication(userId){
    let applied = { 
        applicant : userId, 
        advertisement : new URLSearchParams(window.location.search).get("id"),
        message : document.getElementById('message').value,
    }


    postApplication(applied)
}

function apply(){
    
    if(isUserAuth) {
        processApplication(userId)
    }
    else{
        let User = { name : document.getElementById('fname').value, 
                last_name : document.getElementById('lname').value,
                email : document.getElementById('email').value,
                password : "1234",
                phone : document.getElementById('phone').value,
                location : document.getElementById('location').value,  
        }
        userId = createUser(User);
        if(userId === -1) return;
        processApplication(userId);
    }
}
</script>


<h1> Apply </h1>

<form>
    <label for="fname">First name:</label><br>
    <input type="text" id="fname" name="fname"><br>

    <label for="lname">Last Name :</label><br>
    <input type="text" id="lname" name="lname"><br>

    <label for="email">Email :</label><br>
    <input type="text" id="email" name="email"><br>

    <label for="phone">Phone number :</label><br>
    <input type="text" id="phone" name="phone"><br>

    <label for="location">Location :</label><br>
    <input type="text" id="location" name="location" /><br>
    <br>

    <label for="motivation">Motivation Letter:</label><br>
    <textarea rows="12" cols="60" name="motivation" id="message"></textarea><br>
    <br>
    <br>
    <br>
    <a href="http://localhost:5173/Apply/applied">
    <button class="submit" type="submit" on:click={() => apply()}>Apply</button>
    



</form>