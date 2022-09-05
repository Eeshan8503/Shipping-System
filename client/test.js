import fetch from 'node-fetch';
const userAction = async () => {
    const response = await fetch('http://localhost:5000/getAllClients');
    const myJson = await response.json(); //extract JSON from the http response
    myJson.forEach(element => {
        console.log(element);
    });

  }
userAction();

// const fetcher = async () => {
//   const response = await fetch('http://localhost:5000/addInvoice', {
// 	method: 'post',
// 	body: JSON.stringify(body),
// 	headers: {'Content-Type': 'application/json'}
// });
// const data = await response.json();

// console.log(data);
// }
// fetcher();