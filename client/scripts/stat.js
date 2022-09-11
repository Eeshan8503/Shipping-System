

const fetcher = async (data,api) => {
    const response = await fetch('http://localhost:5000/'+api, {
      method: 'post',
      mode:'cors',
      body: data,
      headers: {'Content-Type': 'application/json'}
  });
  const myJson = await response.json();
  console.log(myJson);
  myJson.forEach(element => {
        // console.log(element)
      renderer(element)
  });
}
function renderer(data){
    let result=document.getElementById('clients')
    
    data.forEach(element => {
        let a=document.createElement('a');
        a.classList.add("dropdown-item");
        let li=document.createElement('li');
        a.innerText=element;
        li.appendChild(a);  
        a.addEventListener('click',function(e){
            alert(e.target.innerText)
            btnhandler(e.target.innerText)
        })
        result.appendChild(li);
    })
    // result.appendChild(tr);
}
function querySubmitter(){
    // alert('hello')
    query={
        "query":"SELECT MS FROM CLIENT"
    }
    query=JSON.stringify(query)
    fetcher(query,"runQuery")
}
function btnhandler(comp){  
    let val=""
    document.getElementById('compname').innerText=comp
    var arr=["max","min","avg"];
    for(i=0;i<arr.length;i++){
        val=arr[i];
        let temp=`SELECT ${val}(AMOUNT) FROM CHARGES WHERE INVOICE_NUM IN (SELECT INVOICE_NUM FROM SHIPPING_AGENT WHERE MS='${comp}')`
        query={
            "query":temp
        }
        query=JSON.stringify(query)
        fetcherr(query,"runQuery",i)
    }
    
}
const fetcherr = async (data,api,i) => {
    const response = await fetch('http://localhost:5000/'+api, {
      method: 'post',
      mode:'cors',
      body: data,
      headers: {'Content-Type': 'application/json'}
  });
  const myJson = await response.json();
  if(i==0)
    document.getElementById('max').innerText=myJson[0][0]
    else if(i==1)
    document.getElementById('min').innerText=myJson[0][0]
    else if(i==2)
    document.getElementById('avg').innerText=myJson[0][0]
  console.log(myJson[0][0])
}
querySubmitter()