function addNewProduct() {

    $.ajax({
        type: 'POST',
        url: "/bay/",
        data: {
            "csrfmiddlewaretoken": window.CSRF_TOKEN,
            "name": $("#name").val(),
            "price": $("#price").val(),
            "category_id": categoryId
        },
        success: function(response) {
            console.log(response);
        }
    });
}

function chooseCategory(button) {

    categoryId = button.dataset.id;
    var elems = document.querySelectorAll(".active");
    [].forEach.call(elems, function(el) {
        el.classList.remove("active");
    });
    button.classList.add('active');
}