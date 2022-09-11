function handler(){
    // document.getElementById("sider").contentWindow.location.reload(true);
data_charges={
    filter:[
    ],
    table:[
            "charges",
            "client",
            "container",
            "shipping_agent"  
    ]
}
const arr=["cur","type","rate","quant","amt","con_num","ves","dest","ms","gst_num","acc_num"];
const headings=[];
let flag=0;
for(let i=0;i<arr.length;i++){
    if(document.getElementById(arr[i]).checked){
        console.log(document.getElementById(arr[i]).value)
        if(document.getElementById(arr[i]).value=='ms'){
            data_charges.filter.push("CLIENT."+document.getElementById(arr[i]).value);    
            headings.push(document.getElementById(arr[i]).value);
            continue;
        }
        else if(document.getElementById(arr[i]).value=='container_num'){
            data_charges.filter.push("CONTAINER."+document.getElementById(arr[i]).value);   
            headings.push(document.getElementById(arr[i]).value); 
            continue;
        }
        
        data_charges.filter.push(document.getElementById(arr[i]).value);
        headings.push(document.getElementById(arr[i]).value);
        
    }
}
data_charges=JSON.stringify(data_charges)
console.log(data_charges);
renderer_init(headings)
fetcher(data_charges,"admin")
}
function renderer_init(heading){
    let head=document.getElementById('heading')
    heading.forEach(element => {
        const th=document.createElement('th');
        th.innerText=element;
        head.appendChild(th);
    })  
}
function renderer(data){
    let result=document.getElementById('results')
    let tr=document.createElement('tr');
    data.forEach(element => {
        // console.log(element+" dsds")
        td=document.createElement('td');
        td.innerText=element;
        tr.appendChild(td);
    })
    result.appendChild(tr);
}
const fetcher = async (data,api) => {
    const response = await fetch('http://localhost:5000/'+api, {
      method: 'post',
      mode:'cors',
      body: data,
      headers: {'Content-Type': 'application/json'}
  });
  const myJson = await response.json();
//   console.log(myJson);
  myJson.forEach(element => {
        // console.log(element)
      renderer(element)
  });
}
function querySubmitter(){
    query={
        "query":document.getElementById('query').value
    }
    query=JSON.stringify(query)
    fetcher(query,"runQuery")
}
function createView(){
    alert(document.getElementById('query').value)
    let v=prompt("Enter the name of the view")
    
    let query={
        "name":v,
        "query":document.getElementById('query').value
    }
    console.log(query)
    query=JSON.stringify(query)
    alert("hold")
    fetcherr(query,"createView")

}
const fetcherr = async (data,api) => {
    const response = await fetch('http://localhost:5000/'+api, {
      method: 'post',
      mode:'cors',
      body: data,
      headers: {'Content-Type': 'application/json'}
  });
  const myJson = await response.json();
}