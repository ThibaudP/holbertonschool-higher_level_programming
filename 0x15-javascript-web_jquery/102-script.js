const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(() => {
  $('input#btn_translate').on('click', () => {
    $.getJSON(url + $('input#language_code').val(), data => {
      $('div#hello').html(data.hello);
    });
  });
});
