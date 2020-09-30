// Use d3.json() to fetch data from JSON file
// Incoming data is internally referred to as incomingData




d3.json("/api/v1.0/canada_covid"). then(function(data){
  console.log(data)
  var filteredData = data.filter(function (d) {
    return d.province_name != "Canada" && d.province_name !=  "Repatriated travellers" && d.date=="18-09-2020";
  });
 
    var location =[];

    
    filteredData.forEach(fdata=>{
      fdata["Coordinate"]=[fdata.latitude, fdata.longitude]
    
    // })
    
  
  })
  console.log(filteredData)
})


d3.json("/api/v1.0/covid_trends"). then(function(data){
  console.log(data)
  var parseTime = d3.timeParse("%d-%b");
data.forEach(d=>{
  

  // Format the data
 

    console.log(d.date)

})
  

  /*dateArray=data.map(d=>d.date)
  scatterData = []
  data.forEach(function(d){
    
    scatterDict={}
    scatterDict["x"]=d.active_cases
    scatterDict["y"]=d[optionvalue]
    scatterData.push(scatterDict)
  })*/
var nline;
  var trendList= ["Bike", "CERB", "Zoom", "Patio","Mask"];
    console.log(trendList)
 // Appending list into a dropdown
    var selectTrend=d3.select("#selTrend")
    trendList.forEach(tag=>{
        
        selectTrend.append("option").attr("value",tag).text(tag)
    })

    var covList= ["confirmed cases", "daily_tests", "daily_cases", "active_cases","daily_deaths"];
    console.log(covList)
 // Appending list into a dropdown
    var selectCov=d3.select("#selCovid")
    covList.forEach(tag=>{
        
        selectCov.append("option").attr("value",tag).text(tag)
    })


 
  var opt1 = "Mask"
  var opt2="daily_tests"
   
  
  var canvas = document.getElementById('myChart');
 var lineData={
    type: 'line',
    data: {
      labels: data.map(d=>d.date),
      datasets: [{
        label: opt1,
        yAxisID: "A",
        data: data.map(d=>d[opt1]),
       borderColor: "Cyan"
      }, {
        label: opt2,
        yAxisID: "B",
        data: data.map(d=>d[opt2]),
        borderColor: "Crimson"
      }]
    },fill: false,
    options: {
      scales: {
        yAxes: [{
          id: "A",
          type: 'linear',
          position: 'left',
          scaleLabel:{
            display: true,
        labelString: opt1
          },
        
        }, {
          id: "B",
          type: 'linear',
          position: 'right',
          scaleLabel:{
            display: true,
        labelString: opt2
          },
          
          
        }],
        xAxes:[
          {scaleLabel:{
            display: true,
        labelString: `Date`
          }
          }
        ]
      }, 
      elements: {
        line: {
                fill: false
        }
    }
    }
  };

  if(window.bar != undefined) 
  window.bar.destroy(); 
  window.bar = new Chart(canvas, lineData);





function updateTrends() {
  

  
  var y1Menu =d3.select("#selTrend");
  var optiony1 = y1Menu.property("value");
  
  var y2Menu =d3.select("#selCovid");
  var optiony2 = y2Menu.property("value")
   
    var opt1 = optiony1
    var opt2=optiony2
     
   
   
    
    var canvas = document.getElementById('myChart').getContext("2d");
    


  
   // var nline =new Chart(canvas, 
     var lineData= {
      type: 'line',
      data: {
        labels: data.map(d=>d.date),
        datasets: [{
          label: opt1,
          yAxisID: opt1,
          data: data.map(d=>d[opt1]),
          borderColor: "Cyan"
        }, {
          label: opt2,
          yAxisID: opt2,
          data: data.map(d=>d[opt2]),
          borderColor: "Crimson"
        }]
      },
      
      options: {
        scales: {
          yAxes: [{
            id: opt1,
            type: 'linear',
            position: 'left',
            scaleLabel:{
              display: true,
          labelString: opt1
            }
          }, {
            id: opt2,
            type: 'linear',
            position: 'right',
            scaleLabel:{
              display: true,
          labelString: opt2
            }
            
          }],
          
          xAxes:[
            {scaleLabel:{
              display: true,
          labelString: `Date`
            }
            }
          ]
        },
        elements: {
          line: {
                  fill: false
          }
      }
   
        }
      
    };
    if(window.bar != undefined) 
    window.bar.destroy(); 
    window.bar = new Chart(canvas, lineData);
  
  }
 


  
  document.getElementById("selTrend").addEventListener("change", updateTrends)
  d3.select("#selCovid").on("change", updateTrends)

  
})

/*var y1Menu =d3.select("#selTrend");
var optiony1 = y1Menu.property("value");
var y2Menu =d3.select("#selCovid");
var optiony2 = y2Menu.property("value");*/