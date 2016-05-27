var player, time_update_interval = 0;

function onYouTubeIframeAPIReady() {
  player = new YT.Player('video-placeholder', {
    videoId: 'gcs8_l3fkVo', // cambiar con videos ejemplos
    events: {
      onReady: initialize
    }
  });
}

function initialize() {

  clearInterval(time_update_interval);

  time_update_interval = setInterval(function() {
    if(vioElVideo()) {
      console.log("Guardar");
      clearInterval(time_update_interval);
    }
  }, 1000);
}

function vioElVideo() {
  var tiempoSegundosVisto = Math.round(player.getCurrentTime());
  var tiempoSegundosVideo = Math.round(player.getDuration());

  if(tiempoSegundosVisto == tiempoSegundosVideo) {
    return true;
  }
  return false;
}
var csrftoken = getCookie('csrftoken'); 
$.ajax({
    url:"http://localhost:8000/prueba_post/",
    type: "POST",
    data: {name:"kevip"},
    beforeSend: before
  })
  .error(function(data){
    console.log(data)
  })
  .success(function(data){
    console.log(data)
  })
  function before(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
  }