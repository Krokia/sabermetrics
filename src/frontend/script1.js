document.getElementById("calculateBtn1").
    addEventListener("click", async() => {

        const H = parseInt(document.getElementById("inpH").value);
        const BB = parseInt(document.getElementById("inpBB").value);
        const GP = parseInt(document.getElementById("inpGP").value);
        const VB = parseInt(document.getElementById("inpVB").value);
        const SH = parseInt(document.getElementById("inpSH").value);
        const single = parseInt(document.getElementById("inpSingle").value);
        const double = parseInt(document.getElementById("inpDouble").value);
        const triple = parseInt(document.getElementById("inpTriple").value);
        const HR = parseInt(document.getElementById("inpHR").value);
        const operation = document.getElementById("operation").value;


        try {
            let method = "";
            let params = {}
            if (operation === "OBP") {
                method = "calc_obp";
                params = {H, BB, GP, VB, SH}
            }
            else if  (operation === "SLG") {
                method = "calc_slg";
                params = {VB, single, double, triple, HR}
            }
            else if  (operation === "OPS") {
                method = "calc_ops";
                params = {H, BB, GP, VB, SH, single, double, triple, HR}
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