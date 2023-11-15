<script>
import { onMount } from 'svelte';
onMount( async () => {
        const token = document.cookie
            .split("; ")
            .find((row) => row.startsWith("token="))
            ?.split("=")[1];

        if(token === undefined) window.location.replace("/login/");
        else{
           await isUserAdvertiser(token)
        }
    });

async function isUserAdvertiser(token){
    const res = await fetch("http://localhost:8000/database/users/type/", {
        method: "POST",
        body : JSON.stringify('{"token" : "'+ token + '"}')
    });

    const json = await res.json();
    if (res.ok){
        if (json["advertiser"] === 'False') window.location.replace("/dashboard/user/");
        else window.location.replace("dashboard/advertiser/");
    } else {
        window.location.replace("/");
    }
}
</script>


