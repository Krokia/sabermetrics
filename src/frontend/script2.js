document.getElementById("calculateBtn2").
    addEventListener("click", async() => {

        const H = parseInt(document.getElementById("inpH").value);
        const BB = parseInt(document.getElementById("inpBB").value);
        const GP = parseInt(document.getElementById("inpGP").value);
        const HR = parseInt(document.getElementById("inpHR").value);
        const K = parseInt(document.getElementById("inpK").value);
        const IP = parseInt(document.getElementById("inpIP").value);
        const IBB = parseInt(document.getElementById("inpIBB").value);
        const SF = parseInt(document.getElementById("inpSF").value);
        const TB = parseInt(document.getElementById("inpTB").value);
        const operation = document.getElementById("operation").value;


        try {
            let method = "";
            let params = {}
            if  (operation === "K9") {
                method = "calc_k9";
                params = {K, IP}
            }
            else if  (operation === "FIP") {
                method = "calc_fip";
                params = {HR, BB, GP, IBB, K, IP}
            }
            else if  (operation === "BABIP") {
                method = "calc_babip";
                params = {H, HR, K, SF, TB}
            }

            // Llamar a mi servicio web (back-end) a través de una http request
            const endpoint = "http://127.0.0.1:8000/" + method;
            const data = {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(params)
            }
            console.log(endpoint)
            console.log(data)
            const response = await fetch(endpoint, data);

            // Mostrar el resultado en la UI
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "An unknown error ocurred")
            }

            const result = await response.json()
            document.getElementById("result").textContent = result.result;
        
        } catch(error) {
            document.getElementById("result").textContent = "Error!";
            console.error(error)
        }

    });
    