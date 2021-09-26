"use strict"
const myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'), {
    keyboard: false
})
const PageScript = function PageScript(outputElName, contentElName, sendUrl) {
    this.outputEl = $(outputElName)
    this.contentElName = contentElName
    this.sendUrl = sendUrl
}
PageScript.ajaxGet = function (sendUrl) {
    return $.ajax({
        url: sendUrl,
        type: 'GET',
        cache: false,
        dataType: 'html'
    })
}
PageScript.ajaxPost = function (sendUrl, sendData = {}) {
    return $.ajax({
        url: sendUrl,
        type: 'POST',
        cache: false,
        dataType: 'html',
        data: sendData
    })
}
PageScript.prototype.doneListView = function (data) {
    const siteHtml = $(data).find(this.contentElName);
    this.outputEl.empty();
    this.outputEl.append(siteHtml.children());
    return data
}
PageScript.openModalEvent = function (SendUrl) {
    PageScript.ajaxGet(SendUrl)
        .then(PageScript.doneListView)
        .then(() => PageScript.linkSet($("#output")))
    myModal.toggle();
    return false
}
// PageScript.linkSet = function (target, SendUrl) {
//     target.find(`a`).click(function () {
//         PageScript.ajaxGet(SendUrl)
//             .then(PageScript.doneListView)
//             .then(() => PageScript.linkSet($("#output")))
//         myModal.toggle();
//         return false
//     })
// }
PageScript.doneFormView = function (data) {
    console.error("done")
    const siteHtml = $(data).find("#contents");
    siteHtml.find("form").submit(function () {
        const data = {}
        $(this).find("input").each(function () {
            data[$(this).attr("name")] = $(this).val()
        })
        PageScript.ajaxPost(URL_NICE_BOARD_THREADS, data)
            .then(() => { console.log("send") })
        return false
    });
    $($("#output")).append(siteHtml.children());
}
PageScript.prototype.doneCreateView = function (data, listInstans) {
    const _this = this;
    const siteHtml = $(data).find(_this.contentElName);
    siteHtml.find("form").submit(function () {
        const postData = {}
        $(this).find("input").each(function () {
            postData[$(this).attr("name")] = $(this).val()
        })
        $(this).find("textarea").each(function () {
            postData[$(this).attr("name")] = $(this).val()
        })
        // _this.sendUrl = "daadd"
        PageScript.ajaxPost(_this.sendUrl, postData)
            .then(resp => {
                _this.doneCreateView(resp, listInstans)
            }, resp => {
                if (resp.status == '404') {
                    alert("送信に失敗しました");
                }
            })
            .then(() => {
                PageScript.ajaxGet(listInstans.sendUrl)
                    .then(resp => listInstans.doneListView(resp))
            })
        return false
    });
    _this.outputEl.empty();
    _this.outputEl.append(siteHtml.children());
}

