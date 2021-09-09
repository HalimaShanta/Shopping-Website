// var updateFavBtns = document.getElementsByClassName('update-fav');

// for(var j =0; j < updateFavBtns.length; j++){
//     updateFavBtns[j].addEventListener('click', function() {
//         var productId = this.dataset.home
//         var action = this.dataset.action
//         console.log('productId:', productId, 'action:', action)


// //         console.log('USER:', user)
// //         if(user == 'AnonymousUser'){
// //             console.log('Not logged In')
// //         }
// //         else{
// //             console.log('User is logged in, sending data...')
// //         }
//       })
// }


// function updateUserFav(productId, action) {
//     // console.log('User is logged in, sending data...')
//     var url = '/favourite'

//         fetch(url, {
//             method: 'POST',
//             headers:{
//                 'content-Type':'application/json',
//                 // 'X-CSRFToken':csrftoken            
//             },
//             body:JSON.stringify({'productId':productId, 'action':action})
//         })
//         .then((response) =>{
//             return response.json()
//         })
//         .then((data) =>{
//             console.log('data:', data)
//         })
// }
// $(document).on('click',".update-fav", function(){
//     // var productId = this.dataset.home
//     var p_id = $(this).attr('data-home');
//     $.ajax({
//         url: "/favourite",
//         data:{
//             product:p_id
//         },
//         dataType:'json',
//         success:function(res){
//             console.log(res);
//         }
//     });
// });