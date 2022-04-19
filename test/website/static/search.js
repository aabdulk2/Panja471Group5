document.getElementById('search-by').addEventListener('change', function(){
    const selected_element = this.value;
    const placeholder = document.getElementById(selected_element);
    console.log('You chose ', selected_element);
    document.getElementById('search-bar').setAttribute('placeholder', 'Search by ' + placeholder.textContent);
})