var switchMonitorVal= false;

function switchMonitor(){
    switchMonitorVal=! switchMonitorVal;
   
}


function httpGet(theUrl) {   let reqHeader = new Headers();
    reqHeader.append('Content-Type', 'text/json');
    let initObject = {
        method: 'GET', headers: reqHeader,
    };

    return fetch(theUrl,initObject)
        .then((response) => { 
            return response.json().then((data) => {
                //console.log(data);
                return data;
            }).catch((err) => {
                console.log(err);
            }) 
        });

}


function populate() {

   
var mypromise=(httpGet(location.origin+"/mydata"));
mypromise.then((data) => {

    document.getElementById('IP').innerHTML=`Public IP: ${data.ip}`;
    document.getElementById('City').innerHTML=`City: ${data.city}`;
    document.getElementById('Region').innerHTML=`Region: ${data.region}`;
    document.getElementById('Country').innerHTML=`Country: ${data.country}`;

  });

}

function connect() {
    var mypromise=(httpGet(location.origin+"/connect"));
    mypromise.then((data) => {
        updateDelayed();  
      });
    }
function disconnect() {
    var mypromise=(httpGet(location.origin+"/disconnect"));
    mypromise.then((data) => {
        updateDelayed();  
      });
    }

function updateDelayed() {
        setTimeout(
          function() {
            populate();
          }, 5000);
      }