Dropzone.autoDiscover = false;

const grid = new gridjs.Grid({
  columns: ["Name", "Probability"],
  data: [
    ["Elon", 0],
    ["Jack Ma", 0],
    ["Jeff Bezos", 0],
    ["Richard Branson", 0],
    ["Warren Buffet", 0]
  ]
}).render(document.getElementById("wrapper"));

function init() {
  let dz = new Dropzone("#dropzone", {
      url: "/",
      maxFiles: 1,
      addRemoveLinks: true,
      dictDefaultMessage: "Some Message",
      autoProcessQueue: false
  });
  
  dz.on("addedfile", function() {
      if (dz.files[1]!=null) {
          dz.removeFile(dz.files[0]);        
      }
  });

  dz.on("complete", function (file) {

      let imageData = file.dataURL;
      
      var url = "/api/classify_person";

      $.post(url, {
          image_data: file.dataURL
      },function(data, status) {
          console.log(data);
          if (!data || data.length==0) {
              $("#success").hide();
              $("#divClassTable").hide();                
              $("#error").show();
              return;
          }
          let players = ["lionel_messi", "maria_sharapova", "roger_federer", "serena_williams", "virat_kohli"];
          
          let match = null;
          let bestScore = -1;
          for (let i=0;i<data.length;++i) {
              let maxScoreForThisClass = Math.max(...data[i].class_probability);
              if(maxScoreForThisClass>bestScore) {
                  match = data[i];
                  bestScore = maxScoreForThisClass;
              }
          }
          if (match) {
              $("#error").hide();
              $("#success").show();
              $("#divClassTable").show();
              $("#resultHolder").html($(`[data-player="${match.class}"`).html());
              let classDictionary = match.class_dict;
              let result_array = []
              let max_prob = 0
              let max_prob_name = ''
              for(let personName in classDictionary) {
                  let index = classDictionary[personName];
                  let proabilityScore = match.class_probability[index];
                  let elementName = "#score_" + personName;
                  $(elementName).html(proabilityScore);
                  result = []
                  result = [personName, proabilityScore]
                  result_array.push(result)

                  if(max_prob < proabilityScore)
                  {
                    max_prob = proabilityScore
                    max_prob_name = personName
                  }
              }

            grid.updateConfig({
            // search: true,
            data: result_array
            }).forceRender();

            $('#success').html(`<img src="./assets/${max_prob_name}.jpg" style="border-radius: 50%;" class="img-fluid" alt="..." width="200"><span class="mt-4" style="text-align: center;font-weight:bold;">it is ${max_prob_name}</span>`);
          }
          // dz.removeFile(file);            
      });
  });

  $("#submitBtn").on('click', function (e) {
      dz.processQueue();		
  });
}

$(document).ready(() => {
  console.log('ready');
  $('#error').hide();
  $("#success").hide();

  init()
})