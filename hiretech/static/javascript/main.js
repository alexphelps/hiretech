jQuery(document).ready(function() {

  $('.form-control.floating-label').on('focus blur', function (e) {
      $(this).parents('.form-group').toggleClass('focused', (e.type === 'focus' || this.value.length > 0));
  }).trigger('blur');
  //token tagging
  $(".timeago").timeago();
});

$('.tokenfield').tokenfield({
  inputType:'text',
});
