// $.ajax({
//     url: '{{url}}',
//     method: 'get',
//     dataType: 'json',
//     success: function(data){
// 	console.dir(data);
//     },
//     error: function (jqXHR, exception) {
// 	if (jqXHR.status === 0) {
// 		alert('Not connect. Verify Network.');
// 	} else if (jqXHR.status == 404) {
// 		alert('Requested page not found (404).');
// 	} else if (jqXHR.status == 500) {
// 		alert('Internal Server Error (500).');
// 	} else if (exception === 'parsererror') {
// 		alert('Requested JSON parse failed.');
// 	} else if (exception === 'timeout') {
// 		alert('Time out error.');
// 	} else if (exception === 'abort') {
// 		alert('Ajax request aborted.');
// 	} else {
// 		alert('Uncaught Error. ' + jqXHR.responseText);
// 	}
//     }
// });



// // const xhr = new XMLHttpRequest();

// // xhr.open('GET', requestURL);
// // xhr.onreadystatechange = function() {
// //     if (xhr.readyState !== 4 || xhr.status !== 200) {
// //         return;
// //     }
// //     // все в порядке, ответ получен
// //     const response = xhr.response;
// //     console.log(response);
// // }
// // xhr.send();


// // <script>
// //                 function getData() {
// //                   // URL на который будем отправлять GET запрос
// //                   const requestURL = '{{url.url_slug}}';
// //                   const xhr = new XMLHttpRequest();
// //                   xhr.open('GET', requestURL);
// //                   xhr.onload = () => {
// //                     if (xhr.status !== 200) {
// //                       return;
// //                     }
// //                     document.querySelector('#result').innerHTML = xhr.response;
// //                   }
// //                   xhr.send();
// //                 }
// //                 document.querySelector('#get').addEventListener('click', () => {
// //                 getData();
// //                 });
// //             </script>