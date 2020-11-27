$(function () {
    $(".dataset-detail").hide();

    $(".op-edit").click(function () {
        $(".btn-back").show();
        $(".dataset-detail").show();
        $(".dataset-list").hide();
        console.log("op click");
    });

    $(".btn-back").click(function () {
        $(".btn-back").hide();
        $(".dataset-list").show();
        $(".dataset-detail").hide();
        console.log("back click");
    });
});