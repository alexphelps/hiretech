jQuery(document).ready(function() {

  $('.form-control.floating-label').on('focus blur', function (e) {
      $(this).parents('.form-group').toggleClass('focused', (e.type === 'focus' || this.value.length > 0));
  }).trigger('blur');

  $(".timeago").timeago();

  //auto remove alerts with auto-close class
  setTimeout(function() {
    $(".alert.auto-close").alert('close');
  }, 2000);

  $('.tokenfield').tokenfield({
    inputType:'text',
  });
});
