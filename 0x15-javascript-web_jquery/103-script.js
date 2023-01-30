window.onload = function() {
  $('#language_code').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
      translate()
    }
  })
  $('INPUT#btn_translate').click(() => {
    translate()
  })
}

function translate () {
  const endpoint = 'https://www.fourtonfish.com/hellosalut/?lang=';

  $('document').ready(() => {
    const lang = $('INPUT#language_code').val();
    $.get(endpoint + lang, (data) => {
      $('DIV#hello').text(data.hello);
    })}
)}
