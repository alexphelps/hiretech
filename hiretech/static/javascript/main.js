jQuery(document).ready(function() {

  //floating lables for material design
  $('.floating-label').on('focus blur', function (e) {
      $(this).parents('.form-group').toggleClass('focused', (e.type === 'focus' || this.value.length > 0));
  }).trigger('blur');

  //intialize timeago
  $(".timeago").timeago();

  //auto remove alerts with auto-close class
  setTimeout(function() {
    $(".alert.auto-close").alert('close');
  }, 2000);

  //intialize tokenfield
  $('.tokenfield').tokenfield({
    inputType:'text',
  });
});
