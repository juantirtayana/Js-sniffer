<?php
if(isset($_POST['username'])){
$username=$_POST['username'];
$creditcard=$_POST['creditcard'];
$expireddate=$_POST['expireddate'];
$cvv=$_POST['cvv'];

$connection=mysqli_connect("localhost","root","password","credit_card");

$sqlquery = "INSERT INTO `card`(`Username`,`Creditcard`,`Expiredate`,`CVV`) VALUES ('$username','$creditcard','$expireddate','$cvv');";
$result = mysqli_query($connection,$sqlquery);

if($result==true){
	echo"inserted";
}
}
?>
