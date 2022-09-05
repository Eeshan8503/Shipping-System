$('#myform').submit(function(event){
    let data={
        invoice_num:"",
        ms:'',
        gst_num:'',
        locality:'',
        city:'',
        state:'',
        pincode:'',
        acc_num:'',
        container_num:'',
        vessel:'',
        destination:'',
        charge_type:'',
        currency:'',
        rate: '',
        amount:'',
        quantity:'',


    }
    alert('submitted');
    element = $('input[name="inv_no"]');
    data.invoice_num=element.val();
    element = $('input[name="ms"]');
    data.ms=element.val();
    element = $('input[name="gst_num"]');
    data.gst_num=element.val();
    element = $('input[name="locality"]');
    data.locality=element.val();
    element = $('input[name="city"]');
    data.city=element.val();
    element = $('input[name="state"]');
    data.state=element.val();
    element = $('input[name="pincode"]');
    data.pincode=element.val();
    element = $('input[name="acc_num"]');
    data.acc_num=element.val();
    element = $('input[name="cont_num"]');
    data.container_num=element.val();
    element = $('input[name="vess"]');
    data.vessel=element.val();
    element = $('input[name="dest"]');
    data.destination=element.val();
    element = $('input[name="chType"]');
    data.charge_type=element.val();
    element = $('input[name="curr"]');
    data.currency=element.val();
    element = $('input[name="rate"]');
    data.rate=element.val();
    element = $('input[name="amt"]');
    data.amount=element.val();
    element = $('input[name="quant"]');
    data.quantity=element.val();
    data=JSON.stringify(data)
    console.log(data);
    fetcher(data)

    event.preventDefault();
});
const fetcher = async (data) => {
    const response = await fetch('http://localhost:5000/addInvoice', {
      method: 'post',
      mode:'cors',
      body: data,
      headers: {'Content-Type': 'application/json'}
  });
  const dataa = await response.json();
  
  console.log(dataa);
  }
