jQuery(document).ready(function() {
  jQuery(".timeago").timeago();
  $('.form-control').on('focus blur', function (e) {
      $(this).parents('.form-group').toggleClass('focused', (e.type === 'focus' || this.value.length > 0));
  }).trigger('blur');
  //token tagging

});
$('.tokenfield').tokenfield({
  inputType:'text',
});