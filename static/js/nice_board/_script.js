$(function () {
    $.ajax({
        url: URL_NICE_BOARD_THREADS,
        type: 'GET',
        cache: false,
        dataType: 'html',
        data: {}
    })
        .done(function (data, textStatus, jqXHR) {
            const siteHtml = $(data).find("#createContents");
            siteHtml.find("#form").submit(() => {
                console.error(siteHtml.find("#form").find("input[name='csrfmiddlewaretoken']").val())
                console.error(siteHtml.find("#form").find("input[name='title']").val())
                $.ajax({
                    url: URL_NICE_BOARD_THREADS,
                    type: 'POST',
                    cache: false,
                    dataType: 'html',
                    data: {
                        csrfmiddlewaretoken: siteHtml.find("#form").find("input[name='csrfmiddlewaretoken']").val(),
                        title: siteHtml.find("#form").find("input[name='title']").val()
                    }
                })
                return false;
            })
            $($("#wrapper")).append(siteHtml);

        })
        .fail(function (jqXHR, textStatus, errorThrown) {
            alert('fail!');
        })
        .always(function (data, textStatus, errorThrown) {
            alert('always!');
        });

})