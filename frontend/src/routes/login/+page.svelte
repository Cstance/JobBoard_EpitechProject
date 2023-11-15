<script>
import { onMount } from 'svelte';
onMount( async () => {
        const cookieValue = document.cookie
            .split("; ")
            .find((row) => row.startsWith("token="))
            ?.split("=")[1];
        if(cookieValue !== undefined) window.location.replace("/dashboard/");
    });

async function verifyUser() {

    let data = { 
            email : document.getElementById('email').value, 
            password : document.getElementById('password').value
    }

    const res = await fetch("http://localhost:8000/login/", {
        method: "POST",
        body : JSON.stringify(data)
    });

    const json = await res.json();
    if (res.ok && json["code"] == 202){
        document.cookie = "token="+json["token"];  
        window.location.replace("/dashboard/")
      

    } else {
        throw new Error(json);
    }

    
}

</script>


<main>

<h2>Login to post or apply </h2>

<form>

    <div class="container">
        <label for="email"><b>Email : </b></label>
        <input type="text" id="email" placeholder="Enter email" name="email" required>
        
        <label for="psw"><b>Password :</b></label>
        <input type="password" id="password" placeholder="Enter Password" name="psw" required>
        
        <button type="submit" on:click={() => verifyUser()}>Login</button>
    </div>
</form>

<h2>Create an account</h2>

<a href="http://localhost:5173/createuser/">
<button type="submit" >Create account</button>
</a>
</main>