const holder=document.querySelector('.intels');


function renderer(client){
    const h31 = document.createElement("h3");
    const h32 = document.createElement("h3");
    const h33 = document.createElement("h3");
    const h34 = document.createElement("h3");
    const h35 = document.createElement("h3");
    const h36 = document.createElement("h3");
    
    const h41 = document.createElement("h4");
    const h42 = document.createElement("h4");
    const h43 = document.createElement("h4");
    const h44 = document.createElement("h4");
    const h45 = document.createElement("h4");
    
    const br1=document.createElement("br");
    const br2=document.createElement("br");
    const br3=document.createElement("br");
    const br4=document.createElement("br");
    const br5=document.createElement("br");

    const hr=document.createElement("hr");  
    h31.innerText=client.ms;
    h32.innerText=client.invoice_num;
    h41.innerText="Invoice Number";

    h33.innerText="Date";
    h42.innerText=client.date;

    h34.innerText="Container Number";
    h43.innerText=client.container_num;

    h35.innerText="Destination";
    h44.innerText=client.destination;

    h36.innerText="Total Amount";
    h45.innerText="Rupees"+client.amount;
    
    holder.appendChild(hr);
    holder.appendChild(h31);
    holder.appendChild(br1);
    holder.appendChild(h32);
    holder.appendChild(h41);
    holder.appendChild(br2);
    holder.appendChild(h33);
    holder.appendChild(h42);
    holder.appendChild(br3);
    holder.appendChild(h34);
    holder.appendChild(h43);
    holder.appendChild(br4);
    holder.appendChild(h35);
    holder.appendChild(h44);
    holder.appendChild(br5);
    holder.appendChild(h36);
    holder.appendChild(h45);

}
const client={
    ms:"MS-1234",
    invoice_num:"INV-1234",
    date:"12/12/2020",
    container_number:"C-1234",
    destination:"India",
    amount:"10000"
}
const userAction = async () => {
    const response = await fetch('http://localhost:5000/getAllClients');
    const myJson = await response.json(); //extract JSON from the http response
    myJson.forEach(element => {
        renderer(element);
    });

  }
userAction();