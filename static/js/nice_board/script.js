"use strict"
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
    const speed = 500;
    const position = $("#footer").offset().top - $(window).height()
    $("html, body").animate({ scrollTop: position }, speed, "swing");

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
// PageScript.prototype.doneFormView = function (data) {
//     const _this = this;
//     const siteHtml = $(data).find("#contents");
//     siteHtml.find("form").submit(function () {
//         const postData = {}
//         $(this).find("input").each(function () {
//             postData[$(this).attr("name")] = $(this).val()
//         })
//         $(this).find("textarea").each(function () {
//             postData[$(this).attr("name")] = $(this).val()
//         })
//         PageScript.ajaxPost(_this.sendUrl, postData)
//             .then(() => { console.log("send") })
//         return false
//     });
//     $(_this.outputEl).empty();
//     $(_this.outputEl).append(siteHtml.children());
// }
// PageScript.prototype.createPostData = function (data, call = () => { }) {
//     const postData = {}
//     $(this).find("input").each(function () {
//         postData[$(this).attr("name")] = $(this).val()
//     })
//     $(this).find("textarea").each(function () {
//         postData[$(this).attr("name")] = $(this).val()
//     })
//     call(postData);
// }
PageScript.prototype.doneCreateView = function (data, listInstans) {
    const _this = this;
    const siteHtml = $(data).find(_this.contentElName);
    siteHtml.find("a").remove();
    siteHtml.find("form").submit(function () {
        const postData = {}
        $(this).find("input").each(function () {
            postData[$(this).attr("name")] = $(this).val()
        })
        $(this).find("textarea").each(function () {
            postData[$(this).attr("name")] = $(this).val()
        })

        PageScript.ajaxPost(_this.sendUrl, postData)
            .then(resp => {
                _this.doneCreateView(resp, listInstans)
            }, resp => {
                alert("送信に失敗しました");
                _this.outputEl.appent("問題がはっせいしました")
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

