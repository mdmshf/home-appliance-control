(function() {
  $(document).ready(function() {
    $('.switch-input').on('change', function() {
      var isChecked = $(this).is(':checked');
      var selectedData;
      var $switchLabel = $('.switch-label');
      console.log('isChecked: ' + isChecked); 
      
      if(isChecked) {
        selectedData = $switchLabel.attr('data-on');
      } else {
        selectedData = $switchLabel.attr('data-off');
      }
      
      console.log('Selected data: ' + selectedData);
      
    });
    
    // Params ($selector, boolean)
    function setSwitchState(el, flag) {
      el.attr('checked', flag);
    }
    
    // Usage
    setSwitchState($('.switch-input'), true);    
  });
  
})();