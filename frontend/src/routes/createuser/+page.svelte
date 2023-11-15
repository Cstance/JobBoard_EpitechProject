<h1> carré dans l'axe </h1>

<script>

    async function getUser(square) {
        const res = await fetch("http://localhost:8000/database/users/", {
            method: "POST",
            body : JSON.stringify(square),
        });
        const json = await res.json();
        console.log(json);
    
        if (res.ok) {
            window.location.replace("/dashboard/")
    } else {
    
        const outputElement = document.getElementById("error");
        outputElement.textContent = "Error: wrong info ";
    }
    
    }
    
    function square(){
        
    let User = { name : document.getElementById('fname').value, 
               last_name : document.getElementById('lname').value,
               email : document.getElementById('email').value,
               password : document.getElementById('password').value,
               phone : document.getElementById('phone').value,
               location : document.getElementById('location').value,
               advertiser : document.getElementById('advertiser').value,
               
    }
    
    
    getUser(User)
    }
    
    
    
    </script>
    
    
    <main>
    <h1>Create your account :</h1>
    
    <form>
    
        <label for="fname"> First name:</label><br>
        <input type="text" id="fname" name="fname"><br>
    
        <label for="lname">Last Name :</label><br>
        <input type="text" id="lname" name="lname"><br>
    
        <label for="email">Email :</label><br>
        <input type="text" id="email" name="email"><br>

        <label for="password">Password :</label><br>
        <input type="password" id="password" name="password"><br>
    
        <label for="phone"> Phone number :</label><br>
        <input type="text" id="phone" name="phone"><br>
    
        <label for="location">Location :</label><br>
        <input type="text" id="location" name="location" /><br>
        <br>

        <label for="advertiser"> Role : </label>
        <select id="advertiser" name="advertiser">
            <option value="False"> User </option>
            <option value="True"> Advertiser </option>
        </select>    
        <br>

    
    
        <br>
        <br>
        <br>
    
        <button on:click={() => square()} >Submit :</button>
            
        <div id="error"> </div>
    
    </form>
    </main>
    