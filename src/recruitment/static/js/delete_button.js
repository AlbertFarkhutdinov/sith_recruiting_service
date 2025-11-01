'use strict';
var checkboxes = document.getElementsByClassName('form-group');
for (var i=0; i < checkboxes.length; i++){
    if(checkboxes[i].firstChild.className == 'form-check'){
        checkboxes[i].innerHTML = '';
    }
}