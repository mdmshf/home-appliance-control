var database = firebase.database();
  (function() {
  $(document).ready(function() {
    $('.switch-input1').on('change', function() {
      var isChecked1 = $(this).is(':checked');
      var ref = firebase.database().ref('devices');
	  if(isChecked1){
ref.child('device1').set(1);
}else{
ref.child('device1').set(0);

}
      console.log('isChecked1: ' + isChecked1); 
      
    });
    

    function setSwitchState(el, flag) {
      el.attr('checked', flag);
    }
    // Usage
    var database1 = firebase.database();
   var ref1 = database1.ref("devices");
   ref1.on("value", gotData1);
   
   function gotData1(data1) {
   var power1 = data1.val();
   console.log('running device1');
   console.log(power1.device1);
   if(power1.device1){
   setSwitchState($('.switch-input1'), true);
   }else{
   setSwitchState($('.switch-input1'), false);
     }
    
    }
    
    
    
    $('.switch-input2').on('change', function() {
      var isChecked2 = $(this).is(':checked');
        var ref = firebase.database().ref('devices');
	  if(isChecked2){
ref.child('device2').set(1);
}else{
ref.child('device2').set(0);

}   
      console.log('isChecked2: ' + isChecked2); 
    });
    
    // Params ($selector, boolean)
    
    // Usage
    var database2 = firebase.database();
   var ref2 = database2.ref("devices");
   ref2.on("value", gotData2);
   
   function gotData2(data2) {
   var power2 = data2.val();
   console.log('running device2');
   console.log(power2.device2);
   if(power2.device2){
   setSwitchState($('.switch-input2'), true);
   }else{
   setSwitchState($('.switch-input2'), false);
     }
    
    }
    
    
    $('.switch-input3').on('change', function() {
      var isChecked3 = $(this).is(':checked');
	       var ref = firebase.database().ref('devices');
	  if(isChecked3){
ref.child('device3').set(1);
}else{
ref.child('device3').set(0);

}


      console.log('isChecked3: ' + isChecked3); 
      
    });
    
    // Params ($selector, boolean)
    
    // Usage
	var database3 = firebase.database();
   var ref3 = database3.ref("devices");
   ref3.on("value", gotData3);
   
   function gotData3(data3) {
   var power3 = data3.val();
   console.log('running device3');
   console.log(power3.device3);
   if(power3.device3){
   setSwitchState($('.switch-input3'), true);
   }else{
   setSwitchState($('.switch-input3'), false);
     }
    
    }
    
    $('.switch-input4').on('change', function() {
      var isChecked4 = $(this).is(':checked');
	         var ref = firebase.database().ref('devices');
	  if(isChecked4){
ref.child('device4').set(1);
}else{
ref.child('device4').set(0);

}
      console.log('isChecked4: ' + isChecked4); 
      
    });
    
    // Params ($selector, boolean)
    
    // Usage
    var database4 = firebase.database();
   var ref4 = database4.ref("devices");
   ref4.on("value", gotData4);
   
   function gotData4(data4) {
   var power4 = data4.val();
   console.log('running device4');
   console.log(power4.device4);
   if(power4.device4){
   setSwitchState($('.switch-input4'), true);
   }else{
   setSwitchState($('.switch-input4'), false);
     }
    }
  });
})();