var categoris_elements = document.querySelectorAll('span')
var temp_inputValue = ""
var temp_cateValue = ""


function find(){

    var inputValue = document.getElementById('text').value

    categoris_elements.forEach(categoris_elements => {

        if(inputValue.length === 0){
            categoris_elements.style.display = 'block';
        }

        for(var i = 0; i < inputValue.length; i++){
            temp_inputValue = inputValue.toLowerCase();
            temp_cateValue = categoris_elements.id.substring(0, inputValue.length).toLowerCase()

            if(temp_inputValue !== temp_cateValue){
                categoris_elements.style.display = 'none';
            }else{
                categoris_elements.style.display = 'block';
            }
            
            //console.log("Cat val: "+temp_cateValue, "Input Val: "+ temp_inputValue)
        }


    });
}