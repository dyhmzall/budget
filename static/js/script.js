function addNewProduct() {

    $('#result').html('').hide();

    $('#nameHelp').html('');
    $('#name').removeClass('is-invalid');

    $('#priceHelp').html('');
    $('#price').removeClass('is-invalid');

    if (!$("#name").val()) {
        $('#nameHelp').html('Заполните поле продукт!');
        $('#name').addClass('is-invalid');
        return;
    }

    if (!$("#price").val()) {
        $('#priceHelp').html('Заполните поле цена!');
        $('#price').addClass('is-invalid');
        return;
    }

    if (!categoryId) {
        alert('Выберите категорию!');
        return;
    }

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
            $('#result').html(response.message).show();
            $("#name").val('');
            $("#price").val('');
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